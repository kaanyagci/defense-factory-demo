"""Persistent SQLite storage for the invoice export demo."""
import sqlite3
from pathlib import Path


def create_database():
    data_dir = Path(__file__).resolve().parent / "data"
    data_dir.mkdir(exist_ok=True)
    db = sqlite3.connect(data_dir / "invoices.sqlite3", check_same_thread=False)
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE IF NOT EXISTS memberships (user_id TEXT NOT NULL, organization_id TEXT NOT NULL,
                                  PRIMARY KEY (user_id, organization_id));
        CREATE TABLE IF NOT EXISTS invoices (id TEXT PRIMARY KEY, organization_id TEXT NOT NULL,
                               customer TEXT NOT NULL, amount_cents INTEGER NOT NULL);
        INSERT OR IGNORE INTO memberships VALUES ('alice', 'acme'), ('bob', 'globex');
        INSERT OR IGNORE INTO invoices VALUES
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
