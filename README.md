# Custom Logger

A Python logging library that provides colored console output with sound effects.

## Installation

To install the package locally:

```bash
pip install git+https://github.com/jebin2/custom_logger.git
```

## Usage

```python
from custom_logger import logger_config

# Different types of logs
logger_config.info("This is an info message")
logger_config.debug("This is a debug message")
logger_config.warning("This is a warning message")
logger_config.success("This is a success message")
logger_config.error("This is an error message")  # This will also play a sound

# Logs with countdown timer
logger_config.info("This message will show a 3-second countdown", seconds=3)

# Logs with overwrite
logger_config.info("This message will be overwritten", overwrite=True)
```