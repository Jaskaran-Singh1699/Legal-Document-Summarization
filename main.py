# Purpose of main.py:
# It will serve as the backend logic of the project.
# It will integrate FileHandler (from utils.py) and ResponseGeneration (from summarizer.py).
# It will act as a bridge between file processing and AI-based summarization.


import os
import sys
from src.utils import FileHandler
from src.summarizer import ResponseGeneration
from src.exception import Custom_Exception
from src.logger import logging

def process_file(file_obj,file_type):
    logging.info('Entered Processing File main')
    try:
        extracted_text= FileHandler.read_file(file_obj,file_type)
        if "Error" in extracted_text:
            return {'Error:':extracted_text}
        summary=ResponseGeneration.GeminiResponse(extracted_text)
        return {'extracted_text':extracted_text,'summary':summary}
    except Exception as e:
        raise Custom_Exception(e,sys)