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
    elif message.text == '🌏Местоположение':
        bot.send_message(message.from_user.id, 'Местоположение 🌏\n'
                         'тут будет информация о местоположении'.format(message.from_user))
    elif message.text == '👫Партнеры':
        bot.send_message(message.from_user.id, 'Партнеры 👫\n'
                         'тут будет информация о партнерах'.format(message.from_user))
    # Всплывающая кнопка-меню
    elif message.text == '📚Другая информация':
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = telebot.types.KeyboardButton('👨🏻‍🎓Создатели')
        button2 = telebot.types.KeyboardButton('👨🏻‍🎓Контакты')
        back = telebot.types.KeyboardButton('⬅️Назад')
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, '📚Другая информация', reply_markup=markup)

    #WIP - кнопка назад

if __name__ == "__main__":
    bot.infinity_polling()