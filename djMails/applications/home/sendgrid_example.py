import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_mail_sendgrid():
    message = Mail(
        from_email='neunapp.teach@gmail.com',
        to_emails='neunapp.cursos@gmail.com',
        subject='Asunto de prueba',
        html_content='<strong>Hola desd e sendgrid</strong>')
    try:
        sg = SendGridAPIClient(
            api_key='-------'
        )
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)