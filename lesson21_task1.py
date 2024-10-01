"""
Create your own class, which can behave like a built-in function open(). Also, you need to extend its functionality
with counter and logging. Pay special attention to the implementation of __exit__ method, which has to cover all the
requirements to context managers mentioned here:
"""

import logging

# Configure logging to show only the message
logging.basicConfig(level=logging.INFO)


class CustomOpen:
    """Custom context manager that duplicates built-in function open() with logging & counter."""

    def __init__(self, file, mode='r'):
        self.file = file
        self.mode = mode
        self.file_handle = None
        self.counter = 0

    def __enter__(self):
        # Open the file & increment the counter
        self.file_handle = open(self.file, self.mode)
        self.counter += 1
        logging.info(f"Opened file: {self.file} | Count: {self.counter}")
        return self.file_handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the file handle
        if self.file_handle:
            self.file_handle.close()
            logging.info(f"Closed file: {self.file}")

        # Handle exceptions
        if exc_type:
            logging.error(f"Exception occured: {exc_val}")
            return False
        return True

