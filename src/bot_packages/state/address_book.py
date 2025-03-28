from collections import UserDict

from .record import Record

class AddressBook(UserDict[str, Record]):
    def add_record(self, record: Record):
        self.data[record.name] = record

    def find(self, name: str):
        for key, record in self.data.items():
            if key == name:
                return record
        return None

    def delete(self, name: str):
        del self.data[name]
