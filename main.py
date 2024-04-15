import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def echo(update, context):
    await update.message.reply_text(f'Я получил сообщение {update.message.text}')


async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет {user.mention_html()}! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!",
    )


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я пока не умею помогать... Я только ваше эхо.")


async def time(update, context):
    """Отправляет сообщение когда получена команда /time"""
    time = datetime.now().time()
    await update.message.reply_text(f'Текущее время: {time}')


async def date(update, context):
    """Отправляет сообщение когда получена команда /date"""
    date = datetime.now().date()
    await update.message.reply_text(f'Текущая дата: {date}')


def main():
    application = Application.builder().token('TOKEN').build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time))
    application.add_handler(CommandHandler("date", date))
    application.add_handler(text_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
