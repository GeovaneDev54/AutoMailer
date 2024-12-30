import smtplib
from email.message import Message
import requests

SMTPS = {
    'gmail': 'smtp.gmail.com: 587',
    'hotmail': 'smtp.live.com: 587',
    'outlook': 'smtp-mail.outlook.com: 587',
    'yahoo': 'smtp.mail.yahoo.com: 587',
    'aol': 'smtp.aol.com: 587',
    'zoho': 'smtp.zoho.com: 587',
    'mail.com': 'smtp.mail.com: 587',
    'yandex': 'smtp.yandex.com: 587',
}

def get_image():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['message']
    else:
        return 'https://ih1.redbubble.net/image.4905811447.8675/flat,750x,075,f-pad,750x1000,f8f8f8.jpg'

class Email:
    def __init__(self):
        self.content = '''
        <img src="image"></img>
        '''

    def get_server(self, email:str):
        position = email.find('@')
        return email[position+1:-4]

    def send_email(self, recipient:str, sender:str, password:str):
        self.msg = Message()
        self.msg['Subject'] = 'Dog image'
        self.msg['From'] = sender
        self.msg['To'] = recipient
        self.msg.add_header('Content-Type', 'text/html')
        self.msg.set_payload(self.content.replace('image', get_image()))

        server = self.get_server(recipient)
        self.smtp = smtplib.SMTP(SMTPS[server])
        self.smtp.starttls()
        self.smtp.login(self.msg['From'], password)

        self.smtp.sendmail(self.msg['From'], [self.msg['To']], self.msg.as_string().encode('UTF-8'))