# to handle file operations such as reading, writing, and listing files.
# Supports TXT, PDF, and DOCX formats, including table extraction

import os
import sys
from io import BytesIO
import PyPDF2
import pdfplumber
import docx
from src.logger import logging
from src.exception import Custom_Exception

class FileHandler:
    @staticmethod
    def read_pdf(file_obj):
        try:
            text


    @staticmethod
    def read_file(file_obj,file_type):
        try:
            if file_type =='txt':
                return file_obj.read().decode('utf-8')
            elif file_type == 'pdf':
                return FileHandler.read


        except Exception as e:
            raise Custom_Exception(e,sys)