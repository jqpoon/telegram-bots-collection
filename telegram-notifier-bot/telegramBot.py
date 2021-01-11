from telegram.ext import (Updater, CommandHandler, MessageHandler, 
                          ConversationHandler, Filters)
import secret

PRE_AUTH, POST_AUTH = range(2)

class telegramNotifierBot():

    def __init__(self):
        self.chatIds = []
        self.botInstance = None

    def start(self, update, context):
        self.botInstance = context.bot
        self.botInstance.send_message(update.effective_chat.id,
                                text="Welcome! This bot does nothing.")

        return PRE_AUTH

    def authUser(self, update, context):
        if update.message.text == secret.PASSWORD:
            self.chatIds.append(update.effective_chat.id)
            update.message.reply_text("Welcome ;)")
            return POST_AUTH
        else:
            update.message.reply_text("I told you it does nothing.")
            return PRE_AUTH

    def echo(self, update, context):
        update.message.reply_text(update.message.text)

    def cancel(self, update, context):
        update.message.reply_text('Bye!')

        return ConversationHandler.END


    # "Public" methods
    def sendTelegramMessage(self, message: str):
        for chatId in self.chatIds:
            self.botInstance.send_message(chatId, text=message)

    def startTelegramBot(self):
        conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', self.start)],
        states={
            PRE_AUTH: [MessageHandler(Filters.text & (~Filters.command), self.authUser)],
            POST_AUTH: [MessageHandler(Filters.text & (~Filters.command), self.echo)],
        },
        fallbacks=[CommandHandler('cancel', self.cancel)])

        updater = Updater(token=secret.BOT_TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(conv_handler)
        updater.start_polling()