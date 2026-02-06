# PDF Data Extractor

Python package to extract **text, words, tables, and images** from PDF files.  
Supports both simple PDFs and complex PDFs with tables and structured layouts.

---

## Features

- ✅ Simple text extraction using **PyPDF2**
- ✅ Complex structured extraction (words, tables) using **pdfplumber**
- ✅ Image extraction using **PyMuPDF**
- 🏗️ Supports `src` layout and pip-installable as a package

---

## Installation

Install the package locally using pip:

```bash
pip install .
````

Or install dependencies manually:

```bash
pip install PyPDF2 pdfplumber pymupdf Pillow
```

---

## Usage

### 1️⃣ Extract Text from Simple PDF

```python
from pdf_data_extractor import simple_pdf_reader

pdf_data = simple_pdf_reader("example.pdf")
print(pdf_data["text"])
print(pdf_data["meta_data"])
```

---

### 2️⃣ Extract Structured Data from Complex PDF

```python
from pdf_data_extractor import complex_pdf_reader

pdf_data = complex_pdf_reader("example_complex.pdf")

# Full text
print(pdf_data["text"])

# Word-level data
print(pdf_data["words"])

# Tables
print(pdf_data["tables"])
```

---

### 3️⃣ Extract Images from PDF

```python
from pdf_data_extractor import extract_images_from_pdf

extract_images_from_pdf("example.pdf", "./images/")
```

> Extracted images are saved in the specified folder with their original format.

---

## Project Structure

```
pyPDF/
├── src/
│   └── pdf_data_extractor/
│       ├── __init__.py
│       ├── extract_img_from_pdf.py
│       ├── extract_text_simple.py
│       └── pdf_reader.py
├── README.md
├── pyproject.toml
```

---

## Dependencies

* Python >= 3.9
* PyPDF2 >= 3.0.0
* pdfplumber >= 0.11.0
* pymupdf >= 1.23.0
* Pillow >= 10.0.0

---

## Notes & Limitations

* ❌ OCR is **not supported**. Image-based PDFs require an OCR tool like Tesseract.
* ❌ Table extraction depends on PDF structure; poorly formatted PDFs may produce inaccurate results.
* For advanced users: You can integrate this package into pipelines for automation or data analysis.
