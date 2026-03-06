# src/utils/logger.py
import logging

def setup_logger(name):
    """Sets up the logger."""
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger

# Usage in scripts
logger = setup_logger('healthcare_logger')
