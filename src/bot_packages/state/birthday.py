from datetime import datetime

from .field import Field

class Birthday(Field):
    def __init__(self, value):
        try:
            super().__init__(datetime.strptime(value, '%d.%m.%Y').date())
        except ValueError:
            raise ValueError("Invalid birthday format, use DD.MM.YYYY")

    def __str__(self):
        return self.value.strftime('%d.%m.%Y')

    def __repr__(self):
        return self.value.strftime('%d.%m.%Y')
