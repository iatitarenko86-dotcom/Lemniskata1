import telebot
from telebot import types
from user_states import set_user_state, get_user_state, update_user_data
from simulator_movement1 import SimulatorMovement1
from simulator_movement2 import SimulatorMovement2
from simulator_movement3 import SimulatorMovement3
from simulator_movement4 import SimulatorMovement4

# Глобальный словарь для хранения тренажеров по пользователям
тренажеры_пользователей = {}


# ==================== ГЛАВНОЕ МЕНЮ ДВИЖЕНИЯ ====================
def show_movement_main_menu(bot, chat_id):
    """Отображает главное меню задач на движение"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_reference = types.KeyboardButton('📚 Справочный материал')
    btn_examples = types.KeyboardButton('📝 Примеры задач')
    btn_training = types.KeyboardButton('🎓 Обучение')
    btn_simulator = types.KeyboardButton('🎯 Тренажер')
    btn_back = types.KeyboardButton('🔙 Назад к типам задач')

    markup.add(btn_reference, btn_examples, btn_training, btn_simulator, btn_back)

    bot.send_message(chat_id,
                     "🚗 *Задачи на движение*\n\n"
                     "Выберите раздел для изучения:\n\n"
                     "• *📚 Справочный материал* - формулы и теория\n"
                     "• *📝 Примеры задач* - готовые решения\n"
                     "• *🎓 Обучение* - пошаговое изучение\n"
                     "• *🎯 Тренажер* - практические задания",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'movement_tasks', 'main_menu')


# ==================== НАЧАЛО РАБОТЫ ====================
def start_movement_tasks(bot, chat_id, user_data):
    """Начинает работу с задачами на движение"""
    show_movement_main_menu(bot, chat_id)


# ==================== МЕНЮ ТРЕНАЖЕРА ====================
def show_simulator_menu(bot, chat_id):
    """Отображает меню тренажера"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_easy = types.KeyboardButton('🟢 Легкий уровень')
    btn_medium = types.KeyboardButton('🟡 Средний уровень')
    btn_hard = types.KeyboardButton('🔴 Сложный уровень')
    btn_random = types.KeyboardButton('🎲 Случайная задача')
    btn_back = types.KeyboardButton('🔙 Назад к меню движения')

    markup.add(btn_easy, btn_medium, btn_hard, btn_random, btn_back)

    bot.send_message(chat_id,
                     "🎯 *Тренажер: Задачи на движение*\n\n"
                     "Выберите уровень сложности:\n\n"
                     "• *🟢 Легкий* - 12 базовых задач\n"
                     "• *🟡 Средний* - 11 задач средней сложности\n"
                     "• *🔴 Сложный* - 9 комплексных задач\n"
                     "• *🎲 Случайная* - задача любого уровня",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'movement_tasks', 'simulator_menu')


# ==================== ЗАПУСК ЛЕГКОГО УРОВНЯ ====================
def start_easy_simulator(bot, chat_id):
    """Запускает легкий уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorMovement1()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorMovement1):
                тренажеры_пользователей[chat_id] = SimulatorMovement1()

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
                         "Введите *ответ* в чат:",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'movement_tasks', 'easy_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске легкого уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СРЕДНЕГО УРОВНЯ ====================
def start_medium_simulator(bot, chat_id):
    """Запускает средний уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorMovement2()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorMovement2):
                тренажеры_пользователей[chat_id] = SimulatorMovement2()

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
                         "Введите *ответ* в чат:",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'movement_tasks', 'medium_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске среднего уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СЛОЖНОГО УРОВНЯ ====================
