import telebot  # импортируем библиотеку
TOKEN ='5544775908:AAHSNC4kh7uBvyj-vd2IB3YHrLJyInbSois' # в константе храним токен нашего бота

name = ' '     # здесь будем хранить имя собеседника
surname = ' '  # здесь будем хранить фамилию собеседника

bot = telebot.TeleBot(TOKEN) # создаем бота как конкретный экземпляр класса

@bot.message_handler(commands=['start', 'help'])        # реагирует на команды 'start' и 'help'
def send_welcome(message):                              # приходит message
    bot.reply_to(message, "Для запуска диалога наберите команду: /reg" + "\n" + "Для выхода из диалога наберите команду: /stop")  # отправляем на message сообщение "Какую помощь

@bot.message_handler(func=lambda m: True)
def echo_all(message):                           # приходит message
    if message.text == '/reg':                   # если в сообщении приходит команда /reg
        bot.send_message(message.from_user.id, 'Как тебя зовут ?')
        bot.register_next_step_handler(message, reg_name) # вызываем функцию reg_name

def reg_name(message):  # создаем функцию reg_name, которая принимает message
    global name  # переменную  name  объявляем глобальной
    name = message.text  # в переменную name записываем текст из пришедшего сообщения
    bot.send_message(message.from_user.id, f'Привет, {name} , напиши свою фамилию') # выводим сообщение
    bot.register_next_step_handler(message, reg_surname) # вызываем функцию reg_surname

def reg_surname(message):  # создаем функцию reg_name, которая принимает message
    global surname  # переменную  name  объявляем глобальной
    surname = message.text  # в переменную surname записываем текст из пришедшего сообщения
    bot.send_message(message.from_user.id, f'Приятно познакомиться, {name} {surname}')

bot.polling()  # запускаем цикл: читаем сообщение - отвечаем на сообщение