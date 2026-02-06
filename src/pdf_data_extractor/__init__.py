"""
PDF Data Extractor Package

Contains functions to extract:
- Text
- Tables
- Words
- Images
"""

from .extract_img_from_pdf import extract_images_from_pdf
from .extract_text_simple import pdf_reader as simple_pdf_reader
from .pdf_reader import pdf_reader as complex_pdf_reader
