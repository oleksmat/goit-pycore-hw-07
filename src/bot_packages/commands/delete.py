from src.bot_packages.state import AddressBook

from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['delete'])
@input_error
def delete_command(state: AddressBook, username: str):
    """
    delete <username>:

    Delete phone contact of <username>.

    Parameters:
        - username (str) - identifier for the user
    """

    record = state.find(username)

    if record is None:
        return f"Contact for '{username}' does not exist"

    state.delete(username)

    return f"Contact for '{username}' was deleted"
