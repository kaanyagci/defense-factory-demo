# Invoice export demo

This intentionally vulnerable teaching application uses fictional organizations, users, tokens, and invoices. It simulates authentication and stores data in a local SQLite database. Run it locally only; do not deploy it or use real data.

For the hypothetical production scenario and its intended access boundary, see [THREAT_MODEL.md](THREAT_MODEL.md).

```sh
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python app.py
```

In another terminal, request a sample export:

```sh
curl -H 'Authorization: Bearer demo-alice' \
  http://127.0.0.1:5000/api/organizations/acme/invoices/inv-100/export
```

`demo-alice` represents Alice, a member of Acme; `demo-bob` represents Bob, a member of Globex. These fixed tokens are mock data, not an authentication system. The database persists in `data/invoices.sqlite3`; to reset it, stop the app and delete that file.
