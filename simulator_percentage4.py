import random
from random_percentage_generator import RandomPercentageGenerator

class SimulatorPercentage4:
    def __init__(self):
        self.тренажер = RandomPercentageGenerator()

    def начать_уровень(self):
        """Начинает уровень со случайными задачами"""
        return self.тренажер.generate_random_task()

    def получить_текущую_задачу(self):
        """Возвращает условие текущей задачи"""
        if hasattr(self.тренажер, 'current_task') and self.тренажер.current_task:
            return self._format_task(self.тренажер.current_task)
        return "Нажмите '🔄 Новая задача' для получения случайной задачи!"

    def получить_следующую_задачу(self):
        """Возвращает следующую случайную задачу"""
        task_data = self.тренажер.generate_random_task()
        self.тренажер.current_task = task_data
        return self._format_task(task_data)

    def проверить_ответ(self, ответ_пользователя):
        """Проверяет ответ пользователя на текущую задачу"""
        if not hasattr(self.тренажер, 'current_task') or not self.тренажер.current_task:
            return False, "Сначала получите задачу!"

        try:
            current_task = self.тренажер.current_task
            correct_answer = current_task["answer"]

            # Проверяем, является ли правильный ответ строкой (для текстовых ответов)
            if isinstance(correct_answer, str):
                # Сравниваем строки, игнорируя регистр и лишние пробелы
                if ответ_пользователя.strip().lower() == correct_answer.lower():
                    # Генерируем новую задачу
                    new_task = self.тренажер.generate_random_task()
                    self.тренажер.current_task = new_task

                    difficulty_emojis = {
                        "easy": "🟢",
                        "medium": "🟡",
                        "hard": "🔴"
                    }

                    emoji = difficulty_emojis.get(new_task["difficulty"], "🎲")
                    level_text = {
                        "easy": "Легкий уровень",
                        "medium": "Средний уровень",
                        "hard": "Сложный уровень"
                    }.get(new_task["difficulty"], "Случайная задача")

                    next_task = f"{emoji} *Случайная задача ({level_text}):*\n\n{new_task['condition']}"

                    return True, f"✅ *Верно!*\n\n*Следующая задача:*\n\n{next_task}"
                else:
                    return False, "❌ *Неверно, попробуйте еще раз!*"

            # Для числовых ответов
            else:
                # Пробуем преобразовать ответ в число
                user_answer = float(str(ответ_пользователя).replace(',', '.').strip())
                correct_answer_float = float(correct_answer)

                # Допустимая погрешность 0.1 для дробных ответов
                if abs(user_answer - correct_answer_float) < 0.1:
                    # Генерируем новую задачу
                    new_task = self.тренажер.generate_random_task()
                    self.тренажер.current_task = new_task

                    difficulty_emojis = {
                        "easy": "🟢",
                        "medium": "🟡",
                        "hard": "🔴"
                    }

                    emoji = difficulty_emojis.get(new_task["difficulty"], "🎲")
                    level_text = {
                        "easy": "Легкий уровень",
                        "medium": "Средний уровень",
                        "hard": "Сложный уровень"
                    }.get(new_task["difficulty"], "Случайная задача")

                    next_task = f"{emoji} *Случайная задача ({level_text}):*\n\n{new_task['condition']}"

                    return True, f"✅ *Верно!*\n\n*Следующая задача:*\n\n{next_task}"
                else:
                    return False, f"❌ *Неверно, попробуйте еще раз!* (Ожидалось: {correct_answer})"

        except ValueError:
            return False, "❌ Пожалуйста, введите число."

    def получить_подсказку(self):
        """Возвращает подсказку для текущей задачи"""
        if hasattr(self.тренажер, 'current_task') and self.тренажер.current_task and "type" in self.тренажер.current_task:
            return self.тренажер.get_hint_for_task(self.тренажер.current_task["type"])
        return "💡 *Подсказка:* Внимательно прочитайте условие задачи. Определите, что дано и что нужно найти. Используйте основные формулы процентов."

    def показать_ответ(self):
        """Показывает правильный ответ для текущей задачи"""
        if hasattr(self.тренажер, 'current_task') and self.тренажер.current_task:
            task = self.тренажер.current_task
            return f"📝 *Ответ:* {task['answer']}\n\n*Решение:*\n{task.get('solution', 'Решение доступно в полной версии.')}"
        return "Нет активной задачи."

    def _format_task(self, task_data):
        """Форматирует задачу для отображения"""
        difficulty_emojis = {
            "easy": "🟢",
            "medium": "🟡",
            "hard": "🔴"
        }

        emoji = difficulty_emojis.get(task_data["difficulty"], "🎲")
        level_text = {
            "easy": "Легкий уровень",
            "medium": "Средний уровень",
            "hard": "Сложный уровень"
        }.get(task_data["difficulty"], "Случайная задача")

        return f"{emoji} *Случайная задача ({level_text}):*\n\n{task_data['condition']}"