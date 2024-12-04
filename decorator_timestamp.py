import logging
from functools import wraps

logging.basicConfig(
    filename="function.log",
    format="%(levelname)s %(name)s %(asctime)s %(message)s",
    datefmt="%X-%x",
    level=logging.DEBUG,
)

def timestamp(original_function):

    @wraps(original_function)
    def _(*args, **kwargs):
        logging.debug("called function %s", original_function.__name__)
        original_function(*args, **kwargs)

    return _


@timestamp
def spam(n):
    print("spam" * n)

# spam = timestamp(spam)

@timestamp
def ham():
    print("ham ham ham")

spam(5)  # calls _()
ham()   # calls _()
ham()
spam(3)

print(f"{spam.__name__ = }")
print(f"{ham.__name__ = }")
