from flask import request, jsonify
import os
import logging
from functools import wraps

def api_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        logging.debug('Middleware function called!')
        api_key = request.headers.get('x-api-key')
        if api_key != os.getenv('BOT_SERVICE_API_KEY'):
            logging.warning('Unauthorized access attempt')
            return jsonify({'status': 'error', 'message': 'Unauthorized'}), 403
        return f(*args, **kwargs)
    return decorated_function

