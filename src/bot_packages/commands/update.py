from ..state import AddressBook

from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['change', 'update'])
@input_error
def update_command(state: AddressBook, username, old_phone, new_phone):
    """
    change(update) <username>:

    Change a <username>'s contact.

    Parameters:
        - username (str) - identifier for the user
    """

    record = state.find(username)

    if record is None:
        return f"Contact for '{username}' does not exists"

    record.edit_phone(old_phone, new_phone)

    return f"Updated contact {old_phone} for '{username}' to {new_phone}"
