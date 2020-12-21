import uuid
import re
from telegram.ext import (Updater, ConversationHandler,
                          CommandHandler, MessageHandler, Filters)

BOT_TOKEN = "NULL"
PRE_AUTH, POST_AUTH = range(2)

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id,
                             text="heheeh hai")

    return PRE_AUTH

def photo(update, context):
    file_uuid = uuid.uuid4()

    file = update.message.photo[-1].get_file()
    file.download('img/' + str(file_uuid) + '.jpg')
    update.message.reply_text("Visit this link to retrieve your file: localhost:8080/img/" + str(file_uuid) + ".jpg")

    return PRE_AUTH

def document(update, context):
    file_uuid = uuid.uuid4()
    ext_pattern = re.compile(r'.*(\..*)')

    document = update.message.document
    file_ext = re.match(ext_pattern, document.file_name).group(1)

    file = document.get_file()
    file.download('img/' + str(file_uuid) + file_ext)
    update.message.reply_text("Visit this link to retrieve your file: localhost:8080/img/" + str(file_uuid) + file_ext)

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.photo, photo))
dispatcher.add_handler(MessageHandler(Filters.document, document))

def start_telegrambot():
    print("Starting telegram bot!")
    updater.start_polling()