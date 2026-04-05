#logger.py
# Import logging to configure and use application-wide logging
import logging  # logging is a standard library module for log messages

# Import sys to direct logs to standard output if needed
import sys  # sys is a standard library module providing access to system-specific parameters


# Define a function to configure and return a logger instance
def get_logger(name: str) -> logging.Logger:
    # Create or retrieve a logger with the given name
    logger = logging.getLogger(name)

    # Set the minimum log level to INFO (can be changed to DEBUG for more detail)
    logger.setLevel(logging.INFO)

    # Check if the logger already has handlers to avoid duplicate logs
    if not logger.handlers:
        # Create a stream handler to send logs to standard output (console)
        handler = logging.StreamHandler(sys.stdout)

        # Define a log message format including time, level, logger name, and message
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

        # Attach the formatter to the handler
        handler.setFormatter(formatter)

        # Add the handler to the logger
        logger.addHandler(handler)

    # Return the configured logger instance
    return logger
