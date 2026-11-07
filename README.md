# Defense factory sample

This small, intentionally vulnerable Python example demonstrates missing object-level authorization. It is local-only and uses fabricated data. Do not deploy it or put real data in it.

Run `python3 -m unittest -v`. The cross-user and missing-identity tests are expected to fail before remediation; owner access and missing-document tests should pass.

The function assumes its caller has authenticated the user; that assumption and the missing authorization check are the scope of this example. No network service or identity provider is included.
