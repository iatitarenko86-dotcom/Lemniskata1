"""
Модуль для управления состояниями пользователей.
Хранит информацию о текущем модуле и подмодуле, в котором находится пользователь.
"""

user_states = {}


def set_user_state(user_id, module, sub_module=None, additional_data=None):
    """Устанавливает состояние пользователя"""
    if user_id not in user_states:
        user_states[user_id] = {}

    user_states[user_id]['current_module'] = module
    if sub_module:
        user_states[user_id]['sub_module'] = sub_module
    if additional_data:
        user_states[user_id].update(additional_data)


def get_user_state(user_id):
    """Получает состояние пользователя"""
    return user_states.get(user_id, {})


def get_current_module(user_id):
    """Получает текущий модуль пользователя"""
    return user_states.get(user_id, {}).get('current_module', '')


def get_current_submodule(user_id):
    """Получает текущий подмодуль пользователя"""
    return user_states.get(user_id, {}).get('sub_module', '')


def update_user_data(user_id, data):
    """Обновляет дополнительные данные пользователя"""
    if user_id not in user_states:
        user_states[user_id] = {}

    user_states[user_id].update(data)


def get_user_data(user_id, key=None):
    """Получает данные пользователя"""
    if user_id not in user_states:
        return None if key else {}

    if key:
        return user_states[user_id].get(key)

    return user_states[user_id]


def clear_user_state(user_id):
    """Очищает состояние пользователя"""
    if user_id in user_states:
        del user_states[user_id]


def is_user_in_module(user_id, module):
    """Проверяет, находится ли пользователь в указанном модуле"""
    current_module = get_current_module(user_id)
    return current_module == module