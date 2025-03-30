import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)

def retry_with_backoff(max_tries=3, base_delay=1):
    """Retry decorator with exponential backoff"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tries = 0
            while tries < max_tries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    tries += 1
                    if tries == max_tries:
                        logger.error(f"Max retries reached for {func.__name__}: {str(e)}")
                        raise
                    
                    delay = base_delay * (2 ** (tries - 1))  # Exponential backoff
                    logger.warning(
                        f"Attempt {tries} failed for {func.__name__}: {str(e)}. "
                        f"Retrying in {delay} seconds..."
                    )
                    time.sleep(delay)
            return None
        return wrapper
    return decorator 