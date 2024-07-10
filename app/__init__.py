from flask import Flask
from app.routes.webhook import webhook_bp
import logging
import logging.config
from app.config import Config
from app.utils.supabase_client import supabase

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    app.register_blueprint(webhook_bp, url_prefix='/')
    
    logging.config.dictConfig(Config.LOGGING_CONFIG)
    
    return app
