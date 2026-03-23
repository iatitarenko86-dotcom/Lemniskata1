mport telebot
from telebot import types
import tasks_movement
import tasks_work
import tasks_concentration
import tasks_percentage
import time
import sys

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

    user_data[user_id] = {
        'state': 'completed',
        'fio': None,
        'class_name': None,
        'school': None
    }

    clear_user_state(user_id)
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

    if user_id not in user_data:
        bot.send_message(user_id, "Пожалуйста, сначала введите команду /start")
        return

    current_state = user_data[user_id].get('state', '')
    current_module = get_current_module(user_id)

    # ========== КНОПКА "НАЗАД" В ГЛАВНОЕ МЕНЮ ==========
    if text == '🔙 Назад в главное меню':
        show_main_menu(user_id)
        return

    # ========== МОДУЛЬ: ЗАДАЧИ НА ДВИЖЕНИЕ ==========
    if is_user_in_module(user_id, 'movement_tasks'):
        tasks_movement.handle_movement_tasks(bot, message, user_data)
        return

    # ========== МОДУЛЬ: ЗАДАЧИ НА КОНЦЕНТРАЦИЮ ==========
    if is_user_in_module(user_id, 'concentration_tasks'):
        try:
            # Проверяем наличие функции в модуле
            if hasattr(tasks_concentration, 'handle_concentration_tasks'):
                tasks_concentration.handle_concentration_tasks(bot, message, user_data)
            else:
                bot.send_message(user_id, "❌ Ошибка: функция обработчика не найдена в модуле концентрации")
                show_text_tasks_menu(user_id)
            return
        except Exception as e:
            bot.send_message(user_id, f"❌ Ошибка в модуле концентрации: {str(e)}")
            show_text_tasks_menu(user_id)
            return

    # ========== МОДУЛЬ: ЗАДАЧИ НА ПРОЦЕНТЫ ==========
    if is_user_in_module(user_id, 'percentage_tasks'):
        try:
            # Проверяем наличие функции в модуле
            if hasattr(tasks_percentage, 'handle_percentage_tasks'):
                tasks_percentage.handle_percentage_tasks(bot, message, user_data)
            else:
                bot.send_message(user_id, "❌ Ошибка: функция обработчика не найдена в модуле процентов")
                show_text_tasks_menu(user_id)
            return
        except Exception as e:
            bot.send_message(user_id, f"❌ Ошибка в модуле процентов: {str(e)}")
            show_text_tasks_menu(user_id)
            return

    # ========== МЕНЮ ТЕКСТОВЫХ ЗАДАЧ ==========
    if current_module == 'text_tasks_menu':
        if text == '🚗 Задачи на движение':
            set_user_state(user_id, 'movement_tasks')
            tasks_movement.start_movement_tasks(bot, user_id, user_data)

        elif text == '🛠️ Задачи на работу':
            set_user_state(user_id, 'work_tasks')
            bot.send_message(user_id,
                             "🛠️ *Задачи на работу*\n\n"
                             "Этот раздел находится в разработке.\n"
                             "Скоро здесь появятся интересные задачи!")
            show_text_tasks_menu(user_id)

        elif text == '🧪 Задачи на концентрацию':
            set_user_state(user_id, 'concentration_tasks')
            try:
                tasks_concentration.start_concentration_tasks(bot, user_id, user_data)
            except Exception as e:
                bot.send_message(user_id, f"❌ Ошибка при запуске модуля концентрации: {str(e)}")
                show_text_tasks_menu(user_id)

        elif text == '📊 Задачи на проценты':
            set_user_state(user_id, 'percentage_tasks')
            try:
                tasks_percentage.start_percentage_tasks(bot, user_id, user_data)
            except Exception as e:
                bot.send_message(user_id, f"❌ Ошибка при запуске модуля процентов: {str(e)}")
                show_text_tasks_menu(user_id)

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

    else:
        show_main_menu(user_id)


