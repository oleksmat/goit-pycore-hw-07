from ..state import AddressBook, Record, Phone

from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['show-birthday', 'get-birthday'])
@input_error
def birthday_get(state: AddressBook, username) -> str:
    """
    show-birthday(get-birthday) <name>:

    Show birthday of a contact.

    Parameters:
        - username (str) - identifier for the user
    """
    record = state.find(username)

    if record is None:
        return f"Record for '{username}' does not exit"

    record = Record(username)

    if record.birthday is None:
        return f"Birthday for '{username}' is missing"
    else:
        return f"Birthday for '{username}' is now {record.birthday}"
