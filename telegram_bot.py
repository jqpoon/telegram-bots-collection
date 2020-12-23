import uuid
import re
from telegram.ext import (Updater, ConversationHandler,
                          CommandHandler, MessageHandler, Filters)

PRE_AUTH, POST_AUTH = range(2)


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id,
                             text="Welcome!")

    return PRE_AUTH


def photo(update, context):
    file_uuid = uuid.uuid4()

    file = update.message.photo[-1].get_file()
    file.download('img/' + str(file_uuid) + '.jpg')
    update.message.reply_text(
        "Visit this link to retrieve your file: localhost:8080/img/" + str(file_uuid) + ".jpg")

    return PRE_AUTH


def document(update, context):
    file_uuid = uuid.uuid4()
    extension_pattern = re.compile(r'.*(\..*)')

    document = update.message.document
    file_ext = re.match(extension_pattern, document.file_name).group(1)

    if (not file_ext):
        update.message.reply_text("Invalid file detected! Please try again.")
    else:
        file = document.get_file()
        file.download('img/' + str(file_uuid) + file_ext)
        update.message.reply_text(
            "Visit this link to retrieve your file: localhost:8080/img/" + str(file_uuid) + file_ext)


def start_telegrambot(BOT_TOKEN: str):
    print("Starting telegram bot!")
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.photo, photo))
    dispatcher.add_handler(MessageHandler(Filters.document, document))
    updater.start_polling()
