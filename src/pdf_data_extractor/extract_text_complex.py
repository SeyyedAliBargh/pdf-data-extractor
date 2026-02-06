# Exporting Data (Text, Words, Tables) From Complex PDF

def pdf_reader(pdf_address: str) -> dict:
    """
    Extract structured data from complex PDFs using pdfplumber.

    This function extracts:
    - Full text content
    - Word-level data with positional information
    - Tables detected inside the PDF

    Args:
        pdf_address (str): Path to the input PDF file.

    Returns:
        dict: Dictionary containing text, words, and tables extracted from the PDF.
    """

    # Import inside function to avoid forcing dependency at module load
    import pdfplumber

    # Variable to store full extracted text
    text = ""

    # List to store word-level structured data
    # Each item contains word text + coordinates
    words = []

    # List to store extracted tables
    tables = []

    # Open PDF safely using context manager
    with pdfplumber.open(pdf_address) as pdf:

        # Iterate through each page of the PDF
        for page in pdf.pages:

            # Extract plain text from page
            # Note: May return None for image-based PDFs
            page_text = page.extract_text()
            if page_text:
                text += page_text

            # Extract word-level data including positions
            # Useful for layout-aware parsing
            words += page.extract_words()

            # Extract tables detected on the page
            # Returns list of tables (each table is list of rows)
            tables += page.extract_tables()

    # Organize extracted data into dictionary
    pdf_data_dict = {
        "text": text,     # Full combined text from all pages
        "words": words,   # Word-level structured data
        "tables": tables  # Extracted tables
    }

    return pdf_data_dict


