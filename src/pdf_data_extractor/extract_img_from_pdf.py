


def extract_images_from_pdf(pdf_path: str, output_dir: str = "./") -> None:
    """
    Extract all images from a PDF file and save them to a specified directory.

    Args:
        pdf_path (str): Path to the input PDF file.
        output_dir (str): Directory where extracted images will be saved.

    Returns:
        None
    """
    # PyMuPDF library for working with PDF files
    import fitz  
    # For file and directory operations
    import os    
    # Create output directory if it does not exist
    os.makedirs(output_dir, exist_ok=True)

    # Open the PDF file safely using context manager
    with fitz.open(pdf_path) as doc:

        # Loop through each page of the PDF
        for page_index, page in enumerate(doc):

            # Get all images from the current page
            for img_index, img in enumerate(page.get_images()):

                # xref is the internal reference number of the image inside the PDF
                xref = img[0]

                # Extract image data using xref
                base_image = doc.extract_image(xref)

                # Raw image bytes
                image_bytes = base_image["image"]

                # Image file extension (png, jpeg, etc.)
                image_ext = base_image["ext"]

                # Create unique filename for each extracted image
                filename = f"image_page{page_index}_img{img_index}.{image_ext}"

                # Build full file path in a cross-platform safe way
                filepath = os.path.join(output_dir, filename)

                # Save image to disk in binary mode
                with open(filepath, "wb") as f:
                    f.write(image_bytes)