# ==================== ЗАПУСК БОТА ====================
if __name__ == "__main__":
    print("🤖 Бот запущен...")
    print("📡 Ожидание сообщений...")
    print("=" * 50)
    print("Доступные модули:")
    print("1. Задачи на движение (с тренажером)")
    print("2. Задачи на работу")
    print("3. Задачи на концентрацию (с тренажером)")
    print("4. Задачи на проценты (с тренажером)")

    # Проверка импорта модулей
    print("\n=== Проверка модулей ===")

    # Проверка модуля движения
    if 'tasks_movement' in sys.modules:
        print("✅ Модуль движения загружен")
        if hasattr(tasks_movement, 'handle_movement_tasks'):
            print("   ✅ handle_movement_tasks найдена")
    else:
        print("❌ Модуль движения НЕ загружен")

    # Проверка модуля концентрации
    if 'tasks_concentration' in sys.modules:
        print("✅ Модуль концентрации загружен")
        if hasattr(tasks_concentration, 'handle_concentration_tasks'):
            print("   ✅ handle_concentration_tasks найдена")
        if hasattr(tasks_concentration, 'start_concentration_tasks'):
            print("   ✅ start_concentration_tasks найдена")
    else:
        print("❌ Модуль концентрации НЕ загружен")

    # Проверка модуля процентов
    if 'tasks_percentage' in sys.modules:
        print("✅ Модуль процентов загружен")
        if hasattr(tasks_percentage, 'handle_percentage_tasks'):
            print("   ✅ handle_percentage_tasks найдена")
        if hasattr(tasks_percentage, 'start_percentage_tasks'):
            print("   ✅ start_percentage_tasks найдена")
    else:
        print("❌ Модуль процентов НЕ загружен")

    print("=" * 50)

    # Запуск с обработкой ошибок
    try:
        bot.infinity_polling(none_stop=True, timeout=30)
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")
        print("Убедитесь, что нет других запущенных экземпляров бота"
исправь код чат-бота, который теперь будет внедряться в ВКimport vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import tasks_movement
import tasks_work
import tasks_concentration
import tasks_percentage
import time
import sys
import random

# Инициализация бота VK
# Замените на свой токен сообщества
VK_TOKEN = "27ecf53927ecf53927ecf5392824d36f75227ec27ecf5394e2cea42448aca1778ccfb9e"
GROUP_ID =236940955 # Замените на ID вашего сообщества

# Авторизация
vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, GROUP_ID)

# Словарь для хранения данных пользователей
user_data = {}

# Словарь для хранения состояний пользователей
user_states = {}

# Словарь для хранения сообщений (для редактирования)
user_messages = {}

# ========== ФУНКЦИИ ДЛЯ УПРАВЛЕНИЯ СОСТОЯНИЯМИ ==========
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

# ========== ФУНКЦИИ ДЛЯ ОТПРАВКИ СООБЩЕНИЙ ==========
def send_message(user_id, text, keyboard=None, edit_message_id=None):
    """Отправка или редактирование сообщения"""
    try:
        if edit_message_id:
            # Редактируем существующее сообщение
            vk.messages.edit(
                peer_id=user_id,
                message_id=edit_message_id,
                message=text,
                keyboard=keyboard
            )
            return edit_message_id
        else:
            # Отправляем новое сообщение
            if keyboard:
                response = vk.messages.send(
                    user_id=user_id,
                    message=text,
                    random_id=random.randint(1, 2**31),
                    keyboard=keyboard
                )
            else:
                response = vk.messages.send(
                    user_id=user_id,
                    message=text,
                    random_id=random.randint(1, 2**31)
                )
            return response
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")
        return None

# ========== ФУНКЦИИ ДЛЯ СОЗДАНИЯ КЛАВИАТУР ==========
def create_keyboard(buttons, one_time=False, inline=False):
    """Создание клавиатуры"""
    keyboard = {
        "one_time": one_time,
        "buttons": []
    }
    
    row = []
    for button in buttons:
        if button == "🔙 Назад в главное меню":
            row.append({
                "action": {
                    "type": "text",
                    "label": button
                },
                "color": "secondary"
            })
        else:
            row.append({
                "action": {
                    "type": "text",
                    "label": button
                }
            })
        
        # Если набрали 2 кнопки в строке или это последняя кнопка
        if len(row) == 2 or button == buttons[-1]:
            keyboard["buttons"].append(row)
            row = []
    
    return vk_api.keyboard.VkKeyboard.get_empty_keyboard() if not buttons else str(keyboard).replace("'", '"')

