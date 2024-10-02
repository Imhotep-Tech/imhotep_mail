# Imhotep Mail

This is a simple Python library for sending emails using Flask and Flask-Mail. It provides an easy way to configure and send emails from a Flask
application.

## Installation

To install the `imhotep_mail` library, you can use pip:

```sh
pip install imhotep-mail
```

## Usage

### Example 1: Sending a Simple Email

Here's how you can use the library to send a simple email:

```python
from imhotep_mail import mail_config, send_mail

# SMTP server configuration
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your-email@example.com'
password = 'your-password'

# Sending an email
to_email = 'recipient@example.com'
subject = 'Hello from Imhotep Mail!'
body = 'This is a test email sent using the Imhotep Mail library.'

send_mail(smtp_server, smtp_port, username, password, to_email, subject, body)
```

### Example 2: Sending an Email with Attachments

If you need to send an email with attachments, you can specify them in the `attachments` parameter:

```python
from imhotep_mail import mail_config, send_mail

# SMTP server configuration
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your-email@example.com'
password = 'your-password'

# Sending an email with attachments
to_email = 'recipient@example.com'
subject = 'Hello from Imhotep Mail!'
body = 'This is a test email sent using the Imhotep Mail library.'

attachments = ['path/to/attachment1.pdf', 'path/to/attachment2.jpg']
send_mail(smtp_server, smtp_port, username, password, to_email, subject, body, attachments)
```

## Configuration

You can customize the mail configuration by passing a dictionary of options to the `mail_config` function:

```python
from imhotep_mail import mail_config

# SMTP server configuration with custom options
smtp_server = 'smtp.example.com'
smtp_port = 587
username = 'your-email@example.com'
password = 'your-password'
user_tls = True
user_ssl = False

# Customizing the mail configuration
mail_app, mail = mail_config(smtp_server, smtp_port, username, password, user_tls, user_ssl)

# Sending an email with custom options
to_email = 'recipient@example.com'
subject = 'Hello from Imhotep Mail!'
body = 'This is a test email sent using the Imhotep Mail library.'

send_mail(mail_app, mail, to_email, subject, body)
```

## Contributing

Contributions are welcome! You can submit issues and pull requests to help improve the library.

## License

MIT License. See [LICENSE](LICENSE) for more information.
