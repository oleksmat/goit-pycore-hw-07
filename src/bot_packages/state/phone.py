from re import match

from .field import Field

def check_phone(phone_str: str) -> bool:
    """
    Validate that `phone_str` is a phone string.

    Either 10 digits or 12 digits prefixed by `+`.

    :param phone_str: phone string to validate
    :return: true, if `phone_str` is a phone string
    """

    return match('^(\d{10}|\+\d{12})$', string=phone_str) is not None

class Phone(Field):
    def __init__(self, value):
        if not check_phone(value):
            raise ValueError(f'Invalid phone number, use "0000000000" or "+000000000000"')
        super().__init__(value)
