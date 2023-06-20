"""
Decorator and logger function
"""
import logging
from functools import wraps


def log_exception(problem, log_file, func_name):
    """
    Logs the exception to a log file.

    :param problem: The exception that occurred during the function execution.
    :param log_file: The path to the log file.
    :param func_name: The name of the function where the exception occurred.
    """
    my_logger = logging.getLogger('exception_logger')
    my_logger.setLevel(logging.ERROR)
    file_handler = next((handler for handler in my_logger.handlers if isinstance(handler, logging.FileHandler)), None)
    if file_handler is None:
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        my_logger.addHandler(file_handler)
    log_message = f"Exception in function {func_name}: {problem.__class__.__name__} {problem.message}"
    my_logger.error(log_message)


# pylint: disable=inconsistent-return-statements
def logger(exception_type, mode):
    """
    Decorator to log exceptions raised by a function.

    :param exception_type: The type of exception to catch.
    :param mode: The logging mode ('console' or 'file').
    :return: The decorated function.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_type as problem:
                if mode == "console":
                    logging.error(f"Exception in function {func.__name__}: {problem.__class__.__name__} " + \
                                  f"{problem.message}")
                elif mode == "file":
                    log_exception(problem, "logs.txt", func.__name__)

        return wrapper

    return decorator
