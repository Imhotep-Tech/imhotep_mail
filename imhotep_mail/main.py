from flask import Flask
from flask_mail import Mail, Message
import os

def hello():
    print("Hello from imhotep_mail!") #a function to be called from the terminale to checks if library is installed or not

def mail_config(smtp_server, smtp_port, username, password, user_tls=True, user_ssl=False):

    app = Flask(__name__) #define the app (teh flask contetxt)

    #defining the mail configuration
    app.config['MAIL_SERVER']= smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USERNAME'] = username
    app.config['MAIL_PASSWORD'] = password
    app.config['MAIL_USE_TLS'] = user_tls
    app.config['MAIL_USE_SSL'] = user_ssl
    app.config['MAIL_DEFAULT_SENDER'] = username
    mail = Mail(app)
    return app, mail

def send_mail(smtp_server, smtp_port, username, password, to_email, subject, body, attachments=None, is_html=False, user_tls=False, user_ssl=True):

    #running the mail config function to run the mail data on a flask context
    app, mail = mail_config(smtp_server, smtp_port, username, password, user_tls, user_ssl)

    #running the function inside flask context
    with app.app_context():
        #sending the mail
        msg = Message(subject=subject, sender=username, recipients=[to_email])
        #the mail body
        msg.body = body
        #if there is an html so the body will run as an html
        msg.html = body if is_html else None

        # Attach files to be sent if teh functin call get it
        if attachments:
            for file_path in attachments:
                if os.path.exists(file_path):
                    try:
                        with open(file_path, 'rb') as fp:
                            msg.attach(
                                filename=os.path.basename(file_path),
                                content_type="application/octet-stream",
                                data=fp.read()
                            )
                    except Exception as e:
                        print(f"Failed to attach file {file_path}: {str(e)}")
                        continue  # Skip this attachment

        try:
            mail.send(msg)
            print("Email sent successfully")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
