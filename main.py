import telebot
from telebot import types
import tasks_movement
import tasks_work
import tasks_concentration
import tasks_percentage
import time

# Инициализация бота
bot = telebot.TeleBot("8460111170:AAGTSFfs9-19khcCeqR4v9J5Vv0nGgR7TPg")

# Словарь для хранения данных пользователей
user_data = {}

# ========== ФУНКЦИИ ДЛЯ УПРАВЛЕНИЯ СОСТОЯНИЯМИ ==========
user_states = {}

def set_user_state(user_id, state):
    user_states[user_id] = state

def get_user_state(user_id):
    return user_states.get(user_id, 'main_menu')

def clear_user_state(user_id):
    if user_id in user_states:
        del user_states[user_id]

def get_current_module(user_id):
    return user_states.get(user_id, 'main_menu')

def is_user_in_module(user_id, module_name):
    return user_states.get(user_id) == module_name


# ==================== ГЛАВНОЕ МЕНЮ ====================
def show_main_menu(chat_id, show_welcome=False):
    """Отображает главное меню с кнопками"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_text_tasks = types.KeyboardButton('📝 Текстовые задачи')
    btn_section2 = types.KeyboardButton('📚 Раздел 2')
    btn_help = types.KeyboardButton('❓ Помощь')

    markup.add(btn_text_tasks, btn_section2, btn_help)

    if show_welcome:
        # Объединяем приветствие и главное меню в одном сообщении
        message_text = (
            '👋 *Добро пожаловать в бот-тренажер!* 📚\n\n'
            'Здесь вы можете тренироваться в решении текстовых задач по математике.\n\n'
            '🏠 *Главное меню*\n'
            'Выберите раздел для тренировки:'
        )
    else:
        message_text = "🏠 *Главное меню*\n\nВыберите раздел для тренировки:"

    bot.send_message(chat_id, message_text, 
                     parse_mode='Markdown',
                     reply_markup=markup)
    set_user_state(chat_id, 'main_menu')


# ==================== МЕНЮ ТЕКСТОВЫХ ЗАДАЧ ====================
def show_text_tasks_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_movement = types.KeyboardButton('🚗 Задачи на движение')
    btn_work = types.KeyboardButton('🛠️ Задачи на работу')
    btn_concentration = types.KeyboardButton('🧪 Задачи на концентрацию')
    btn_percentage = types.KeyboardButton('📊 Задачи на проценты')
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

    # Устанавливаем состояние как 'completed' для всех пользователей
    user_data[user_id] = {
        'state': 'completed',
        'fio': None,
        'class_name': None,
        'school': None
    }

    # Сбрасываем состояние навигации
    clear_user_state(user_id)

    # Отправляем приветственное сообщение с главным меню в одном сообщении
    show_main_menu(user_id, show_welcome=True)


# ==================== ФУНКЦИЯ ПОМОЩИ ====================
def show_help(chat_id):
    help_text = (
        "ℹ️ *Помощь по боту-тренажеру*\n\n"
        "1. *Начало работы:* Введите /start для отображения главного меню\n"
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

    # Если пользователь не начал с /start, предлагаем начать
    if user_id not in user_data:
        bot.send_message(user_id, "Пожалуйста, сначала введите команду /start")
        return

    current_state = user_data[user_id].get('state', '')

    # ========== ПОСЛЕ ПРИВЕТСТВИЯ ==========
    if current_state == 'completed':
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
            if text == '🔙 Назад к типам задач':
                show_text_tasks_menu(user_id)
                return
            else:
                # Здесь будет обработчик задач на работу
                tasks_work.handle_work_tasks(bot, message, user_data)
                return

        # ========== МОДУЛЬ: ЗАДАЧИ НА КОНЦЕНТРАЦИЮ ==========
        elif is_user_in_module(user_id, 'concentration_tasks'):
            if text == '🔙 Назад к типам задач':
                show_text_tasks_menu(user_id)
                return
            else:
                # Здесь будет обработчик задач на концентрацию
                tasks_concentration.handle_concentration_tasks(bot, message, user_data)
                return

        # ========== МОДУЛЬ: ЗАДАЧИ НА ПРОЦЕНТЫ ==========
        elif is_user_in_module(user_id, 'percentage_tasks'):
            # Обрабатываем кнопку возврата к типам задач
            if text == '🔙 Назад к типам задач':
                show_text_tasks_menu(user_id)
                return
            # Обрабатываем кнопку возврата к меню процентов
            elif text == '🔙 Назад к меню процентов':
                tasks_percentage.show_percentage_main_menu(bot, user_id)
                return
            # Обрабатываем все остальные сообщения через модуль процентов
            else:
                tasks_percentage.handle_percentage_tasks(bot, message, user_data)
                return

        # ========== МЕНЮ ТЕКСТОВЫХ ЗАДАЧ ==========
        elif current_module == 'text_tasks_menu':
            if text == '🚗 Задачи на движение':
                set_user_state(user_id, 'movement_tasks')
                tasks_movement.start_movement_tasks(bot, user_id, user_data)

            elif text == '🛠️ Задачи на работу':
                set_user_state(user_id, 'work_tasks')
                # Вызов функции запуска задач на работу
                tasks_work.start_work_tasks(bot, user_id, user_data)

            elif text == '🧪 Задачи на концентрацию':
                set_user_state(user_id, 'concentration_tasks')
                # Вызов функции запуска задач на концентрацию
                tasks_concentration.start_concentration_tasks(bot, user_id, user_data)

            elif text == '📊 Задачи на проценты':
                set_user_state(user_id, 'percentage_tasks')
                tasks_percentage.start_percentage_tasks(bot, user_id, user_data)

            elif text == '🔙 Назад в главное меню':
                show_main_menu(user_id)

            else:
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
                show_main_menu(user_id)

        # ========== НЕИЗВЕСТНОЕ СОСТОЯНИЕ ==========
        else:
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
    print("1. Задачи на движение (с тренажером)")
    print("2. Задачи на работу")
    print("3. Задачи на концентрацию")
    print("4. Задачи на проценты (с тренажером)")
    print("=" * 50)
    bot.infinity_polling(none_stop=True)