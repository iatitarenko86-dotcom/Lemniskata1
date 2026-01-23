import telebot
from telebot import types
import tasks_movement
import tasks_work
import tasks_concentration
import tasks_percentage
from user_states import *

# Инициализация бота
bot = telebot.TeleBot("8460111170:AAGTSFfs9-19khcCeqR4v9J5Vv0nGgR7TPg")

# Словарь для хранения регистрационных данных пользователей
user_data = {}


# ==================== ГЛАВНОЕ МЕНЮ ====================
def show_main_menu(chat_id):
    """Отображает главное меню с кнопками"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_text_tasks = types.KeyboardButton('📝 Текстовые задачи')
    btn_section2 = types.KeyboardButton('📚 Раздел 2')
    btn_help = types.KeyboardButton('❓ Помощь')

    markup.add(btn_text_tasks, btn_section2, btn_help)

    bot.send_message(chat_id,
                     "🏠 *Главное меню*\n\n"
                     "Выберите раздел для тренировки:",
                     parse_mode='Markdown',
                     reply_markup=markup)
    set_user_state(chat_id, 'main_menu')


# ==================== МЕНЮ ТЕКСТОВЫХ ЗАДАЧ ====================
def show_text_tasks_menu(chat_id):
    """Отображает меню типов текстовых задач"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_movement = types.KeyboardButton('🚗 Задачи на движение')
    btn_work = types.KeyboardButton('🛠️ Задачи на работу')
    btn_concentration = types.KeyboardButton('🧪 Задачи на концентрацию')
    btn_percentage = types.KeyboardButton('📊 Задачи на %')
    btn_back = types.KeyboardButton('🔙 Назад в главное меню')

    markup.add(btn_movement, btn_work, btn_concentration, btn_percentage, btn_back)

    bot.send_message(chat_id,
                     "📝 *Текстовые задачи*\n\n"
                     "Выберите тип задач для тренировки:",
                     parse_mode='Markdown',
                     reply_markup=markup)
    set_user_state(chat_id, 'text_tasks_menu')


# ==================== КОМАНДА /START ====================
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id

    # Инициализируем регистрационные данные пользователя
    user_data[user_id] = {
        'state': 'waiting_fio',
        'fio': None,
        'class_name': None,
        'school': None
    }

    # Сбрасываем состояние навигации
    clear_user_state(user_id)

    markup = types.ReplyKeyboardRemove()

    bot.send_message(user_id,
                     '👋 *Добро пожаловать в бот-тренажер!* 📚\n\n'
                     'Пожалуйста, введите ваши данные.\n\n'
                     'Для начала введите ваши фамилию, имя и отчество:',
                     parse_mode='Markdown',
                     reply_markup=markup)


# ==================== ОБРАБОТЧИК РЕГИСТРАЦИИ ====================
def handle_fio_input(user_id, text):
    """Обработка ввода ФИО"""
    if text and len(text.split()) >= 2:
        user_data[user_id]['fio'] = text
        user_data[user_id]['state'] = 'waiting_class'
        bot.send_message(user_id, "✅ Отлично! Теперь введите ваш класс обучения (например, 10А):")
    else:
        bot.send_message(user_id, "⚠️ Пожалуйста, введите фамилию, имя и отчество полностью (минимум 2 слова):")


def handle_class_input(user_id, text):
    """Обработка ввода класса"""
    if text:
        user_data[user_id]['class_name'] = text
        user_data[user_id]['state'] = 'waiting_school'
        bot.send_message(user_id, "✅ Хорошо! Теперь введите вашу образовательную организацию:")
    else:
        bot.send_message(user_id, "⚠️ Пожалуйста, введите ваш класс обучения:")


def handle_school_input(user_id, text):
    """Обработка ввода образовательной организации"""
    if text:
        user_data[user_id]['school'] = text
        user_data[user_id]['state'] = 'completed'

        # Формируем итоговое сообщение
        final_message = (
            "✅ *Спасибо! Ваши данные сохранены:*\n\n"
            f"👤 *ФИО:* {user_data[user_id]['fio']}\n"
            f"🎓 *Класс:* {user_data[user_id]['class_name']}\n"
            f"🏫 *Образовательная организация:* {user_data[user_id]['school']}\n\n"
            "Теперь вы можете приступить к тренировкам!"
        )

        bot.send_message(user_id, final_message, parse_mode='Markdown')

        # Показываем главное меню
        show_main_menu(user_id)
    else:
        bot.send_message(user_id, "⚠️ Пожалуйста, введите название образовательной организации:")


# ==================== ФУНКЦИЯ ПОМОЩИ ====================
def show_help(chat_id):
    help_text = (
        "ℹ️ *Помощь по боту-тренажеру*\n\n"
        "1. *Регистрация:* Введите /start для начала работы\n"
        "2. *Навигация:* Используйте кнопки для перехода между разделами\n"
        "3. *Текстовые задачи:* Выберите тип задач для тренировки\n"
        "4. *Раздел 2:* Дополнительные материалы (в разработке)\n\n"
        "Для возврата в главное меню используйте кнопку 'Назад'"
    )
    bot.send_message(chat_id, help_text, parse_mode='Markdown')


