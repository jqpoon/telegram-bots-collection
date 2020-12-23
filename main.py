import threading
from telegram_bot import start_telegrambot
from webserver import start_webserver

telegrambot_thread = threading.Thread(target=start_telegrambot)
webserver_thread = threading.Thread(target=start_webserver)

if __name__ == "__main__":
    telegrambot_thread.start()
    webserver_thread.start()