def show_main_menu(user_id, show_welcome=False):
    """Отображает главное меню с кнопками"""
    buttons = ["📝 Текстовые задачи", "📚 Раздел 2", "❓ Помощь"]
    keyboard = create_keyboard(buttons)
    
    if show_welcome:
        message_text = (
            '👋 Добро пожаловать в бот-тренажер! 📚\n\n'
            'Здесь вы можете тренироваться в решении текстовых задач по математике.\n\n'
            '🏠 Главное меню\n'
            'Выберите раздел для тренировки:'
        )
    else:
        message_text = "🏠 Главное меню\n\nВыберите раздел для тренировки:"
    
    send_message(user_id, message_text, keyboard)
    set_user_state(user_id, 'main_menu')

def show_text_tasks_menu(user_id):
    """Отображает меню текстовых задач"""
    buttons = [
        "🚗 Задачи на движение",
        "🛠️ Задачи на работу",
        "🧪 Задачи на концентрацию",
        "📊 Задачи на проценты",
        "🔙 Назад в главное меню"
    ]
    keyboard = create_keyboard(buttons)
    
    message_text = (
        "📝 Текстовые задачи\n\n"
        "Выберите тип задач для тренировки:"
    )
    
    send_message(user_id, message_text, keyboard)
    set_user_state(user_id, 'text_tasks_menu')

def show_help(user_id):
    """Показывает справку"""
    help_text = (
        "ℹ️ Помощь по боту-тренажеру\n\n"
        "1. Начало работы: Напишите любое сообщение для отображения главного меню\n"
        "2. Навигация: Используйте кнопки для перехода между разделами\n"
        "3. Текстовые задачи: Выберите тип задач для тренировки\n"
        "4. Раздел 2: Дополнительные материалы (в разработке)\n\n"
        "Для возврата в главное меню используйте кнопку 'Назад'"
    )
    send_message(user_id, help_text)

