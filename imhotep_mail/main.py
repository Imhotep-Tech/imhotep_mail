from flask import Flask
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()

# Global variable to store SMTP configuration
smtp_config = {}

def hello():
    print("Hello from imhotep_mail!") #a function to be called from the terminale to checks if library is installed or not

def set_mail_config(smtp_server, smtp_port, username, password, user_tls=True, user_ssl=False):
    """
    Set global SMTP configuration.
    """
    global smtp_config
    smtp_config = {
        'smtp_server': smtp_server,
        'smtp_port': smtp_port,
        'username': username,
        'password': password,
        'user_tls': user_tls,
        'user_ssl': user_ssl
    }

def configure_mail_from_env():
    """
    Set global SMTP configuration using environment variables.
    """
    set_mail_config(
        smtp_server=os.getenv('SMTP_SERVER'),
        smtp_port=int(os.getenv('SMTP_PORT', 587)),
        username=os.getenv('SMTP_USERNAME'),
        password=os.getenv('SMTP_PASSWORD'),
        user_tls=os.getenv('SMTP_USE_TLS', 'True') == 'True',
        user_ssl=os.getenv('SMTP_USE_SSL', 'False') == 'True',
    )

def mail_config():
    """
    Create and return a Flask app and Mail instance using the global SMTP configuration.
    """
    global smtp_config
    app = Flask(__name__)  # Define the app (Flask context)

    # Defining the mail configuration
    app.config['MAIL_SERVER'] = smtp_config['smtp_server']
    app.config['MAIL_PORT'] = smtp_config['smtp_port']
    app.config['MAIL_USERNAME'] = smtp_config['username']
    app.config['MAIL_PASSWORD'] = smtp_config['password']
    app.config['MAIL_USE_TLS'] = smtp_config['user_tls']
    app.config['MAIL_USE_SSL'] = smtp_config['user_ssl']
    app.config['MAIL_DEFAULT_SENDER'] = smtp_config['username']
    mail = Mail(app)
    return app, mail

def _send_email(app, mail, sender, to_email, subject, body, is_html, attachments):
    """
    Helper function to send an email using Flask-Mail.
    """
    with app.app_context():
        msg = Message(subject=subject, sender=sender, recipients=[to_email])
        msg.body = body
        msg.html = body if is_html else None

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
            return "Email sent successfully", None
        except Exception as e:
            return None, f"Failed to send email: {str(e)}"

def send_mail(*args, **kwargs):
    """
    Send an email using either the global SMTP configuration (new method) or by passing SMTP configuration directly (legacy method).
    """
    if len(args) >= 4:  # Legacy method
        smtp_server, smtp_port, username, password = args[:4]
        to_email = kwargs.get('to_email')
        subject = kwargs.get('subject')
        body = kwargs.get('body')
        is_html = kwargs.get('is_html', False)
        attachments = kwargs.get('attachments', None)
        user_tls = kwargs.get('user_tls', False)
        user_ssl = kwargs.get('user_ssl', True)

        app = Flask(__name__)
        app.config.update(
            MAIL_SERVER=smtp_server,
            MAIL_PORT=smtp_port,
            MAIL_USERNAME=username,
            MAIL_PASSWORD=password,
            MAIL_USE_TLS=user_tls,
            MAIL_USE_SSL=user_ssl,
            MAIL_DEFAULT_SENDER=username
        )
        mail = Mail(app)
        return _send_email(app, mail, username, to_email, subject, body, is_html, attachments)

    else:  # New method
        to_email = kwargs.get('to_email')
        subject = kwargs.get('subject')
        body = kwargs.get('body')
        is_html = kwargs.get('is_html', False)
        attachments = kwargs.get('attachments', None)

        app, mail = mail_config()
        return _send_email(app, mail, smtp_config['username'], to_email, subject, body, is_html, attachments)
