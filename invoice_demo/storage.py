"""In-memory SQLite fixture for the invoice export demo."""
import sqlite3


def create_database():
    db = sqlite3.connect(":memory:", check_same_thread=False)
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE memberships (user_id TEXT NOT NULL, organization_id TEXT NOT NULL,
                                  PRIMARY KEY (user_id, organization_id));
        CREATE TABLE invoices (id TEXT PRIMARY KEY, organization_id TEXT NOT NULL,
                               customer TEXT NOT NULL, amount_cents INTEGER NOT NULL);
        INSERT INTO memberships VALUES ('alice', 'acme'), ('bob', 'globex');
        INSERT INTO invoices VALUES
            ('inv-100', 'acme', 'Acme sample customer', 12500),
            ('inv-200', 'globex', 'Globex sample customer', 87000);
    """)
    db.commit()
    return db


def is_member(db, user_id, organization_id):
    return db.execute(
        "SELECT 1 FROM memberships WHERE user_id = ? AND organization_id = ?",
        (user_id, organization_id),
    ).fetchone() is not None


def find_invoice(db, invoice_id):
    return db.execute(
        "SELECT id, organization_id, customer, amount_cents FROM invoices WHERE id = ?",
        (invoice_id,),
    ).fetchone()
