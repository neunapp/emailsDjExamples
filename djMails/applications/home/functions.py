import os.path
from email.mime.text import MIMEText

from google.oauth2 import service_account

import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def send_mail_google():

    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(
        access_type='offline',
        prompt=None,
        login_hint='neunapp.cursos@gmail.com'
    )
    
    service = build('gmail', 'v1', credentials=creds)
    
    message = MIMEText('Mensaje de prueba Neun')
    message['to'] = 'neunapp.teach@gmail.com'
    message['subject'] = 'Prueba api gmail01'
    create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    try:
        message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message')
    except HttpError as error:
        print(F'******** ocurrio un error****: {error}')
        message = None


def send_mail_server_to_server():
    credentials = service_account.Credentials.from_service_account_file(
        'acountcreds.json', 
        scopes=SCOPES
    )
    delegated_credentials = credentials.with_subject('neunapp.cursos@gmail.com')
    print(credentials.token)
    servicio = build('gmail', 'v1', credentials=credentials)
    print(servicio)
    return True