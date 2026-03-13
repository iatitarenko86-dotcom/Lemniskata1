import telebot
from telebot import types
from user_states import set_user_state, get_user_state, update_user_data
from simulator_concentration1 import SimulatorConcentration1
from simulator_concentration2 import SimulatorConcentration2
from simulator_concentration3 import SimulatorConcentration3
from simulator_concentration4 import SimulatorConcentration4
import inspect

# Глобальный словарь для хранения тренажеров по пользователям
тренажеры_пользователей = {}


# ==================== ФУНКЦИЯ-ОБЕРТКА ДЛЯ НАВИГАЦИИ ====================
def show_text_tasks_menu_wrapper(bot, chat_id):
    """Обертка для вызова show_text_tasks_menu из main.py"""
    try:
        # Пробуем импортировать функцию
        from main import show_text_tasks_menu

        # Проверяем сигнатуру функции
        sig = inspect.signature(show_text_tasks_menu)

        if len(sig.parameters) == 1:
            # Функция принимает только chat_id
            show_text_tasks_menu(chat_id)
        else:
            # Функция принимает bot и chat_id
            show_text_tasks_menu(bot, chat_id)
    except ImportError:
        # Если функция не найдена в main.py, показываем меню концентрации
        show_concentration_main_menu(bot, chat_id)
    except Exception as e:
        print(f"Ошибка при вызове show_text_tasks_menu: {e}")
        show_concentration_main_menu(bot, chat_id)


# ==================== ГЛАВНОЕ МЕНЮ КОНЦЕНТРАЦИИ ====================
def show_concentration_main_menu(bot, chat_id):
    """Отображает главное меню задач на концентрацию"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_reference = types.KeyboardButton('📚 Справочный материал')
    btn_examples = types.KeyboardButton('📝 Примеры задач')
    btn_training = types.KeyboardButton('🎓 Обучение')
    btn_simulator = types.KeyboardButton('🎯 Тренажер')
    btn_back = types.KeyboardButton('🔙 Назад к типам задач')

    markup.add(btn_reference, btn_examples, btn_training, btn_simulator, btn_back)

    bot.send_message(chat_id,
                     "🧪 *Задачи на концентрацию смесей и сплавов*\n\n"
                     "Выберите раздел для изучения:\n\n"
                     "• *📚 Справочный материал* - формулы и теория\n"
                     "• *📝 Примеры задач* - готовые решения\n"
                     "• *🎓 Обучение* - пошаговое изучение\n"
                     "• *🎯 Тренажер* - практические задания",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'concentration_tasks', 'main_menu')


# ==================== НАЧАЛО РАБОТЫ ====================
def start_concentration_tasks(bot, chat_id, user_data):
    """Начинает работу с задачами на концентрацию"""
    show_concentration_main_menu(bot, chat_id)


# ==================== МЕНЮ ТРЕНАЖЕРА ====================
def show_simulator_menu(bot, chat_id):
    """Отображает меню тренажера"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_easy = types.KeyboardButton('🟢 Легкий уровень')
    btn_medium = types.KeyboardButton('🟡 Средний уровень')
    btn_hard = types.KeyboardButton('🔴 Сложный уровень')
    btn_random = types.KeyboardButton('🎲 Случайная задача')
    btn_back = types.KeyboardButton('🔙 Назад к меню концентрации')

    markup.add(btn_easy, btn_medium, btn_hard, btn_random, btn_back)

    bot.send_message(chat_id,
                     "🎯 *Тренажер: Задачи на концентрацию*\n\n"
                     "Выберите уровень сложности:\n\n"
                     "• *🟢 Легкий* - базовые задачи на смешивание\n"
                     "• *🟡 Средний* - задачи с системой уравнений\n"
                     "• *🔴 Сложный* - задачи на сплавы и высушивание\n"
                     "• *🎲 Случайная* - задача любого уровня",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'concentration_tasks', 'simulator_menu')


