from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# triggered when /help command is sent to bot
def help_receiver(update,context):
    update.message.reply_text('help command received')

# triggered when /start command is sent to bot
def start_receiver(update,context):
    update.message.reply_text('hello welcome to Telegram Bot')

# triggered when /book command is sent to bot
def book_receiver(update,context):
    update.message.reply_text('booking started')

# triggered when a plain text is sent to bot
def echo(update,context):
    user_msg=update.message.text
    update.message.reply_text(user_msg)

# heart of telegram bot where all the incoming messages are filtered and handled.
# refer https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.html for documentation
def main():
    try:
        #configure the updater with your bot token
        updater = Updater("insert your bot token", use_context=True)

        #configure a dispatcher (responsible for receiving messages from bot )
        dp = updater.dispatcher

        #configure the command handlers
        """
        telegram bots have a default command '/start', 
        when you try to make a conversation with the bot for the first time, you can use the /start command
        You can add your custom commands using add_handler method.
        CommandHandler is responsible for handling the command type messages, they usually look like /start,/help,etc
        I configured a custom command 'book', so when the user sends '/book' the function book_receiver wil be called   
        """
        dp.add_handler(CommandHandler("start", start_receiver))
        dp.add_handler(CommandHandler("book", book_receiver))
        dp.add_handler(CommandHandler("help", help_receiver))

        """
        Just like command handler, we have MessageHandler which takes care of all the incoming messages other than commands
        we can filter out the various messages using Filters.text or Filters.audio
        where Filters.text will handle all the plain text messages sent to the bot 
        Filters.audio will handle all the audio files sent to the bot    
        """
        # on non-command i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text,echo))

        # Start getting updates from the bot
        updater.start_polling()
        updater.idle()
    #exception handling can be used in this manner as deploying this bot will give you many webhook errors,etc if not configured properly
    #handle them carefully, if not this may lead to program crash in production.
    except:
        #incase of any errors, i am calling the main function  to reset the program execution.
        main()

#indicates that the bot started to listen the responses
print("bot started")

#call the main function
main()
