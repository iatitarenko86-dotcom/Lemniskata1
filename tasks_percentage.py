import telebot
from telebot import types
from user_states import set_user_state, get_user_state, update_user_data
from simulator_percentage1 import SimulatorPercentage1
from simulator_percentage2 import SimulatorPercentage2
from simulator_percentage3 import SimulatorPercentage3
from simulator_percentage4 import SimulatorPercentage4

# Глобальный словарь для хранения тренажеров по пользователям
тренажеры_пользователей = {}


# ==================== ГЛАВНОЕ МЕНЮ ПРОЦЕНТЫ ====================
def show_percentage_main_menu(bot, chat_id):
    """Отображает главное меню задач на проценты"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_reference = types.KeyboardButton('📚 Справочный материал')
    btn_examples = types.KeyboardButton('📝 Примеры задач')
    btn_training = types.KeyboardButton('🎓 Обучение')
    btn_simulator = types.KeyboardButton('🎯 Тренажер')
    btn_back = types.KeyboardButton('🔙 Назад к типам задач')

    markup.add(btn_reference, btn_examples, btn_training, btn_simulator, btn_back)

    bot.send_message(chat_id,
                     "📊 *Задачи на проценты*\n\n"
                     "Выберите раздел для изучения:\n\n"
                     "• *📚 Справочный материал* - формулы и теория\n"
                     "• *📝 Примеры задач* - готовые решения\n"
                     "• *🎓 Обучение* - пошаговое изучение\n"
                     "• *🎯 Тренажер* - практические задания",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'percentage_tasks', 'main_menu')


# ==================== НАЧАЛО РАБОТЫ ====================
def start_percentage_tasks(bot, chat_id, user_data):
    """Начинает работу с задачами на проценты"""
    show_percentage_main_menu(bot, chat_id)


# ==================== МЕНЮ ТРЕНАЖЕРА ====================
def show_simulator_menu(bot, chat_id):
    """Отображает меню тренажера"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_easy = types.KeyboardButton('🟢 Легкий уровень')
    btn_medium = types.KeyboardButton('🟡 Средний уровень')
    btn_hard = types.KeyboardButton('🔴 Сложный уровень')
    btn_random = types.KeyboardButton('🎲 Случайная задача')
    btn_back = types.KeyboardButton('🔙 Назад к меню процентов')

    markup.add(btn_easy, btn_medium, btn_hard, btn_random, btn_back)

    bot.send_message(chat_id,
                     "🎯 *Тренажер: Задачи на проценты*\n\n"
                     "Выберите уровень сложности:\n\n"
                     "• *🟢 Легкий* - базовые задачи\n"
                     "• *🟡 Средний* - задачи средней сложности\n"
                     "• *🔴 Сложный* - комплексные задачи\n"
                     "• *🎲 Случайная* - задача любого уровня",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'percentage_tasks', 'simulator_menu')


