# Applicant Tracking System (ATS)

The Applicant Tracking System (ATS) is an advanced tool powered by the Google Gemini Pro Vision API. This project is designed to analyze resumes, compare them with job descriptions, and provide actionable suggestions for enhancing resumes to better match job requirements.

## Project Files

- **`ATS.py`**: The main application file that runs the ATS.
- **`requirements.txt`**: Lists all the dependencies and libraries required to run the project.

## LinkedIn Post

For more information and updates, check out our LinkedIn post: [ATS LinkedIn Post](https://www.linkedin.com/posts/suraj-kumar-362360289_ai-machinelearning-googlegemini-activity-7224672538549796864-ZmbR?utm_source=share&utm_medium=member_desktop)

## Installation

To get started with the ATS, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create an environment file:**
    Create a `.env` file in the project directory and add your Google API key:
    ```plaintext
    GOOGLE_API_KEY=your-generated-api-key-from-google-ai-studio
    ```

## Running the Application

Once you have installed all the required libraries, start the application using:

```bash
python -m streamlit run app.py
