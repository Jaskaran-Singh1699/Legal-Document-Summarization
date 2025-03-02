# Implement a function to send document text to Gemini Pro and retrieve a summary.
# Handle errors and ensure a clean response.
import os
import sys
import google.generativeai as genai
from src.logger import logging
from src.exception import Custom_Exception
from dotenv import load_dotenv

load_dotenv()
class ResponseGeneration:

    def __init__(self,api_key,model='gemini-1.5-flash-latest'):
        self.api_key=os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            raise ValueError('API Key not found! Set GOOGLE_API_KEY environment variable.')

        self.model=model
        genai.configure(api_key=self.api_key) 
           

    def GeminiResponse(self,prompt):
        logging.info("Entered Gemini Response method")

        try:
            # Send document text to Gemini Pro and retrieve a summary
            model_instance=genai.GenerativeModel(self.model)
            response=model_instance.generate_content(prompt)
            return response.text if response and response.text else 'no response recieved'
        except Exception as e:
            raise Custom_Exception(e,sys)



