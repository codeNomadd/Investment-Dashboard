from functools import wraps
from flask import request, jsonify, current_app
from datetime import datetime
import hashlib
import hmac
import secrets
from app.models.api_key import APIKey
from app.extensions import db

def generate_api_key():
    """Generate a secure API key with prefix for easy identification"""
    prefix = 'sk_'
    key = prefix + secrets.token_urlsafe(32)
    key_hash = hashlib.sha256(key.encode()).hexdigest()
    return key, key_hash

def verify_api_key(key_hash, provided_key):
    """Verify API key using constant-time comparison"""
    expected_hash = hashlib.sha256(provided_key.encode()).hexdigest()
    return hmac.compare_digest(key_hash, expected_hash)

class APIKeyAuth:
    def __init__(self, scopes=None, rate_limit="5 per minute"):
        self.scopes = scopes or []
        self.rate_limit = rate_limit

    def require_api_key(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            api_key = request.headers.get('X-API-Key')
            if not api_key:
                return jsonify({
                    'status': 'error',
                    'message': 'Missing API key'
                }), 401

            # Check API key in database
            key_record = APIKey.query.filter_by(
                is_active=True
            ).first()

            if not key_record or not verify_api_key(key_record.key_hash, api_key):
                return jsonify({
                    'status': 'error',
                    'message': 'Invalid API key'
                }), 401

            # Check if key is expired
            if key_record.expires_at and key_record.expires_at < datetime.utcnow():
                return jsonify({
                    'status': 'error',
                    'message': 'API key has expired'
                }), 401

            # Check scopes if specified
            if self.scopes and not all(s in key_record.scopes for s in self.scopes):
                return jsonify({
                    'status': 'error',
                    'message': 'Insufficient permissions'
                }), 403

            # Update last used timestamp
            key_record.last_used_at = datetime.utcnow()
            db.session.commit()

            return f(*args, **kwargs)
        return decorated 