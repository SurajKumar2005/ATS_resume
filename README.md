# ATS_resume
skillcred

PDF Analyzer Bot is an innovative tool designed to leverage the Gemini API and LangChain for advanced document analysis capabilities. This project facilitates advanced parsing, insightful analysis, and streamlined data extraction from PDF documents.

## Project Files

- **`app.py`**: The main application file that runs the PDF Analyzer Bot.
- **`requirements.txt`**: Lists all the dependencies and libraries required to run the project.

## LinkedIn Post

For more information and updates, check out our LinkedIn post: [PDF Analyzer Bot LinkedIn Post](https://www.linkedin.com/posts/suraj-kumar-362360289_ai-machinelearning-googlegemini-activity-7224672538549796864-ZmbR?utm_source=share&utm_medium=member_desktop)

## Installation

To get started with the PDF Analyzer Bot, follow these steps:

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

After installing the required libraries, start the application using the following command:

```bash
python -m streamlit run app.py
