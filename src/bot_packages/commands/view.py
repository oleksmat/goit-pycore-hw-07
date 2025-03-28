from ..state import AddressBook

from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['view', 'phone'])
@input_error
def view_command(state: AddressBook, username):
    """
    phone(view) <username>:

    View phone contact of <username>.

    Parameters:
        - username (str) - identifier for the user
    """

    record = state.find(username)

    if record is None:
        return f"Contact for '{username}' does not exist"

    return f"Contact(s) for '{username}' is {','.join([str(phone) for phone in record.phones])}"
