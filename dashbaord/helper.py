import random
import string
from django.utils.text import slugify


def generate_str(n):
    return ''.join(random.choices(string.ascii_lowercase+string.digits,k=n))


def generate_referal_code(text):
    return text + generate_str(5)
    
    