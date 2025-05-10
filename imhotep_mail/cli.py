import argparse
import os
from .main import send_mail, set_mail_config

def main():
    parser = argparse.ArgumentParser(description="Send emails using Imhotep Mail.")
    
    # Email parameters
    parser.add_argument('--to', required=True, help="Recipient email address")
    parser.add_argument('--subject', required=True, help="Email subject")
    parser.add_argument('--body', required=True, help="Email body")
    parser.add_argument('--is-html', action='store_true', help="Send email as HTML")
    parser.add_argument('--attachments', nargs='*', help="Paths to attachment files")
    
    # Optional SMTP configuration (overrides environment variables if provided)
    parser.add_argument('--smtp-server', help="SMTP server address")
    parser.add_argument('--smtp-port', type=int, help="SMTP server port")
    parser.add_argument('--smtp-username', help="SMTP username")
    parser.add_argument('--smtp-password', help="SMTP password")
    parser.add_argument('--use-tls', action='store_true', help="Use TLS for SMTP")
    parser.add_argument('--use-ssl', action='store_true', help="Use SSL for SMTP")

    args = parser.parse_args()

    # Configure SMTP settings
    set_mail_config(
        smtp_server=args.smtp_server,
        smtp_port=args.smtp_port,
        username=args.smtp_username,
        password=args.smtp_password,
        user_tls=args.use_tls,
        user_ssl=args.use_ssl
    )

    # Send the email
    success, error = send_mail(
        to_email=args.to,
        subject=args.subject,
        body=args.body,
        is_html=args.is_html,
        attachments=args.attachments
    )
    if success:
        print(success)
    else:
        print(error)