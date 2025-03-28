from .phone import Phone
from .birthday import Birthday


class Record:
    def __init__(self, name: str):
        self.name: str = name
        self.phones: list[Phone] = []
        self.birthday = None

    def add_phone(self, phone: str):
        for p in self.phones:
            if p == phone:
                return
        self.phones.append(Phone(phone))

    def edit_phone(self, old_phone: str, new_phone: str):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return

    def find_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def remove_phone(self, phone: str):
        self.phones = [p for p in self.phones if p.value != phone]

    def list_phones(self):
        return ','.join([p.value for p in self.phones])

    def set_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_birthday(self, birthday):
        return self.birthday

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"
