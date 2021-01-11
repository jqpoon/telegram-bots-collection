import threading
import atexit
from telegramBot import telegramNotifierBot
from messageListener import messageListener

botInstance = telegramNotifierBot()
listenerInstance = messageListener()
telegrambotThread = threading.Thread(target=botInstance.startTelegramBot)
listenerThread = threading.Thread(target=listenerInstance.startListener, 
                                  args=[botInstance.sendTelegramMessage])

@atexit.register
def onExit():
    listenerInstance.stopListener()
    botInstance.stopTelegramBot()

if __name__ == "__main__":
    telegrambotThread.start()
    listenerThread.start()