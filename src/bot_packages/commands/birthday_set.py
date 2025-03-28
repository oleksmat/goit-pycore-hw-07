from ..state import AddressBook, Record

from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['add-birthday', 'set-birthday'])
@input_error
def birthday_set(state: AddressBook, username, birthday) -> str:
    """
    add-birthday(set-birthday) <name> <birthday>:

    Set birthday of a contact.

    Parameters:
        - username (str) - identifier for the user
        - birthday (str) - birthday date for user
    """
    record = state.find(username)

    if record is None:
        return f"Record for '{username}' does not exit"

    record.set_birthday(birthday)

    return f"Birthday for '{username}' is now {record.birthday}"
