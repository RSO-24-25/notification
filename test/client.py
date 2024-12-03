import grpc
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import email_pb2
import email_pb2_grpc

def run():
    # Connect to the server
    channel = grpc.insecure_channel('localhost:50051')
    stub = email_pb2_grpc.EmailServiceStub(channel)
    
    # Send a test email
    response = stub.SendEmail(email_pb2.EmailRequest(
        recipient_email="matej.kovack@gmail.com",
        subject="Obvestilo o naročnini na storitev odrasle vsebine",
        message="""Spoštovani Matej Mateo,
                    prejšnji teden ste uspešno opravili naročilo na storitev Paket ultra XXX, ki vam omogoča dostop do ekskluzivne odrasle vsebine. V skladu s pogoji naročnine bo vaša kartica mesečno bremenjena za znesek 9,99 EUR.

                    Podrobnosti naročnine:

                    Ime naročnine: Paket ultra XXX
                    Znesek: 9,99 EUR
                    Interval: mesečno
                    Datum prvega bremena: 5.12.2024
                    Če želite upravljati svojo naročnino, jo preklicati ali potrebujete dodatne informacije, nas lahko kontaktirate preko:

                    E-pošte: tvoj.prijatelj@gmail.com
                    Telefonske številke: 041 456 789
                    Zahvaljujemo se vam za zaupanje in želimo prijetno uporabo naših storitev.

                    Lep pozdrav,
                    Vodja ekipe Vedno Zadoscen, dipl. ing. Gal Menase
                    """
    ))
    print("Response from server:", response.status)

if __name__ == "__main__":
    run()
