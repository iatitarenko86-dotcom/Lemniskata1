import telebot
from telebot import types
import tasks_movement
import tasks_work
import tasks_concentration
import tasks_percentage
import time
import sys
import os
import signal
import atexit

# Инициализация бота
TOKEN = "8460111170:AAGTSFfs9-19khcCeqR4v9J5Vv0nGgR7TPg"
bot = telebot.TeleBot(TOKEN)

# Файл блокировки
LOCK_FILE = 'bot.lock'

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


# ========== ФУНКЦИИ ДЛЯ ПРЕДОТВРАЩЕНИЯ МНОЖЕСТВЕННЫХ ЗАПУСКОВ ==========
def create_lock():
    """Создает файл блокировки"""
    try:
        with open(LOCK_FILE, 'x') as f:
            f.write(str(os.getpid()))
        return True
    except FileExistsError:
        # Проверяем, существует ли процесс с PID из файла
        try:
            with open(LOCK_FILE, 'r') as f:
                old_pid = int(f.read().strip())
            # Проверяем, жив ли процесс
            os.kill(old_pid, 0)
            print(f"❌ Бот уже запущен с PID: {old_pid}")
            print("💡 Используйте force_stop.py для остановки")
            return False
        except (ProcessLookupError, ValueError):
            # Процесс не существует, удаляем старый lock файл
            os.remove(LOCK_FILE)
            with open(LOCK_FILE, 'x') as f:
                f.write(str(os.getpid()))
            return True
    except Exception as e:
        print(f"⚠️ Ошибка при создании блокировки: {e}")
        return True


def remove_lock():
    """Удаляет файл блокировки"""
    try:
        if os.path.exists(LOCK_FILE):
            os.remove(LOCK_FILE)
    except:
        pass


# Регистрируем удаление lock файла при выходе
atexit.register(remove_lock)


# Обработчик сигналов
def signal_handler(sig, frame):
    print("\n👋 Получен сигнал остановки...")
    remove_lock()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


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
        "4. *Задачи на движение:* тренировка с тренажером\n"
        "5. *Задачи на концентрацию:* смеси, сплавы, растворы\n"
        "6. *Задачи на проценты:* проценты, скидки, вклады\n\n"
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
    # Проверяем, не запущен ли уже бот
    if not create_lock():
        print("\n❌ Не удалось запустить бота. Другой экземпляр уже работает.")
        print("💡 Запустите force_stop.py для завершения всех процессов")
        sys.exit(1)

    print("🤖 Бот запущен...")
    print("📡 Ожидание сообщений...")
    print("=" * 50)
    print("Доступные модули:")
    print("1. Задачи на движение (с тренажером)")
    print("2. Задачи на работу")
    print("3. Задачи на концентрацию (с тренажером)")
    print("4. Задачи на проценты (с тренажером)")
    print("=" * 50)
    print(f"📊 PID процесса: {os.getpid()}")
    print("⚠️  Для остановки бота нажмите Ctrl+C")
    print("=" * 50)

    # Запуск с обработкой ошибок
    try:
        bot.infinity_polling(none_stop=True, timeout=30, long_polling_timeout=30)
    except KeyboardInterrupt:
        print("\n👋 Бот остановлен пользователем")
    except Exception as e:
        print(f"❌ Ошибка при запуске бота: {e}")
    finally:
        remove_lock()