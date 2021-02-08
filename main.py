from telegram import Update
from telegram import Bot 
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.utils.request import Request



updater = Updater(
        token='1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA',
        use_context=True)

def start(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
    text="Привет, я бот для отправки отзывов и пожеланий \nПожалуйста пишите весь текст одним сообщения, что бы мне было проще обработать ❤️")




def message_handler(update, context):
    text = update.message.text 
    
    doc = open("reviews.txt", "a")
    doc.write(text + ",\n")
    doc.close()
    
    context.bot.send_message(chat_id=update.effective_chat.id, text='Отправил в обработку ❤️')
    

echo_handler = MessageHandler(Filters.text &  (~Filters.command), message_handler)
updater.dispatcher.add_handler(echo_handler) 
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()
