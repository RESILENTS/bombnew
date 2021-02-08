import telebot

bot = telebot.TeleBot('1543845399:AAGMq9rrQW7xSvgAPnXUjpjBNVfw6G1E9HA')

bom = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
bom.row('Запустить бомбер 💣')
bom.row('Купить рекламу 💸')


xui = telebot.types.InlineKeyboardMarkup()
lol = telebot.types.InlineKeyboardButton(text='Запустить ✅', callback_data='play')
xui.add(lol)

anime = telebot.types.InlineKeyboardMarkup()
piz = telebot.types.InlineKeyboardButton(text='Остановить спам 🚫',callback_data='stop')
anime.add(piz)


@bot.message_handler(commands=['start'])
def send_sms(message):
    bot.send_message(message.chat.id, '<b>Добро пожаловать, вы попали в BOMBER BOT\n\nРазработчик бота @badboyee</b>', parse_mode='html', reply_markup=bom)
    
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Запустить бомбер 💣':
        bot.send_message(message.chat.id, '<b>Введите номер телефона в формате:\n+380XXXXXXXXX UA🇺🇦\n+7XXXXXXXXXX RU🇷🇺</b>', parse_mode='html')
    if message.text == 'Купить рекламу 💸':
        bot.send_message(message.chat.id, 'По поводу покупки рекламы писать @badboyee')
    elif message.text.startswith('+380') or message.text.startswith('+7'):
        number = message.text
        bot.send_message(message.from_user.id, f'<b>Ваш номер: {number}</b>', reply_markup=xui, parse_mode='html')
        
        
@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text == 'Купить рекламу 💸':
        bot.send_message(message.chat.id, 'По поводу покупки рекламы писать @badboyee')




     
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
        if call.data == 'stop':
            bot.send_message(call.message.chat.id, '<b>Спам будет остановлен в течении 5 минут!</b>', parse_mode='html')
        if call.data == 'play':
            bot.send_message(call.message.chat.id, '<b>SMS спам запущен на 20 минут!⏱</b>', parse_mode='html', reply_markup=anime)





bot.polling(none_stop=True)