# ==================== ЗАПУСК ЛЕГКОГО УРОВНЯ ====================
def start_easy_simulator(bot, chat_id):
    """Запускает легкий уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorPercentage1()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorPercentage1):
                тренажеры_пользователей[chat_id] = SimulatorPercentage1()

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

        set_user_state(chat_id, 'percentage_tasks', 'easy_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске легкого уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СРЕДНЕГО УРОВНЯ ====================
def start_medium_simulator(bot, chat_id):
    """Запускает средний уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorPercentage2()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorPercentage2):
                тренажеры_пользователей[chat_id] = SimulatorPercentage2()

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

        set_user_state(chat_id, 'percentage_tasks', 'medium_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске среднего уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СЛОЖНОГО УРОВНЯ ====================
def start_hard_simulator(bot, chat_id):
    """Запускает сложный уровень тренажера"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorPercentage3()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorPercentage3):
                тренажеры_пользователей[chat_id] = SimulatorPercentage3()

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

        set_user_state(chat_id, 'percentage_tasks', 'hard_simulator')
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при запуске сложного уровня: {str(e)}")
        show_simulator_menu(bot, chat_id)


# ==================== ЗАПУСК СЛУЧАЙНЫХ ЗАДАЧ ====================
def start_random_simulator(bot, chat_id):
    """Запускает режим случайных задач"""
    try:
        # Создаем или получаем тренажер для пользователя
        if chat_id not in тренажеры_пользователей:
            тренажеры_пользователей[chat_id] = SimulatorPercentage4()
        else:
            # Если тренажер уже существует, но другого типа - заменяем
            if not isinstance(тренажеры_пользователей[chat_id], SimulatorPercentage4):
                тренажеры_пользователей[chat_id] = SimulatorPercentage4()

        тренажер = тренажеры_пользователей[chat_id]

        # Начинаем уровень
        задача = тренажер.начать_уровень()

        # Сохраняем задачу в атрибут
        тренажер.текущая_задача = задача

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
                         f"{задача['condition'] if isinstance(задача, dict) else задача}\n\n"
                         "Введите *ответ* в чат:",
                         parse_mode='Markdown',
                         reply_markup=markup)

        set_user_state(chat_id, 'percentage_tasks', 'random_simulator')
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
                                     f"{задача['condition'] if isinstance(задача, dict) else задача}\n\n"
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
                             f"{задача['condition'] if isinstance(задача, dict) else задача}\n\n"
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
    """Отправляет справочный материал по процентам"""
    reference_text = (
        "📚 *Справочный материал по задачам на проценты*\n\n"
        "*Основные понятия:*\n\n"
        "🔹 *Процент* - это одна сотая часть числа или величины.\n"
        "   Обозначение: 1% = 1/100 = 0,01\n\n"
        "*Основные формулы:*\n\n"
        "1. *Нахождение процента от числа:*\n"
        "   `p% от числа A = A × p ÷ 100`\n"
        "   *Пример:* 15% от 200 = 200 × 15 ÷ 100 = 30\n\n"
        "2. *Нахождение числа по его проценту:*\n"
        "   Если p% числа равны B, то число A = B × 100 ÷ p\n"
        "   *Пример:* Если 20% числа равны 40, то число = 40 × 100 ÷ 20 = 200\n\n"
        "3. *Сколько процентов одно число составляет от другого:*\n"
        "   p% = (B ÷ A) × 100%\n"
        "   *Пример:* 25 от 200 составляет (25 ÷ 200) × 100% = 12,5%\n\n"
        "*Изменение величины в процентах:*\n\n"
        "4. *Увеличение на p%:*\n"
        "   Новая величина = A × (1 + p/100)\n\n"
        "5. *Уменьшение на p%:*\n"
        "   Новая величина = A × (1 - p/100)\n\n"
        "6. *Последовательные изменения:*\n"
        "   При двух последовательных изменениях на p% и q%:\n"
        "   A × (1 ± p/100) × (1 ± q/100)\n\n"
        "*Простые примеры:*\n\n"
        "🔸 *Найти 8% от 50:*\n"
        "   50 × 8 ÷ 100 = 400 ÷ 100 = 4\n\n"
        "🔸 *Найти число, если 12% его равны 36:*\n"
        "   36 × 100 ÷ 12 = 3600 ÷ 12 = 300\n\n"
        "🔸 *Сколько процентов составляет 15 от 60:*\n"
        "   (15 ÷ 60) × 100% = 0,25 × 100% = 25%\n\n"
        "*Важно!* Задачи на смеси и сплавы рассматриваются в другом разделе."
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к меню процентов')
    markup.add(btn_back)

    bot.send_message(chat_id, reference_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'percentage_tasks', 'reference')


# ==================== МЕНЮ ПРИМЕРОВ (5 КНОПОК) ====================
def show_examples_menu(bot, chat_id):
    """Отображает меню примеров задач с 5 кнопками"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_example1 = types.KeyboardButton('📱 Пример 1: Скидка на телефон')
    btn_example2 = types.KeyboardButton('🧈 Пример 2: Скидка пенсионерам')
    btn_example3 = types.KeyboardButton('📚 Пример 3: Двойное снижение цены')
    btn_example4 = types.KeyboardButton('💰 Пример 4: Налог на доходы')
    btn_example5 = types.KeyboardButton('🌳 Пример 5: Деревья в парке')
    btn_back = types.KeyboardButton('🔙 Назад к меню процентов')

    markup.add(btn_example1, btn_example2, btn_example3, btn_example4, btn_example5, btn_back)

    bot.send_message(chat_id,
                     "📝 *Примеры задач на проценты*\n\n"
                     "Выберите пример для изучения:\n\n"
                     "Каждый пример содержит:\n"
                     "• Полное условие задачи\n"
                     "• Развернутое решение\n"
                     "• Итоговый ответ",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'percentage_tasks', 'examples_menu')


# ==================== ПРИМЕРЫ ЗАДАЧ ====================

def send_example_1(bot, chat_id):
    """Отправляет пример 1: Скидка на телефон"""
    example_text = (
        "📱 *Пример 1: Скидка на телефон*\n\n"
        "*Условие задачи:*\n"
        "Мобильный телефон стоил 5000 рублей. Через некоторое время цену на\n"
        "эту модель снизили до 3000 рублей. На сколько процентов была снижена\n"
        "цена?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+---------------------+--------------+\n"
        "|      Параметр       |   Значение   |\n"
        "+---------------------+--------------+\n"
        "| Начальная цена      | 5000 руб.    |\n"
        "| Конечная цена       | 3000 руб.    |\n"
        "| Снижение цены       | 2000 руб.    |\n"
        "| Процент снижения    |      ?       |\n"
        "+---------------------+--------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Находим абсолютное снижение цены:*\n"
        "   Δ = 5000 - 3000 = 2000 рублей\n\n"
        "2. *Определяем, какую часть составляет снижение от начальной цены:*\n"
        "   Часть = 2000 ÷ 5000 = 0,4\n\n"
        "3. *Переводим в проценты:*\n"
        "   Процент снижения = 0,4 × 100% = 40%\n\n"
        "4. *Проверяем другим способом:*\n"
        "   Новая цена составляет: 3000 ÷ 5000 = 0,6 = 60% от старой\n"
        "   Значит, цена снизилась на: 100% - 60% = 40%\n\n"
        "5. *Формулируем ответ:*\n"
        "   *Ответ:* цена была снижена на 40%.\n\n"
        "*Формула для запоминания:*\n"
        "Процент снижения = ((Старая цена - Новая цена) ÷ Старая цена) × 100%"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'percentage_tasks', 'viewing_example')


def send_example_2(bot, chat_id):
    """Отправляет пример 2: Скидка пенсионерам"""
    example_text = (
        "🧈 *Пример 2: Скидка пенсионерам*\n\n"
        "*Условие задачи:*\n"
        "Пачка сливочного масла стоит 60 рублей. Пенсионерам магазин делает\n"
        "скидку 5%. Сколько рублей стоит пачка масла для пенсионера?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+----------------------+--------------+\n"
        "|      Параметр        |   Значение   |\n"
        "+----------------------+--------------+\n"
        "| Цена без скидки      | 60 руб.      |\n"
        "| Скидка для пенсионера| 5%           |\n"
        "| Размер скидки        |      ?       |\n"
        "| Цена со скидкой      |      ?       |\n"
        "+----------------------+--------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "**Способ 1: Через нахождение процента от числа**\n\n"
        "1. *Находим размер скидки:*\n"
        "   Скидка = 5% от 60 рублей = 60 × 5 ÷ 100 = 300 ÷ 100 = 3 рубля\n\n"
        "2. *Вычитаем скидку из цены:*\n"
        "   Цена со скидкой = 60 - 3 = 57 рублей\n\n"
        "**Способ 2: Через процент от цены**\n\n"
        "1. *Пенсионер платит:* 100% - 5% = 95% от полной цены\n\n"
        "2. *Находим 95% от 60 рублей:*\n"
        "   60 × 95 ÷ 100 = 60 × 0,95 = 57 рублей\n\n"
        "3. *Проверяем:*\n"
        "   Оба способа дают одинаковый результат ✓\n\n"
        "4. *Формулируем ответ:*\n"
        "   *Ответ:* пачка масла для пенсионера стоит 57 рублей.\n\n"
        "*Формула для запоминания:*\n"
        "Цена со скидкой = Цена × (100% - Скидка%) ÷ 100"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'percentage_tasks', 'viewing_example')


def send_example_3(bot, chat_id):
    """Отправляет пример 3: Двойное снижение цены"""
    example_text = (
        "📚 *Пример 3: Двойное снижение цены*\n\n"
        "*Условие задачи:*\n"
        "До снижения цен книга в киоске стоила 120 рублей. Вычислите цену\n"
        "книги после двух последовательных снижений, если первое снижение\n"
        "было на 10%, а второе на 5%.\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+--------------------+--------------+---------------+\n"
        "|      Параметр      |   Процент    |    Цена       |\n"
        "+--------------------+--------------+---------------+\n"
        "| Начальная цена     |      -       | 120 руб.      |\n"
        "| После 1-го снижения|    -10%      |      ?        |\n"
        "| После 2-го снижения|    -5%       |      ?        |\n"
        "+--------------------+--------------+---------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "**Способ 1: Последовательные вычисления**\n\n"
        "1. *Первое снижение на 10%:*\n"
        "   Цена после первого снижения = 120 × (100% - 10%) = 120 × 0,9 = 108 рублей\n\n"
        "2. *Второе снижение на 5%:*\n"
        "   Цена после второго снижения = 108 × (100% - 5%) = 108 × 0,95 = 102,6 рублей\n\n"
        "**Способ 2: Общая формула**\n\n"
        "1. *Общий коэффициент снижения:*\n"
        "   k = 0,9 × 0,95 = 0,855\n\n"
        "2. *Конечная цена:*\n"
        "   120 × 0,855 = 102,6 рублей\n\n"
        "3. *Проверяем:*\n"
        "   Общее снижение: 100% - 85,5% = 14,5%\n\n"
        "4. *Формулируем ответ:*\n"
        "   *Ответ:* после двух снижений книга стоит 102,6 рубля.\n\n"
        "*Формула для запоминания:*\n"
        "При последовательных изменениях: A × (1 - p₁/100) × (1 - p₂/100)"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'percentage_tasks', 'viewing_example')


def send_example_4(bot, chat_id):
    """Отправляет пример 4: Налог на доходы"""
    example_text = (
        "💰 *Пример 4: Налог на доходы*\n\n"
        "*Условие задачи:*\n"
        "Налог на доходы составляет 13% от заработной платы. После удержания\n"
        "налога на доходы Мария Константиновна получила 9570 рублей. Сколько\n"
        "рублей составляет заработная плата Марии Константиновны?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-----------------------+--------------+\n"
        "|      Параметр         |   Значение   |\n"
        "+-----------------------+--------------+\n"
        "| Налог                 | 13%          |\n"
        "| Получено на руки      | 9570 руб.    |\n"
        "| Зарплата до вычета    |      ?       |\n"
        "+-----------------------+--------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Анализируем условие:*\n"
        "   После вычета налога 13% Мария получила 9570 рублей.\n"
        "   Значит, полученная сумма составляет 100% - 13% = 87% от зарплаты.\n\n"
        "2. *Составляем пропорцию:*\n"
        "   87% = 9570 рублей\n"
        "   100% = X рублей\n\n"
        "3. *Находим зарплату:*\n"
        "   X = 9570 × 100 ÷ 87 = 957000 ÷ 87 = 11000 рублей\n\n"
        "4. *Проверяем:*\n"
        "   Налог: 11000 × 13% = 11000 × 0,13 = 1430 руб.\n"
        "   На руки: 11000 - 1430 = 9570 руб. ✓\n\n"
        "5. *Формулируем ответ:*\n"
        "   *Ответ:* заработная плата составляет 11000 рублей.\n\n"
        "*Формула для запоминания:*\n"
        "Зарплата = Сумма на руки ÷ (100% - налог%) × 100%"
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'percentage_tasks', 'viewing_example')


def send_example_5(bot, chat_id):
    """Отправляет пример 5: Деревья в парке"""
    example_text = (
        "🌳 *Пример 5: Деревья в парке*\n\n"
        "*Условие задачи:*\n"
        "В парке 25% всех деревьев составляют берёзы, третью часть --- клёны.\n"
        "Дубов в этом парке на 24 больше, чем клёнов, а остальные 46 деревьев --- липы.\n"
        "Сколько всего деревьев в этом парке?\n\n"
        "*Таблица данных:*\n"
        "```\n"
        "+-------------------+--------------+\n"
        "|   Вид деревьев    |   Количество |\n"
        "+-------------------+--------------+\n"
        "| Берёзы            | 25% от X     |\n"
        "| Клёны             | X/3          |\n"
        "| Дубы              | X/3 + 24     |\n"
        "| Липы              | 46           |\n"
        "+-------------------+--------------+\n"
        "```\n\n"
        "*Развернутое решение:*\n\n"
        "1. *Обозначим общее количество деревьев за X:*\n\n"
        "2. *Выражаем каждую группу:*\n"
        "   • Берёзы: 0,25X\n"
        "   • Клёны: X/3\n"
        "   • Дубы: X/3 + 24\n"
        "   • Липы: 46\n\n"
        "3. *Составляем уравнение:*\n"
        "   0,25X + X/3 + (X/3 + 24) + 46 = X\n\n"
        "4. *Приводим к общему знаменателю:*\n"
        "   0,25X = X/4\n"
        "   X/4 + X/3 + X/3 + 70 = X\n"
        "   X/4 + 2X/3 + 70 = X\n\n"
        "5. *Умножаем на 12:*\n"
        "   3X + 8X + 840 = 12X\n"
        "   11X + 840 = 12X\n\n"
        "6. *Находим X:*\n"
        "   12X - 11X = 840\n"
        "   X = 840\n\n"
        "7. *Проверяем:*\n"
        "   Берёзы: 840 × 0,25 = 210\n"
        "   Клёны: 840 ÷ 3 = 280\n"
        "   Дубы: 280 + 24 = 304\n"
        "   Липы: 46\n"
        "   Сумма: 210 + 280 + 304 + 46 = 840 ✓\n\n"
        "8. *Формулируем ответ:*\n"
        "   *Ответ:* в парке 840 деревьев."
    )

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_back = types.KeyboardButton('🔙 Назад к примерам')
    markup.add(btn_back)

    bot.send_message(chat_id, example_text, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'percentage_tasks', 'viewing_example')


# ==================== ОБУЧЕНИЕ ====================
def show_training_menu(bot, chat_id):
    """Отображает меню обучения"""
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_lesson1 = types.KeyboardButton('📖 Урок 1: Основные формулы')
    btn_lesson2 = types.KeyboardButton('📖 Урок 2: Нахождение процента')
    btn_lesson3 = types.KeyboardButton('📖 Урок 3: Изменение величины')
    btn_back = types.KeyboardButton('🔙 Назад к меню процентов')

    markup.add(btn_lesson1, btn_lesson2, btn_lesson3, btn_back)

    bot.send_message(chat_id,
                     "🎓 *Обучение: Задачи на проценты*\n\n"
                     "Выберите урок для изучения:\n\n"
                     "Пошаговое изучение тем:\n"
                     "1. Основные формулы и понятия\n"
                     "2. Нахождение процента от числа и числа по проценту\n"
                     "3. Изменение величины в процентах",
                     parse_mode='Markdown',
                     reply_markup=markup)

    set_user_state(chat_id, 'percentage_tasks', 'training_menu')


def send_lesson(bot, chat_id, lesson_number):
    """Отправляет урок"""
    if lesson_number == 1:
        lesson_content = (
            "📖 *Урок 1: Основные формулы процентов*\n\n"
            "*Основные понятия:*\n\n"
            "🔹 *Процент* - это одна сотая часть числа или величины.\n"
            "   1% = 1/100 = 0,01\n\n"
            "*Основные формулы:*\n\n"
            "1. *Нахождение процента от числа:*\n"
            "   p% от A = A × p ÷ 100\n"
            "   *Пример:* 15% от 200 = 200 × 15 ÷ 100 = 30\n\n"
            "2. *Нахождение числа по его проценту:*\n"
            "   Если p% числа равны B, то A = B × 100 ÷ p\n"
            "   *Пример:* 20% числа равны 40, число = 40 × 100 ÷ 20 = 200\n\n"
            "3. *Сколько процентов одно число составляет от другого:*\n"
            "   p% = (B ÷ A) × 100%\n"
            "   *Пример:* 25 от 200 составляет (25 ÷ 200) × 100% = 12,5%"
        )
    elif lesson_number == 2:
        lesson_content = (
            "📖 *Урок 2: Нахождение процента*\n\n"
            "*Типы задач:*\n\n"
            "1. *Нахождение процента от числа:*\n"
            "   Задача: Найти 8% от 50.\n"
            "   Решение: 50 × 8 ÷ 100 = 400 ÷ 100 = 4\n\n"
            "2. *Нахождение числа по его проценту:*\n"
            "   Задача: Найти число, если 12% его равны 36.\n"
            "   Решение: 36 × 100 ÷ 12 = 3600 ÷ 12 = 300\n\n"
            "3. *Нахождение процентного отношения:*\n"
            "   Задача: Сколько процентов составляет 15 от 60?\n"
            "   Решение: 15 ÷ 60 × 100% = 0,25 × 100% = 25%"
        )
    elif lesson_number == 3:
        lesson_content = (
            "📖 *Урок 3: Изменение величины в процентах*\n\n"
            "*Формулы изменения:*\n\n"
            "1. *Увеличение на p%:*\n"
            "   Новая величина = A × (1 + p/100)\n"
            "   *Пример:* Увеличить 200 на 15%: 200 × 1,15 = 230\n\n"
            "2. *Уменьшение на p%:*\n"
            "   Новая величина = A × (1 - p/100)\n"
            "   *Пример:* Уменьшить 200 на 15%: 200 × 0,85 = 170\n\n"
            "3. *Последовательные изменения:*\n"
            "   При двух изменениях на p% и q%:\n"
            "   A × (1 ± p/100) × (1 ± q/100)\n\n"
            "4. *Нахождение первоначальной величины:*\n"
            "   Если после увеличения на p% получили B, то A = B ÷ (1 + p/100)\n"
            "   Если после уменьшения на p% получили B, то A = B ÷ (1 - p/100)"
        )
    else:
        lesson_content = "Урок не найден."

    # Сохраняем текущий урок
    update_user_data(chat_id, {'current_lesson': lesson_number})

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn_prev = types.KeyboardButton('⬅️ Предыдущий урок')
    btn_next = types.KeyboardButton('➡️ Следующий урок')
    btn_back = types.KeyboardButton('🔙 Назад к урокам')
    markup.add(btn_prev, btn_next, btn_back)

    bot.send_message(chat_id, lesson_content, parse_mode='Markdown', reply_markup=markup)
    set_user_state(chat_id, 'percentage_tasks', 'viewing_lesson')


# ==================== ОБРАБОТЧИК СООБЩЕНИЙ ДЛЯ ПРОЦЕНТОВ ====================
def handle_percentage_tasks(bot, message, user_data):
    """Обрабатывает сообщения в модуле задач на проценты"""
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
            '🎲 Случайная задача', '🔙 Назад к меню процентов', '🔙 Назад к типам задач',
            '🔙 Назад к примерам', '🔙 Назад к урокам', '📖 Урок 1: Основные формулы',
            '📖 Урок 2: Нахождение процента', '📖 Урок 3: Изменение величины',
            '📱 Пример 16: Скидка на телефон', '🧈 Пример 17: Скидка пенсионерам',
            '📚 Пример 18: Двойное снижение цены', '💰 Пример 19: Налог на доходы',
            '🌳 Пример 20: Деревья в парке'
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

    elif text == '🔙 Назад к меню процентов':
        show_percentage_main_menu(bot, user_id)
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

    # ========== ГЛАВНОЕ МЕНЮ ПРОЦЕНТОВ ==========
    elif text == '📚 Справочный материал':
        send_reference_material(bot, user_id)

    elif text == '📝 Примеры задач':
        show_examples_menu(bot, user_id)

    elif text == '🎓 Обучение':
        show_training_menu(bot, user_id)

    elif text == '🎯 Тренажер':
        show_simulator_menu(bot, user_id)

    # ========== ВЫБОР ПРИМЕРОВ ИЗ МЕНЮ (5 КНОПОК) ==========
    elif text == '📱 Пример 16: Скидка на телефон':
        send_example_16(bot, user_id)

    elif text == '🧈 Пример 17: Скидка пенсионерам':
        send_example_17(bot, user_id)

    elif text == '📚 Пример 18: Двойное снижение цены':
        send_example_18(bot, user_id)

    elif text == '💰 Пример 19: Налог на доходы':
        send_example_19(bot, user_id)

    elif text == '🌳 Пример 20: Деревья в парке':
        send_example_20(bot, user_id)

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

    elif text == '📖 Урок 2: Нахождение процента':
        send_lesson(bot, user_id, 2)

    elif text == '📖 Урок 3: Изменение величины':
        send_lesson(bot, user_id, 3)

    else:
        # Если сообщение не распознано, показываем главное меню процентов

        show_percentage_main_menu(bot, user_id)
