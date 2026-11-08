"""Render a requested invoice as CSV."""
import csv
import io
from storage import find_invoice


def invoice_csv(db, organization_id, invoice_id):
    invoice = find_invoice(db, invoice_id)
    if invoice is None:
        return None
    output = io.StringIO(newline="")
    writer = csv.writer(output)
    writer.writerow(["invoice_id", "organization", "customer", "amount_cents"])
    writer.writerow([invoice["id"], invoice["organization_id"], invoice["customer"], invoice["amount_cents"]])
    return output.getvalue()
