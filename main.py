import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

# Устанавливаем ключ API из переменной окружения
openai.api_key = os.environ["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"]


# Обработчик команды /start
def start_handler(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я помощник. Чем я могу вам помочь?")


# Обработчик сообщений от пользователя
def message_handler(update: Update, context: CallbackContext) -> None:
    # Получаем текст сообщения пользователя
    message_text = update.message.text

    # Генерируем ответ с помощью API ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message_text,
        temperature=0.5,
        max_tokens=50
    )

    # Отправляем ответ пользователю
    update.message.reply_text(response.choices[0].text)


# Создаем бота и добавляем обработчики
updater = Updater(token="5861887570:AAFuLYKNLAS_za1TJA5eQwkASiivXLAyAng", use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start_handler))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))

# Запускаем бота
updater.start_polling()
updater.idle()
