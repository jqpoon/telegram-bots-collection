import threading
from telegramBot import telegramNotifierBot
from messageListener import startListener

botInstance = telegramNotifierBot()
telegrambotThread = threading.Thread(target=botInstance.startTelegramBot)
listenerThread = threading.Thread(target=startListener, 
                                  args=[botInstance.sendTelegramMessage])

if __name__ == "__main__":
    telegrambotThread.start()
    listenerThread.start()