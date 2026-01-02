import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("./decorator.log", "a")
logger.addHandler(file_handler)


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"function: {func.__name__}")
        if args:
            logger.info(f"positional parameters: {list(args)}")
        else:
            logger.info("positional parameters: none")
        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")
        result = func(*args, **kwargs)
        logger.info(f"return: {result}")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")


say_hello()

@logger_decorator
def func_with_positional(*args):
    return True

func_with_positional(1, "two", 3.14)

@logger_decorator
def func_with_keywords(**kwargs):
    return logger_decorator

func_with_keywords(a=1, b=2)

      