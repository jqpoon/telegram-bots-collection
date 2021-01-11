import secret
from typing import Callable
from multiprocessing.connection import Listener

def startListener(messageConsumer: Callable[[str], None]):
    address = ("localhost", secret.MESSAGE_PORT)
    listener = Listener(address, authkey=secret.AUTH_KEY)

    while True:
        conn = listener.accept()
        message = conn.recv()
        messageConsumer(message)
        if message == "close":
            print("Closing connection!")
            conn.close()
            break

    listener.close()