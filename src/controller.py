from model import Model
from view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def load(self):
        return self.model.load()

    def save(self, recipient:str, days:list, hours:list, sender:str, password:str):
        self.model.save(recipient, days, hours, sender, password)

    def run(self):
        self.view.run()