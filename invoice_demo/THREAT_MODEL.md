# Invoice service security boundaries

The invoice service holds billing records for multiple customer organizations. Invoices include customer names and billing amounts. Each user has an individual API credential, and organization membership controls access to that organization's invoice exports. Users must not be able to access invoices belonging to another organization.

API credentials are provisioned by administrators and should be delivered securely to their intended users. The service stores credential hashes and persistent invoice records in SQLite. Network deployments should use TLS at a trusted reverse proxy and restrict access to the database and administrative commands.
