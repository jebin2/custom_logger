from .logger import CustomLogger

import os
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

# Create a default instance
logger_config = CustomLogger()

__all__ = ['CustomLogger', 'logger_config']