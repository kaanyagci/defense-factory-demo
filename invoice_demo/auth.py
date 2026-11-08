"""Demo-only identity and organization membership."""
from functools import wraps
from flask import abort, g, request
from storage import is_member

DEMO_IDENTITIES = {"demo-alice": "alice", "demo-bob": "bob"}


def require_organization_member(db):
    def decorate(view):
        @wraps(view)
        def wrapped(organization_id, *args, **kwargs):
            scheme, _, token = request.headers.get("Authorization", "").partition(" ")
            user_id = DEMO_IDENTITIES.get(token) if scheme == "Bearer" else None
            if not user_id:
                abort(401)
            if not is_member(db, user_id, organization_id):
                abort(403)
            g.user_id = user_id
            return view(organization_id, *args, **kwargs)
        return wrapped
    return decorate