def start_hard_simulator(bot, chat_id):
    """Запускает сложный уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorMovement3()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorMovement3):
                тренажеры_пользователей[chat_id] = SimulatorMovement3()

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
                         "Введите *ответ* в чат:",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'movement_tasks', 'hard_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске сложного уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СЛУЧАЙНЫХ ЗАДАЧ ====================
def start_random_simulator(bot, chat_id):
    """Запускает режим случайных задач"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorMovement4()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorMovement4):
                тренажеры_пользователей[chat_id] = SimulatorMovement4()

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
                         "Введите *ответ* в чат:",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'movement_tasks', 'random_simulator')
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

        данные_уровня = уровень_данные.get(уровень, {'эмодзи': '🎯', 'текст': 'Тренажер'})

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
            if "Следующая задача" in сообщение:
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

            данные_уровня = уровень_данные.get(submodule, {'эмодзи': '🎯', 'текст': 'Тренажер'})

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

            данные_уровня = уровень_данные.get(submodule, {'эмодзи': '🎯', 'текст': 'Тренажер'})

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
    """Отправляет ссылку на справочный материал"""
    reference_text = (
        "📚 *Справочный материал по задачам на движение*\n\n"
        "Здесь вы найдете все основные формулы, понятия и теории:\n\n"
        "*Основные формулы движения:*\n"
        "```\n"
        "+---------------------+---------------------+---------------------+\n"
        "|      Формула        |     Обозначение     |      Единицы        |\n"
        "+---------------------+---------------------+---------------------+\n"
        "|   S = v × t         | S - расстояние      | км, м               |\n"
        "|   v = S / t         | v - скорость        | км/ч, м/с           |\n"
        "|   t = S / v         | t - время           | ч, мин, с           |\n"
        "+---------------------+---------------------+---------------------+\n"
        "```\n\n"
        "*Единицы измерения:*\n"
        "• 1 м/с = 3.6 км/ч\n"
        "• 1 км/ч ≈ 0.278 м/с\n"
        "• 1 час = 60 минут = 3600 секунд\n\n"
        "Для подробного изучения перейдите по ссылке:"
    )

    # Создаем инлайн-кнопку с ссылкой
    markup = types.InlineKeyboardMarkup()
    btn_link = types.InlineKeyboardButton(
        text="📖 Открыть справочник",
        url="https://disk.yandex.ru/i/a1LXK4704Y7hMQ"
    )
    markup.add(btn_link)

    # Добавляем кнопку для возврата
    reply_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к меню движения')
    reply_markup.add(btn_back)

    bot.send_message(chat_id, reference_text, parse_mode='Markdown', reply_markup=reply_markup)
    bot.send_message(chat_id, "Ссылка на справочный материал:", reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'reference')


