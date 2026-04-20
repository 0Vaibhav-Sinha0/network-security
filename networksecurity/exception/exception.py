'''This module defines a custom exception class, NetworkSecurityException, which captures the file name and line number where the exception occurred for better debugging. The class inherits from the built-in Exception class and takes an error message and error details (using sys) as input. The __str__ method is overridden to provide a formatted string representation of the error, including the file name, line number, and error message. This custom exception can be used throughout the network security project to provide more informative error messages and facilitate easier debugging.'''

import sys


class NetworkSecurityException(Exception):
    """Custom exception class that captures file name and line number for better debugging."""

    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)

        _, _, exc_tb = error_details.exc_info()

        if exc_tb is not None:
            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.lineno = exc_tb.tb_lineno
        else:
            self.file_name = None
            self.lineno = None

        self.error_message = error_message

    def __str__(self):
        return (
            f"Error occurred in script [{self.file_name}] "
            f"at line [{self.lineno}] : {self.error_message}"
        )