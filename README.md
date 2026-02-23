AI Research Assistant

An AI-powered research assistant built with Streamlit and Google Gemini API.
This application provides concise, structured explanations for topics in Artificial Intelligence, Machine Learning, Deep Learning, and Generative AI.

📌 Overview

The AI Research Assistant is designed to support students, researchers, and developers by delivering clear and focused responses to AI-related queries.
It leverages the Gemini 2.5 Flash model to generate high-quality research-oriented answers within a controlled response structure.

🚀 Key Features

Interactive chat-based interface

AI-specialized responses (ML, DL, GenAI)

Structured and concise answers (3–6 sentences)

Secure API key management using environment variables

Clean and minimal user interface

🛠️ Technology Stack

Language: Python

Frontend: Streamlit

LLM: Google Gemini (gemini-2.5-flash)

Environment Management: python-dotenv

⚙️ Installation & Setup
1. Clone the Repository
2. Create a Virtual Environment (Recommended)
python -m venv venv

Activate the environment:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Environment Variables

Create a .env file in the root directory:

gemini_class=YOUR_GOOGLE_API_KEY

⚠️ Ensure that the .env file is included in .gitignore.

5. Run the Application
streamlit run chatapp.py

Access the application at:

http://localhost:8501
🔐 Security Note

API keys are managed using environment variables via python-dotenv.
Sensitive credentials should never be committed to version control.

📈 Future Enhancements

Document upload and research paper summarization

Persistent chat memory using database storage

Citation and reference generation

Deployment on Streamlit Cloud or AWS

👨‍💻 Author

Anugu Hruthik Reddy
AI & Generative AI Enthusiast
