"""SQLite storage for invoice exports."""
import hashlib
import os
import sqlite3
from pathlib import Path


def create_database():
    path = Path(os.environ.get("INVOICE_DB_PATH", Path(__file__).resolve().parent / "data" / "invoices.sqlite3"))
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, check_same_thread=False)
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE IF NOT EXISTS memberships (user_id TEXT NOT NULL, organization_id TEXT NOT NULL,
                                  PRIMARY KEY (user_id, organization_id));
        CREATE TABLE IF NOT EXISTS invoices (id TEXT PRIMARY KEY, organization_id TEXT NOT NULL,
                               customer TEXT NOT NULL, amount_cents INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS api_credentials (token_digest TEXT PRIMARY KEY, user_id TEXT NOT NULL);
    """)
    db.commit()
    return db


def user_for_token(db, token):
    digest = hashlib.sha256(token.encode()).hexdigest()
    row = db.execute("SELECT user_id FROM api_credentials WHERE token_digest = ?", (digest,)).fetchone()
    return row["user_id"] if row else None


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
