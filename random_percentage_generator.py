import random
import math


class RandomPercentageGenerator:
    def __init__(self):
        self.task_templates = []
        self._initialize_templates()
        self.current_task = None

    def _initialize_templates(self):
        """Инициализация шаблонов задач по категориям"""

        # ========== КАТЕГОРИЯ 1: Простые задачи (аналогично simulator_percentage1) ==========
        simple_templates = [
            {
                "type": "simple_percent_of_number",
                "generate": self._generate_simple_percent_of_number,
                "difficulty": "easy"
            },
            {
                "type": "simple_number_by_percent",
                "generate": self._generate_simple_number_by_percent,
                "difficulty": "easy"
            },
            {
                "type": "simple_percent_ratio",
                "generate": self._generate_simple_percent_ratio,
                "difficulty": "easy"
            },
            {
                "type": "simple_price_change",
                "generate": self._generate_simple_price_change,
                "difficulty": "easy"
            },
            {
                "type": "simple_discount",
                "generate": self._generate_simple_discount,
                "difficulty": "easy"
            }
        ]

        # ========== КАТЕГОРИЯ 2: Средние задачи (аналогично simulator_percentage2) ==========
        medium_templates = [
            {
                "type": "medium_percentage_increase_decrease",
                "generate": self._generate_medium_percentage_increase_decrease,
                "difficulty": "medium"
            },
            {
                "type": "medium_percentage_of_remainder",
                "generate": self._generate_medium_percentage_of_remainder,
                "difficulty": "medium"
            },
            {
                "type": "medium_consecutive_changes",
                "generate": self._generate_medium_consecutive_changes,
                "difficulty": "medium"
            },
            {
                "type": "medium_reverse_percentage",
                "generate": self._generate_medium_reverse_percentage,
                "difficulty": "medium"
            },
            {
                "type": "medium_percentage_comparison",
                "generate": self._generate_medium_percentage_comparison,
                "difficulty": "medium"
            }
        ]

        # ========== КАТЕГОРИЯ 3: Сложные задачи (аналогично simulator_percentage3) ==========
        hard_templates = [
            {
                "type": "hard_complex_percentage",
                "generate": self._generate_hard_complex_percentage,
                "difficulty": "hard"
            },
            {
                "type": "hard_mixture_problem",
                "generate": self._generate_hard_mixture_problem,
                "difficulty": "hard"
            },
            {
                "type": "hard_fraction_percentage",
                "generate": self._generate_hard_fraction_percentage,
                "difficulty": "hard"
            },
            {
                "type": "hard_multiple_percentages",
                "generate": self._generate_hard_multiple_percentages,
                "difficulty": "hard"
            },
            {
                "type": "hard_bank_interest",
                "generate": self._generate_hard_bank_interest,
                "difficulty": "hard"
            },
            {
                "type": "hard_percentage_equation",
                "generate": self._generate_hard_percentage_equation,
                "difficulty": "hard"
            }
        ]

        self.task_templates = simple_templates + medium_templates + hard_templates

    def generate_random_task(self, difficulty=None):
        """Генерирует случайную задачу"""
        if difficulty:
            # Фильтруем шаблоны по сложности
            filtered_templates = [t for t in self.task_templates if t["difficulty"] == difficulty]
            if filtered_templates:
                template = random.choice(filtered_templates)
            else:
                template = random.choice(self.task_templates)
        else:
            # Выбираем случайный шаблон любой сложности
            template = random.choice(self.task_templates)

        # Генерируем задачу
        task_data = template["generate"]()
        task_data["type"] = template["type"]
        task_data["difficulty"] = template["difficulty"]

        self.current_task = task_data
        return task_data

    # ========== МЕТОДЫ ГЕНЕРАЦИИ ПРОСТЫХ ЗАДАЧ ==========

    def _generate_simple_percent_of_number(self):
        """Генерация задачи на нахождение процента от числа"""
        number = random.choice([5000, 8000, 12000, 15000, 20000, 25000, 30000])
        percent = random.choice([5, 8, 10, 12, 15, 20, 25])

        result = number * percent / 100

        task = {
            "condition": f"Найдите {percent}% от числа {number}.",
            "answer": result,
            "solution": f"{percent}% от {number} = {number} × {percent} ÷ 100 = {number * percent} ÷ 100 = {result}"
        }
        return task

    def _generate_simple_number_by_percent(self):
        """Генерация задачи на нахождение числа по его проценту"""
        percent = random.choice([8, 10, 12, 15, 20, 25, 30])
        part = random.choice([24, 36, 45, 60, 75, 90, 120])

        number = part * 100 / percent

        task = {
            "condition": f"Найдите число, если {percent}% его равны {part}.",
            "answer": number,
            "solution": f"Число = {part} × 100 ÷ {percent} = {part * 100} ÷ {percent} = {number}"
        }
        return task

    def _generate_simple_percent_ratio(self):
        """Генерация задачи на нахождение процентного отношения"""
        number1 = random.choice([15, 20, 25, 30, 40, 50])
        number2 = random.choice([60, 75, 80, 100, 120, 150])

        percent = number1 / number2 * 100

        task = {
            "condition": f"Сколько процентов составляет число {number1} от числа {number2}?",
            "answer": round(percent, 1),
            "solution": f"{number1} ÷ {number2} × 100% = {number1 / number2:.3f} × 100% = {round(percent, 1)}%"
        }
        return task

    def _generate_simple_price_change(self):
        """Генерация задачи на изменение цены"""
        old_price = random.choice([500, 800, 1200, 1500, 2000, 2500])
        new_price = old_price + random.choice([50, 75, 100, 150, 200])

        percent_change = (new_price - old_price) / old_price * 100

        task = {
            "condition": f"Цена товара повысилась с {old_price} рублей до {new_price} рублей. На сколько процентов повысилась цена?",
            "answer": round(percent_change, 1),
            "solution": f"Повышение: {new_price} - {old_price} = {new_price - old_price} руб.\nПроцент повышения: {new_price - old_price} ÷ {old_price} × 100% = {round(percent_change, 1)}%"
        }
        return task

    def _generate_simple_discount(self):
        """Генерация задачи на скидку"""
        price = random.choice([600, 750, 900, 1200, 1500, 1800])
        discount_percent = random.choice([5, 10, 15, 20, 25])

        discount = price * discount_percent / 100
        new_price = price - discount

        task = {
            "condition": f"Товар стоит {price} рублей. На него действует скидка {discount_percent}%. Сколько рублей составит скидка? Какова новая цена товара? Ответ дайте в формате: 'скидка: X руб, новая цена: Y руб'",
            "answer": f"скидка: {discount} руб, новая цена: {new_price} руб",
            "solution": f"Скидка: {price} × {discount_percent} ÷ 100 = {discount} руб.\nНовая цена: {price} - {discount} = {new_price} руб."
        }
        return task

    # ========== МЕТОДЫ ГЕНЕРАЦИИ СРЕДНИХ ЗАДАЧ ==========

    def _generate_medium_percentage_increase_decrease(self):
        """Генерация задачи на увеличение/уменьшение числа на процент"""
        number = random.choice([200, 300, 400, 500, 600])
        percent = random.choice([10, 15, 20, 25, 30])
        operation = random.choice(["увеличили", "уменьшили"])

        if operation == "увеличили":
            result = number * (1 + percent / 100)
            solution_op = f"{number} × (1 + {percent}/100) = {number} × 1.{percent} = {result}"
        else:
            result = number * (1 - percent / 100)
            solution_op = f"{number} × (1 - {percent}/100) = {number} × 0.{100 - percent if percent < 100 else 0} = {result}"

        task = {
            "condition": f"Число {number} {operation} на {percent}%. Какое число получилось?",
            "answer": round(result, 2),
            "solution": solution_op
        }
        return task

    def _generate_medium_percentage_of_remainder(self):
        """Генерация задачи на процент от остатка"""
        total = random.choice([400, 500, 600, 700, 800])
        first_percent = random.choice([20, 25, 30, 40])
        second_percent = random.choice([20, 25, 30, 40, 50])

        first_part = total * first_percent / 100
        remainder = total - first_part
        second_part = remainder * second_percent / 100

        task = {
            "condition": f"Число {total} сначала уменьшили на {first_percent}%, а затем от полученного остатка взяли {second_percent}%. Сколько получилось в итоге?",
            "answer": round(second_part, 2),
            "solution": f"1) {first_percent}% от {total} = {first_part}\n2) Остаток: {total} - {first_part} = {remainder}\n3) {second_percent}% от {remainder} = {second_part}"
        }
        return task

    def _generate_medium_consecutive_changes(self):
        """Генерация задачи на последовательные изменения"""
        price = random.choice([1000, 1500, 2000, 2500, 3000])
        first_change = random.choice([-20, -15, -10, 10, 15, 20])
        second_change = random.choice([-10, -5, 5, 10, 15])

        result = price
        changes_desc = []

        if first_change > 0:
            result *= (1 + first_change / 100)
            changes_desc.append(f"повысили на {first_change}%")
        else:
            result *= (1 + first_change / 100)  # first_change отрицательный
            changes_desc.append(f"снизили на {abs(first_change)}%")

        if second_change > 0:
            result *= (1 + second_change / 100)
            changes_desc.append(f"повысили на {second_change}%")
        else:
            result *= (1 + second_change / 100)
            changes_desc.append(f"снизили на {abs(second_change)}%")

        overall_change = (result - price) / price * 100

        task = {
            "condition": f"Цена товара {price} рублей сначала {changes_desc[0]}, а затем {changes_desc[1]}. Сколько стал стоить товар? На сколько процентов изменилась цена в итоге? Ответ дайте в формате: 'цена: X руб, изменение: Y%'",
            "answer": f"цена: {round(result, 2)} руб, изменение: {round(overall_change, 1)}%",
            "solution": f"После первого изменения: {price} → {price * (1 + first_change / 100)} руб.\nПосле второго изменения: → {result} руб.\nОбщее изменение: {round(overall_change, 1)}%"
        }
        return task

    def _generate_medium_reverse_percentage(self):
        """Генерация задачи на нахождение исходного числа после изменения"""
        final = random.choice([850, 1020, 1260, 1440, 1710])
        percent = random.choice([15, 20, 25, 30])
        operation = random.choice(["увеличили", "уменьшили"])

        if operation == "увеличили":
            # final = original * (1 + percent/100)
            original = final / (1 + percent / 100)
            op_desc = f"увеличили на {percent}%"
        else:
            # final = original * (1 - percent/100)
            original = final / (1 - percent / 100)
            op_desc = f"уменьшили на {percent}%"

        task = {
            "condition": f"Число {op_desc} и получили {final}. Найдите исходное число.",
            "answer": round(original, 2),
            "solution": f"Пусть x - исходное число.\nx × (1 {'+' if operation == 'увеличили' else '-'} {percent}/100) = {final}\nx = {final} ÷ {1 + percent / 100 if operation == 'увеличили' else 1 - percent / 100} = {round(original, 2)}"
        }
        return task

    def _generate_medium_percentage_comparison(self):
        """Генерация задачи на сравнение в процентах"""
        a = random.choice([80, 120, 150, 180, 200])
        b = random.choice([100, 150, 200, 240, 300])

        percent_a_less = (b - a) / b * 100
        percent_b_more = (b - a) / a * 100

        task = {
            "condition": f"Число A = {a}, число B = {b}. На сколько процентов A меньше B? На сколько процентов B больше A? Ответ дайте в формате: 'A меньше B на X%, B больше A на Y%'",
            "answer": f"A меньше B на {round(percent_a_less, 1)}%, B больше A на {round(percent_b_more, 1)}%",
            "solution": f"Разница: {b} - {a} = {b - a}\nA меньше B на: {b - a} ÷ {b} × 100% = {round(percent_a_less, 1)}%\nB больше A на: {b - a} ÷ {a} × 100% = {round(percent_b_more, 1)}%"
        }
        return task

    # ========== МЕТОДЫ ГЕНЕРАЦИИ СЛОЖНЫХ ЗАДАЧ ==========

    def _generate_hard_complex_percentage(self):
        """Генерация сложной задачи с несколькими процентными изменениями"""
        price = 100
        changes = []
        for _ in range(random.randint(3, 4)):
            change = random.choice([-25, -20, -15, -10, 10, 15, 20, 25])
            changes.append(change)

        result = price
        changes_desc = []
        for change in changes:
            if change > 0:
                result *= (1 + change / 100)
                changes_desc.append(f"повысили на {change}%")
            else:
                result *= (1 + change / 100)
                changes_desc.append(f"снизили на {abs(change)}%")

        overall_change = (result - price) / price * 100

        condition = f"Цену товара "
        for i, desc in enumerate(changes_desc):
            if i == 0:
                condition += desc
            elif i == len(changes_desc) - 1:
                condition += f" и затем {desc}"
            else:
                condition += f", затем {desc}"
        condition += ". Как и на сколько процентов изменилась цена по сравнению с первоначальной?"

        # Строим решение
        solution_parts = ["Пусть первоначальная цена = 100"]
        current = 100
        for i, change in enumerate(changes):
            current = current * (1 + change / 100)
            solution_parts.append(f"После {i + 1}-го изменения: → {round(current, 2)}")

        solution = "\n".join(solution_parts) + f"\nИтоговое изменение: {round(overall_change, 1)}%"

        task = {
            "condition": condition,
            "answer": round(overall_change, 1),
            "solution": solution
        }
        return task

    def _generate_hard_mixture_problem(self):
        """Генерация задачи на смеси и сплавы"""
        volume1 = random.choice([2, 3, 4, 5])
        percent1 = random.choice([10, 15, 20, 25, 30])
        volume2 = random.choice([3, 4, 5, 6])
        percent2 = random.choice([40, 45, 50, 55, 60])

        total_volume = volume1 + volume2
        substance = volume1 * percent1 / 100 + volume2 * percent2 / 100
        result_percent = substance / total_volume * 100

        task = {
            "condition": f"Смешали {volume1} л {percent1}% раствора соли и {volume2} л {percent2}% раствора соли. Сколько процентов соли содержит полученный раствор?",
            "answer": round(result_percent, 1),
            "solution": f"Соль в 1-м растворе: {volume1} × {percent1}% = {volume1 * percent1 / 100} л\nСоль во 2-м растворе: {volume2} × {percent2}% = {volume2 * percent2 / 100} л\nВсего соли: {volume1 * percent1 / 100 + volume2 * percent2 / 100} л\nОбщий объем: {volume1} + {volume2} = {total_volume} л\nКонцентрация: {substance} / {total_volume} × 100% = {round(result_percent, 1)}%"
        }
        return task

    def _generate_hard_fraction_percentage(self):
        """Генерация задачи с дробями и процентами"""
        fraction = random.choice(["1/2", "1/3", "2/3", "1/4", "3/4", "2/5", "3/5"])
        num, den = map(int, fraction.split('/'))

        # Увеличим числитель на процент
        percent_increase = random.choice([10, 20, 25, 30, 40, 50])
        new_num = num * (1 + percent_increase / 100)

        # На сколько нужно уменьшить знаменатель, чтобы дробь увеличилась вдвое
        # Исходная дробь: num/den
        # Новая дробь: (new_num)/(new_den) = 2 * (num/den)
        # new_den = new_num * den / (2 * num)
        new_den = new_num * den / (2 * num)
        decrease_percent = (den - new_den) / den * 100

        task = {
            "condition": f"Числитель дроби {fraction} увеличили на {percent_increase}%. На сколько процентов нужно уменьшить её знаменатель, чтобы дробь увеличилась вдвое?",
            "answer": round(decrease_percent, 1),
            "solution": f"Исходная дробь: {num}/{den}\nНовый числитель: {num} × (1 + {percent_increase}/100) = {new_num}\nНовая дробь должна быть: 2 × {num}/{den} = {2 * num}/{den}\nНовый знаменатель: {new_num} ÷ ({2 * num}/{den}) = {new_num} × {den} / {2 * num} = {new_den}\nУменьшение знаменателя: {den} → {new_den}, что на {den - new_den} меньше\nПроцент уменьшения: {den - new_den} / {den} × 100% = {round(decrease_percent, 1)}%"
        }
        return task

    def _generate_hard_multiple_percentages(self):
        """Генерация задачи с несколькими процентными соотношениями"""
        total = random.choice([500, 600, 700, 800, 900, 1000])
        percent1 = random.choice([20, 25, 30, 35, 40])
        percent2 = random.choice([10, 15, 20, 25])
        percent3 = random.choice([5, 8, 10, 12, 15])

        part1 = total * percent1 / 100
        part2 = total * percent2 / 100
        part3 = total * percent3 / 100
        remainder = total - part1 - part2 - part3

        condition = f"Из суммы в {total} рублей потратили {percent1}% на книги, {percent2}% на канцтовары и {percent3}% на транспорт. Сколько рублей осталось?"

        task = {
            "condition": condition,
            "answer": round(remainder, 2),
            "solution": f"На книги: {total} × {percent1}% = {part1} руб.\nНа канцтовары: {total} × {percent2}% = {part2} руб.\nНа транспорт: {total} × {percent3}% = {part3} руб.\nВсего потрачено: {part1} + {part2} + {part3} = {part1 + part2 + part3} руб.\nОсталось: {total} - {part1 + part2 + part3} = {remainder} руб."
        }
        return task

    def _generate_hard_bank_interest(self):
        """Генерация задачи на банковские проценты"""
        deposit = random.choice([10000, 15000, 20000, 25000, 30000])
        rate = random.choice([8, 9, 10, 11, 12])
        years = random.randint(2, 4)

        # Простые проценты
        simple = deposit * (1 + rate * years / 100)

        # Сложные проценты
        compound = deposit * (1 + rate / 100) ** years

        task = {
            "condition": f"Вкладчик положил в банк {deposit} рублей под {rate}% годовых. Какая сумма будет на счету через {years} года при начислении простых процентов? А при начислении сложных процентов? Ответ дайте в формате: 'простые: X руб, сложные: Y руб'",
            "answer": f"простые: {round(simple, 2)} руб, сложные: {round(compound, 2)} руб",
            "solution": f"Простые проценты: {deposit} × (1 + {rate}% × {years}) = {deposit} × (1 + {rate * years / 100}) = {round(simple, 2)} руб.\nСложные проценты: {deposit} × (1 + {rate}/100)^{years} = {deposit} × {round((1 + rate / 100) ** years, 4)} = {round(compound, 2)} руб."
        }
        return task

    def _generate_hard_percentage_equation(self):
        """Генерация задачи, требующей составления уравнения"""
        total = random.choice([200, 250, 300, 350, 400])
        percent_x = random.choice([20, 25, 30, 35, 40])
        percent_y = random.choice([50, 55, 60, 65, 70])

        # Случай 1: Нахождение чисел по их процентному содержанию
        if random.choice([True, False]):
            x = random.choice([80, 100, 120, 140, 160])
            y = total - x
            result = x * percent_x / 100 + y * percent_y / 100

            task = {
                "condition": f"Сумма двух чисел равна {total}. {percent_x}% первого числа и {percent_y}% второго числа вместе составляют {round(result, 1)}. Найдите эти числа. Ответ дайте в формате: 'первое: X, второе: Y'",
                "answer": f"первое: {x}, второе: {y}",
                "solution": f"Пусть первое число = x, тогда второе = {total} - x.\n{percent_x}% от x = {percent_x / 100}x\n{percent_y}% от ({total}-x) = {percent_y / 100}({total}-x)\nУравнение: {percent_x / 100}x + {percent_y / 100}({total}-x) = {round(result, 1)}\nРешая, получаем x = {x}, второе = {total} - {x} = {y}"
            }
        else:
            # Случай 2: Изменение числа на процент
            number = random.choice([80, 100, 120, 140])
            increase = random.choice([10, 15, 20, 25])
            decrease = random.choice([5, 8, 10, 12])

            # Увеличили на increase%, затем уменьшили на decrease%
            result = number * (1 + increase / 100) * (1 - decrease / 100)

            task = {
                "condition": f"Число увеличили на {increase}%, а затем полученное число уменьшили на {decrease}%. В результате получили {round(result, 2)}. Найдите исходное число.",
                "answer": number,
                "solution": f"Пусть x - исходное число.\nПосле увеличения: x × (1 + {increase}/100) = x × 1.{increase}\nПосле уменьшения: x × 1.{increase} × (1 - {decrease}/100) = x × 1.{increase} × 0.{100 - decrease} = {result}\nx = {result} ÷ (1.{increase} × 0.{100 - decrease}) = {number}"
            }
        return task

    def get_hint_for_task(self, task_type):
        """Возвращает подсказку для типа задачи"""
        hints = {
            "simple_percent_of_number": "💡 *Подсказка:* Чтобы найти процент от числа, нужно число умножить на процент и разделить на 100.",
            "simple_number_by_percent": "💡 *Подсказка:* Чтобы найти число по его проценту, нужно данное число умножить на 100 и разделить на процент.",
            "simple_percent_ratio": "💡 *Подсказка:* Чтобы найти, сколько процентов одно число составляет от другого, нужно первое число разделить на второе и умножить на 100%.",
            "simple_price_change": "💡 *Подсказка:* Найдите абсолютное изменение, затем разделите на первоначальную величину и умножьте на 100%.",
            "simple_discount": "💡 *Подсказка:* Скидка = цена × процент скидки ÷ 100. Новая цена = старая цена - скидка.",
            "medium_percentage_increase_decrease": "💡 *Подсказка:* При увеличении на p% число умножается на (1 + p/100). При уменьшении - на (1 - p/100).",
            "medium_percentage_of_remainder": "💡 *Подсказка:* Выполняйте действия последовательно. Сначала найдите первое изменение, затем от остатка - второе.",
            "medium_consecutive_changes": "💡 *Подсказка:* При последовательных изменениях нельзя просто складывать проценты. Нужно перемножать коэффициенты (1 ± p/100).",
            "medium_reverse_percentage": "💡 *Подсказка:* Если число увеличили на p% и получили B, то исходное число = B ÷ (1 + p/100).",
            "medium_percentage_comparison": "💡 *Подсказка:* Чтобы узнать, на сколько процентов одно число больше другого, нужно разность разделить на то число, с которым сравнивают.",
            "hard_complex_percentage": "💡 *Подсказка:* Обозначьте первоначальную цену за 100 и выполните последовательные действия. Конечный результат покажет изменение.",
            "hard_mixture_problem": "💡 *Подсказка:* Найдите массу вещества в каждом растворе, сложите, затем разделите на общий объем и умножьте на 100%.",
            "hard_fraction_percentage": "💡 *Подсказка:* Обозначьте исходную дробь как a/b. После изменений составьте уравнение и найдите новый знаменатель.",
            "hard_multiple_percentages": "💡 *Подсказка:* Сумма всех процентов должна быть 100%. Найдите, сколько процентов составляет остаток, затем найдите его величину.",
            "hard_bank_interest": "💡 *Подсказка:* Простые проценты: S = P × (1 + nr). Сложные проценты: S = P × (1 + r)^n.",
            "hard_percentage_equation": "💡 *Подсказка:* Обозначьте неизвестное за x и составьте уравнение по условию задачи."
        }

        return hints.get(task_type,
                         "💡 *Подсказка:* Внимательно прочитайте условие и определите, какие формулы нужно применить.")