# ==================== МЕНЮ ПРИМЕРОВ (7 КНОПОК) ====================
def show_examples_menu(bot, chat_id):
    """Отображает меню примеров задач с 7 кнопками"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_example1 = types.KeyboardButton('🚗 Пример 1: Два автомобиля')
    btn_example2 = types.KeyboardButton('🚂 Пример 2: Поезд и мост')
    btn_example3 = types.KeyboardButton('🚢 Пример 3: Два теплохода')
    btn_example4 = types.KeyboardButton('🚶 Пример 4: Пешеход и велосипедист')
    btn_example5 = types.KeyboardButton('🏙️ Пример 5: А→Б→А со скоростью')
    btn_example6 = types.KeyboardButton('🏎️ Пример 6: Болиды по кругу')
    btn_example7 = types.KeyboardButton('🛶 Пример 7: Лодка по реке')
    btn_back = types.KeyboardButton('🔙 Назад к меню движения')

    markup.add(btn_example1, btn_example2, btn_example3, btn_example4,
               btn_example5, btn_example6, btn_example7, btn_back)

    bot.send_message(chat_id,
                     "📝 *Примеры задач на движение*\n\n"
                     "Выберите пример для изучения:\n\n"
                     "Каждый пример содержит:\n"
                     "• Полное условие задачи\n"
                     "• Развернутое решение\n"
                     "• Итоговый ответ",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'movement_tasks', 'examples_menu')


def send_example_1(bot, chat_id):
    """Отправляет пример 1: Два автомобиля"""
    example_text = (
         "🚗 *Пример 1: Два автомобиля*\n\n"
        "*Условие задачи:*\n"
        "Из двух городов, расстояние между которыми 420 км, одновременно навстречу друг другу выехали два автомобиля. "
        "Скорость первого автомобиля 60 км/ч, скорость второго — 80 км/ч. Через сколько часов они встретятся?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+---------------------+----------+----------+\n"
        "|      Параметр       | 1-й авто | 2-й авто |\n"
        "+---------------------+----------+----------+\n"
        "|   Скорость (км/ч)   |    60    |    80    |\n"
        "|   Расстояние (км)   |    ?     |    ?     |\n"
        "|   Время (ч)         |    t     |    t     |\n"
        "+---------------------+----------+----------+\n"
        "|   Общее расстояние  |   420 км            |\n"
        "+---------------------+---------------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Определяем тип движения:*\n"
        "   Движение навстречу друг другу.\n\n"
        "2. *Находим скорость сближения:*\n"
        "   При движении навстречу скорости складываются:\n"
        "   v = v₁ + v₂ = 60 + 80 = 140 км/ч\n\n"
        "3. *Находим время встречи:*\n"
        "   Используем формулу t = S / v:\n"
        "   t = 420 / 140 = 3 часа\n\n"
        "4. *Проверяем решение:*\n"
        "   • За 3 часа первый автомобиль проедет: 60 × 3 = 180 км\n"
        "   • За 3 часа второй автомобиль проедет: 80 × 3 = 240 км\n"
        "   • Сумма: 180 + 240 = 420 км ✓\n\n"
        "5. *Формулируем ответ:*\n"
        "   *Ответ:* автомобили встретятся через 3 часа.\n\n"
        "*Формула для запоминания:*\n"
        "t = S / (v₁ + v₂) - время встречи при движении навстречу."
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'viewing_example')


def send_example_2(bot, chat_id):
    """Отправляет пример 2: Поезд и мост"""
    example_text = (
        "🚂 *Пример 2: Поезд и мост*\n\n"
        "*Условие задачи:*\n"
        "Поезд длиной 250 м проезжает мост длиной 150 м за 20 секунд. "
        "С какой скоростью движется поезд? Ответ дайте в км/ч.\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+------------+----------+\n"
        "|      Параметр         |   Значение | Единицы  |\n"
        "+-----------------------+------------+----------+\n"
        "| Длина поезда          |    250     |    м     |\n"
        "| Длина моста           |    150     |    м     |\n"
        "| Время проезда         |    20      |    с     |\n"
        "| Скорость (м/с)        |     ?      |   м/с    |\n"
        "| Скорость (км/ч)       |     ?      |  км/ч    |\n"
        "+-----------------------+------------+----------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Анализируем условие:*\n"
        "   При проезде моста поезд проходит путь, равный сумме своей длины и длины моста.\n\n"
        "2. *Находим полный путь:*\n"
        "   S = длина поезда + длина моста\n"
        "   S = 250 + 150 = 400 м\n\n"
        "3. *Находим скорость в м/с:*\n"
        "   Используем формулу v = S / t:\n"
        "   v = 400 / 20 = 20 м/с\n\n"
        "4. *Переводим скорость в км/ч:*\n"
        "   1 м/с = 3.6 км/ч\n"
        "   v = 20 × 3.6 = 72 км/ч\n\n"
        "5. *Проверяем единицы измерения:*\n"
        "   Время дано в секундах, путь в метрах → скорость в м/с.\n"
        "   Ответ нужно дать в км/ч → делаем перевод.\n\n"
        "6. *Формулируем ответ:*\n"
        "   *Ответ:* скорость поезда 72 км/ч.\n\n"
        "*Важное замечание:*\n"
        "В задачах с протяженными объектами (поездами, тоннелями, мостами) нужно учитывать полный путь, который проходит объект."
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'viewing_example')


def send_example_3(bot, chat_id):
    """Отправляет пример 3: Два теплохода"""
    example_text = (
         "🚢 *Пример 3: Два теплохода*\n\n"
        "*Условие задачи:*\n"
        "Два теплохода вышли одновременно навстречу друг другу из двух портов, расстояние между которыми 300 км. "
        "Скорость первого теплохода 20 км/ч, второго — 30 км/ч. Через сколько часов они встретятся?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+---------------------+------------+------------+\n"
        "|      Параметр       | Теплоход 1 | Теплоход 2 |\n"
        "+---------------------+------------+------------+\n"
        "|   Скорость (км/ч)   |     20     |     30     |\n"
        "|   Время (ч)         |     t      |     t      |\n"
        "|   Расстояние (км)   |     ?      |     ?      |\n"
        "+---------------------+------------+------------+\n"
        "|   Общее расстояние  |       300 км            |\n"
        "+---------------------+-------------------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Анализируем тип движения:*\n"
        "   Теплоходы движутся навстречу друг другу.\n\n"
        "2. *Применяем формулу для встречного движения:*\n"
        "   Скорость сближения равна сумме скоростей:\n"
        "   v = v₁ + v₂ = 20 + 30 = 50 км/ч\n\n"
        "3. *Находим время встречи:*\n"
        "   t = S / v = 300 / 50 = 6 часов\n\n"
        "4. *Дополнительно находим расстояния:*\n"
        "   • Путь первого теплохода: S₁ = 20 × 6 = 120 км\n"
        "   • Путь второго теплохода: S₂ = 30 × 6 = 180 км\n"
        "   • Проверка: 120 + 180 = 300 км ✓\n\n"
        "5. *Интерпретируем результат:*\n"
        "   Теплоходы встретятся через 6 часов после начала движения.\n"
        "   Место встречи находится на расстоянии 120 км от первого порта\n"
        "   и 180 км от второго порта.\n\n"
        "6. *Формулируем ответ:*\n"
        "   *Ответ:* теплоходы встретятся через 6 часов.\n\n"
        "*Формула:*\n"
        "t = S / (v₁ + v₂)"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'viewing_example')


def send_example_4(bot, chat_id):
    """Отправляет пример 4: Пешеход и велосипедист"""
    example_text = (
         "🚶 *Пример 4: Пешеход и велосипедист*\n\n"
        "*Условие задачи:*\n"
        "Из одной точки в противоположных направлениях одновременно вышли пешеход и велосипедист. "
        "Скорость пешехода 5 км/ч, велосипедиста — 15 км/ч. Какое расстояние будет между ними через 2 часа?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+---------------------+------------+-----------------+\n"
        "|      Параметр       |  Пешеход   | Велосипедист    |\n"
        "+---------------------+------------+-----------------+\n"
        "|   Скорость (км/ч)   |     5      |       15        |\n"
        "|   Время (ч)         |     2      |        2        |\n"
        "|   Расстояние (км)   |     ?      |        ?        |\n"
        "+---------------------+------------+-----------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Анализируем тип движения:*\n"
        "   Движение в противоположных направлениях из одной точки.\n\n"
        "2. *Способ 1: Через скорость удаления*\n"
        "   • Скорость удаления: v = v₁ + v₂ = 5 + 15 = 20 км/ч\n"
        "   • Расстояние через 2 часа: S = v × t = 20 × 2 = 40 км\n\n"
        "3. *Способ 2: Через индивидуальные пути*\n"
        "   • Путь пешехода: S₁ = 5 × 2 = 10 км\n"
        "   • Путь велосипедиста: S₂ = 15 × 2 = 30 км\n"
        "   • Общее расстояние: S = S₁ + S₂ = 10 + 30 = 40 км\n\n"
        "4. *Проверяем логику решения:*\n"
        "   Через 1 час: расстояние = 5 + 15 = 20 км\n"
        "   Через 2 часа: расстояние = 20 × 2 = 40 км\n"
        "   Оба способа дают одинаковый результат.\n\n"
        "5. *Выбираем оптимальный способ:*\n"
        "   Для движения в противоположных направлениях удобнее использовать\n"
        "   скорость удаления (v₁ + v₂), так как это сокращает вычисления.\n\n"
        "6. *Формулируем ответ:*\n"
        "   *Ответ:* через 2 часа расстояние между ними будет 40 км.\n\n"
        "*Формула для запоминания:*\n"
        "При движении в противоположных направлениях: v = v₁ + v₂"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'viewing_example')


def send_example_5(bot, chat_id):
    """Отправляет пример 5: А→Б→А со скоростью"""
    example_text = (
        "🏙️ *Пример 5: А→Б→А со скоростью*\n\n"
        "*Условие задачи:*\n"
        "Автомобиль выехал с постоянной скоростью из города А в город Б, расстояние между которыми равно 180 км. "
        "На следующий день он отправился обратно в А, увеличив скорость на 5 км/ч, в результате чего затратил на обратный путь на 24 минуты меньше. "
        "Найдите скорость автомобиля на пути из А в Б.\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+---------------------+---------------+---------------+\n"
        "|      Параметр       |   Туда (А→Б)  |  Обратно (Б→А)|\n"
        "+---------------------+---------------+---------------+\n"
        "|   Расстояние (км)   |      180      |      180      |\n"
        "|   Скорость (км/ч)   |       x       |     x + 5     |\n"
        "|   Время (ч)         |     180/x     |  180/(x+5)    |\n"
        "+---------------------+---------------+---------------+\n"
        "|   Разница во времени|        24 минуты = 0.4 часа    |\n"
        "+---------------------+--------------------------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Вводим переменную:*\n"
        "   Пусть x - скорость из А в Б (км/ч)\n"
        "   Тогда скорость обратно: x + 5 (км/ч)\n\n"
        "2. *Записываем выражения для времени:*\n"
        "   • Время туда: t₁ = 180 / x (часов)\n"
        "   • Время обратно: t₂ = 180 / (x + 5) (часов)\n\n"
        "3. *Составляем уравнение:*\n"
        "   Разница во времени: 24 минуты = 24/60 = 0.4 часа\n"
        "   t₁ - t₂ = 0.4\n"
        "   180/x - 180/(x + 5) = 0.4\n\n"
        "4. *Решаем уравнение:*\n"
        "   Умножаем обе части на x(x + 5):\n"
        "   180(x + 5) - 180x = 0.4x(x + 5)\n"
        "   180x + 900 - 180x = 0.4x² + 2x\n"
        "   900 = 0.4x² + 2x\n\n"
        "5. *Приводим к квадратному уравнению:*\n"
        "   0.4x² + 2x - 900 = 0\n"
        "   Умножаем на 5 для удобства:\n"
        "   2x² + 10x - 4500 = 0\n"
        "   Делим на 2:\n"
        "   x² + 5x - 2250 = 0\n\n"
        "6. *Находим корни:*\n"
        "   Дискриминант: D = 5² - 4×1×(-2250) = 25 + 9000 = 9025\n"
        "   √D = √9025 = 95\n"
        "   x₁ = (-5 + 95)/2 = 90/2 = 45\n"
        "   x₂ = (-5 - 95)/2 = -100/2 = -50 (не подходит, скорость > 0)\n\n"
        "7. *Проверяем решение:*\n"
        "   • Скорость туда: 45 км/ч, время: 180/45 = 4 часа\n"
        "   • Скорость обратно: 50 км/ч, время: 180/50 = 3.6 часа\n"
        "   • Разница: 4 - 3.6 = 0.4 часа = 24 минуты ✓\n\n"
        "8. *Формулируем ответ:*\n"
        "   *Ответ:* скорость автомобиля на пути из А в Б равна 45 км/ч.\n\n"
        "*Алгоритм решения:*\n"
        "1. Ввести переменную для неизвестной скорости\n"
        "2. Выразить время для каждого направления\n"
        "3. Составить уравнение на основе разницы во времени\n"
        "4. Решить квадратное уравнение\n"
        "5. Выбрать положительный корень"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'viewing_example')


def send_example_6(bot, chat_id):
    """Отправляет пример 6: Болиды по кругу"""
    example_text = (
        "🏎️ *Пример 6: Болиды по кругу*\n\n"
        "*Условие задачи:*\n"
        "Два болида стартуют одновременно в одном направлении из двух диаметрально противоположных точек круговой трассы, длина которой равна 19,5 км. "
        "Через сколько минут болиды поравняются в первый раз, если скорость одного из них на 13 км/ч больше скорости другого?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+--------------+--------------+\n"
        "|      Параметр         |  Медленный   |  Быстрый     |\n"
        "+-----------------------+--------------+--------------+\n"
        "|   Длина трассы        |     19.5 км                 |\n"
        "|   Начальное расстояние|    9.75 км (половина)       |\n"
        "|   Скорость (км/ч)     |      v       |    v + 13    |\n"
        "|   Время встречи (ч)   |      t       |      t       |\n"
        "+-----------------------+--------------+--------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Анализируем условие:*\n"
        "   • Болиды стартуют из диаметрально противоположных точек\n"
        "   • Значит, начальное расстояние между ними равно половине длины трассы\n"
        "   • S₀ = 19.5 / 2 = 9.75 км\n"
        "   • Движение в одном направлении\n\n"
        "2. *Вводим переменные:*\n"
        "   Пусть v - скорость медленного болида (км/ч)\n"
        "   Тогда скорость быстрого: v + 13 (км/ч)\n\n"
        "3. *Определяем тип движения:*\n"
        "   Движение вдогонку. Быстрый болид должен догнать медленного.\n"
        "   Скорость сближения: v₁ - v₂ = (v + 13) - v = 13 км/ч\n\n"
        "4. *Составляем уравнение:*\n"
        "   Для движения вдогонку: t = S₀ / (v₁ - v₂)\n"
        "   t = 9.75 / 13\n\n"
        "5. *Вычисляем время:*\n"
        "   t = 9.75 / 13 = 0.75 часа\n\n"
        "6. *Переводим в минуты:*\n"
        "   0.75 часа × 60 = 45 минут\n\n"
        "7. *Проверяем логику:*\n"
        "   За 0.75 часа быстрый болид проедет на 13 × 0.75 = 9.75 км больше,\n"
        "   чем медленный, что как раз равно начальному расстоянию.\n\n"
        "8. *Особенность кругового движения:*\n"
        "   При движении по кругу из диаметрально противоположных точек\n"
        "   вдогонку нужно преодолеть половину круга, а не целый круг.\n\n"
        "9. *Формулируем ответ:*\n"
        "   *Ответ:* болиды поравняются в первый раз через 45 минут.\n\n"
        "*Формула для запоминания:*\n"
        "Для движения вдогонку по кругу из диаметрально противоположных точек:\n"
        "t = (L/2) / (v₁ - v₂), где L - длина круга."
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'viewing_example')


def send_example_7(bot, chat_id):
    """Отправляет пример 7: Лодка по реке"""
    example_text = (
         "🛶 *Пример 7: Лодка по реке*\n\n"
        "*Условие задачи:*\n"
        "Моторная лодка прошла 10 км по озеру и 4 км против течения реки, затратив на весь путь 1 час. "
        "Найдите собственную скорость лодки, если скорость течения реки равна 3 км/ч.\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+----------------+---------------+\n"
        "|      Параметр         |  По озеру      | Против течения|\n"
        "+-----------------------+----------------+---------------+\n"
        "|   Расстояние (км)     |      10        |       4       |\n"
        "|   Собственная скорость|     v          |      v        |\n"
        "|   Скорость течения    |       0        |       3       |\n"
        "|   Фактическая скорость|     v          |     v - 3     |\n"
        "|   Время (ч)           |     10/v       |   4/(v - 3)   |\n"
        "+-----------------------+----------------+---------------+\n"
        "|   Общее время         |           1 час                |\n"
        "+-----------------------+--------------------------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Анализируем условие:*\n"
        "   • По озеру: движение в стоячей воде, скорость = v\n"
        "   • Против течения: скорость = v - 3 (течение замедляет)\n"
        "   • Общее время: 1 час\n\n"
        "2. *Вводим переменную:*\n"
        "   Пусть v - собственная скорость лодки (км/ч)\n\n"
        "3. *Записываем выражения для времени:*\n"
        "   • Время по озеру: t₁ = 10 / v\n"
        "   • Время против течения: t₂ = 4 / (v - 3)\n\n"
        "4. *Составляем уравнение:*\n"
        "   t₁ + t₂ = 1\n"
        "   10/v + 4/(v - 3) = 1\n\n"
        "5. *Решаем уравнение:*\n"
        "   Умножаем обе части на v(v - 3):\n"
        "   10(v - 3) + 4v = v(v - 3)\n"
        "   10v - 30 + 4v = v² - 3v\n"
        "   14v - 30 = v² - 3v\n\n"
        "6. *Приводим к квадратному уравнению:*\n"
        "   v² - 3v - 14v + 30 = 0\n"
        "   v² - 17v + 30 = 0\n\n"
        "7. *Находим корни:*\n"
        "   Дискриминант: D = (-17)² - 4×1×30 = 289 - 120 = 169\n"
        "   √D = √169 = 13\n"
        "   v₁ = (17 + 13)/2 = 30/2 = 15\n"
        "   v₂ = (17 - 13)/2 = 4/2 = 2\n\n"
        "8. *Проверяем корни:*\n"
        "   • При v = 15 км/ч:\n"
        "     - По озеру: 10/15 = 2/3 часа = 40 минут\n"
        "     - Против течения: 4/(15-3) = 4/12 = 1/3 часа = 20 минут\n"
        "     - Общее: 40 + 20 = 60 минут = 1 час ✓\n"
        "   • При v = 2 км/ч:\n"
        "     - Против течения: v - 3 = -1 (скорость отрицательная!) - не подходит\n\n"
        "9. *Интерпретируем результат:*\n"
        "   Собственная скорость лодки должна быть больше скорости течения (3 км/ч),\n"
        "   иначе она не сможет двигаться против течения.\n\n"
        "10. *Формулируем ответ:*\n"
        "    *Ответ:* собственная скорость лодки равна 15 км/ч.\n\n"
        "*Алгоритм решения задач с течением:*\n"
        "1. vₛ - собственная скорость в стоячей воде\n"
        "2. vₜ - скорость течения\n"
        "3. По течению: v = vₛ + vₜ\n"
        "4. Против течения: v = vₛ - vₜ"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'movement_tasks', 'viewing_example')


# ==================== ОБУЧЕНИЕ ====================
def show_training_menu(bot, chat_id):
    """Отображает меню обучения"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_lesson1 = types.KeyboardButton('📖 Урок 1: Основные формулы')
    btn_lesson2 = types.KeyboardButton('📖 Урок 2: Движение навстречу')
    btn_lesson3 = types.KeyboardButton('📖 Урок 3: Движение вдогонку')
    btn_back = types.KeyboardButton('🔙 Назад к меню движения')

    markup.add(btn_lesson1, btn_lesson2, btn_lesson3, btn_back)

    bot.send_message(chat_id,
                     "🎓 *Обучение: Задачи на движение*\n\n"
                     "Выберите урок для изучение:\n\n"
                     "Пошаговое изучение тем:\n"
                     "1. Основные формулы и понятия\n"
                     "2. Движение навстречу друг другу\n"
                     "3. Движение вдогонку",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'movement_tasks', 'training_menu')


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
    set_user_state(chat_id, 'movement_tasks', 'viewing_lesson')


