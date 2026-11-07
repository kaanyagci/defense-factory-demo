# Defense factory sample

This small, intentionally vulnerable Python example demonstrates missing object-level authorization. It is local-only and uses fabricated data. Do not deploy it or put real data in it.

It requires Python 3 and uses only the standard library. Run the example from this directory:

```sh
python3 demo.py --user alice --document report-1
```

Try `python3 demo.py --user alice --document report-2` to see the flaw: Alice can read Bob's mock document. The `--user` argument simulates an already authenticated caller; it is not authentication.

The function assumes its caller has authenticated the user; that assumption and the missing authorization check are the scope of this example. No network service or identity provider is included.
