import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv

load_dotenv()  # load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt1 = """
Imagine you're an advanced AI-powered Resume Evaluation System, equipped with in-depth knowledge of 
various technical fields including software engineering, data science, data analysis, and big data 
engineering. Your primary objective is to assess resumes against specific job descriptions in a highly 
competitive job market. Your assessment should focus on determining the degree of alignment between the 
resume and the job description, assigning a percentage match based on key criteria outlined in the job 
description, and identifying any missing keywords with pinpoint accuracy. The ultimate goal is to provide
actionable insights and recommendations to help candidates improve their resumes and increase their chances
of success in securing the desired position.
resume:{text}
description:{input_text}

I want the response in neat and well-mannered format structure string having the structure

**JD Match:**
- %

**Missing Keywords:**
- []

**Profile Summary:**
- 
"""

input_prompt2 = """
You are a highly proficient ATS (Applicant Tracking System) scanner, well-versed in the nuances of 
data science and the intricacies of ATS functionality. Your primary objective is to meticulously evaluate
a given resume against the provided job description, ensuring a high degree of accuracy. Your evaluation
should begin with providing the percentage of match between the resume and the job description, followed
by a detailed list of any missing keywords identified in the resume. Finally, offer insightful final 
thoughts summarizing the overall alignment between the resume and the job requirements, highlighting
areas of strength and potential areas for improvement. Your assessment should aim to provide actionable 
feedback to help optimize the candidate's chances of success in the competitive job market.
"""

# Function to check if text is meaningful
def is_meaningful_text(text):
    return len(text.split()) > 2

# Streamlit app
st.set_page_config(page_title="Smart ATS", page_icon=":briefcase:", layout="wide")

# Custom CSS for dark mode
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        color: #f5f5f5;
    }
    .stButton button {
        background-color: #333;
        color: #f5f5f5;
        border: 1px solid #f5f5f5;
    }
    .stTextInput textarea {
        background-color: #333;
        color: #f5f5f5;
        border: 1px solid #f5f5f5;
    }
    .stFileUploader label {
        color: #f5f5f5;
    }
    .stAlert {
        background-color: #333;
        color: #f5f5f5;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #333;
        color: #f5f5f5;
        text-align: center;
        padding: 10px;
        box-shadow: 0 -1px 5px rgba(0, 0, 0, 0.1);
    }
    .center-text {
        text-align: center;
    }
    .header-text {
        font-size: 2em;
        color: #f5f5f5;
        font-weight: bold;
    }

    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="center-text header-text">Smart ATS</div>', unsafe_allow_html=True)
st.markdown('<div class="center-text">Improve Your Resume for ATS</div>', unsafe_allow_html=True)

input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

if st.button("Submit"):
    if not input_text:
        st.warning("Please provide a job description.")
    elif not is_meaningful_text(input_text):
        st.warning("Please provide a meaningful job description.")
    elif uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt1.format(text=pdf_content, input_text=input_text))
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume.")

if st.button("Tell Me About the Resume"):
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        if not is_meaningful_text(input_text):
            response = get_gemini_response(f"Analyze this resume:\n{pdf_content}")
        else:
            response = get_gemini_response(input_prompt2.format(text=pdf_content, input_text=input_text))
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload the resume.")

# Footer
st.markdown(
    """
    <div class="footer">
        <p>Made with ❤️ by Aditya</p>
    </div>
    """,
    unsafe_allow_html=True
)
