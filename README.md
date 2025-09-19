# ChatBot
Chatbot Invoice Parsing

A Python-based chatbot that parses invoice documents (PDFs or images) and extracts key information such as vendor, invoice number, invoice date, due date, and total amount. It uses **Tesseract OCR** and regex for text extraction and parsing.

## Requirements

- Python 3.8+

- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
  (This version is well-maintained for Windows.)

- Install it (default location usually is:
  C:\Program Files\Tesseract-OCR\tesseract.exe)

- Add the path to your environment variables:
- Press Win + R → type sysdm.cpl → Advanced → Environment Variables
- Add a new variable in System variables:
  TESSDATA_PREFIX = C:\Program Files\Tesseract-OCR\
- Add C:\Program Files\Tesseract-OCR to your PATH. 
- Restart your terminal/IDE.

- Python libraries:
  pip install pytesseract pdf2image pillow regex





