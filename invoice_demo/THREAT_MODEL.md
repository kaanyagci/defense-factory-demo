# Invoice service: hypothetical production context

This document describes an imagined production use case for the teaching example. The code in this repository is a local-only, intentionally vulnerable demo with fictional records and mock tokens. It is not deployed as the service described below.

Imagine a hosted invoice portal serving many customer organizations. Each organization stores invoices containing customer names, amounts, and other confidential billing details. Signed-in members can export invoices belonging to their own organization. A production identity provider would establish each user's identity; organization membership would determine which invoices that user may access.

The security boundary is between customer organizations: membership in one organization must not allow a user to view or export another organization's invoices, even if they know an invoice identifier. The application should authorize the requested invoice against the same organization for which membership was checked.

For the local exercise, authentication is simulated by fixed, public demo tokens and the database contains fictional data. The example does not implement a production identity provider or prove that any real service is exposed.
