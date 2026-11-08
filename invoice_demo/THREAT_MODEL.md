# Invoice service: product context

This document describes a hypothetical hosted invoice portal. The application in this repository is a local prototype using fictional records and mock tokens; it is not deployed as the hosted service described below.

Imagine a hosted invoice portal serving many customer organizations. Each organization stores invoices containing customer names, amounts, and other confidential billing details. Signed-in members can export invoices belonging to their own organization. A production identity provider would establish each user's identity; organization membership would determine which invoices that user may access.

Each organization manages its own invoices, and signed-in members can export invoices for their organization.

For the local exercise, authentication is simulated by fixed, public demo tokens and the database contains fictional data. The example does not implement a production identity provider or prove that any real service is exposed.
