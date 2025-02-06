# test_logger_config.py

from custom_logger import logger_config
import time

def test_logger():

    logger_config.info("This is an info message")
    time.sleep(1)
    
    logger_config.debug("This is a debug message")
    time.sleep(1)
    
    logger_config.warning("This is a warning message")
    time.sleep(1)
    
    logger_config.success("This is a success message")
    time.sleep(1)
    
    logger_config.error("This is an error message")
    time.sleep(1)

    logger_config.info("This message will have a 3 second countdown", seconds=3)

    logger_config.info("This message will be overwritten in 2 seconds")
    time.sleep(2)
    logger_config.info("This message overwrites the previous one", overwrite=True)

    for i in range(3):
        logger_config.info(f"Processing item {i+1}")
        time.sleep(1)

    logger_config.error("This error message should play a sound")
    logger_config.error("This error message with no sound", play_sound=False)

if __name__ == "__main__":
    test_logger()