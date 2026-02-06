# Exporting Data (Text) From PDF

def pdf_reader(pdf_address: str, pdf_password: str = None) -> dict:
    """
    Read text and metadata from a PDF file.

    Args:
        pdf_address (str): Path to the PDF file.
        pdf_password (str, optional): Password for encrypted PDFs. Defaults to None.

    Returns:
        dict: Dictionary containing extracted text, metadata, and PDF header.
    """

    # Import inside function to reduce global dependency load
    from PyPDF2 import PdfReader

    # Initialize PDF reader with optional password
    reader = PdfReader(pdf_address, password=pdf_password)

    # Variable to store extracted text
    text = ""

    # Iterate through all pages and extract text
    for page in reader.pages:
        # extract_text() returns text content of each page
        text += page.extract_text()

    # Store extracted data in dictionary structure
    pdf_data_dict = {
        "text": text,                 # Full extracted text from all pages
        "meta_data": reader.metadata, # PDF metadata (author, title, etc.)
        "pdf_header": reader.pdf_header  # PDF version/header information
    }

    return pdf_data_dict
