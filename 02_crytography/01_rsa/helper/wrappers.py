from flask import request, jsonify
from functools import wraps


def api_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = None
        if 'api_key' in request.headers:
            api_key = request.headers['api_key']

        if not api_key:
            return jsonify({'message': 'API key is missing!'}), 401

        if api_key != "a3f5e01a-613e-4647-b9db-c550acdd1df3":
            return jsonify({'message': 'API key is invalid!'}), 401

        return f(*args, **kwargs)
    return decorated
