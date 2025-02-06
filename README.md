# Custom Logger

A Python logging library that provides colored console output with sound effects.

## Installation

To install the package locally:

```bash
pip install -e .
```

## Usage

```python
from custom_logger import CustomLogger

logger = CustomLogger()

# Different types of logs
logger.info("This is an info message")
logger.debug("This is a debug message")
logger.warning("This is a warning message")
logger.success("This is a success message")
logger.error("This is an error message")  # This will also play a sound

# Logs with countdown timer
logger.info("This message will show a 3-second countdown", seconds=3)

# Logs with overwrite
logger.info("This message will be overwritten", overwrite=True)
```