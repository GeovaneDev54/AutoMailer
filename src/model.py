import json
import os
import sys

class Model:
    def __init__(self):
        self.file = self.get_data_file_path('src/db/data.json')

    def get_data_file_path(self, filename):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, filename)
        return os.path.join(os.path.abspath('.'), filename)

    def create_file(self):
        data = {
            'recipient': '',
            'days': [],
            'hours': [],
            'sender': '',
            'password': ''
        }

        with open(self.file, 'w') as file:
            json.dump(data, file)

        return [data['recipient'], data['days'], data['hours'], data['sender'], data['password']]

    def load(self):
        try:
            with open(self.file, 'r') as file:
                data = json.load(file)
            return [data['recipient'], data['days'], data['hours'], data['sender'], data['password']]
        except FileNotFoundError:
            return self.create_file()

    def save(self, recipient: str, days: list, hours: list, sender: str, password: str):
        data = {
            'recipient': recipient,
            'days': days,
            'hours': hours,
            'sender': sender,
            'password': password
        }

        with open(self.file, 'w') as file:
            json.dump(data, file)