# ==================== ЗАПУСК ЛЕГКОГО УРОВНЯ ====================
def start_easy_simulator(bot, chat_id):
    """Запускает легкий уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorConcentration1()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorConcentration1):
                тренажеры_пользователей[chat_id] = SimulatorConcentration1()

        тренажер = тренажеры_пользователей[chat_id]

        # Начинаем уровень
        задача = тренажер.начать_уровень()

        # Сохраняем состояние
        update_user_data(chat_id, {
            'тренажер_активен': True,
            'уровень_тренажера': 'легкий'
        })

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_hint = types.KeyboardButton('💡 Подсказка')
        btn_answer = types.KeyboardButton('📝 Показать ответ')
        btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
        markup.add(btn_hint, btn_answer, btn_back)

        bot.send_message(chat_id,
                         f"🟢 *Легкий уровень тренажера*\n\n"
                         f"{задача}\n\n"
                         "Введите *ответ* в чат (только число, без процентов и единиц измерения):",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'concentration_tasks', 'easy_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске легкого уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СРЕДНЕГО УРОВНЯ ====================
def start_medium_simulator(bot, chat_id):
    """Запускает средний уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorConcentration2()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorConcentration2):
                тренажеры_пользователей[chat_id] = SimulatorConcentration2()

        тренажер = тренажеры_пользователей[chat_id]

        # Начинаем уровень
        задача = тренажер.начать_уровень()

        # Сохраняем состояние
        update_user_data(chat_id, {
            'тренажер_активен': True,
            'уровень_тренажера': 'средний'
        })

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_hint = types.KeyboardButton('💡 Подсказка')
        btn_answer = types.KeyboardButton('📝 Показать ответ')
        btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
        markup.add(btn_hint, btn_answer, btn_back)

        bot.send_message(chat_id,
                         f"🟡 *Средний уровень тренажера*\n\n"
                         f"{задача}\n\n"
                         "Введите *ответ* в чат (только число, без процентов и единиц измерения):",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'concentration_tasks', 'medium_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске среднего уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СЛОЖНОГО УРОВНЯ ====================
def start_hard_simulator(bot, chat_id):
    """Запускает сложный уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorConcentration3()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorConcentration3):
                тренажеры_пользователей[chat_id] = SimulatorConcentration3()

        тренажер = тренажеры_пользователей[chat_id]

        # Начинаем уровень
        задача = тренажер.начать_уровень()

        # Сохраняем состояние
        update_user_data(chat_id, {
            'тренажер_активен': True,
            'уровень_тренажера': 'сложный'
        })

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_hint = types.KeyboardButton('💡 Подсказка')
        btn_answer = types.KeyboardButton('📝 Показать ответ')
        btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
        markup.add(btn_hint, btn_answer, btn_back)

        bot.send_message(chat_id,
                         f"🔴 *Сложный уровень тренажера*\n\n"
                         f"{задача}\n\n"
                         "Введите *ответ* в чат (только число, без процентов и единиц измерения):",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'concentration_tasks', 'hard_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске сложного уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СЛУЧАЙНЫХ ЗАДАЧ ====================
def start_random_simulator(bot, chat_id):
    """Запускает режим случайных задач"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorConcentration4()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorConcentration4):
                тренажеры_пользователей[chat_id] = SimulatorConcentration4()

        тренажер = тренажеры_пользователей[chat_id]

        # Начинаем уровень
        задача = тренажер.начать_уровень()

        # Сохраняем состояние
        update_user_data(chat_id, {
            'тренажер_активен': True,
            'уровень_тренажера': 'случайные'
        })

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_hint = types.KeyboardButton('💡 Подсказка')
        btn_answer = types.KeyboardButton('📝 Показать ответ')
        btn_next = types.KeyboardButton('🔄 Новая задача')
        btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
        markup.add(btn_hint, btn_answer, btn_next, btn_back)

        bot.send_message(chat_id,
                         f"🎲 *Случайная задача*\n\n"
                         f"{задача}\n\n"
                         "Введите *ответ* в чат (только число, без процентов и единиц измерения):",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'concentration_tasks', 'random_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске случайных задач: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ОБЩИЕ ФУНКЦИИ ДЛЯ ТРЕНАЖЕРА ====================
def handle_simulator_input(bot, chat_id, user_input, уровень):
    """Обрабатывает ввод ответа в тренажере"""
    try:
        if chat_id not in тренажеры_пользователей:
            bot.send_message(chat_id, "❌ Тренажер не инициализирован. Начните заново.")
            show_simulator_menu(bot, chat_id)
            return

        тренажер = тренажеры_пользователей[chat_id]

        успех, сообщение = тренажер.проверить_ответ(user_input)

        # Определяем текст и эмодзи для уровня
        уровень_данные = {
            'легкий': {'эмодзи': '🟢', 'текст': 'Легкий уровень тренажера'},
            'средний': {'эмодзи': '🟡', 'текст': 'Средний уровень тренажера'},
            'сложный': {'эмодзи': '🔴', 'текст': 'Сложный уровень тренажера'},
            'случайные': {'эмодзи': '🎲', 'текст': 'Случайная задача'}
        }

        данные_уровня = уровень_данные.get(уровень, {'эмодзи': '🧪', 'текст': 'Тренажер'})

        # Создаем разметку кнопок
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_hint = types.KeyboardButton('💡 Подсказка')
        btn_answer = types.KeyboardButton('📝 Показать ответ')

        if уровень == 'случайные':
            btn_next = types.KeyboardButton('🔄 Новая задача')
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_hint, btn_answer, btn_next, btn_back)
        else:
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_hint, btn_answer, btn_back)

        if успех:
            if "Следующая задача" in сообщение or "следующая задача" in сообщение.lower():
                # Показываем следующую задачу
                задача = тренажер.получить_текущую_задачу()

                bot.send_message(chat_id,
                                 f"{данные_уровня['эмодзи']} *{данные_уровня['текст']}*\n\n"
                                 f"✅ *Правильно!*\n\n"
                                 f"{задача}\n\n"
                                 "Введите *ответ* в чат:",
                                 parse_mode='Markdown',
                                 reply_markup=markup)
            else:
                # Все задачи решены (только для уровневых тренажеров)
                if уровень != 'случайные':
                    final_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    btn_back_final = types.KeyboardButton('🔙 Назад к тренажеру')
                    final_markup.add(btn_back_final)

                    bot.send_message(chat_id,
                                     f"✅ *Поздравляем!*\n\n"
                                     f"🎉 *Вы успешно решили все задачи {уровень} уровня!*\n\n"
                                     f"Можете вернуться в меню тренажера или выбрать другой уровень.",
                                     parse_mode='Markdown',
                                     reply_markup=final_markup)
                else:
                    # Для случайных задач просто показываем следующую
                    задача = тренажер.получить_следующую_задачу()
                    bot.send_message(chat_id,
                                     f"✅ *Правильно!*\n\n"
                                     f"🎲 *Следующая случайная задача:*\n\n"
                                     f"{задача}\n\n"
                                     "Введите *ответ* в чат:",
                                     parse_mode='Markdown',
                                     reply_markup=markup)
        else:
            # Неправильный ответ
            задача = тренажер.получить_текущую_задачу()

            bot.send_message(chat_id,
                             f"{данные_уровня['эмодзи']} *{данные_уровня['текст']}*\n\n"
                             f"{сообщение}\n\n"
                             f"{задача}\n\n"
                             "Введите *ответ* в чат:",
                             parse_mode='Markdown',
                             reply_markup=markup)
    except Exception as e:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_hint = types.KeyboardButton('💡 Подсказка')
        btn_answer = types.KeyboardButton('📝 Показать ответ')
        btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
        markup.add(btn_hint, btn_answer, btn_back)

        bot.send_message(chat_id,
                         f"❌ Ошибка при проверке ответа: {str(e)}\n\n"
                         "Попробуйте еще раз или вернитесь в меню:",
                         parse_mode='Markdown',
                         reply_markup=markup)


