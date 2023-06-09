import random
import string


def random_lowercase_string(len=32) -> str:
    """Random string generation for testing.
    """
    return "".join(random.choices(string.ascii_lowercase, k=len))
    

def random_email(len=32) -> str:
    """Generating a random email address for testing.
    """
    return f"{random_lowercase_string(len)}@gmail.com"
