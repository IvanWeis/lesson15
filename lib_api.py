import telebot  # импортируем библиотеку
TOKEN ='5544775908:AAHSNC4kh7uBvyj-vd2IB3YHrLJyInbSois' # в константе храним токен нашего бота

bot = telebot.TeleBot(TOKEN) # создаем бота как конкретный экземпляр класса

# @bot.message_handler(commands=['start', 'help'])        # реагирует на команды 'start' и 'help'
# def send_welcome(message):                              # приходит message
#     bot.reply_to(message, "Какую помощь Вам оказать ?")  # отправляем на message сообщение "Какую помощь

# @bot.message_handler(content_types='text')        # реагирует на принятый текст
# def send_welcome(message):                              # приходит message
#     bot.reply_to(message, "Привет от Федора Ивановича")  # отправляем на message сообщение "Howdy,...

@bot.message_handler(content_types='text')        # реагирует на принятый текст
def send_welcome(message):                              # приходит message
    text = message.text # вытаскиваем из message введенный текст
    #print(text)
    if text == '1':
        answer = 'Привет мальчик'
    else:
        answer = 'Привет девочка'
    bot.reply_to(message, answer)  # отправляем на message сообщение "Howdy,.

bot.polling()  # запускаем цикл: читаем сообщение - отвечаем на сообщение