def send_simulator_hint(bot, chat_id):
    """Отправляет подсказку для тренажера"""
    try:
        if chat_id not in тренажеры_пользователей:
            bot.send_message(chat_id, "❌ Тренажер не инициализирован.")
            return

        тренажер = тренажеры_пользователей[chat_id]
        подсказка = тренажер.получить_подсказку()

        # Сохраняем кнопки после подсказки
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        user_state = get_user_state(chat_id)
        submodule = user_state.get('sub_module', '')

        if submodule == 'random_simulator':
            btn_hint = types.KeyboardButton('💡 Подсказка')
            btn_answer = types.KeyboardButton('📝 Показать ответ')
            btn_next = types.KeyboardButton('🔄 Новая задача')
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_hint, btn_answer, btn_next, btn_back)
        else:
            btn_hint = types.KeyboardButton('💡 Подсказка')
            btn_answer = types.KeyboardButton('📝 Показать ответ')
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_hint, btn_answer, btn_back)

        bot.send_message(chat_id, подсказка, parse_mode='Markdown', reply_markup=markup)
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при получении подсказки: {str(e)}")


def show_simulator_answer(bot, chat_id):
    """Показывает ответ для тренажера"""
    try:
        if chat_id not in тренажеры_пользователей:
            bot.send_message(chat_id, "❌ Тренажер не инициализирован.")
            return

        тренажер = тренажеры_пользователей[chat_id]
        ответ = тренажер.показать_ответ()

        user_state = get_user_state(chat_id)
        submodule = user_state.get('sub_module', '')

        if submodule == 'random_simulator':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn_next = types.KeyboardButton('🔄 Новая задача')
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_next, btn_back)

            bot.send_message(chat_id,
                             f"🎲 *Случайная задача*\n\n"
                             f"{ответ}\n\n"
                             "Нажмите 'Новая задача' для продолжения:",
                             parse_mode='Markdown',
                             reply_markup=markup)
        else:
            # Определяем уровень для уровневых тренажеров
            уровень_данные = {
                'easy_simulator': {'эмодзи': '🟢', 'текст': 'Легкий уровень тренажера'},
                'medium_simulator': {'эмодзи': '🟡', 'текст': 'Средний уровень тренажера'},
                'hard_simulator': {'эмодзи': '🔴', 'текст': 'Сложный уровень тренажера'}
            }

            данные_уровня = уровень_данные.get(submodule, {'эмодзи': '🧪', 'текст': 'Тренажер'})

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn_next = types.KeyboardButton('➡️ Следующая задача')
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_next, btn_back)

            bot.send_message(chat_id,
                             f"{данные_уровня['эмодзи']} *{данные_уровня['текст']}*\n\n"
                             f"{ответ}\n\n"
                             "Нажмите 'Следующая задача' для продолжения:",
                             parse_mode='Markdown',
                             reply_markup=markup)
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при показе ответа: {str(e)}")


def next_simulator_task(bot, chat_id):
    """Переходит к следующей задаче в тренажере"""
    try:
        if chat_id not in тренажеры_пользователей:
            bot.send_message(chat_id, "❌ Тренажер не инициализирован.")
            return

        тренажер = тренажеры_пользователей[chat_id]
        user_state = get_user_state(chat_id)
        submodule = user_state.get('sub_module', '')

        if submodule == 'random_simulator':
            # Для случайных задач получаем новую задачу
            задача = тренажер.получить_следующую_задачу()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn_hint = types.KeyboardButton('💡 Подсказка')
            btn_answer = types.KeyboardButton('📝 Показать ответ')
            btn_next = types.KeyboardButton('🔄 Новая задача')
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_hint, btn_answer, btn_next, btn_back)

            bot.send_message(chat_id,
                             f"🎲 *Случайная задача*\n\n"
                             f"{задача}\n\n"
                             "Введите *ответ* в чат:",
                             parse_mode='Markdown',
                             reply_markup=markup)
        else:
            # Для уровневых тренажеров переходим к следующей задаче
            if hasattr(тренажер, 'текущая_задача'):
                тренажер.текущая_задача += 1

            задача = тренажер.получить_текущую_задачу()

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn_hint = types.KeyboardButton('💡 Подсказка')
            btn_answer = types.KeyboardButton('📝 Показать ответ')
            btn_back = types.KeyboardButton('🔙 Назад к тренажеру')
            markup.add(btn_hint, btn_answer, btn_back)

            # Определяем уровень
            уровень_данные = {
                'easy_simulator': {'эмодзи': '🟢', 'текст': 'Легкий уровень тренажера'},
                'medium_simulator': {'эмодзи': '🟡', 'текст': 'Средний уровень тренажера'},
                'hard_simulator': {'эмодзи': '🔴', 'текст': 'Сложный уровень тренажера'}
            }

            данные_уровня = уровень_данные.get(submodule, {'эмодзи': '🧪', 'текст': 'Тренажер'})

            bot.send_message(chat_id,
                             f"{данные_уровня['эмодзи']} *{данные_уровня['текст']}*\n\n"
                             f"{задача}\n\n"
                             "Введите *ответ* в чат:",
                             parse_mode='Markdown',
                             reply_markup=markup)
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при переходе к следующей задаче: {str(e)}")


