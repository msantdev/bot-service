import re
import logging
from datetime import datetime
from app.models import Category
from app.utils.supabase_client import supabase

def process_expense_message(message):
    try:
        logging.debug(f"Processing message: {message}")
        message_lower = message.lower()

        category = "Other"
        amount = 0.0

        # Load categories and their keywords
        response = supabase.table('categories').select('*').execute()
        categories_dict = {cat['name']: cat['keywords'] for cat in response.data}
        logging.debug(f"Categories and Keywords: {categories_dict}")

        # Initialize variables to store best match
        best_category = "Other"
        max_keywords_matched = 0

        # Iterate through categories to find the best match based on keywords
        for cat_name, keywords in categories_dict.items():
            keywords_set = set(keywords)  # Convert keywords to a set
            matched_keywords = sum(keyword in message_lower for keyword in keywords_set)

            if matched_keywords > max_keywords_matched:
                best_category = cat_name
                max_keywords_matched = matched_keywords

        category = best_category
        logging.debug(f"Best category match: {category}")

        # Extract amount
        amount_match = re.search(r'\b\d+(\.\d{1,2})?\b', message_lower)
        if amount_match:
            amount = float(amount_match.group())
            logging.debug(f"Extracted amount: {amount}")
        else:
            logging.debug("No amount found in message")
            return False, None, None

        return True, category, amount

    except Exception as e:
        logging.error(f"Error processing expense message: {e}", exc_info=True)
        return False, None, None
