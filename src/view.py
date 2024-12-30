import FreeSimpleGUI as sg

sg.theme('DarkBlue3')

HOME_LAYOUT = [
    [sg.Push(), sg.Text('Auto Mailer', font=('Helvetica', 20, 'bold'), text_color='white'), sg.Push()],
    [sg.HorizontalSeparator(color='white')],
    [sg.Text('Recipient E-mail:', size=(15, 1), font=('Helvetica', 12), text_color='white'), sg.InputText(size=(35, 1), key='recipient')],
    [
        sg.Push(),
        sg.Column([
            [sg.Text('Days', font=('Helvetica', 12, 'bold'), text_color='white')],
            [sg.Checkbox('Monday', font=('Helvetica', 12), text_color='white', key='monday')],
            [sg.Checkbox('Tuesday', font=('Helvetica', 12), text_color='white', key='tuesday')],
            [sg.Checkbox('Wednesday', font=('Helvetica', 12), text_color='white', key='wednesday')],
            [sg.Checkbox('Thursday', font=('Helvetica', 12), text_color='white', key='thursday')],
            [sg.Checkbox('Friday', font=('Helvetica', 12), text_color='white', key='friday')],
            [sg.Checkbox('Saturday', font=('Helvetica', 12), text_color='white', key='saturday')],
            [sg.Checkbox('Sunday', font=('Helvetica', 12), text_color='white', key='sunday')],
        ], pad=(5, 5)),
        sg.VSeparator(),
        sg.Column([
            [sg.Text('Hours', font=('Helvetica', 12, 'bold'), text_color='white')],
            [sg.Checkbox('00:00', font=('Helvetica', 12), text_color='white', key='00:00')],
            [sg.Checkbox('05:00', font=('Helvetica', 12), text_color='white', key='05:00')],
            [sg.Checkbox('08:00', font=('Helvetica', 12), text_color='white', key='08:00')],
            [sg.Checkbox('12:00', font=('Helvetica', 12), text_color='white', key='12:00')],
            [sg.Checkbox('15:00', font=('Helvetica', 12), text_color='white', key='15:00')],
            [sg.Checkbox('17:00', font=('Helvetica', 12), text_color='white', key='17:00')],
            [sg.Checkbox('22:00', font=('Helvetica', 12), text_color='white', key='22:00')],
        ], pad=(5, 5)),
        sg.Push()
    ],
    [sg.HorizontalSeparator(color='white', pad=(10, 20))],
    [sg.Push(), sg.Button('Settings', size=(12, 1), button_color=('white', '#007ACC'), font=('Helvetica', 12), key='-SETTINGS-'),
     sg.Button('Save', size=(12, 1), button_color=('white', '#007ACC'), font=('Helvetica', 12), key='-SAVE-'),
     sg.Button('Close', size=(12, 1), button_color=('white', '#D32F2F'), font=('Helvetica', 12), key='-CLOSE-'), sg.Push()],
]

SETTINGS_LAYOUT = [
    [sg.Push(), sg.Text('Auto Mailer', font=('Helvetica', 20, 'bold'), text_color='white'), sg.Push()],
    [sg.HorizontalSeparator(color='white')],
    [sg.Text('Sender E-Mail:', size=(15, 1), font=('Helvetica', 12), text_color='white'), sg.InputText(key='sender', size=(35, 1))],
    [sg.Text('E-Mail Password:', size=(15, 1), font=('Helvetica', 12), text_color='white'), sg.InputText(key='password', password_char='*', size=(35, 1))],
    [sg.HorizontalSeparator(color='white', pad=(10, 20))],
    [
        sg.Push(), sg.Button('Home', size=(12, 1), button_color=('white', '#007ACC'), font=('Helvetica', 12), key='-HOME-'), sg.Push()
    ],
]

LAYOUT = [
    [sg.Column(HOME_LAYOUT, key='-HOME_LAYOUT-', visible=True),
     sg.Column(SETTINGS_LAYOUT, key='-SETTINGS_LAYOUT-', visible=False)]
]

class View:
    def __init__(self, controller):
        self.window = sg.Window('Auto Mailer', LAYOUT, finalize=True)
        self.controller = controller
        self.load()

    def _get_days(self, values):
        days = [day for day, value in values.items() if value and day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']]
        return days

    def _get_hours(self, values):
        hours = [hour for hour, value in values.items() if value and ':' in hour]
        return hours

    def load(self):
        recipient, days, hours, sender, password = self.controller.load()
        self.window['recipient'].update(recipient)

        for day in days:
            self.window[day].update(True)

        for hour in hours:
            self.window[hour].update(True)

        self.window['sender'].update(sender)
        self.window['password'].update(password)

    def save(self, values):
        recipient = values['recipient']
        days = self._get_days(values)
        hours = self._get_hours(values)
        sender = values['sender']
        password = values['password']
        self.controller.save(recipient, days, hours, sender, password)

    def run(self):
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == '-CLOSE-':
                self.window.hide()
                break

            if event == '-SETTINGS-':
                self.window['-HOME_LAYOUT-'].update(visible=False)
                self.window['-SETTINGS_LAYOUT-'].update(visible=True)

            if event == '-HOME-':
                self.window['-SETTINGS_LAYOUT-'].update(visible=False)
                self.window['-HOME_LAYOUT-'].update(visible=True)

            if event == '-SAVE-':
                self.save(values)

        self.window.close()