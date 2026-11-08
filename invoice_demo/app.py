"""Local demonstration service for exporting mock invoices."""
from flask import Flask, Response, abort
from auth import require_organization_member
from export_service import invoice_csv
from storage import create_database

app = Flask(__name__)
db = create_database()


@app.get("/api/organizations/<organization_id>/invoices/<invoice_id>/export")
@require_organization_member(db)
def export_invoice(organization_id, invoice_id):
    content = invoice_csv(db, organization_id, invoice_id)
    if content is None:
        abort(404)
    return Response(content, content_type="text/csv; charset=utf-8")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False, threaded=False)
