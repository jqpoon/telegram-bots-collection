from telegram.ext import (Updater, CommandHandler, MessageHandler, 
                          ConversationHandler, Filters)
import secret

PRE_AUTH, POST_AUTH = range(2)

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id,
                             text="Welcome! Please enter the password.")

    return PRE_AUTH

def authUser(update, context):
    if update.message.text == secret.PASSWORD:
        update.message.reply_text("Correct password!")
        return POST_AUTH
    else:
        update.message.reply_text("Wrong password!")
        return PRE_AUTH

def echo(update, context):
    update.message.reply_text(update.message.text)

def cancel(update, context):
    update.message.reply_text('Bye!')

    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        PRE_AUTH: [MessageHandler(Filters.text & (~Filters.command), authUser)],
        POST_AUTH: [MessageHandler(Filters.text & (~Filters.command), echo)],
    },

    fallbacks=[CommandHandler('cancel', cancel)]
)

if __name__ == "__main__":
    updater = Updater(token=secret.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(conv_handler)
    updater.start_polling()