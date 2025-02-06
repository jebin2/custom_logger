# custom_logger/__init__.py
from .logger import CustomLogger

# Create a default instance
logger_config = CustomLogger()

# You can export both the class and the default instance
__all__ = ['CustomLogger', 'logger_config']