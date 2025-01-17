import grpc
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import email_pb2
import email_pb2_grpc

def run():
    # Connect to the server
    channel = grpc.insecure_channel('72.144.72.133:50051')
    stub = email_pb2_grpc.EmailServiceStub(channel)
    
    # Send a test email
    response = stub.SendEmail(email_pb2.EmailRequest(
        recipient_email="gal.menase@gmail.com",
        subject="Super Vsebina Dneva",
        message="""Zelo informativno sporocilo, poslano le tebi!"""
    ))
    print("Response from server:", response.status)

if __name__ == "__main__":
    run()
