# Smart ATS (Applicant Tracking System)

Smart ATS is a Streamlit-based application designed to enhance resume evaluation using Google's generative AI capabilities. It allows users to assess resumes against job descriptions with precision and provide actionable feedback.

## Features

- **Resume Evaluation**: Evaluate resumes against specific job descriptions.
- **PDF Parsing**: Extract text from uploaded PDF resumes for analysis.
- **AI-Powered Assessment**: Utilize Google's generative AI to analyze resumes for job suitability.
- **Job Description Match**: Calculate the percentage match between the resume and job requirements.
- **Keyword Analysis**: Identify missing keywords crucial for job application success.
- **Insightful Feedback**: Offer detailed feedback and improvement suggestions for candidates.

## Setup

To run the Smart ATS locally or deploy it, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/smart-ats.git
   cd smart-ats
   ```

2. **Install Dependencies**:
   Ensure Python 3.x is installed. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Google API key to the `.env` file:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key_here
     ```

4. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

5. **Access the Application**:
   Open a web browser and go to `http://localhost:8501` to access the Smart ATS application.

## Usage

- **Job Description Input**: Enter the job description for which resumes will be evaluated.
- **Resume Upload**: Upload resumes in PDF format for evaluation.
- **Submit**: Evaluate the uploaded resume against the provided job description.
- **Analysis Results**: View the percentage match, missing keywords, and detailed profile summary based on the evaluation.

## Contributing

Contributions to enhance Smart ATS are welcome! Please fork the repository, create a new branch, commit your changes, and open a pull request.

## Credits

- **Streamlit**: Python framework for building interactive web applications.
- **Google's Generative AI**: Powered by Google's AI models for advanced text generation.
- **PyPDF2**: Library for extracting text from PDF documents.
- **dotenv**: Library for loading environment variables from a `.env` file.


---
