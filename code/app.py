from flask import Flask, render_template, request, jsonify
from sklearnex import patch_sklearn
patch_sklearn()  # Use optimized scikit-learn
import fitz  # PyMuPDF for PDF handling
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Get the Google API key from the environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Path to the directory containing PDF files
pdf_directory = "datasets/"  # Update this to your directory path

def get_pdf_text(pdf_file_path):
    """Extract text from a PDF file."""
    text = ""
    with fitz.open(pdf_file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def get_text_chunks(text):
    """Split text into chunks for processing."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks, api_key):
    """Create and save a FAISS vector store from text chunks."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def initialize_vector_store():
    """Initialize vector store from all PDF files in the directory if it doesn't already exist."""
    if not os.path.exists("faiss_index"):
        print("Creating FAISS vector store from the PDF files in the directory...")
        all_text = ""
        
        # Iterate through all PDF files in the specified directory
        for filename in os.listdir(pdf_directory):
            if filename.endswith(".pdf"):
                pdf_file_path = os.path.join(pdf_directory, filename)
                raw_text = get_pdf_text(pdf_file_path)
                all_text += raw_text
                print(f"Debug: Processed {filename} with text length: {len(raw_text)}")
        
        text_chunks = get_text_chunks(all_text)
        print(f"Debug: Total number of chunks created: {len(text_chunks)}")
        
        get_vector_store(text_chunks, api_key)
        print("Vector store created successfully!")

def get_conversational_chain():
    """Set up the conversational chain for Q&A."""
    prompt_template = """
        You are an expert Indian legal assistant with deep knowledge of Indian laws, regulations, and legal procedures. When responding to legal queries:
        
        1. Start with a clear humanised explaination based on the user's concern or query
        2. Provide accurate information based on current Indian laws and regulations
        3. Explain legal concepts in simple, easy-to-understand language
        4. Include relevant sections of acts/laws when applicable
        5. Suggest practical next steps or procedures the user should follow
        6. Mention any important deadlines or time limitations
        7. If relevant, explain which court or authority has jurisdiction
        8. Clarify if any documentation or evidence would be required
        9. Try to list down some important points as bulletin points one below the other when necessary and not like paragraphs.
        
        Remember to maintain a professional yet approachable tone, and always emphasize that while you provide legal information, users should consult a practicing lawyer for specific legal advice. 
        Context: {context}
        Question: {question}
        Response:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3, google_api_key=api_key)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    return chain

def user_input(user_question):
    """Handle user input and generate a response."""
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
        print("Debug: Embeddings created")
        
        new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
        print("Debug: Vector store loaded")
        
        docs = new_db.similarity_search(user_question)
        print(f"Debug: Found {len(docs)} relevant documents")
        print(f"Debug: First doc content: {docs[0].page_content if docs else 'No docs found'}")

        chain = get_conversational_chain()
        response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
        print(f"Debug: Generated response: {response}")

        return response.get("output_text", "No response generated.")
    except Exception as e:
        print(f"Error in user_input: {str(e)}")
        return f"An error occurred: {str(e)}"

    if not docs:
        return "No matches found."

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    return response.get("output_text", "No response generated.")

@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests."""
    user_question = request.form.get('user_question')
    
    if not user_question:
        return jsonify({'error': 'No question provided.'})
    
    response = user_input(user_question)
    
    return jsonify({'response': response})

# Initialize the vector store when the app starts
initialize_vector_store()

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode