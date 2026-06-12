from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(str(value)) != 10:
            raise ValueError("The number must be 10 digits long.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones.remove(Phone(phone))

    def edit_phone(self, old_p, new_p):
        if len(old_p) != 10 or len(new_p) != 10:
            raise ValueError("The number must be 10 digits long.")
        i = self.phones.index(Phone(old_p))
        self.phones[i] = Phone(new_p)

    def find_phone(self, phone):
        i = self.phones.index(Phone(phone))
        if i == -1:
            return None
        return self.phones[i]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __str__(self):
        return str(self.data.name)

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        self.data.pop(name)