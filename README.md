### Legal-Document-Summarization
# Legal Document Summarization

## Introduction
Legal Document Summarization is an AI-powered tool designed to extract and summarize text from legal documents. This application utilizes Google Gemini Pro to generate concise summaries, making legal information more accessible and digestible.

## Project Structure
```
Legal-Document-Summarization/
│── data/                 # Folder to store input legal documents
│── notebooks/            # Jupyter Notebook for rough execution
│── src/                  # Source code folder
│   │── __init__.py       # Marks `src` as a Python package
│   │── summarizer.py     # Handles API interaction with Gemini Pro
│   │── utils.py          # Helper functions (e.g., file handling)
│── app.py                # Streamlit UI for user interaction
│── main.py               # Backend logic
│── requirements.txt      # Dependencies list
│── config.py             # Stores API keys (or uses `.env` for security)
│── .env                  # API keys (optional, for security)
│── README.md             # Project documentation
│── .gitignore            # Ignore unnecessary files
```

## Workflow
1. **User Uploads a Document**
   - Supports PDF, DOCX, and TXT files.
2. **Text Extraction**
   - Extracts text using the `FileHandler` utility.
3. **Summarization**
   - Sends extracted text to Gemini Pro via `ResponseGeneration`.
4. **Displaying the Summary**
   - The summarized output is shown on the Streamlit UI.

## Future Scope
- **Improving Summarization Accuracy**
  - Fine-tune the model to better handle legal jargon.
- **Multilingual Support**
  - Enable processing documents in multiple languages.
- **Enhanced UI/UX**
  - Add additional features like highlighting key legal terms.
- **Integration with Legal Databases**
  - Fetch related case laws and references for better legal analysis.

## How to Run
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
2. Run the Streamlit app:  
   ```bash
   streamlit run app.py
   ```



We should start with the API interaction module in src/summarizer.py, as it forms the core of your project by handling the communication with Google Gemini Pro for summarization.

# Steps:
* **Set Up API Interaction (summarizer.py)**

1. Implement a function to send document text to Gemini Pro and retrieve a summary.
2. Handle errors and ensure a clean response.
3. Build Utility Functions (utils.py)

* **File reading (loading legal documents).**
1. File writing (saving summaries).
2. Develop config.py or .env

* **Store API keys securely.**
1. Create the Backend Logic (main.py)

* **Read documents, call the summarizer, and store the output.**
1. Build the Streamlit UI (app.py)

* **Design a user-friendly interface for input and output.**
1. Finalize Jupyter Notebook (notebooks/)

*Experiment and fine-tune the summarization process.*