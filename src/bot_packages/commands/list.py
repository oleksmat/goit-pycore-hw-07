from ..state import AddressBook

from .helpers.register_command import register_command
from .helpers.input_error import input_error

@register_command(aliases=['all', 'list'])
@input_error
def list_command(state: AddressBook):
    """
    all(list):

    View all phone contacts.
    """

    if len(state) == 0:
        return "No contacts yet"

    return '\n'.join([f" -- '{username}' - {state[username].list_phones()} -- {state[username].birthday}" for username in state.keys()])
