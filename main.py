import threading
from telegramBot import startTelegrambot
from webserver import startWebserver

telegrambot_thread = threading.Thread(target=startTelegrambot)
webserver_thread = threading.Thread(target=startWebserver)

if __name__ == "__main__":
    telegrambot_thread.start()
    webserver_thread.start()