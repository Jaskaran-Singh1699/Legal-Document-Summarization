import streamlit as st
import os
import sys
from src.utils import FileHandler
from src.summarizer import  ResponseGeneration
from src.logger import logging
from dotenv import load_dotenv

load_dotenv()


def main():
    logging.info('Entered main app.py')
    st.set_page_config(page_title='Legal Document Summarization',layout='wide')
    st.title('📝 AI-Powered Legal Document Summarization')

    uploaded_file=st.file_uploader("Upload Document", type=['pdf','docx','txt'])

    if uploaded_file:
        st.success("✅ File successfully uploaded!")
        file_type=identify_file_type(uploaded_file)
        if file_type:
            process_uploaded_file(uploaded_file,file_type)
            
        else:
            st.error("Invalid file type. Please upload a PDF, DOCX or TXT file")


def identify_file_type(file):
    logging.info('Entered indentify_file_type app.py')
    try:
        if file.type == 'application/pdf':
            return 'pdf'
        elif file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            return 'docx'
        elif file.type == 'text/plain':
            return 'txt'
        else:
            return None
    except Exception as e:
        return None


def process_uploaded_file(file,file_type):
    logging.info('Entered process_uploaded_file app.py')
    st.subheader('Extracted Text')

    try:
        extracted_text=FileHandler.read_file(file,file_type)
        if extracted_text is None or (isinstance(extracted_text,str) and extracted_text.lower().startswith('error')):
            raise ValueError('Failed to extract')
        
        st.text_area("Extracted Conetent",extracted_text,height=200)
        

        if st.button('Summarize'):
            summarize_text(extracted_text)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")


def summarize_text(text):
    logging.info('Entered summarize_text app.py')
    with st.spinner("Generating Summary..."):
        try:
            api_k=os.getenv('GOOGLE_API_KEY')
            response_generator=ResponseGeneration(api_key=api_k)
            summary=response_generator.GeminiResponse(prompt=text)

            st.subheader('Summary:')
            st.success(summary)
        
        except Exception as e:
            st.error(f"Summarization Failed: {str(e)}")

if __name__== "__main__":
    main()