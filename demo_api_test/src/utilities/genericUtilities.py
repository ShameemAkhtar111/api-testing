import random
import string


def generate_random_email_and_password(domain=None,email_prefix=None):

    if not domain:
        domain = "gmail.com"

    if not email_prefix:
        email_prefix = "testuser"

    random_email_string_length = 6
    random_string = ''.join(random.choices(string.ascii_lowercase,k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    random_password_length = 8
    password_string = ''.join(random.choices(string.ascii_letters, k=random_password_length))

    random_info = {'email': email, 'password':password_string}

    return random_info

