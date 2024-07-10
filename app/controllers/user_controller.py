from flask import jsonify
from app.database import supabase  

def get_user_by_telegram_id(telegram_user_id):
    try:
        result = supabase.table('users').select('*').eq('telegram_id', str(telegram_user_id)).limit(1).execute()
        
        if result['error']:
            return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
        
        user = result['data'][0] if result['data'] else None
        
        if not user:
            return jsonify({'status': 'error', 'message': 'User not found'}), 404
        
        return jsonify({'status': 'success', 'user': user}), 200
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
