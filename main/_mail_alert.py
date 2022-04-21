from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser
import smtplib


class Email_Alert:

    def __init__(self, text):

        config = configparser.ConfigParser()
        config.read('D:/My_Projects/Python/Mail-Alert/config/config.ini')

        self.EMAIL_CONFIG = {
            'server': config['Email']['Server'],
            'user': config['Email']['User'],
            'ssl': config['Email']['SSL'],
            'password': config['Email']['Password'],
            'ToAddress': config['Email']['To_Address']
        }

        if len(config['Email']['To_Address']) > 1:
            self.to_Address = config['Email']['To_Address'].split(',')
        else:
            self.to_Address = config['Email']['To_Address']

        self.alert_msg = text

    def message_format(self):

        msg = MIMEMultipart()
        msg['From'] = self.EMAIL_CONFIG['user']
        msg['To'] = self.EMAIL_CONFIG['ToAddress']
        #here you can change the subject 
        msg['Subject'] = 'Alert'
        message = str(self.alert_msg)
        msg.attach(MIMEText(message))

        return msg

    def Set_connection(self):

        form = self.message_format()

        try:
            server = smtplib.SMTP_SSL(
                self.EMAIL_CONFIG['server'], self.EMAIL_CONFIG['ssl'])
            server.connect(
                self.EMAIL_CONFIG['server'], self.EMAIL_CONFIG['ssl'])
            server.ehlo()

            server.login(self.EMAIL_CONFIG['user'],
                         self.EMAIL_CONFIG['password'])

            server.sendmail(self.EMAIL_CONFIG['user'], self.to_Address,
                            form.as_string())

            print('CONNECTION SUCCESSFUL')
        except Exception as e:
            print(f'Error in connection ={e}')

