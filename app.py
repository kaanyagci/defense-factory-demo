"""A deliberately vulnerable, local-only document lookup demo."""

DOCUMENTS = {
    "report-1": {"owner": "alice", "body": "Alice's planning notes"},
    "report-2": {"owner": "bob", "body": "Bob's planning notes"},
}


def get_document(authenticated_user, document_id):
    """Look up a document for a previously authenticated caller.

    Deliberate flaw: the caller's identity is not checked against the owner.
    This is a self-contained teaching fixture, not a deployable service.
    """
    return DOCUMENTS.get(document_id)
