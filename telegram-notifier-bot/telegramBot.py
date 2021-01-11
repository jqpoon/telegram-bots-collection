from telegram.ext import (Updater, CommandHandler, MessageHandler, 
                          ConversationHandler, Filters)
import secret

PRE_AUTH, POST_AUTH = range(2)
global started
started = False

def start(update, context):
    global started, botInstance, chatId
    started = True
    chatId = update.effective_chat.id
    botInstance = context.bot
    botInstance.send_message(chatId,
                             text="Welcome! This bot does nothing.")

    return PRE_AUTH

def authUser(update, context):
    if update.message.text == secret.PASSWORD:
        update.message.reply_text("Welcome ;)")
        return POST_AUTH
    else:
        update.message.reply_text("I told you it does nothing.")
        return PRE_AUTH

def echo(update, context):
    update.message.reply_text(update.message.text)

def cancel(update, context):
    update.message.reply_text('Bye!')

    return ConversationHandler.END

def sendTelegramMessage(message: str):
    if not started:
        print("Please start the bot with /start on your telegram client first!")
    else:
        botInstance.send_message(chatId, text=message)

def startTelegrambot():

    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        PRE_AUTH: [MessageHandler(Filters.text & (~Filters.command), authUser)],
        POST_AUTH: [MessageHandler(Filters.text & (~Filters.command), echo)],
    },
    fallbacks=[CommandHandler('cancel', cancel)])

    updater = Updater(token=secret.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(conv_handler)
    updater.start_polling()