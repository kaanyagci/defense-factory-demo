"""Administrative commands for the invoice service."""
import argparse
import hashlib
import secrets
from storage import create_database


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("seed", help="Create example organizations and invoices")
    token_parser = commands.add_parser("issue-token", help="Issue a credential for a user")
    token_parser.add_argument("user_id")
    args = parser.parse_args()
    db = create_database()
    if args.command == "seed":
        db.executemany("INSERT OR IGNORE INTO memberships VALUES (?, ?)", [("alice", "acme"), ("bob", "globex")])
        db.executemany("INSERT OR IGNORE INTO invoices VALUES (?, ?, ?, ?)", [
            ("inv-100", "acme", "Acme customer", 12500),
            ("inv-200", "globex", "Globex customer", 87000),
        ])
        db.commit()
    else:
        if not db.execute("SELECT 1 FROM memberships WHERE user_id = ?", (args.user_id,)).fetchone():
            parser.error("unknown user")
        token = secrets.token_urlsafe(32)
        db.execute("INSERT INTO api_credentials VALUES (?, ?)", (hashlib.sha256(token.encode()).hexdigest(), args.user_id))
        db.commit()
        print(token)
    db.close()


if __name__ == "__main__":
    main()
