import Constants as keys
from telegram.ext import *
import Responses as R

print("Fired up and ready to serve!")

def start_command(update, context):
    update.message.reply_text("Fired up and ready to serve!")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling(2)
    updater.idle()

main()        
        