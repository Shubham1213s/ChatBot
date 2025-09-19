# ChatBot
Chatbot Invoice Parsing

A Python-based chatbot that parses invoice documents (PDFs or images) and extracts key information such as vendor, invoice number, invoice date, due date, and total amount. It uses **Tesseract OCR** and regex for text extraction and parsing.

## How It Works

- After uploading your invoices or selecting them from a source, the chatbot parses and indexes the data.
- You can then query the data in natural language.
- The bot returns structured answers based on your question.

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
   - Press `Win + R`, type `sysdm.cpl`, go to Advanced → Environment Variables.
   - In System variables, add a new variable:
     ```
     Variable name: TESSDATA_PREFIX
     Variable value: C:\Program Files\Tesseract-OCR\
     ```
    - Add C:\Program Files\Tesseract-OCR to your PATH variable.
    - Restart your terminal or IDE.

## Folder Structure 

   invoice-chatbot:
   - │── invoices/ # Sample invoices (PDF/image) for testing
   - │── parsed_invoices.json # Output file storing extracted structured data
   - │── main.py # Entry point to run the chatbot
   - │── chatbot.py # Chatbot interface logic (Q&A)
   - │── invoice_parser.py # OCR + parsing logic
   - │── requirements.txt # Python dependencies
   - │── README.md # Instructions + Example Q&A

## Instructions and Example Q&A

1. Run the chatbot and select invoice files using a file dialog:

```bash
python main.py
```

2. A file selection window will open. Choose one or multiple invoices (PDF, PNG, or JPG).
3. The invoices will be parsed and saved to: `parsed_invoices.json`
4. After parsing, the interactive chatbot will start. You can ask questions like:

```
How many invoices are due in the next 7 days?
```
Ans: 1 invoice(s): East Repair In , due 26/02/2019, $145.0

```
What is the total value of the invoice from East Repair In ?
```
Ans: $145.00

```
List all vendors with invoices > $140
```
Ans: East Repair In ($145.0)

5. Exit
 
- Type `exit` to close the chatbot.  
- The chatbot answers queries based on the invoices you selected.



