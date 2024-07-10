from flask import Blueprint, request, jsonify
import logging
from app.controllers.expense_controller import process_webhook_data
from app.middlewares.authMiddleware import api_key_required

webhook_bp = Blueprint('webhook_bp', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
@api_key_required
def webhook():
    try:
        data = request.json
        logging.debug(f"Received data: {data}")
        
        return process_webhook_data(data)

    except Exception as e:
        logging.error(f"Error processing webhook: {e}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
