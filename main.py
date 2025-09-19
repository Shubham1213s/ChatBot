import json
from tkinter import Tk, filedialog
from invoice_parser import parse_invoice
from chatbot import chatbot

if __name__ == "__main__":
    print("Select invoice files...")
    Tk().withdraw()  # hide empty Tk window
    files = filedialog.askopenfilenames(
        title="Select Invoice Files",
        filetypes=[("PDF/Images", "*.pdf *.png *.jpg")]
    )

    invoices = [parse_invoice(f) for f in files]

    # Save structured data
    with open("parsed_invoices.json", "w") as f:
        json.dump(invoices, f, indent=2)

    print("Invoices parsed and saved to parsed_invoices.json")

    # Interactive chatbot
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        print("Ans", chatbot(query, invoices))
