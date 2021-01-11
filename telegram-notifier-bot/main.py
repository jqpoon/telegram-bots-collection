import threading
from telegramBot import startTelegrambot, sendTelegramMessage
from messageListener import startListener

telegrambotThread = threading.Thread(target=startTelegrambot)
listenerThread = threading.Thread(target=startListener, 
                                  args=[sendTelegramMessage])

if __name__ == "__main__":
    telegrambotThread.start()
    listenerThread.start()