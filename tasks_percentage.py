from telebot import types


def start_percentage_tasks(bot, chat_id):
    """Начинает работу с задачами на проценты"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к типам задач')
    markup.add(btn_back)

    bot.send_message(chat_id,
                     "📊 *Задачи на проценты*\n\n"
                     "Этот раздел находится в разработке.\n"
                     "Скоро здесь появятся интересные задачи!",
                     parse_mode='Markdown',
                     reply_markup=markup)