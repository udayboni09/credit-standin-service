#config.py
# Import os to read environment variables for configuration
import os  # os is a standard library module for interacting with the operating system

# Import typing for type hints
from typing import Optional  # typing is a standard library module for type annotations


# Define a function to get a configuration value from environment variables
def get_config(key: str, default: Optional[str] = None) -> Optional[str]:
    # Use os.getenv to read the environment variable with the given key
    # If the variable is not set, return the provided default value
    return os.getenv(key, default)
