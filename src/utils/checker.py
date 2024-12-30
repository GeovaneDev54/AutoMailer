import time
from datetime import datetime, timedelta
from utils.sendemail import Email
import json
import sched
import os
import sys

class Checker:
    def __init__(self):
        self.email = Email()
        self.config = self.get_data_file_path('src/db/data.json')
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def get_data_file_path(self, filename):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, filename)
        return os.path.join(os.path.abspath('.'), filename)

    def load_config(self):
        try:
            with open(self.config, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return None

    def check_and_send_email(self):
        config = self.load_config()
        if config is None:
            return

        recipient = config['recipient']
        sender = config['sender']
        password = config['password']
        days = config['days']
        hours = config['hours']

        now = datetime.now()
        current_day = now.strftime('%A').lower()
        current_time = now.strftime('%H:%M')

        if current_day in days and current_time in hours:
            self.email.send_email(recipient, sender, password)

    def schedule_checks(self):
        while True:
            now = datetime.now()
            next_minute = (now + timedelta(minutes=1)).replace(second=0, microsecond=0)
            delay = (next_minute - now).total_seconds()
            self.scheduler.enter(delay, 1, self.check_and_send_email)
            self.scheduler.run()

def run_checker():
    checker = Checker()
    checker.schedule_checks()