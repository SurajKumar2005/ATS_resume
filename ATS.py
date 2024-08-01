import os
import PyPDF2 as pdf
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load the environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Application Tracking System 💻", page_icon=":robot:")

# Sidebar content
st.sidebar.header("Resume Analyzer Info")
st.sidebar.write("Welcome to the Application Tracking System (ATS)! This tool helps you improve your resume by analyzing it against job descriptions.")
st.sidebar.write("**Instructions:**")
st.sidebar.write("1. Enter the job description in the text area provided.")
st.sidebar.write("2. Upload your resume in PDF format.")
st.sidebar.write("3. Click on the 'Submit' button to get your resume analyzed.")
st.sidebar.write("**Features:**")
st.sidebar.write("- Matches your resume against the job description.")
st.sidebar.write("- Identifies missing keywords.")
st.sidebar.write("- Provides a profile summary.")
st.sidebar.write("**Note:** The job market is very competitive. Make sure to tailor your resume for each job application!")

# Main page content
st.header("APPLICATION TRACKING SYSTEM 🤖 ")
st.text("Improve Your Resume ATS Score")
jd = st.text_area("Job Description 📝 ")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit 🚀")

# Prompt Template
input_prompt = """
You are a skilled and very experienced ATS (Application Tracking System) with a deep understanding of the tech field, software engineering,
data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide the best assistance for improving resumes.
Assign the percentage Matching based on Job description and the missing keywords with high accuracy.
Resume:
Description:

I want the response in 3 sections as follows:
* Job Description Match: \n
* Missing Keywords: \n
* Profile Summary: \n
"""

if submit:
    if uploaded_file is not None:
        reader = pdf.PdfReader(uploaded_file)
        extracted_text = ""
        for page in range(len(reader.pages)):
            page = reader.pages[page]
            extracted_text += str(page.extract_text())
        input_prompt += f"\nResume: {extracted_text}\nDescription: {jd}\n"
        response = model.generate_content(input_prompt)
        st.write(response.text)
