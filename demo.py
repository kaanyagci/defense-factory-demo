"""Run the mock document lookup without a web server or external dependencies."""
import argparse
import json

from app import get_document


def main():
    parser = argparse.ArgumentParser(description="Look up a mock document (intentionally vulnerable demo).")
    parser.add_argument("--user", default="alice", help="Simulated authenticated user")
    parser.add_argument("--document", default="report-1", help="Mock document ID")
    args = parser.parse_args()
    print(json.dumps(get_document(args.user, args.document), indent=2))


if __name__ == "__main__":
    main()
