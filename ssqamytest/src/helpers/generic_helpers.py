import random
import string
import logging as logger


def generate_random_email(domain=None, email_prefix=None):
    if not domain:
        domain = 'nadiatest.com'
    if not email_prefix:
        email_prefix = 'testuser'
    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k=random_email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain
    logger.info(f'Generated random email: {email}')
    return email


def generate_random_password():
    random_password_string_length = 20
    random_letters = ''.join(random.choices(string.ascii_letters, k=random_password_string_length))
    random_digits = ''.join(random.choices(string.digits))
    random_password = random_letters + random_digits
    logger.info(f'Random password: {random_password}')
    return random_password