import telebot

bot = telebot.TeleBot("7472443435:AAHMk55YuhkMLtC12LTc1fKpeSwxycVlV8w")

# Меню
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('🙋🏻О нас')
    button2 = telebot.types.KeyboardButton('✨Продукты')
    button3 = telebot.types.KeyboardButton('🌏Местоположение')
    button4 = telebot.types.KeyboardButton('👫Партнеры')
    button5 = telebot.types.KeyboardButton('📚Другая информация')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=markup)

# Обработчик кнопки
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '🙋🏻О нас':
        bot.send_message(message.from_user.id, 'Привет друг 👋🏻\n'
                         'тут будет информация о нас'.format(message.from_user))
    elif message.text == '✨Продукты':
        bot.send_message(message.from_user.id, 'Продукты ✨\n'
                         'тут будет информация о продуктах'.format(message.from_user))
    elif message.text == '👫Партнеры':
        bot.send_message(message.from_user.id, 'Партнеры 👫\n'
                         'тут будет информация о партнерах'.format(message.from_user))

    #Геолокация
    elif message.text == '🌏Местоположение':
        bot.send_message(message.from_user.id, 'Местоположение 🌏\n'
                         'тут будет информация о местоположении'.format(message.from_user))
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        location_button = telebot.types.KeyboardButton(text="⛳️Текущее местоположение", request_location=True)
        markup.add(location_button)
        bot.send_message(message.from_user.id, 'Показать где ты находишься?', reply_markup=markup)
    #WIP - button back

    # Всплывающая кнопка-меню
    elif message.text == '📚Другая информация':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = telebot.types.KeyboardButton('👨🏻Создатели')
        button2 = telebot.types.KeyboardButton('☎️Контакты')
        button3 = telebot.types.KeyboardButton('🗓️Расписание работы')
        back = telebot.types.KeyboardButton('⬅️Назад')
        markup.add(button1, button2, button3, back)
        bot.send_message(message.chat.id, '📚Другая информация', reply_markup=markup)

    elif message.text == '👨🏻Создатели':
        bot.send_message(message.from_user.id, '👨🏻‍Создатели\n'
            'тут будет информация о создателях'.format(message.from_user))

    elif message.text == '☎️Контакты':
        bot.send_message(message.from_user.id, '☎️Контакты\n'
            'тут будет информация о наших контактах'.format(message.from_user))

    elif message.text == '🗓️Расписание работы':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = telebot.types.KeyboardButton('Понедельник')
        button2 = telebot.types.KeyboardButton('Вторник')
        button3 = telebot.types.KeyboardButton('Среда')
        button4 = telebot.types.KeyboardButton('Четверг')
        button5 = telebot.types.KeyboardButton('Пятница')
        button6 = telebot.types.KeyboardButton('Суббота')
        button7 = telebot.types.KeyboardButton('Воскресенье')
        back = telebot.types.KeyboardButton('⬅️Назад')
        markup.add(button1, button2, button3, button4, button5, button6, button7, back)
        bot.send_message(message.chat.id, '🗓️Расписание работы', reply_markup=markup)

    elif message.text == 'Понедельник':
        bot.send_message(message.from_user.id, 'График работы:\n'
                         '09:00-20:00'.format(message.from_user))

    elif message.text == 'Вторник':
        bot.send_message(message.from_user.id, 'График работы:\n'
                         '09:00-20:00'.format(message.from_user))

    elif message.text == 'Среда':
        bot.send_message(message.from_user.id, 'График работы:\n'
                         '09:00-20:00'.format(message.from_user))

    elif message.text == 'Четверг':
        bot.send_message(message.from_user.id, 'График работы:\n'
                         '09:00-20:00'.format(message.from_user))

    elif message.text == 'Пятница':
        bot.send_message(message.from_user.id, 'График работы:\n'
                         '10:00-19:00'.format(message.from_user))

    elif message.text == 'Суббота':
        bot.send_message(message.from_user.id, 'График работы:\n'
                         '10:00-15:00'.format(message.from_user))

    elif message.text == 'Воскресенье':
        bot.send_message(message.from_user.id, 'График работы:\n'
                         '10:00-15:00'.format(message.from_user))

    #Кнопка назад
    elif message.text == '⬅️Назад':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = telebot.types.KeyboardButton('🙋🏻О нас')
        button2 = telebot.types.KeyboardButton('✨Продукты')
        button3 = telebot.types.KeyboardButton('🌏Местоположение')
        button4 = telebot.types.KeyboardButton('👫Партнеры')
        button5 = telebot.types.KeyboardButton('📚Другая информация')
        markup.add(button1, button2, button3, button4, button5)
        bot.send_message(message.chat.id, '⬅️Назад', reply_markup=markup)

    #WIP - button inline

if __name__ == "__main__":
    bot.infinity_polling()