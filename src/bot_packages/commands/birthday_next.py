from datetime import datetime, timedelta

from ..state import AddressBook, Record, Phone

from .helpers.register_command import register_command
from .helpers.input_error import input_error

def get_upcoming_birthdays(state: AddressBook) -> list[dict[str, str]]:
    # results list
    users_to_greet: list[dict[str, str]] = list()

    today = datetime.now().date()

    for user in state.values():
        birthday_date = user.birthday.value

        # get the next birthday after today
        next_birthday = birthday_date.replace(year=today.year)
        if next_birthday < today:
            next_birthday = birthday_date.replace(year=today.year + 1)

        # if next birthday is more than 7 days a week,
        # user is not added to the results list
        if (next_birthday - today).days > 7:
            continue

        congratulation_date = next_birthday

        weekday = next_birthday.weekday()

        if weekday > 4:
            # 1 for Sunday
            # 2 for Saturday
            days_to_add = 7 - weekday

            congratulation_date = next_birthday + timedelta(days=days_to_add)

        # adding user to set of results with correct congratulation date
        users_to_greet.append({
            "name": user.name,
            "congratulation_date": congratulation_date,
            "congratulation_date_str": congratulation_date.strftime("%d.%m")
        })

    users_to_greet.sort(key=lambda u: u['congratulation_date'])

    return users_to_greet

@register_command(aliases=['birthdays', 'upcoming-birthday'])
@input_error
def birthday_next(state: AddressBook) -> str:
    """
    show-birthday(get-birthday) <name>:

    Show birthday of a contact.

    Parameters:
        - username (str) - identifier for the user
    """
    congrats = get_upcoming_birthdays(state)

    if len(congrats) == 0:
        return "No upcoming birthdays"

    return 'Upcoming birthdays:\n'.join([
        f" -- '{user['name']}' - {user['congratulation_date_str']}" for user in congrats
    ])
