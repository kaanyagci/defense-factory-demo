# Defense factory sample

This small, intentionally vulnerable Python example is local-only and uses fabricated data. Do not deploy it or put real data in it.

It requires Python 3 and uses only the standard library. Run the example from this directory:

```sh
python3 demo.py --user alice --document report-1
```

The `--user` argument simulates an already authenticated caller; it is not authentication.

The function assumes its caller has authenticated the user. No network service or identity provider is included.
