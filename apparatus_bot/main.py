import logging
import keys
import attributes

from telegram import *
from telegram.ext import *

logging.basicConfig(    
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Starts the game and asks the user about attribute it wants to set first."""
    reply_keyboard = [["/yes", "/no"]]

    await update.message.reply_text(
        "Привіт. Ви хочете грати у гру? Виберіть 'так', якщо так. Лівніть, якщо ні. "
        "Пришліть /no щоб лівнути.\n\n"
        "/yes для людей з великим мозком.",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Так чи ні?"
        )
    )

async def yes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_keyboard = [["Інтелект", "Психіка", "Сила", "Моторика"]]

    await update.message.reply_text("Супер, тепер вам потрібно розкидати очки по атрибутам. У вас 8 очок, обирайте розумно.")
    reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="Що буде першим?"
        ),

async def no(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Ну, вийти у вас не вийде, поки не заблочите бота, тому вибирайте /yes.")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = "Я не розумію команди, метал твердіший за плоть.")

if __name__ == '__main__':
    
    application = ApplicationBuilder().token(keys.token).build()
    
    start_handler = CommandHandler('start', start)
    yes_handler = CommandHandler('yes', yes)
    no_handler = CommandHandler('no', no)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(yes_handler)
    application.add_handler(no_handler)

    application.add_handler(unknown_handler)

    application.run_polling()
