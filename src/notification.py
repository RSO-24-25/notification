from concurrent import futures
import grpc
import email_pb2
import email_pb2_grpc
import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# test CI/CD
# Load environment variables
load_dotenv()

class EmailServiceServicer(email_pb2_grpc.EmailServiceServicer):
    def SendEmail(self, request, context):
        try:
            sender_email = os.getenv("EMAIL")
            print(sender_email)
            sender_password = os.getenv("SUPER_SECRET")
            # Get sender credentials from environment variables
            if not sender_email or not sender_password:
                raise ValueError("Sender credentials are not configured in the environment variables.")

            # Extract recipient details and message content from the request
            recipient_email = request.recipient_email
            subject = request.subject
            message = request.message
            
            # SMTP server configuration (example for Gmail)
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            
            # Set up the MIME
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            
            # Send the email
            with SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
            
            # Return success status
            return email_pb2.EmailResponse(status="Email sent successfully!")
        except Exception as e:
            return email_pb2.EmailResponse(status=f"Failed to send email: {e}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    email_pb2_grpc.add_EmailServiceServicer_to_server(EmailServiceServicer(), server)
    server.add_insecure_port('[::]:50051')  # Listen on port 50051
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
