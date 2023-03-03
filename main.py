import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# create a Telegram Bot object
bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

# define a command handler function for /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm a Telegram bot!")

# define a message handler function to echo user messages
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# create an Updater object
updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)

# create handlers and add them to the dispatcher
start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(echo_handler)

# start polling for updates
updater.start_polling()
updater.idle()
