import streamlit as st
import groq  # Ensure you have installed the groq package
import PyPDF2
import docx
import os

# Load API Key securely
api_key = os.getenv("GROQ_API_KEY", "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")  # Replace with a secure method

client = groq.Client(api_key=api_key)

def extract_text_from_pdf(pdf_file):
    """Extract text from PDF file."""
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        return text if text.strip() else "No readable text found in the PDF."
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def extract_text_from_docx(docx_file):
    """Extract text from DOCX file."""
    try:
        doc = docx.Document(docx_file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text if text.strip() else "No readable text found in the DOCX."
    except Exception as e:
        return f"Error reading DOCX: {str(e)}"

def generate_interview_question(resume_text, chat_history):
    """Generate the next interview question based on the resume and conversation."""
    prompt = f"""
    Given the following resume and previous conversation, continue the interview by asking a relevant question.
    Resume:
    {resume_text}
    
    Previous conversation:
    {chat_history}
    
    The question should be clear, relevant to the resume, and encourage detailed responses.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a professional interviewer conducting a technical and HR interview."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating question: {str(e)}"

def evaluate_answer(question, user_answer):
    """AI evaluates the student's answer and provides feedback."""
    prompt = f"""
    Interview Question: {question}
    Candidate's Answer: {user_answer}
    
    Provide a professional evaluation of the answer, highlighting strengths, weaknesses, and areas for improvement.
    """
    
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are an expert interviewer providing feedback on candidate answers."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in evaluation: {str(e)}"

# Streamlit UI
st.title("AI-Powered Placement & Interview Simulator")

uploaded_file = st.file_uploader("Upload Your Resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file) if uploaded_file.type == "application/pdf" else extract_text_from_docx(uploaded_file)
    
    if resume_text and "Error" not in resume_text:
        st.subheader("AI-Driven Interview Session")
        
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = ""

        if "current_question" not in st.session_state:
            st.session_state.current_question = generate_interview_question(resume_text, st.session_state.chat_history)

        st.write("**AI Interviewer:**", st.session_state.current_question)

        user_response = st.text_area("Your Response:", key="user_response")

        if st.button("Submit Answer"):
            if user_response.strip():
                feedback = evaluate_answer(st.session_state.current_question, user_response)
                st.write("**AI Feedback:**", feedback)
                
                # Update chat history
                st.session_state.chat_history += f"\nAI: {st.session_state.current_question}\nYou: {user_response}\nFeedback: {feedback}\n"
                
                # Enable the Continue button
                st.session_state.next_question_ready = True
            else:
                st.warning("Please enter a response before submitting.")

        if st.session_state.get("next_question_ready", False):
            if st.button("Continue to Next Question"):
                st.session_state.current_question = generate_interview_question(resume_text, st.session_state.chat_history)
                st.session_state.next_question_ready = False  # Reset the state for the next question
                st.experimental_rerun()
    else:
        st.error("Failed to extract text. Please upload a clear and readable resume.")

