"""
Exceptions file
"""


class RefuelException(Exception):
    """
    Exception raised when refueling fails.

    Args:
        message (str): Custom error message. Defaults to "Too much".
    """

    def __init__(self, message="Too much"):
        self.message = message
        super().__init__(self.message)


class DescendException(Exception):
    """
    Exception raised when descending fails.

    Args:
        message (str): Custom error message. Defaults to "Altitude cannot be less than 0".
    """

    def __init__(self, message="Altitude cannot be less than 0"):
        self.message = message
        super().__init__(self.message)


class AscendException(Exception):
    """
    Exception raised when ascending fails.

    Args:
        message (str): Custom error message. Defaults to "Too high".
    """

    def __init__(self, message="Too high"):
        self.message = message
        super().__init__(self.message)
