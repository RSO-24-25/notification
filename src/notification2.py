import os
import smtplib
from concurrent import futures
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import grpc
from dotenv import load_dotenv

import email_pb2
import email_pb2_grpc

load_dotenv()


def send_email_notification(
    sender_email, sender_password, recipient_email, subject, message
):
    try:
        # SMTP server configuration (example for Gmail)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # TLS port

        # Set up the MIME
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Attach the plain text message
        msg.attach(MIMEText(message, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with your credentials and recipient details
    sender_email = os.getenv("EMAIL")
    sender_password = os.getenv("SUPER_SECRET")  # Use App Password if needed
    recipient_email = "bcovi.angelcki@gmail.com"
    subject = "Test Email Notification"
    message = "This is a test email sent from Python."

    send_email_notification(
        sender_email, sender_password, recipient_email, subject, message
    )
