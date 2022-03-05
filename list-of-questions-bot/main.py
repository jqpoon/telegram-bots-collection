
from questions import questions_list
from secret import BOT_TOKEN
from random import randint

from telegram import Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# Define a few command handlers. These usually take the two arguments update and
# context.

# Command handlers
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[InlineKeyboardButton("Next Question", callback_data='next_question')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Click me', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer()

    keyboard = [[InlineKeyboardButton("Next Question", callback_data='next_question')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    question = questions_list[randint(0, len(questions_list) - 1)]

    query.edit_message_text(text=f"{question}", reply_markup=reply_markup)

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()