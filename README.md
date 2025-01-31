# 💻 AI-Powered Placement & Interview Simulator 📝

## 📌 Overview
The **AI-Powered Placement & Interview Simulator** is a Streamlit-based application designed to help students prepare for technical and HR interviews. It dynamically generates interview questions based on the candidate's resume, allowing for an interactive and realistic interview experience.

## 🚀 Features
- **Resume Parsing:** Extracts text from uploaded **PDF** or **DOCX** resumes.
- **AI-Generated Interview Questions:** Dynamically generates technical and HR interview questions.
- **Candidate Response Input:** Allows students to answer interview questions.
- **AI Feedback & Evaluation:** Provides constructive feedback on candidate responses.
- **Interactive Interview Flow:** Users can continue to the next question using a "Continue" button.

## 🛠️ Tech Stack
- **Python**
- **Streamlit** (UI Framework)
- **Groq API** (AI Chat Completions)
- **PyPDF2** (PDF Text Extraction)
- **python-docx** (DOCX Text Extraction)

## 📂 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/AI-Powered-Placement-Interview-Simulator.git
cd AI-Powered-Placement-Interview-Simulator
```

### 2️⃣ Create a Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Add Groq API Key
Create api from this website https://console.groq.com/keys and add:
```sh
GROQ_API_KEY=your-api-key-here
```
Or set it in your environment:
```sh
export GROQ_API_KEY=your-api-key-here  # MacOS/Linux
set GROQ_API_KEY=your-api-key-here  # Windows
```

### 5️⃣ Run the Application
```sh
streamlit run app.py
```

## 🎥 How It Works
1. Upload a **PDF** or **DOCX** resume.
2. The AI **analyzes** the resume and starts the interview.
3. The AI **asks a question**, and the user types a response.
4. AI **evaluates** the answer and provides feedback.
5. Click **"Continue to Next Question"** to proceed.
6. Repeat until the interview session completes!

## 🖼️ Demo Screenshot
![AI Interview Simulator Screenshot](screenshot.png)

## 🤖 API Used
- **Groq AI Chat Completions API**

## 📌 Future Enhancements
- ✅ Support for **multi-round interviews** (Technical + HR)
- ✅ Option to select **specific job roles** for tailored questions
- ✅ **Speech-to-text** support for voice-based interviews
- ✅ **Interview report generation** for tracking progress

## Contributing 🤝
- We welcome contributions! If you would like to improve or add new features to this project, please fork the repository and submit a pull request.

## Connect with Me 🌐

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)

