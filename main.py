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
        if len(str(value)) != 10 or not str(value).isdigit():
            raise ValueError("The number must be 10 digits long.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        old_p = self.find_phone(phone)
        self.phones.remove(old_p)

    def edit_phone(self, old_p, new_p):
        phone = self.find_phone(old_p)
        if not phone:
            raise ValueError("The number must be 10 digits long.")
        self.add_phone(new_p)
        self.remove_phone(old_p)       

    def find_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                return el
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __str__(self):
        return str(self.data.name)

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name)