# ==================== ОСНОВНОЙ ОБРАБОТЧИК СООБЩЕНИЙ ====================
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.chat.id
    text = message.text.strip()

    # Если пользователь не начал с /start
    if user_id not in user_data:
        bot.send_message(user_id, "Пожалуйста, сначала введите команду /start")
        return

    current_state = user_data[user_id].get('state', '')

    # ========== РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЯ ==========
    if current_state == 'waiting_fio':
        handle_fio_input(user_id, text)
        return

    elif current_state == 'waiting_class':
        handle_class_input(user_id, text)
        return

    elif current_state == 'waiting_school':
        handle_school_input(user_id, text)
        return

    # ========== ПОСЛЕ РЕГИСТРАЦИИ ==========
    elif current_state == 'completed':
        # Получаем текущий модуль пользователя
        current_module = get_current_module(user_id)

        # ========== КНОПКА "НАЗАД" В ГЛАВНОЕ МЕНЮ ==========
        if text == '🔙 Назад в главное меню':
            show_main_menu(user_id)
            return

        # ========== МОДУЛЬ: ЗАДАЧИ НА ДВИЖЕНИЕ ==========
        elif is_user_in_module(user_id, 'movement_tasks'):
            tasks_movement.handle_movement_tasks(bot, message, user_data)
            return

        # ========== МОДУЛЬ: ЗАДАЧИ НА РАБОТУ ==========
        elif is_user_in_module(user_id, 'work_tasks'):
            # Здесь будет обработка задач на работу
            if text == '🔙 Назад к типам задач':
                show_text_tasks_menu(user_id)
                return

        # ========== МОДУЛЬ: ЗАДАЧИ НА КОНЦЕНТРАЦИЮ ==========
        elif is_user_in_module(user_id, 'concentration_tasks'):
            # Здесь будет обработка задач на концентрацию
            if text == '🔙 Назад к типам задач':
                show_text_tasks_menu(user_id)
                return

        # ========== МОДУЛЬ: ЗАДАЧИ НА ПРОЦЕНТЫ ==========
        elif is_user_in_module(user_id, 'percentage_tasks'):
            # Здесь будет обработка задач на проценты
            if text == '🔙 Назад к типам задач':
                show_text_tasks_menu(user_id)
                return

        # ========== МЕНЮ ТЕКСТОВЫХ ЗАДАЧ ==========
        elif current_module == 'text_tasks_menu':
            if text == '🚗 Задачи на движение':
                set_user_state(user_id, 'movement_tasks')
                tasks_movement.start_movement_tasks(bot, user_id, user_data)

            elif text == '🛠️ Задачи на работу':
                set_user_state(user_id, 'work_tasks')
                tasks_work.start_work_tasks(bot, user_id)

            elif text == '🧪 Задачи на концентрацию':
                set_user_state(user_id, 'concentration_tasks')
                tasks_concentration.start_concentration_tasks(bot, user_id)

            elif text == '📊 Задачи на %':
                set_user_state(user_id, 'percentage_tasks')
                tasks_percentage.start_percentage_tasks(bot, user_id)

            elif text == '🔙 Назад в главное меню':
                show_main_menu(user_id)

            else:
                # Если сообщение не распознано, показываем меню текстовых задач
                show_text_tasks_menu(user_id)

        # ========== ГЛАВНОЕ МЕНЮ ==========
        elif current_module in ['main_menu', '']:
            if text == '📝 Текстовые задачи':
                show_text_tasks_menu(user_id)

            elif text == '📚 Раздел 2':
                bot.send_message(user_id,
                                 "📚 *Раздел 2*\n\n"
                                 "Этот раздел находится в разработке...\n"
                                 "Скоро здесь появятся новые материалы!",
                                 parse_mode='Markdown')

            elif text == '❓ Помощь':
                show_help(user_id)

            else:
                # Если сообщение не распознано, показываем главное меню
                show_main_menu(user_id)

        # ========== НЕИЗВЕСТНОЕ СОСТОЯНИЕ ==========
        else:
            # Если модуль не определен, показываем главное меню
            show_main_menu(user_id)

    # ========== СОСТОЯНИЕ НЕ ОПРЕДЕЛЕНО ==========
    else:
        bot.send_message(user_id, "Произошла ошибка. Пожалуйста, введите /start для начала работы.")


# ==================== ЗАПУСК БОТА ====================
if __name__ == "__main__":
    print("🤖 Бот запущен...")
    print("📡 Ожидание сообщений...")
    print("=" * 50)
    print("Доступные модули:")
    print("1. Задачи на движение")
    print("2. Задачи на работу")
    print("3. Задачи на концентрацию")
    print("4. Задачи на проценты")
    print("=" * 50)
    bot.infinity_polling(none_stop=True)