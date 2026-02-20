import os
from twilio.rest import Client
from dotenv import load_dotenv
import smtplib

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
        self._email = os.environ['EMAIL']
        self._password = os.environ['password']
        self.smtp_address = os.environ['SMTP_ADDRESS']
    
    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ['TWILIO_VIRTUAL_NUMBER'],
            body=message_body,
            to=os.environ["TWILIO_VIRTUAL_NUMBER"]
        )
        print(message.sid)

    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f"whatsapp:{os.environ['TWILIO_VIRTUAL_NUMBER']}",
            body=message_body,
            to=f"whatsapp:{os.environ['TWILIO_VERIFIED_NUMBER']}"
        )
        print(message.sid)
    
    def send_emails(self, to_email, message_body):
        with smtplib.SMTP(self.smtp_address) as connection:
            connection.starttls()
            connection.login(user=self._email, password=self._password)
            connection.sendmail(
                from_addr=self._email, 
                to_addrs=to_email, 
                msg=message_body
                )