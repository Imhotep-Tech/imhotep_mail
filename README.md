# Imhotep Mail

This is a simple Python library for sending emails. It provides an easy way to configure and send emails from any Python code.

## Installation

To install the `imhotep_mail` library, you can use pip:

```sh
pip install imhotep-mail
```

## Usage

### Recommended Method: Configure SMTP Settings Globally

The recommended way to use the library is by configuring SMTP settings globally using the `set_mail_config` function:

```python
from imhotep_mail import set_mail_config

# Set global SMTP configuration
set_mail_config(
    smtp_server='smtp.example.com',
    smtp_port=465,
    username='your-email@example.com',
    password='your-password',
    user_tls=True,  # Optional, default is True
    user_ssl=False  # Optional, default is False
)
```

Then, send emails using the `send_mail` function:

```python
from imhotep_mail import send_mail

# Sending an email
success, error = send_mail(
    to_email='recipient@example.com',
    subject='Hello from Imhotep Mail!',
    body='This is a test email sent using the Imhotep Mail library.',
    is_html=False
)
if error:
    print(f"Error: {error}")
else:
    print(success)
```

### Legacy Method: Passing SMTP Configuration Directly

For backward compatibility, you can still use the `send_mail` function by passing SMTP configuration directly. This method is not recommended for new code:

```python
from imhotep_mail import send_mail

# Sending an email using the legacy method
success, error = send_mail(
    'smtp.example.com', 465, 'your-email@example.com', 'your-password',
    to_email='recipient@example.com',
    subject='Hello from Imhotep Mail!',
    body='This is a test email sent using the Imhotep Mail library.',
    is_html=False
)
if error:
    print(f"Error: {error}")
else:
    print(success)
```

## Using Gmail with App Passwords

If you are using Gmail, you need to enable "App Passwords" to use this library. Follow these steps:

1. Go to your [Google Account Security Settings](https://myaccount.google.com/security).
2. Enable 2-Step Verification if it is not already enabled.
3. Under "Signing in to Google," click on "App Passwords."
4. Generate an app password for "Mail" and "Other" (e.g., "Imhotep Mail").
5. Use the generated password in place of your Gmail account password in the `set_mail_config` function.

Example:

```python
from imhotep_mail import set_mail_config, send_mail

# Set global SMTP configuration for Gmail
set_mail_config(
    smtp_server='smtp.gmail.com',
    smtp_port=587,
    username='your-email@gmail.com',
    password='your-app-password',
    user_tls=True,
    user_ssl=False
)

# Send an email
success, error = send_mail(
    to_email='recipient@example.com',
    subject='Hello from Imhotep Mail!',
    body='This is a test email sent using Gmail with App Passwords.',
    is_html=False
)
if error:
    print(f"Error: {error}")
else:
    print(success)
```

### Sending an Email with Attachments

Both methods support sending emails with attachments. For example, using the recommended method:

```python
from imhotep_mail import send_mail

# Sending an email with attachments
success, error = send_mail(
    to_email='recipient@example.com',
    subject='Hello from Imhotep Mail!',
    body='This is a test email sent using the Imhotep Mail library.',
    is_html=False,
    attachments=['path/to/attachment1.pdf', 'path/to/attachment2.jpg']
)
if error:
    print(f"Error: {error}")
else:
    print(success)
```

## Using the CLI

The library also provides a CLI tool for sending emails. To use it, run the following command:

```sh
imhotep-mail-cli --to recipient@example.com --subject "Hello from CLI" --body "This is a test email sent using the CLI." --is-html --attachments path/to/attachment1.pdf path/to/attachment2.jpg --smtp-server smtp.gmail.com --smtp-port 587 --smtp-username your-email@gmail.com --smtp-password your-app-password --use-tls
```

### CLI Arguments

- `--to`: Recipient email address (required).
- `--subject`: Email subject (required).
- `--body`: Email body (required).
- `--is-html`: Send email as HTML (optional).
- `--attachments`: Paths to attachment files (optional).
- `--smtp-server`: SMTP server address (optional, overrides environment variables).
- `--smtp-port`: SMTP server port (optional, overrides environment variables).
- `--smtp-username`: SMTP username (optional, overrides environment variables).
- `--smtp-password`: SMTP password (optional, overrides environment variables).
- `--use-tls`: Use TLS for SMTP (optional).
- `--use-ssl`: Use SSL for SMTP (optional).

## Contributing

Contributions are welcome! You can submit issues and pull requests to help improve the library.

## License

MIT License. See [LICENSE](LICENSE) for more information.
