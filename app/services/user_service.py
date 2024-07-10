from app.utils.supabase_client import supabase

def get_user_by_telegram_id(telegram_id):
    response = supabase.table('users').select('*').eq('telegram_id', str(telegram_id)).execute()
    if response.data:
        user_data = response.data[0]
        return user_data
    return None
