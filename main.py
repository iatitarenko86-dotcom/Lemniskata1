iimport vk_api
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
