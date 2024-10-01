"""
Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many
use cases as you can, positive ones when a file exists and everything works as designed. And also, write tests when
your class raises errors or you have errors in the runtime context suite.
"""

import pytest
import os
from lesson21_task1 import CustomOpen


@pytest.fixture
def temp_file():
    """Temp file for testing"""
    test_file = "test_file.txt"
    with open(test_file, "w") as f:
        f.write("Test message!")
    yield test_file

    # Clean up
    if os.path.exists(test_file):
        os.remove(test_file)


def test_writing(temp_file):
    """Test that the file can be opened & written to"""
    with CustomOpen(temp_file, "w") as f:
        f.write("Test message!")

    # Verification
    with CustomOpen(temp_file, "r") as f:
        content = f.read()
    assert content == "Test message!"


def test_open_non_existent_file():
    """Test that attempting to open a non-existent file raises an error"""
    with pytest.raises(FileNotFoundError):
        with CustomOpen('non_existent_file.txt', 'r'):
            pass  # Context manager should raise an error


def test_write_error_handling():
    """Test that writing to a file that can't be opened raises an error."""
    # Attempt to write to a non-existent directory
    with pytest.raises(FileNotFoundError):
        with CustomOpen('non_existent_directory/test_file.txt', 'w'):
            pass  # Context manager should raise an error


if __name__ == '__main__':
    pytest.main()
