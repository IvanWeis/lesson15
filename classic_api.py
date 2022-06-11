import pprint  # для красивого вывода на печать
import time # для того, чтобыработалазадержка
import requests # импортируем библиотеку, необходимуюдля запросов

TOKEN ='5544775908:AAHSNC4kh7uBvyj-vd2IB3YHrLJyInbSois' # в константе храним токен нашего бота

MAIN_URL = f'https://api.telegram.org/bot{TOKEN}' # ссылка на api + TOKEN

# url = f'{MAIN_URL}/getMe' # getMe - метод api нашего бота, который возвращает информацию о боте
# result = requests.get(url)  # в переменной result сохраняем результат запроса к api нашего бота
# print(result.json()) # печатаем результат запроса в формате json
# pprint.pprint(result.json()) # печатаем вформате словаря

while True:   # никогда неостанавливается
    time.sleep(5)
    url = f'{MAIN_URL}/getUpdates' #  getUpdates - метод, который возвращает информацию об изменениях в боте
    #                                # например, информацию о пришедших сообщениях
    result = requests.get(url)  # в переменной result сохраняем результат запроса к api нашего бота
    # pprint.pprint(result.json())
    messages = result.json()['result'] # сохраням содержимое сообщения (id, text и т.д.) в messages

    for message in messages:   # отправляем ответ на пришедшее сообщение
        chat_id = message['message']['chat']['id'] # вытаскиваем chat_id из пришедшего сообщения
        url = f'{MAIN_URL}/sendMessage' #  sendMessage - метод, который отправляет сообщение от имени нашего бота
        params = {
            'chat_id': chat_id,   # отправляем сообщение на id входящего сообщения
            'text' : 'Привет от Федора Ивановича !' # текст отправляемого сообщения
        }
    result = requests.post(url, params=params) # отправляем сообщение с помощью метода POST


