import functools
import time
from loguru import logger


def user_repeat_non_stop(func):
    @functools.wraps(func)
    def wrapper(self):
        while True:
            try:
                return func(self)
            except Exception as error:
                logger.error(error)
    return wrapper


def error_logger(func):
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            pach = str(func).partition('<function')[2].partition(' at ')[0]
            logger.error(f"Functions {pach}: {error}")
            return False

    return wrapped


def error_scripts(func):
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            pach = str(func).partition('<function')[2].partition(' at ')[0]
            logger.error(f'Scripts {pach}: {error}')
            return [0, time.time() + 500]
    return wrapped
