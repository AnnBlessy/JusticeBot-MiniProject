## JusticeBot : A Virtual Legal Assistant
The JusticeBot is an innovative Retrieval-Augmented Generation (RAG) based chatbot designed to revolutionize legal information access on Justice Department. Leveraging advanced language models and cutting-edge AI technologies, the JusticeBot facilitates immediate, accurate, and user-friendly guidance across various legal and judicial services. It streamlines complex procedures by providing detailed explanations and step-by-step instructions, ensuring users can efficiently navigate their legal needs.

## About
JusticeBot, a Retrieval-Augmented Generation (RAG) based chatbot, is designed to enhance user experience by offering instant access to various eCourt services, including case searches, hearing schedules, court orders, and payment processes for fines. It further simplifies access to citizen services by delivering clear and concise guidance on legal aid, petition filing, and traffic violation settlements. Additionally, the chatbot promotes transparency in the judicial system by facilitating the live streaming of court cases, while ensuring 24/7 availability of crucial legal information.
Utilizing ChromaDB for efficient data management and data retrieval and AWS infrastructure for scalable and cost-effective deployment, the JusticeBot is built for cost-efficiency and future expansion, with capabilities for Reinforcement Learning with Human Feedback (RLHF) and potential multilingual support. Despite challenges such as local LLM limitations and the complexity of processing large legal documents, the JusticeBot promises significant social, economic, and environmental benefits by promoting legal awareness, reducing operational costs, and minimizing paper usage, the JusticeBot empowers users, fostering confidence and equitable access to justice.

## Features

- Implements advanced Retrieval-Augmented Generation (RAG) using Gemini Pro for precise and context-aware legal guidance.
- Provides user-friendly access to eCourt services, including case searches, hearing schedules, court orders, and fine payments.
- Simplifies complex legal processes with step-by-step instructions and detailed explanations.
- Enables real-time access to live-streamed court cases, promoting judicial transparency.
- Offers 24/7 availability of essential legal and judicial information.
- Leverages Facebook AI Similarity Search (FAISS) for efficient and fast data retrieval.
- Scalable and cost-effective deployment using Vercel infrastructure.
- Reduces paper usage and operational costs, contributing to environmental sustainability.

## Requirements

- Operating System: Requires a 64-bit OS (Windows 10, macOS, or Ubuntu) for hosting and development compatibility.
- Development Environment: Python 3.8 or later for implementing machine learning and natural language processing models.
- AI Frameworks: TensorFlow, PyTorch, or JAX for model development and fine-tuning.
- Database and Search Index: FAISS for similarity search and efficient legal document retrieval.
- Hosting Platform: Vercel or similar for scalable cloud deployment and seamless accessibility.
- Version Control: Git for collaborative development and maintaining code repositories.
- Additional Dependencies:
    1. transformers for managing pre-trained language models.
    2. faiss-cpu for similarity search optimization.
    3. FastAPI or Flask for building the chatbot’s API interface.
    4. Front-end frameworks like React.js for user-friendly interfaces.
- Hardware Requirements: GPU-enabled servers for efficient model inference and real-time query processing. Minimum 16 GB RAM and 50 GB storage for running the development environment.
- IDE: Use of VSCode as the Integrated Development Environment for coding, debugging, and version control integration.

## System Architecture
<!--Embed the system architecture diagram as shown below-->
![image](https://github.com/user-attachments/assets/10fc8392-7909-48b3-8c82-9ba6d7a7e755)


## Output

#### Output1 - ChatBot Frontend UI

![image](https://github.com/user-attachments/assets/daa78ac0-1414-4d2a-9762-b155de60f29c)

#### Output2 - Response Sample 1
![image](https://github.com/user-attachments/assets/9b06fa38-b139-4cb5-bc3b-bdef9214abd9)

## Results and Impact

The evaluation of JusticeBot highlights its performance in addressing legal queries with a focus on three key metrics: accuracy, response time, and user satisfaction. These insights showcase its ability to deliver reliable, efficient, and user- centric solutions for legal information retrieval.
1.	Accuracy JusticeBot effectively responded to a diverse range of legal queries by leveraging the combined strengths of Retrieval-Augmented Generation (RAG) and the Gemini Pro model. Its ability to provide precise and contextually relevant answers was particularly evident in areas with well-defined legal structures, such as family law, property disputes, and general legal procedures.
While JusticeBot performed well across most scenarios, it occasionally encountered challenges with ambiguous or highly complex legal issues. These instances highlighted areas for future improvement, particularly in fine-tuning its ability to interpret nuanced questions. The integration of advanced retrieval mechanisms ensured that even multi-layered queries were addressed with a high level of accuracy.
2.	Response Time JusticeBot demonstrated excellent effi- ciency in generating responses, with minimal delays observed during query processing. Its architecture, designed to opti- mize retrieval and generation tasks, allowed users to receive information quickly and seamlessly. The system maintained consistent performance, even during high-demand periods, ensuring a reliable experience for users.
The quick response time proved beneficial in scenarios requiring urgent legal guidance. Users noted that the chatbot’s ability to retrieve and present information promptly made it a practical tool for both routine inquiries and time-sensitive legal matters.

JusticeBot excelled in delivering accurate and timely legal information, with a strong emphasis on user-friendly interactions. It was particularly effective in guiding users through commonly encountered legal issues, providing both procedural clarity and relevant case insights.


## Articles published / References
1.	S. Adhikari, “Using BERT embeddings for intelligent legal document retrieval,” Journal of AI and Law, vol. 8, no. 4, pp. 233–245, 2022.
2.	R, Anitha., N, Kishore., Vijay Anand, M. ”NextGen Dynamic Video Generator using AI.” 2023 9th International Conference on Smart Struc- tures and Systems (ICSSS), Saveetha Engineering College, Chennai, India. IEEE, 2023.
3. N. Alemzadeh, “AI-powered legal assistants: Bridging the gap in access to justice,” in International Conference on Social Computing, 2021.
4. Ramyadevi, R., Sasidharan, G. ”Cogniwealth: Revolutionizing Finance, Empowering Investors, and Shaping the Future of Wealth Management.” 2024 International Conference on Computing, Power, and Communica- tion Technologies (IC2PCT), Saveetha Engineering College, Chennai, India. IEEE, 2024.





