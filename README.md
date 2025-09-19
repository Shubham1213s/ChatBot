# ChatBot
Chatbot Invoice Parsing

A Python-based chatbot that parses invoice documents (PDFs or images) and extracts key information such as vendor, invoice number, invoice date, due date, and total amount. It uses **Tesseract OCR** and regex for text extraction and parsing.

## Requirements

- Python 3.8+

- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
  (This version is well-maintained for Windows.)

- Python libraries:
  ```
  pip install pytesseract pdf2image pillow regex
  ```
## Installation

1. Clone the repository:

```bash
git clone https://github.com/Shubham1213s/ChatBot.git
```

2. Install Python dependencies:
```
pip install -r requirements.txt
```

3. Install Tesseract OCR:

Windows:
 - Install Tesseract.
 - Press Win + R, type sysdm.cpl, go to Advanced → Environment Variables.
 - In System variables, add a new variable:
   ```
   Variable name: TESSDATA_PREFIX
   Variable value: C:\Program Files\Tesseract-OCR\
   ```
  - Add C:\Program Files\Tesseract-OCR to your PATH variable.
  - Restart your terminal or IDE.


