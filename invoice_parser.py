import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import re

# Path to tesseract (Windows only – adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def parse_invoice(file_path):
    """Extract vendor, invoice number, dates, and total from invoice."""
    # Convert PDF to image if needed
    if file_path.endswith(".pdf"):
        images = convert_from_path(file_path)
        image = images[0]
    else:
        image = Image.open(file_path)

    text = pytesseract.image_to_string(image)

    # Regex extraction (simple demo logic)
    vendor = re.search(r'^(.*?)(?:INVOICE|Invoice)', text, re.MULTILINE | re.IGNORECASE)
    invoice_number = re.search(r'(?:Invoice #|Tax Invoice #|INV[-\s]*)(\S+)', text, re.IGNORECASE)
    total = re.search(r'(?:TOTAL|Total)[:\s]*[R$]?([0-9,]+\.\d{2})', text, re.IGNORECASE)
    due_date = re.search(r'Due Date[:\s]*([0-9]{2}/[0-9]{2}/[0-9]{4})', text)
    invoice_date = re.search(r'Invoice Date[:\s]*([0-9]{2}/[0-9]{2}/[0-9]{4})', text)

    return {
        "vendor": vendor.group(1) if vendor else "Unknown",
        "invoice_number": invoice_number.group(0) if invoice_number else "",
        "invoice_date": invoice_date.group(1) if invoice_date else "",
        "due_date": due_date.group(1) if due_date else "",
        "total": float(total.group(1).replace(",", "")) if total else 0.0
    }



