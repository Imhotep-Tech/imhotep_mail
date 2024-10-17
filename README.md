# Imhotep Mail

This is a simple Python library for sending emails. It provides an easy way to configure and send emails from any Python code.

## Installation

To install the `imhotep_mail` library, you can use pip:

```sh
pip install imhotep-mail
```

## Usage

### Example 1: Sending a Simple Email

Here's how you can use the library to send a simple email:

```python
from imhotep_mail import send_mail

# SMTP server configuration
smtp_server = 'smtp.example.com'
smtp_port = 465
username = 'your-email@example.com'
password = 'your-password'

#those are optional not required
user_ssl = False
user_tls = True

# Sending an email
to_email = 'recipient@example.com'
subject = 'Hello from Imhotep Mail!'
body = 'This is a test email sent using the Imhotep Mail library.'
is_html = False

success, error = send_mail(smtp_server, smtp_port, username, password, to_email, subject, body, is_html)
if error:
    #do somthing
```

### Example 2: Sending an Email with Attachments

If you need to send an email with attachments, you can specify them in the `attachments` parameter:

```python
from imhotep_mail import send_mail

# SMTP server configuration
smtp_server = 'smtp.example.com'
smtp_port = 465
username = 'your-email@example.com'
password = 'your-password'

#those are optional not required
user_ssl = False
user_tls = True

# Sending an email with attachments
to_email = 'recipient@example.com'
subject = 'Hello from Imhotep Mail!'
body = 'This is a test email sent using the Imhotep Mail library.'
is_html = False

attachments = ['path/to/attachment1.pdf', 'path/to/attachment2.jpg']
success, error = send_mail(smtp_server, smtp_port, username, password, to_email, subject, body, is_html, attachments, user_tls, user_ssl)
if error:
    #do somthing
```
# Gmail Example
```python
from imhotep_mail import send_mail

# SMTP server configuration for Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 465
username = 'your-email@gmail.com'  # Replace with your Gmail email address
password = 'your-app-password'    # Replace with the app password generated from Google account settings

# Sending an email to a Gmail address
to_email = 'recipient@example.com'
subject = 'Hello from Imhotep Mail!'
body = 'This is a test email sent using the Imhotep Mail library.'
is_html = False

success, error = send_mail(smtp_server, smtp_port, username, password, to_email, subject, body, is_html)
if error:
    #do somthing
```

In this example, you need to replace `'your-app-password'` with the actual app password generated from your Gmail account settings. The app password
is different from your regular password and allows access to only your Gmail account, so it's more secure than your regular password.

For more information on how to generate an app password for Google, you can refer to [Google's
documentation](https://support.google.com/accounts/1107213).

## Contributing

Contributions are welcome! You can submit issues and pull requests to help improve the library.

## License

MIT License. See [LICENSE](LICENSE) for more information.
