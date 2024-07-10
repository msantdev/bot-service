from flask import jsonify
from datetime import datetime
import logging
from app.services.expense_service import process_expense_message
from app.services.user_service import get_user_by_telegram_id
from app.utils.supabase_client import supabase

def process_webhook_data(data):
    try:
        message = data.get('message', {}).get('text')
        telegram_user_id = data.get('message', {}).get('from', {}).get('id')

        success, category, amount = process_expense_message(message)

        if success:
            user = get_user_by_telegram_id(telegram_user_id)
            if not user:
                return jsonify({'status': 'error', 'message': 'User not found'}), 404

            category_obj = supabase.table('categories').select('*').eq('name', category).execute().data[0]

            new_expense = {
                "user_id": user['id'],
                "description": message,
                "amount": amount,
                "category_id": category_obj['id'],
                "added_at": datetime.now().isoformat()
            }
            supabase.table('expenses').insert(new_expense).execute()

            response_message = f'{category} expense added ✅'
            logging.info(response_message)
            return jsonify({'status': 'success', 'message': response_message}), 200
        else:
            logging.debug("Failed to process expense")
            return jsonify({'status': 'error', 'message': 'Failed to process expense'}), 400

    except Exception as e:
        logging.error(f"Error processing webhook data: {e}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