def get_lesson_1_content():
    """Контент урока 1"""
    return (
        "📖 *Урок 1: Основные формулы движения*\n\n"
        "*Основные формулы:*\n\n"
        "1. *Расстояние:* S = v × t\n"
        "   где S - расстояние, v - скорость, t - время\n\n"
        "2. *Скорость:* v = S / t\n"
        "3. *Время:* t = S / v\n\n"
        "*Единицы измерения:*\n"
        "• 1 м/с = 3.6 км/ч\n"
        "• 1 км/ч ≈ 0.278 м/с\n"
        "• 1 час = 60 минут = 3600 секунд\n\n"
        "*Пример:*\n"
        "Автомобиль проехал 180 км за 3 часа. Найти скорость.\n"
        "v = 180 / 3 = 60 км/ч"
    )


def get_lesson_2_content():
    """Контент урока 2"""
    return (
        "📖 *Урок 2: Движение навстречу друг другу*\n\n"
        "*Формула скорости сближения:*\n"
        "v = v₁ + v₂\n\n"
        "*Формула времени встречи:*\n"
        "t = S / (v₁ + v₂)\n\n"
        "*Пример:*\n"
        "Из пунктов A и B, расстояние между которыми 120 км, выехали два автомобиля. "
        "Скорость первого 40 км/ч, второго — 60 км/ч.\n\n"
        "*Решение:*\n"
        "1. v = 40 + 60 = 100 км/ч\n"
        "2. t = 120 / 100 = 1.2 часа = 1 ч 12 мин\n\n"
        "*Ответ:* встретятся через 1 час 12 минут."
    )