# ==================== СПРАВОЧНЫЙ МАТЕРИАЛ ====================
def send_reference_material(bot, chat_id):
    """Отправляет справочный материал по задачам на концентрацию"""
    reference_text = (
        "📚 *Справочный материал по задачам на концентрацию*\n\n"
        "*Основные понятия:*\n\n"
        "• *Концентрация* вещества в растворе (смеси, сплаве) — это отношение массы (объёма) этого вещества к общей массе (объёму) раствора, выраженное в процентах.\n\n"
        "• *Формула концентрации:*\n"
        "```\n"
        "           m(вещества)\n"
        "    c = ─────────────── × 100%\n"
        "           m(раствора)\n"
        "```\n"
        "где c — концентрация в процентах,\n"
        "m(вещества) — масса вещества,\n"
        "m(раствора) — общая масса раствора.\n\n"
        "• *Масса вещества в растворе:*\n"
        "```\n"
        "    m(вещества) = m(раствора) × c / 100%\n"
        "```\n\n"
        "*Основные типы задач:*\n\n"
        "1. *Смешивание растворов одного вещества*\n"
        "   При смешивании двух растворов масса вещества в новом растворе равна сумме масс веществ в исходных растворах, а общая масса равна сумме масс исходных растворов.\n\n"
        "   *Уравнение:*\n"
        "   ```\n"
        "   m₁·c₁ + m₂·c₂ = (m₁ + m₂)·c\n"
        "   ```\n"
        "   где m₁, m₂ — массы исходных растворов,\n"
        "   c₁, c₂ — их концентрации,\n"
        "   c — концентрация конечного раствора.\n\n"
        "2. *Задачи на сплавы*\n"
        "   Аналогично растворам, но работаем с массами металлов.\n\n"
        "3. *Задачи на высушивание*\n"
        "   При высушивании удаляется вода, а масса сухого вещества остаётся неизменной.\n\n"
        "   *Уравнение:*\n"
        "   ```\n"
        "   m₁ · (100% - w₁)/100% = m₂ · (100% - w₂)/100%\n"
        "   ```\n"
        "   где m₁, m₂ — массы продукта до и после высушивания,\n"
        "   w₁, w₂ — процентное содержание воды.\n\n"
        "*Методы решения:*\n\n"
        "• *Метод стаканчиков* — визуальное представление смешивания растворов\n"
        "• *Метод креста (правило смешения)* — для быстрого нахождения соотношения компонентов\n"
        "• *Составление системы уравнений* — для сложных задач с двумя неизвестными\n\n"
        "*Правило креста:*\n"
        "```\n"
        "      a         |c - b|\n"
        "        \\     /\n"
        "          c\n"
        "        /     \\\n"
        "      b         |a - c|\n"
        "```\n"
        "Соотношение a : b = |c - b| : |a - c|"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к меню концентрации')
    markup.add(btn_back)

    bot.send_message(chat_id, reference_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'concentration_tasks', 'reference')


# ==================== МЕНЮ ПРИМЕРОВ (5 КНОПОК) ====================
def show_examples_menu(bot, chat_id):
    """Отображает меню примеров задач с 5 кнопками"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_example1 = types.KeyboardButton('🧪 Пример 1: Смешивание растворов')
    btn_example2 = types.KeyboardButton('⚗️ Пример 2: Система уравнений')
    btn_example3 = types.KeyboardButton('🏺 Пример 3: Сплав латуни')
    btn_example4 = types.KeyboardButton('🍎 Пример 4: Высушивание фруктов')
    btn_example5 = types.KeyboardButton('📊 Пример 5: Дополнительная задача')
    btn_back = types.KeyboardButton('🔙 Назад к меню концентрации')

    markup.add(btn_example1, btn_example2, btn_example3, btn_example4, btn_example5, btn_back)

    bot.send_message(chat_id,
                     "📝 *Примеры задач на концентрацию*\n\n"
                     "Выберите пример для изучения:\n\n"
                     "Каждый пример содержит:\n"
                     "• Полное условие задачи\n"
                     "• Таблицу данных\n"
                     "• Развернутое решение\n"
                     "• Итоговый ответ",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'concentration_tasks', 'examples_menu')


# ==================== ПРИМЕРЫ ЗАДАЧ ====================

def send_example_1(bot, chat_id):
    """Отправляет пример 1: Смешивание растворов"""
    example_text = (
        "🧪 *Пример 1: Смешивание растворов*\n\n"
        "*Условие задачи:*\n"
        "Смешали 8 литров 15%-го водного раствора некоторого вещества с 12 литрами 25%-го водного раствора этого же вещества. "
        "Сколько процентов составляет концентрация получившегося раствора?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "|      Параметр         |  Раствор 1  |  Раствор 2  |   Смесь     |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "| Объем раствора (л)    |      8      |     12      |     20      |\n"
        "| Концентрация (%)      |     15      |     25      |      ?      |\n"
        "| Объем вещества (л)    |   8·0,15    |  12·0,25    |    сумма    |\n"
        "|                       |    1,2      |    3,0      |    4,2      |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Анализируем условие:*\n"
        "   Имеем два раствора одного вещества с разными концентрациями. Нужно найти концентрацию смеси.\n\n"
        "2. *Находим объём чистого вещества в первом растворе:*\n"
        "   V₁ = 8 × 15% = 8 × 0,15 = 1,2 л\n\n"
        "3. *Находим объём чистого вещества во втором растворе:*\n"
        "   V₂ = 12 × 25% = 12 × 0,25 = 3 л\n\n"
        "4. *Находим общий объём чистого вещества в смеси:*\n"
        "   V = V₁ + V₂ = 1,2 + 3 = 4,2 л\n\n"
        "5. *Находим общий объём смеси:*\n"
        "   V_смеси = 8 + 12 = 20 л\n\n"
        "6. *Вычисляем концентрацию смеси:*\n"
        "   c = (V / V_смеси) × 100% = (4,2 / 20) × 100% = 0,21 × 100% = 21%\n\n"
        "7. *Проверяем решение:*\n"
        "   • Можно использовать правило креста:\n"
        "       15%       4% (25 - 21)\n"
        "           \\   /\n"
        "            21%\n"
        "           /   \\\n"
        "       25%       6% (21 - 15)\n"
        "   Соотношение 4:6 = 2:3 соответствует 8:12 ✓\n\n"
        "8. *Формулируем ответ:*\n"
        "   *Ответ:* концентрация получившегося раствора составляет 21%.\n\n"
        "*Основная формула:*\n"
        "c = (V₁·c₁ + V₂·c₂) / (V₁ + V₂)"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'concentration_tasks', 'viewing_example')


def send_example_2(bot, chat_id):
    """Отправляет пример 2: Система уравнений"""
    example_text = (
        "⚗️ *Пример 2: Система уравнений*\n\n"
        "*Условие задачи:*\n"
        "Смешали 30%-й раствор соляной кислоты с 10%-ым раствором и получили 600 г 15%-го раствора. "
        "Сколько граммов каждого раствора надо было взять?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "|      Параметр         |  Раствор 1  |  Раствор 2  |   Смесь     |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "| Масса раствора (г)    |      x      |      y      |    600      |\n"
        "| Концентрация (%)      |     30      |     10      |     15      |\n"
        "| Масса кислоты (г)     |    0,3x     |    0,1y     |  0,15·600  |\n"
        "|                       |             |             |     90      |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Вводим переменные:*\n"
        "   Пусть x г — масса 30%-го раствора,\n"
        "   y г — масса 10%-го раствора.\n\n"
        "2. *Составляем систему уравнений:*\n"
        "   • По общей массе: x + y = 600\n"
        "   • По массе чистой кислоты: 0,3x + 0,1y = 0,15 × 600 = 90\n\n"
        "3. *Решаем систему методом подстановки:*\n"
        "   Из первого уравнения: y = 600 - x\n\n"
        "   Подставляем во второе:\n"
        "   0,3x + 0,1(600 - x) = 90\n"
        "   0,3x + 60 - 0,1x = 90\n"
        "   0,2x + 60 = 90\n"
        "   0,2x = 30\n"
        "   x = 150\n\n"
        "4. *Находим y:*\n"
        "   y = 600 - 150 = 450\n\n"
        "5. *Проверяем решение:*\n"
        "   • Масса кислоты в 30% растворе: 150 × 0,3 = 45 г\n"
        "   • Масса кислоты в 10% растворе: 450 × 0,1 = 45 г\n"
        "   • Общая масса кислоты: 45 + 45 = 90 г\n"
        "   • Концентрация смеси: 90/600 × 100% = 15% ✓\n\n"
        "6. *Формулируем ответ:*\n"
        "   *Ответ:* нужно взять 150 г 30%-го раствора и 450 г 10%-го раствора.\n\n"
        "*Алгоритм решения:*\n"
        "1. Ввести переменные для масс исходных растворов\n"
        "2. Составить систему уравнений:\n"
        "   - сумма масс равна массе смеси\n"
        "   - сумма масс чистого вещества равна массе вещества в смеси\n"
        "3. Решить систему"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'concentration_tasks', 'viewing_example')


def send_example_3(bot, chat_id):
    """Отправляет пример 3: Сплав латуни"""
    example_text = (
        "🏺 *Пример 3: Сплав латуни*\n\n"
        "*Условие задачи:*\n"
        "Латунь — сплав меди и цинка. Кусок латуни содержит меди на 11 кг больше, чем цинка. "
        "Этот кусок латуни сплавили с 12 кг меди и получили латунь, в которой 75% меди. "
        "Сколько килограммов меди было в куске латуни первоначально?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "|      Параметр         | Исходный    | Добавка     |   Новый     |\n"
        "|                       |   сплав     |             |   сплав     |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "| Масса меди (кг)       |     x       |     12      |    x+12     |\n"
        "| Масса цинка (кг)      |     y       |      0      |     y       |\n"
        "| Общая масса (кг)      |    x+y      |     12      |   x+y+12    |\n"
        "| Соотношение           |  x = y+11   |      -      |  75% меди   |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Вводим переменные:*\n"
        "   Пусть x кг — масса меди в исходном сплаве,\n"
        "   y кг — масса цинка в исходном сплаве.\n\n"
        "2. *Составляем уравнения по условию:*\n"
        "   • Меди больше на 11 кг: x = y + 11\n\n"
        "3. *Анализируем новый сплав:*\n"
        "   • Масса меди в новом сплаве: x + 12\n"
        "   • Масса цинка: y (без изменений)\n"
        "   • Общая масса нового сплава: (x + y) + 12\n\n"
        "4. *Условие по концентрации нового сплава:*\n"
        "   В новом сплаве 75% меди, значит:\n"
        "   (x + 12) / ((x + y) + 12) = 0,75\n\n"
        "5. *Подставляем x = y + 11:*\n"
        "   (y + 11 + 12) / ((y + 11 + y) + 12) = 0,75\n"
        "   (y + 23) / (2y + 23) = 0,75\n\n"
        "6. *Решаем уравнение:*\n"
        "   y + 23 = 0,75(2y + 23)\n"
        "   y + 23 = 1,5y + 17,25\n"
        "   y - 1,5y = 17,25 - 23\n"
        "   -0,5y = -5,75\n"
        "   y = 11,5 кг\n\n"
        "7. *Находим x:*\n"
        "   x = y + 11 = 11,5 + 11 = 22,5 кг\n\n"
        "8. *Проверяем решение:*\n"
        "   • Исходный сплав: медь 22,5 кг, цинк 11,5 кг, всего 34 кг\n"
        "   • Меди больше на 11 кг: 22,5 - 11,5 = 11 ✓\n"
        "   • Новый сплав: медь 22,5 + 12 = 34,5 кг, всего 34 + 12 = 46 кг\n"
        "   • Концентрация меди: 34,5/46 × 100% = 75% ✓\n\n"
        "9. *Формулируем ответ:*\n"
        "   *Ответ:* в исходном куске латуни было 22,5 кг меди.\n\n"
        "*Особенность задачи:*\n"
        "При сплавлении масса цинка не меняется, добавляется только медь."
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'concentration_tasks', 'viewing_example')


def send_example_4(bot, chat_id):
    """Отправляет пример 4: Высушивание фруктов"""
    example_text = (
        "🍎 *Пример 4: Высушивание фруктов*\n\n"
        "*Условие задачи:*\n"
        "Свежие фрукты содержат 80% воды, а высушенные — 28%. "
        "Сколько сухих фруктов получится из 288 кг свежих фруктов?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+-------------+-------------+\n"
        "|      Параметр         |  Свежие     |  Сушеные    |\n"
        "+-----------------------+-------------+-------------+\n"
        "| Общая масса (кг)      |    288      |      x      |\n"
        "| Содержание воды (%)   |     80      |     28      |\n"
        "| Содержание сухого (%) |     20      |     72      |\n"
        "| Масса сухого (кг)     |  288·0,2    |   x·0,72    |\n"
        "|                       |    57,6     |             |\n"
        "+-----------------------+-------------+-------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Ключевая идея:*\n"
        "   При высушивании удаляется только вода. Масса сухого вещества остаётся неизменной.\n\n"
        "2. *Находим массу сухого вещества в свежих фруктах:*\n"
        "   Свежие фрукты содержат 80% воды, значит сухого вещества: 100% - 80% = 20%\n"
        "   m(сухого) = 288 × 0,2 = 57,6 кг\n\n"
        "3. *В сушёных фруктах сухое вещество составляет:*\n"
        "   100% - 28% = 72%\n\n"
        "4. *Составляем уравнение:*\n"
        "   Пусть x кг — масса сушёных фруктов.\n"
        "   Масса сухого вещества в сушёных фруктах: 0,72x\n"
        "   По закону сохранения массы сухого вещества:\n"
        "   0,72x = 57,6\n\n"
        "5. *Решаем уравнение:*\n"
        "   x = 57,6 / 0,72 = 80 кг\n\n"
        "6. *Проверяем решение:*\n"
        "   • В свежих: вода 288 × 0,8 = 230,4 кг, сухое 57,6 кг\n"
        "   • В сушёных: вода 80 × 0,28 = 22,4 кг, сухое 57,6 кг\n"
        "   • Вода испарилась: 230,4 - 22,4 = 208 кг\n"
        "   • Общая масса уменьшилась: 288 - 80 = 208 кг ✓\n\n"
        "7. *Формулируем ответ:*\n"
        "   *Ответ:* из 288 кг свежих фруктов получится 80 кг сушёных.\n\n"
        "*Важная формула:*\n"
        "m₁ × (100% - w₁)/100% = m₂ × (100% - w₂)/100%\n"
        "где w₁, w₂ — процентное содержание воды."
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'concentration_tasks', 'viewing_example')


def send_example_5(bot, chat_id):
    """Отправляет пример 5: Дополнительная задача"""
    example_text = (
        "📊 *Пример 5: Дополнительная задача*\n\n"
        "*Условие задачи:*\n"
        "Имеется два сплава. Первый сплав содержит 10% меди, второй — 40% меди. Масса второго сплава больше массы первого на 3 кг. "
        "Из этих двух сплавов получили третий сплав, содержащий 30% меди. Найдите массу третьего сплава. Ответ дайте в килограммах.\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "|      Параметр         |  Сплав 1    |  Сплав 2    |   Сплав 3   |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "| Масса сплава (кг)     |      x      |    x + 3    |   2x + 3    |\n"
        "| Концентрация меди (%) |     10      |     40      |     30      |\n"
        "| Масса меди (кг)       |    0,1x     |   0,4(x+3)  |  0,3(2x+3)  |\n"
        "+-----------------------+-------------+-------------+-------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Вводим переменные:*\n"
        "   Пусть x кг — масса первого сплава.\n"
        "   Тогда масса второго сплава: x + 3 кг.\n\n"
        "2. *Находим массу меди в каждом сплаве:*\n"
        "   • В первом сплаве: 0,1x кг\n"
        "   • Во втором сплаве: 0,4(x + 3) = 0,4x + 1,2 кг\n\n"
        "3. *Масса третьего сплава:*\n"
        "   m₃ = x + (x + 3) = 2x + 3 кг\n\n"
        "4. *Масса меди в третьем сплаве:*\n"
        "   По условию концентрация меди 30%, значит:\n"
        "   m₃(меди) = 0,3(2x + 3) = 0,6x + 0,9 кг\n\n"
        "5. *Составляем уравнение (закон сохранения меди):*\n"
        "   Сумма масс меди в исходных сплавах равна массе меди в третьем сплаве:\n"
        "   0,1x + (0,4x + 1,2) = 0,6x + 0,9\n\n"
        "6. *Решаем уравнение:*\n"
        "   0,1x + 0,4x + 1,2 = 0,6x + 0,9\n"
        "   0,5x + 1,2 = 0,6x + 0,9\n"
        "   1,2 - 0,9 = 0,6x - 0,5x\n"
        "   0,3 = 0,1x\n"
        "   x = 3 кг\n\n"
        "7. *Находим массу третьего сплава:*\n"
        "   m₃ = 2x + 3 = 2 × 3 + 3 = 9 кг\n\n"
        "8. *Проверяем решение:*\n"
        "   • Первый сплав: масса 3 кг, меди 0,3 кг\n"
        "   • Второй сплав: масса 6 кг, меди 2,4 кг\n"
        "   • Третий сплав: масса 9 кг, меди 0,3 + 2,4 = 2,7 кг\n"
        "   • Концентрация: 2,7/9 × 100% = 30% ✓\n\n"
        "9. *Формулируем ответ:*\n"
        "   *Ответ:* масса третьего сплава равна 9 кг.\n\n"
        "*Алгоритм:*\n"
        "1. Ввести переменную для неизвестной массы\n"
        "2. Выразить через неё все остальные величины\n"
        "3. Составить уравнение по закону сохранения вещества\n"
        "4. Найти искомую величину"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'concentration_tasks', 'viewing_example')


# ==================== ОБУЧЕНИЕ ====================
def show_training_menu(bot, chat_id):
    """Отображает меню обучения"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_lesson1 = types.KeyboardButton('📖 Урок 1: Основные понятия и формулы')
    btn_lesson2 = types.KeyboardButton('📖 Урок 2: Смешивание растворов')
    btn_lesson3 = types.KeyboardButton('📖 Урок 3: Сплавы и высушивание')
    btn_back = types.KeyboardButton('🔙 Назад к меню концентрации')

    markup.add(btn_lesson1, btn_lesson2, btn_lesson3, btn_back)

    bot.send_message(chat_id,
                     "🎓 *Обучение: Задачи на концентрацию*\n\n"
                     "Выберите урок для изучения:\n\n"
                     "Пошаговое изучение тем:\n"
                     "1. Основные понятия и формулы\n"
                     "2. Смешивание растворов\n"
                     "3. Сплавы и высушивание",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'concentration_tasks', 'training_menu')


def send_lesson(bot, chat_id, lesson_number):
    """Отправляет урок"""
    if lesson_number == 1:
        lesson_content = get_lesson_1_content()
    elif lesson_number == 2:
        lesson_content = get_lesson_2_content()
    elif lesson_number == 3:
        lesson_content = get_lesson_3_content()
    else:
        lesson_content = get_lesson_1_content()

    # Сохраняем текущий урок
    update_user_data(chat_id, {'current_lesson': lesson_number})

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_prev = types.KeyboardButton('⬅️ Предыдущий урок')
    btn_next = types.KeyboardButton('➡️ Следующий урок')
    btn_back = types.KeyboardButton('🔙 Назад к урокам')
    markup.add(btn_prev, btn_next, btn_back)

    bot.send_message(chat_id, lesson_content, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'concentration_tasks', 'viewing_lesson')


def get_lesson_1_content():
    """Контент урока 1"""
    return (
        "📖 *Урок 1: Основные понятия и формулы*\n\n"
        "*Что такое концентрация?*\n\n"
        "Концентрация вещества в растворе (смеси, сплаве) — это отношение массы (объёма) этого вещества к общей массе (объёму) раствора, выраженное в процентах.\n\n"
        "*Основные формулы:*\n\n"
        "1. *Концентрация:*\n"
        "   ```\n"
        "            m(вещества)\n"
        "    c = ─────────────── × 100%\n"
        "            m(раствора)\n"
        "   ```\n\n"
        "2. *Масса вещества:*\n"
        "   ```\n"
        "    m(вещества) = m(раствора) × c / 100%\n"
        "   ```\n\n"
        "3. *Закон сохранения массы:*\n"
        "   При смешивании растворов общая масса вещества сохраняется:\n"
        "   ```\n"
        "    m₁·c₁ + m₂·c₂ = (m₁ + m₂)·c\n"
        "   ```\n\n"
        "*Пример:*\n"
        "В 200 г раствора содержится 30 г соли. Найти концентрацию.\n"
        "c = (30/200) × 100% = 15%\n\n"
        "*Важно:* Концентрация всегда выражается в процентах и не может превышать 100%."
    )


def get_lesson_2_content():
    """Контент урока 2"""
    return (
        "📖 *Урок 2: Смешивание растворов*\n\n"
        "*Метод стаканчиков:*\n\n"
        "Представим каждый раствор как стакан, в котором:\n"
        "• Нижняя часть — чистое вещество\n"
        "• Верхняя часть — растворитель\n\n"
        "При смешивании содержимое стаканов объединяется.\n\n"
        "*Алгоритм решения:*\n\n"
        "1. Найти массу (объём) чистого вещества в каждом растворе\n"
        "2. Сложить эти массы — получим массу вещества в смеси\n"
        "3. Сложить массы растворов — получим массу смеси\n"
        "4. Разделить массу вещества на массу смеси и умножить на 100%\n\n"
        "*Правило креста (для двух компонентов):*\n\n"
        "```\n"
        "% первого  \\        /  разность с целевой\n"
        "раствора    \\      /   концентрацией второго\n"
        "              целевая\n"
        "            концентрация\n"
        "% второго  /        \\  разность с целевой\n"
        "раствора  /          \\ концентрацией первого\n"
        "```\n\n"
        "Полученные числа показывают, в каком соотношении нужно взять растворы.\n\n"
        "*Пример:*\n"
        "Нужно получить 20% раствор из 10% и 30%.\n"
        "    10%      10% (30-20)\n"
        "        \\   /\n"
        "         20%\n"
        "        /   \\\n"
        "    30%      10% (20-10)\n"
        "Соотношение 10:10 = 1:1, значит нужно взять равные массы."
    )


def get_lesson_3_content():
    """Контент урока 3"""
    return (
        "📖 *Урок 3: Сплавы и высушивание*\n\n"
        "*Сплавы:*\n\n"
        "Задачи на сплавы решаются аналогично задачам на растворы, но вместо объёма используется масса.\n\n"
        "*Особенности:*\n"
        "• Металлы в сплаве не реагируют друг с другом\n"
        "• Общая масса сплава равна сумме масс компонентов\n"
        "• Процентное содержание — это отношение массы компонента к массе сплава\n\n"
        "*Высушивание:*\n\n"
        "Ключевая идея: при высушивании удаляется только вода, масса сухого вещества остаётся неизменной!\n\n"
        "*Формула для задач на высушивание:*\n"
        "```\n"
        "m₁ × (100% - w₁)/100% = m₂ × (100% - w₂)/100%\n"
        "```\n"
        "где w₁, w₂ — процентное содержание воды.\n\n"
        "*Или через сухое вещество:*\n"
        "m₁ × k₁ = m₂ × k₂, где k — доля сухого вещества.\n\n"
        "*Пример:*\n"
        "Свежие грибы содержат 90% воды, сушёные — 12%. Сколько сушёных грибов получится из 22 кг свежих?\n\n"
        "*Решение:*\n"
        "• Сухого в свежих: 10% → 22 × 0,1 = 2,2 кг\n"
        "• Сухого в сушёных: 88% → 2,2 / 0,88 = 2,5 кг\n"
        "*Ответ:* 2,5 кг."
    )


# ==================== ОБРАБОТЧИК СООБЩЕНИЙ ====================
def handle_concentration_tasks(bot, message, user_data):
    """Обрабатывает сообщения в модуле задач на концентрацию"""
    user_id = message.chat.id
    text = message.text
    user_state = get_user_state(user_id)

    # Получаем текущий подмодуль
    current_submodule = user_state.get('sub_module', '')

    # ========== ОБРАБОТКА ВВОДА ОТВЕТА В ТРЕНАЖЕРАХ ==========
    if current_submodule in ['easy_simulator', 'medium_simulator', 'hard_simulator', 'random_simulator']:
        # Список всех кнопок, которые НЕ считаются ответом пользователя
        системные_кнопки = [
            '💡 Подсказка', '📝 Показать ответ', '🔙 Назад к тренажеру', '➡️ Следующая задача',
            '🔄 Новая задача', '📚 Справочный материал', '📝 Примеры задач', '🎓 Обучение',
            '🎯 Тренажер', '🟢 Легкий уровень', '🟡 Средний уровень', '🔴 Сложный уровень',
            '🎲 Случайная задача', '🔙 Назад к меню концентрации', '🔙 Назад к типам задач',
            '🔙 Назад к примерам', '🔙 Назад к урокам', '📖 Урок 1: Основные понятия и формулы',
            '📖 Урок 2: Смешивание растворов', '📖 Урок 3: Сплавы и высушивание',
            '🧪 Пример 1: Смешивание растворов', '⚗️ Пример 2: Система уравнений',
            '🏺 Пример 3: Сплав латуни', '🍎 Пример 4: Высушивание фруктов',
            '📊 Пример 5: Дополнительная задача'
        ]

        # Если это НЕ системная кнопка, то это ответ пользователя
        if text not in системные_кнопки:
            уровень_соответствие = {
                'easy_simulator': 'легкий',
                'medium_simulator': 'средний',
                'hard_simulator': 'сложный',
                'random_simulator': 'случайные'
            }
            уровень = уровень_соответствие.get(current_submodule, 'легкий')
            handle_simulator_input(bot, user_id, text, уровень)
            return

    # ========== НАВИГАЦИЯ НАЗАД ==========
    if text == '🔙 Назад к типам задач':
        show_text_tasks_menu_wrapper(bot, user_id)
        return

    elif text == '🔙 Назад к меню концентрации':
        show_concentration_main_menu(bot, user_id)
        return

    elif text == '🔙 Назад к примерам':
        show_examples_menu(bot, user_id)
        return

    elif text == '🔙 Назад к урокам':
        show_training_menu(bot, user_id)
        return

    elif text == '🔙 Назад к тренажеру':
        show_simulator_menu(bot, user_id)
        return

    # ========== ГЛАВНОЕ МЕНЮ КОНЦЕНТРАЦИИ ==========
    elif text == '📚 Справочный материал':
        send_reference_material(bot, user_id)

    elif text == '📝 Примеры задач':
        show_examples_menu(bot, user_id)

    elif text == '🎓 Обучение':
        show_training_menu(bot, user_id)

    elif text == '🎯 Тренажер':
        show_simulator_menu(bot, user_id)

    # ========== ВЫБОР ПРИМЕРОВ ИЗ МЕНЮ (5 КНОПОК) ==========
    elif text == '🧪 Пример 1: Смешивание растворов':
        send_example_1(bot, user_id)

    elif text == '⚗️ Пример 2: Система уравнений':
        send_example_2(bot, user_id)

    elif text == '🏺 Пример 3: Сплав латуни':
        send_example_3(bot, user_id)

    elif text == '🍎 Пример 4: Высушивание фруктов':
        send_example_4(bot, user_id)

    elif text == '📊 Пример 5: Дополнительная задача':
        send_example_5(bot, user_id)

    # ========== ТРЕНАЖЕР УРОВНЕЙ ==========
    elif text == '🟢 Легкий уровень':
        start_easy_simulator(bot, user_id)

    elif text == '🟡 Средний уровень':
        start_medium_simulator(bot, user_id)

    elif text == '🔴 Сложный уровень':
        start_hard_simulator(bot, user_id)

    elif text == '🎲 Случайная задача':
        start_random_simulator(bot, user_id)

    # ========== КНОПКИ В ТРЕНАЖЕРЕ ==========
    elif text == '💡 Подсказка' and current_submodule in ['easy_simulator', 'medium_simulator', 'hard_simulator',
                                                         'random_simulator']:
        send_simulator_hint(bot, user_id)

    elif text == '📝 Показать ответ' and current_submodule in ['easy_simulator', 'medium_simulator', 'hard_simulator',
                                                              'random_simulator']:
        show_simulator_answer(bot, user_id)

    elif text == '➡️ Следующая задача' and current_submodule in ['easy_simulator', 'medium_simulator',
                                                                 'hard_simulator']:
        next_simulator_task(bot, user_id)

    elif text == '🔄 Новая задача' and current_submodule == 'random_simulator':
        next_simulator_task(bot, user_id)

    # ========== НАВИГАЦИЯ В УРОКАХ ==========
    elif text == '➡️ Следующий урок' and current_submodule == 'viewing_lesson':
        current_lesson = user_state.get('current_lesson', 1)
        next_lesson = current_lesson + 1 if current_lesson < 3 else 1
        send_lesson(bot, user_id, next_lesson)

    elif text == '⬅️ Предыдущий урок' and current_submodule == 'viewing_lesson':
        current_lesson = user_state.get('current_lesson', 1)
        prev_lesson = current_lesson - 1 if current_lesson > 1 else 3
        send_lesson(bot, user_id, prev_lesson)

    # ========== ВЫБОР УРОКОВ ==========
    elif text == '📖 Урок 1: Основные понятия и формулы':
        send_lesson(bot, user_id, 1)

    elif text == '📖 Урок 2: Смешивание растворов':
        send_lesson(bot, user_id, 2)

    elif text == '📖 Урок 3: Сплавы и высушивание':
        send_lesson(bot, user_id, 3)

    else:
        # Если сообщение не распознано, показываем главное меню концентрации
        show_concentration_main_menu(bot, user_id)