# ==================== ОСНОВНОЙ ОБРАБОТЧИК СООБЩЕНИЙ ====================
def handle_message(event):
    user_id = event.obj.message['from_id']
    text = event.obj.message['text'].strip()
    
    # Инициализация данных пользователя
    if user_id not in user_data:
        user_data[user_id] = {
            'state': 'completed',
            'fio': None,
            'class_name': None,
            'school': None
        }
    
    current_module = get_current_module(user_id)
    
    # ========== КНОПКА "НАЗАД" В ГЛАВНОЕ МЕНЮ ==========
    if text == '🔙 Назад в главное меню':
        show_main_menu(user_id)
        return
    
    # ========== МОДУЛЬ: ЗАДАЧИ НА ДВИЖЕНИЕ ==========
    if is_user_in_module(user_id, 'movement_tasks'):
        if hasattr(tasks_movement, 'handle_movement_tasks'):
            tasks_movement.handle_movement_tasks(vk, user_id, text, user_data)
        return
    
    # ========== МОДУЛЬ: ЗАДАЧИ НА РАБОТУ ==========
    if is_user_in_module(user_id, 'work_tasks'):
        # Адаптация для VK
        if hasattr(tasks_work, 'handle_work_tasks'):
            tasks_work.handle_work_tasks(vk, user_id, text, user_data)
        return
    
    # ========== МОДУЛЬ: ЗАДАЧИ НА КОНЦЕНТРАЦИЮ ==========
    if is_user_in_module(user_id, 'concentration_tasks'):
        try:
            if hasattr(tasks_concentration, 'handle_concentration_tasks'):
                tasks_concentration.handle_concentration_tasks(vk, user_id, text, user_data)
            else:
                send_message(user_id, "❌ Ошибка: функция обработчика не найдена в модуле концентрации")
                show_text_tasks_menu(user_id)
            return
        except Exception as e:
            send_message(user_id, f"❌ Ошибка в модуле концентрации: {str(e)}")
            show_text_tasks_menu(user_id)
            return
    
    # ========== МОДУЛЬ: ЗАДАЧИ НА ПРОЦЕНТЫ ==========
    if is_user_in_module(user_id, 'percentage_tasks'):
        try:
            if hasattr(tasks_percentage, 'handle_percentage_tasks'):
                tasks_percentage.handle_percentage_tasks(vk, user_id, text, user_data)
            else:
                send_message(user_id, "❌ Ошибка: функция обработчика не найдена в модуле процентов")
                show_text_tasks_menu(user_id)
            return
        except Exception as e:
            send_message(user_id, f"❌ Ошибка в модуле процентов: {str(e)}")
            show_text_tasks_menu(user_id)
            return
    
    # ========== МЕНЮ ТЕКСТОВЫХ ЗАДАЧ ==========
    if current_module == 'text_tasks_menu':
        if text == '🚗 Задачи на движение':
            set_user_state(user_id, 'movement_tasks')
            if hasattr(tasks_movement, 'start_movement_tasks'):
                tasks_movement.start_movement_tasks(vk, user_id, user_data)
            else:
                send_message(user_id, "Модуль задач на движение загружается...")
                show_text_tasks_menu(user_id)
        
        elif text == '🛠️ Задачи на работу':
            set_user_state(user_id, 'work_tasks')
            send_message(user_id,
                         "🛠️ Задачи на работу\n\n"
                         "Этот раздел находится в разработке.\n"
                         "Скоро здесь появятся интересные задачи!")
            show_text_tasks_menu(user_id)
        
        elif text == '🧪 Задачи на концентрацию':
            set_user_state(user_id, 'concentration_tasks')
            try:
                if hasattr(tasks_concentration, 'start_concentration_tasks'):
                    tasks_concentration.start_concentration_tasks(vk, user_id, user_data)
                else:
                    send_message(user_id, "❌ Ошибка: функция запуска не найдена")
                    show_text_tasks_menu(user_id)
            except Exception as e:
                send_message(user_id, f"❌ Ошибка при запуске модуля концентрации: {str(e)}")
                show_text_tasks_menu(user_id)
        
        elif text == '📊 Задачи на проценты':
            set_user_state(user_id, 'percentage_tasks')
            try:
                if hasattr(tasks_percentage, 'start_percentage_tasks'):
                    tasks_percentage.start_percentage_tasks(vk, user_id, user_data)
                else:
                    send_message(user_id, "❌ Ошибка: функция запуска не найдена")
                    show_text_tasks_menu(user_id)
            except Exception as e:
                send_message(user_id, f"❌ Ошибка при запуске модуля процентов: {str(e)}")
                show_text_tasks_menu(user_id)
        
        else:
            show_text_tasks_menu(user_id)
    
    # ========== ГЛАВНОЕ МЕНЮ ==========
    elif current_module in ['main_menu', '']:
        if text == '📝 Текстовые задачи':
            show_text_tasks_menu(user_id)
        
        elif text == '📚 Раздел 2':
            send_message(user_id,
                         "📚 Раздел 2\n\n"
                         "Этот раздел находится в разработке...\n"
                         "Скоро здесь появятся новые материалы!")
        
        elif text == '❓ Помощь':
            show_help(user_id)
        
        else:
            show_main_menu(user_id)
    
    else:
        show_main_menu(user_id)

# ==================== ЗАПУСК БОТА ====================
if __name__ == "__main__":
    print("🤖 Бот ВКонтакте запущен...")
    print("📡 Ожидание сообщений...")
    print("=" * 50)
    print("Доступные модули:")
    print("1. Задачи на движение (с тренажером)")
    print("2. Задачи на работу")
    print("3. Задачи на концентрацию (с тренажером)")
    print("4. Задачи на проценты (с тренажером)")
    
    # Проверка импорта модулей
    print("\n=== Проверка модулей ===")
    
    if 'tasks_movement' in sys.modules:
        print("✅ Модуль движения загружен")
    else:
        print("❌ Модуль движения НЕ загружен")
    
    if 'tasks_work' in sys.modules:
        print("✅ Модуль работы загружен")
    else:
        print("❌ Модуль работы НЕ загружен")
    
    if 'tasks_concentration' in sys.modules:
        print("✅ Модуль концентрации загружен")
    else:
        print("❌ Модуль концентрации НЕ загружен")
    
    if 'tasks_percentage' in sys.modules:
        print("✅ Модуль процентов загружен")
    else:
        print("❌ Модуль процентов НЕ загружен")
    
    print("=" * 50)
    
    # Основной цикл обработки сообщений
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.obj.message['from_id'] > 0:  # Проверяем, что сообщение от пользователя
                    handle_message(event)
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")