def get_lesson_3_content():
    """Контент урока 3"""
    return (
        "📖 *Урок 3: Движение вдогонку*\n\n"
        "*Формула скорости сближения:*\n"
        "v = v₁ - v₂ (если v₁ > v₂)\n\n"
        "*Формула времени сближения:*\n"
        "t = S₀ / (v₁ - v₂)\n"
        "где S₀ - начальное расстояние\n\n"
        "*Пример:*\n"
        "Из пункта A в пункт B выехал велосипедист со скоростью 12 км/ч. "
        "Через 2 часа из A в том же направлении выехал мотоциклист со скоростью 20 км/ч. "
        "Через сколько часов мотоциклист догонит велосипедиста?\n\n"
        "*Решение:*\n"
        "1. За 2 часа велосипедист проехал: 12 × 2 = 24 км\n"
        "2. Скорость сближения: 20 - 12 = 8 км/ч\n"
        "3. Время: t = 24 / 8 = 3 часа\n\n"
        "*Ответ:* мотоциклист догонит через 3 часа."
    )


# ==================== ОБРАБОТЧИК СООБЩЕНИЙ ====================
def handle_movement_tasks(bot, message, user_data):
    """Обрабатывает сообщения в модуле задач на движение"""
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
            '🎲 Случайная задача', '🔙 Назад к меню движения', '🔙 Назад к типам задач',
            '🔙 Назад к примерам', '🔙 Назад к урокам', '📖 Урок 1: Основные формулы',
            '📖 Урок 2: Движение навстречу', '📖 Урок 3: Движение вдогонку',
            '🚗 Пример 1: Два автомобиля', '🚂 Пример 2: Поезд и мост', '🚢 Пример 3: Два теплохода',
            '🚶 Пример 4: Пешеход и велосипедист', '🏙️ Пример 5: А→Б→А со скоростью',
            '🏎️ Пример 6: Болиды по кругу', '🛶 Пример 7: Лодка по реке'
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
        from main import show_text_tasks_menu
        show_text_tasks_menu(user_id)
        return

    elif text == '🔙 Назад к меню движения':
        show_movement_main_menu(bot, user_id)
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

    # ========== ГЛАВНОЕ МЕНЮ ДВИЖЕНИЯ ==========
    elif text == '📚 Справочный материал':
        send_reference_material(bot, user_id)

    elif text == '📝 Примеры задач':
        show_examples_menu(bot, user_id)

    elif text == '🎓 Обучение':
        show_training_menu(bot, user_id)

    elif text == '🎯 Тренажер':
        show_simulator_menu(bot, user_id)

    # ========== ВЫБОР ПРИМЕРОВ ИЗ МЕНЮ (7 КНОПОК) ==========
    elif text == '🚗 Пример 1: Два автомобиля':
        send_example_1(bot, user_id)

    elif text == '🚂 Пример 2: Поезд и мост':
        send_example_2(bot, user_id)

    elif text == '🚢 Пример 3: Два теплохода':
        send_example_3(bot, user_id)

    elif text == '🚶 Пример 4: Пешеход и велосипедист':
        send_example_4(bot, user_id)

    elif text == '🏙️ Пример 5: А→Б→А со скоростью':
        send_example_5(bot, user_id)

    elif text == '🏎️ Пример 6: Болиды по кругу':
        send_example_6(bot, user_id)

    elif text == '🛶 Пример 7: Лодка по реке':
        send_example_7(bot, user_id)

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
    elif text == '📖 Урок 1: Основные формулы':
        send_lesson(bot, user_id, 1)

    elif text == '📖 Урок 2: Движение навстречу':
        send_lesson(bot, user_id, 2)

    elif text == '📖 Урок 3: Движение вдогонку':
        send_lesson(bot, user_id, 3)

    else:
        # Если сообщение не распознано, показываем главное меню движения
        show_movement_main_menu(bot, user_id)