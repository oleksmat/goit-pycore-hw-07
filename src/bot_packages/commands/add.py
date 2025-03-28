from ..state import AddressBook, Record, Phone

from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['add'])
@input_error
def add_command(state: AddressBook, username, phone_str) -> str:
    """
    add <name> <number>:

    Adds a contact to the contacts book.

    Parameters:
        - username (str) - identifier for the user
        - phone (str) - user's phone number
    """
    record = state.find(username)

    if record is not None:
        record.add_phone(phone_str)

        return f"Contact for '{username}' is now also {phone_str}"
    else:
        record = Record(username)

        record.add_phone(phone_str)

        state.add_record(record)

        return f"Contact for '{username}' is now {phone_str}"
