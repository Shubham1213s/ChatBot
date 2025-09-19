from datetime import datetime, timedelta

def chatbot(query, invoices):
    """Answer user queries based on parsed invoice data."""
    today = datetime(2019, 2, 24)  # fixed date for demo
    response = ""

    if "due in the next 7 days" in query.lower():
        upcoming = []
        for inv in invoices:
            if inv["due_date"]:
                due = datetime.strptime(inv["due_date"], "%d/%m/%Y")
                if today <= due <= today + timedelta(days=7):
                    upcoming.append(inv)
        if upcoming:
            response = f"{len(upcoming)} invoice(s): " + ", ".join(
                [f'{i["vendor"]}, due {i["due_date"]}, ${i["total"]}' for i in upcoming]
            )
        else:
            response = "No invoices due in the next 7 days."

    elif "total value of the invoice from" in query.lower():
        vendor = query.split("from")[-1].strip().rstrip("?")
        for inv in invoices:
            if inv["vendor"].lower() == vendor.lower():
                response = f"${inv['total']:.2f}"
                break
        else:
            response = f"No invoice found from {vendor}."

    elif "vendors with invoices >" in query.lower():
        try:
            threshold = float(query.split(">")[-1].replace("$", "").strip())
            vendors = [f'{i["vendor"]} (${i["total"]})' for i in invoices if i["total"] > threshold]
            response = ", ".join(vendors) if vendors else "No vendors found."
        except:
            response = "Couldn't understand the threshold amount."

    else:
        response = "I can answer about due invoices, totals, and vendors."

    return response
