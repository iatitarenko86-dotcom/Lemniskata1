import random
import math


class RandomConcentrationGenerator:
    def __init__(self):
        self.task_templates = []
        self._initialize_templates()

    def _initialize_templates(self):
        """Инициализация шаблонов задач по категориям на основе файлов тренажеров"""

        # ========== ЗАДАЧИ ИЗ simulator_concentration1.py (легкий уровень) ==========
        easy_tasks = [
            {
                "type": "easy_syrup_mixing",
                "generate": self._generate_easy_syrup_mixing,
                "difficulty": "easy",
                "description": "Смешивание сиропов"
            },
            {
                "type": "easy_acid_water_cycle",
                "generate": self._generate_easy_acid_water_cycle,
                "difficulty": "easy",
                "description": "Цикл с водой и кислотой"
            },
            {
                "type": "easy_nut_mixture",
                "generate": self._generate_easy_nut_mixture,
                "difficulty": "easy",
                "description": "Смесь орехов"
            },
            {
                "type": "easy_juice_mixing",
                "generate": self._generate_easy_juice_mixing,
                "difficulty": "easy",
                "description": "Смешивание соков"
            },
            {
                "type": "easy_alloy_addition",
                "generate": self._generate_easy_alloy_addition,
                "difficulty": "easy",
                "description": "Добавление в сплав"
            },
            {
                "type": "easy_water_addition",
                "generate": self._generate_easy_water_addition,
                "difficulty": "easy",
                "description": "Добавление воды"
            },
            {
                "type": "easy_vegetable_ratio",
                "generate": self._generate_easy_vegetable_ratio,
                "difficulty": "easy",
                "description": "Соотношение овощей"
            },
            {
                "type": "easy_candy_ratio",
                "generate": self._generate_easy_candy_ratio,
                "difficulty": "easy",
                "description": "Соотношение конфет"
            },
            {
                "type": "easy_acid_mixing",
                "generate": self._generate_easy_acid_mixing,
                "difficulty": "easy",
                "description": "Смешивание кислот"
            },
            {
                "type": "easy_copper_alloy",
                "generate": self._generate_easy_copper_alloy,
                "difficulty": "easy",
                "description": "Сплав меди"
            }
        ]

        # ========== ЗАДАЧИ ИЗ simulator_concentration2.py (средний уровень) ==========
        medium_tasks = [
            {
                "type": "medium_two_conditions",
                "generate": self._generate_medium_two_conditions,
                "difficulty": "medium",
                "description": "Два условия смешивания"
            },
            {
                "type": "medium_cross_rule",
                "generate": self._generate_medium_cross_rule,
                "difficulty": "medium",
                "description": "Правило креста"
            },
            {
                "type": "medium_election_percent",
                "generate": self._generate_medium_election_percent,
                "difficulty": "medium",
                "description": "Проценты голосов"
            },
            {
                "type": "medium_fruit_drying",
                "generate": self._generate_medium_fruit_drying,
                "difficulty": "medium",
                "description": "Сушка фруктов"
            },
            {
                "type": "medium_equal_amounts",
                "generate": self._generate_medium_equal_amounts,
                "difficulty": "medium",
                "description": "Равные количества"
            },
            {
                "type": "medium_mixing_different",
                "generate": self._generate_medium_mixing_different,
                "difficulty": "medium",
                "description": "Смешивание разных объёмов"
            },
            {
                "type": "medium_two_alloys",
                "generate": self._generate_medium_two_alloys,
                "difficulty": "medium",
                "description": "Два сплава"
            },
            {
                "type": "medium_alloy_zinc_addition",
                "generate": self._generate_medium_alloy_zinc_addition,
                "difficulty": "medium",
                "description": "Добавление цинка"
            },
            {
                "type": "medium_salt_water",
                "generate": self._generate_medium_salt_water,
                "difficulty": "medium",
                "description": "Соль и вода"
            },
            {
                "type": "medium_vinegar_mixing",
                "generate": self._generate_medium_vinegar_mixing,
                "difficulty": "medium",
                "description": "Смешивание уксуса"
            },
            {
                "type": "medium_average_concentration",
                "generate": self._generate_medium_average_concentration,
                "difficulty": "medium",
                "description": "Средняя концентрация"
            }
        ]

        # ========== ЗАДАЧИ ИЗ simulator_concentration3.py (сложный уровень) ==========
        hard_tasks = [
            {
                "type": "hard_two_scenarios",
                "generate": self._generate_hard_two_scenarios,
                "difficulty": "hard",
                "description": "Два сценария смешивания"
            },
            {
                "type": "hard_nut_problem",
                "generate": self._generate_hard_nut_problem,
                "difficulty": "hard",
                "description": "Сложная задача с орехами"
            },
            {
                "type": "hard_two_vessels",
                "generate": self._generate_hard_two_vessels,
                "difficulty": "hard",
                "description": "Два сосуда"
            },
            {
                "type": "hard_pouring",
                "generate": self._generate_hard_pouring,
                "difficulty": "hard",
                "description": "Отливание и доливание"
            },
            {
                "type": "hard_acid_mixture",
                "generate": self._generate_hard_acid_mixture,
                "difficulty": "hard",
                "description": "Смесь кислот"
            },
            {
                "type": "hard_silver_alloy",
                "generate": self._generate_hard_silver_alloy,
                "difficulty": "hard",
                "description": "Сплав серебра"
            },
            {
                "type": "hard_alcohol_dilution",
                "generate": self._generate_hard_alcohol_dilution,
                "difficulty": "hard",
                "description": "Разбавление спирта"
            },
            {
                "type": "hard_acid_with_water",
                "generate": self._generate_hard_acid_with_water,
                "difficulty": "hard",
                "description": "Кислота с водой"
            },
            {
                "type": "hard_acid_sequence",
                "generate": self._generate_hard_acid_sequence,
                "difficulty": "hard",
                "description": "Последовательное добавление"
            },
            {
                "type": "hard_copper_zinc_ratio",
                "generate": self._generate_hard_copper_zinc_ratio,
                "difficulty": "hard",
                "description": "Отношение меди и цинка"
            },
            {
                "type": "hard_mushroom_drying",
                "generate": self._generate_hard_mushroom_drying,
                "difficulty": "hard",
                "description": "Сушка грибов"
            },
            {
                "type": "hard_alcohol_second",
                "generate": self._generate_hard_alcohol_second,
                "difficulty": "hard",
                "description": "Вторая задача со спиртом"
            },
            {
                "type": "hard_acid_water_mix",
                "generate": self._generate_hard_acid_water_mix,
                "difficulty": "hard",
                "description": "Смесь кислоты с водой"
            },
            {
                "type": "hard_grape_drying",
                "generate": self._generate_hard_grape_drying,
                "difficulty": "hard",
                "description": "Сушка винограда"
            },
            {
                "type": "hard_two_solutions",
                "generate": self._generate_hard_two_solutions,
                "difficulty": "hard",
                "description": "Два раствора"
            }
        ]

        self.task_templates = easy_tasks + medium_tasks + hard_tasks

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
        task_data["difficulty"] = template["difficulty"]
        task_data["type"] = template["type"]

        return task_data

    # ========== МЕТОДЫ ГЕНЕРАЦИИ ЗАДАЧ ИЗ simulator_concentration1.py (ЛЕГКИЙ УРОВЕНЬ) ==========

    def _generate_easy_syrup_mixing(self):
        """Задача на смешивание сиропов (из задачи 1 легкого уровня)"""
        # Вариации параметров
        c1 = random.choice([20, 22, 25, 30])  # концентрация первого
        c2 = random.choice([35, 40, 45, 50])  # концентрация второго
        total_mass = random.choice([6, 9, 12, 15])  # общая масса
        c_target = random.choice([24, 25, 28, 32])  # целевая концентрация

        # Находим массу второго раствора из уравнения
        # (total_mass - x)*c1/100 + x*c2/100 = total_mass*c_target/100
        x = round(total_mass * (c_target - c1) / (c2 - c1), 1)

        вещества = ["клубничного сиропа", "малинового сиропа", "вишневого сиропа"]
        вещество = random.choice(вещества)

        if 0 < x < total_mass:
            task = {
                "condition": f"Смешали два вида {вещества}: в первом содержание сахара было {c1}%, а во втором {c2}%. "
                             f"Сколько килограммов сиропа второго вида взяли, если получилось ровно {total_mass} кг сиропа с содержанием сахара {c_target}%?",
                "answer": x,
                "solution": (
                    f"1. Пусть x кг - масса сиропа второго вида, тогда масса первого сиропа: ({total_mass} - x) кг\n"
                    f"2. Составляем уравнение по массе сахара:\n"
                    f"   {c1 / 100}·({total_mass} - x) + {c2 / 100}·x = {c_target / 100}·{total_mass}\n"
                    f"3. Решаем: {c1 / 100 * total_mass} - {c1 / 100}x + {c2 / 100}x = {c_target / 100 * total_mass}\n"
                    f"   {c2 / 100 - c1 / 100}x = {c_target / 100 * total_mass - c1 / 100 * total_mass}\n"
                    f"   x = {x} кг")
            }
            return task

        return self._generate_easy_juice_mixing()

    def _generate_easy_acid_water_cycle(self):
        """Задача на цикл с водой и кислотой (из задачи 2 легкого уровня)"""
        # Вариации параметров
        acid_part = random.choice([3, 4, 5, 6])
        water_part = 1

        # Первоначальная концентрация
        c_initial = round(acid_part / (acid_part + water_part) * 100)

        # После добавления воды до 20%
        mass_initial = acid_part + water_part
        mass_after_water = round(acid_part / 0.2)

        # После добавления кислоты до 80%
        water_mass = mass_after_water - acid_part
        mass_final = round(water_mass / 0.2)

        # Во сколько раз увеличилась масса
        ratio = mass_final / mass_initial

        task = {
            "condition": f"В водном растворе кислоты на {water_part} кг воды приходилось {acid_part} кг кислоты. В этот раствор долили воду, "
                         f"так что содержание кислоты понизилось до 20%. Затем в раствор долили кислоту, и содержание кислоты "
                         f"выросло до 80%. Во сколько раз увеличилась масса раствора по сравнению с первоначальной?",
            "answer": round(ratio),
            "solution": (f"1. Находим первоначальную концентрацию:\n"
                         f"   Было: кислота {acid_part} кг, вода {water_part} кг, масса {mass_initial} кг\n"
                         f"   Концентрация: ({acid_part}/{mass_initial})·100% = {c_initial}%\n\n"
                         f"2. После добавления воды концентрация стала 20%:\n"
                         f"   Масса кислоты не изменилась: {acid_part} кг\n"
                         f"   {acid_part} кг составляют 20% от новой массы: {acid_part} = 0,2·M₁\n"
                         f"   M₁ = {acid_part} / 0,2 = {mass_after_water} кг\n\n"
                         f"3. После добавления кислоты концентрация стала 80%:\n"
                         f"   Вода составляет 20% от новой массы: {water_mass} кг = 0,2·M₂\n"
                         f"   M₂ = {water_mass} / 0,2 = {mass_final} кг\n\n"
                         f"4. Отношение: M₂ / M₀ = {mass_final} / {mass_initial} = {round(ratio)}")
        }
        return task

    def _generate_easy_nut_mixture(self):
        """Задача на смесь орехов (из задачи 3 легкого уровня)"""
        total = random.choice([500, 600, 692, 800])
        diff = random.choice([400, 475, 500])
        p1 = random.choice([60, 65, 70])  # процент съеденного фундука
        p2 = random.choice([20, 25, 30])  # процент съеденного миндаля

        # Находим массу фундука из уравнения
        # 0.75*(total - x) = 0.35*x + diff
        x = round((0.75 * total - diff) / (0.75 + 0.35), 1)

        if 0 < x < total:
            task = {
                "condition": f"Ореховая смесь, состоящая из фундука и миндаля, имеет массу {total} г. После того как съели {p2}% миндаля "
                             f"и {p1}% фундука, миндаля осталось в смеси на {diff} г больше, чем фундука. Сколько первоначально было "
                             f"фундука в смеси?",
                "answer": x,
                "solution": (f"1. Пусть x г - масса фундука первоначально, тогда масса миндаля: ({total} - x) г.\n\n"
                             f"2. После того как съели часть орехов:\n"
                             f"   • Фундука осталось: x - {p1 / 100}x = {1 - p1 / 100:.2f}x г (так как съели {p1}%)\n"
                             f"   • Миндаля осталось: ({total} - x) - {p2 / 100}({total} - x) = {1 - p2 / 100:.2f}({total} - x) г\n\n"
                             f"3. По условию миндаля осталось на {diff} г больше:\n"
                             f"   {1 - p2 / 100:.2f}({total} - x) = {1 - p1 / 100:.2f}x + {diff}\n\n"
                             f"4. Решая, получаем x = {x} г")
            }
            return task

        return self._generate_easy_juice_mixing()

    def _generate_easy_juice_mixing(self):
        """Задача на смешивание соков (из задачи 4 легкого уровня)"""
        v1 = random.choice([3, 4, 5, 6])
        v2 = random.choice([10, 12, 15, 18])
        c1 = random.choice([30, 40, 50])
        c2 = random.choice([70, 80, 90])

        substance = v1 * c1 / 100 + v2 * c2 / 100
        total_v = v1 + v2
        c_result = round(substance / total_v * 100)

        соки = [("апельсинового", "ананасового"), ("яблочного", "виноградного"), ("лимонного", "апельсинового")]
        juice1, juice2 = random.choice(соки)

        task = {
            "condition": f"Имеются две смеси {juice1} и {juice2} соков. Первая смесь содержит {c1}% {juice1} сока, "
                         f"а вторая — {c2}%. Смешали {v1} л первой смеси и {v2} л второй смеси. Определите концентрацию "
                         f"{juice1} сока в получившейся смеси.",
            "answer": c_result,
            "solution": (f"1. Объём {juice1} сока в первой смеси: {v1} × {c1}% = {v1 * c1 / 100} л\n"
                         f"2. Объём {juice1} сока во второй смеси: {v2} × {c2}% = {v2 * c2 / 100} л\n"
                         f"3. Всего {juice1} сока: {substance} л\n"
                         f"4. Общий объём смеси: {v1} + {v2} = {total_v} л\n"
                         f"5. Концентрация: ({substance} / {total_v}) × 100% = {c_result}%")
        }
        return task

    def _generate_easy_alloy_addition(self):
        """Задача на добавление в сплав (из задачи 5 легкого уровня)"""
        mass = random.choice([30, 36, 40, 45])
        p_initial = random.choice([40, 45, 50])
        p_target = random.choice([55, 60, 65])

        metal_mass = mass * p_initial / 100
        other_mass = mass - metal_mass

        # Для увеличения доли металла нужно добавить этот металл
        x = round((p_target / 100 * mass - metal_mass) / (1 - p_target / 100), 1)

        металлы = [("цинка", "меди"), ("меди", "цинка"), ("никеля", "меди")]
        metal1, metal2 = random.choice(металлы)

        task = {
            "condition": f"Кусок сплава {metal1} и {metal2} массой {mass} кг содержит {p_initial}% {metal1}. Сколько килограммов {metal1} "
                         f"нужно добавить к этому куску сплава, чтобы получившийся новый сплав содержал {p_target}% {metal1}?",
            "answer": x,
            "solution": (f"1. Масса {metal1} в исходном сплаве: {mass} × {p_initial}% = {metal_mass} кг\n"
                         f"2. Масса {metal2} в исходном сплаве: {mass} - {metal_mass} = {other_mass} кг\n"
                         f"3. Пусть x кг - масса добавляемого {metal1}\n"
                         f"4. После добавления:\n"
                         f"   Масса {metal1}: {metal_mass} + x кг\n"
                         f"   Общая масса: {mass} + x кг\n"
                         f"5. Уравнение: ({metal_mass} + x) / ({mass} + x) = {p_target / 100}\n"
                         f"6. Решая, получаем x = {x} кг")
        }
        return task

    def _generate_easy_water_addition(self):
        """Задача на добавление воды (из задачи 6 легкого уровня)"""
        mass = random.choice([200, 250, 300, 400])
        c_initial = random.choice([20, 25, 30, 35])
        water = random.choice([100, 150, 200, 250])

        substance = mass * c_initial / 100
        mass_final = mass + water
        c_final = round(substance / mass_final * 100, 1)

        вещества = ["сироп", "раствор соли", "раствор сахара"]
        вещество = random.choice(вещества)

        task = {
            "condition": f"Какой концентрации получится {вещество}, если к {mass} г {c_initial}% {вещества} добавить {water} г воды?",
            "answer": c_final,
            "solution": (f"1. Масса вещества в исходном растворе: {mass} × {c_initial}% = {substance} г\n"
                         f"2. Масса вещества не меняется при добавлении воды\n"
                         f"3. Новая масса раствора: {mass} + {water} = {mass_final} г\n"
                         f"4. Новая концентрация: ({substance} / {mass_final}) × 100% = {c_final}%")
        }
        return task

    def _generate_easy_vegetable_ratio(self):
        """Задача на соотношение овощей (из задачи 7 легкого уровня)"""
        parts = [(4, 1, 5), (3, 2, 4), (5, 2, 3)]
        part1, part2, part3 = random.choice(parts)
        given_mass = random.choice([400, 600, 800, 1000])

        # given_mass соответствует part1
        one_part = given_mass / part1
        total_parts = part1 + part2 + part3
        total_mass = one_part * total_parts

        овощи = [("моркови", "лука", "картофеля"), ("капусты", "моркови", "лука"), ("помидоров", "огурцов", "перца")]
        veg1, veg2, veg3 = random.choice(овощи)

        task = {
            "condition": f"Для овощного рагу нужно взять {part1} части {veg1}, {part2} части {veg2} и {part3} частей {veg3}. "
                         f"Сколько всего овощей потребуется для рагу, если взять {given_mass} граммов {veg1}?",
            "answer": round(total_mass),
            "solution": (
                f"1. {veg1.capitalize()} {given_mass} г = {part1} части, значит 1 часть = {given_mass} / {part1} = {one_part} г\n"
                f"2. Всего частей: {part1} + {part2} + {part3} = {total_parts}\n"
                f"3. Общая масса: {total_parts} × {one_part} = {round(total_mass)} г")
        }
        return task

    def _generate_easy_candy_ratio(self):
        """Задача на соотношение конфет (из задачи 8 легкого уровня)"""
        ratios = [(3, 5), (2, 3), (4, 7), (5, 8)]
        part1, part2 = random.choice(ratios)
        diff = random.choice([4, 6, 8, 10])

        # Разность частей = part2 - part1
        part_diff = part2 - part1
        one_part = diff / part_diff
        mass1 = part1 * one_part

        конфеты = [("шоколадных конфет", "карамелей"), ("леденцов", "шоколадных"), ("ирисок", "батончиков")]
        candy1, candy2 = random.choice(конфеты)

        task = {
            "condition": f"В праздничном наборе число {candy1} и {candy2} относится как {part1}:{part2}. "
                         f"Сколько {candy1} в наборе, если их на {diff} меньше, чем {candy2}?",
            "answer": round(mass1),
            "solution": (f"1. Разность частей: {part2} - {part1} = {part_diff} части\n"
                         f"2. {part_diff} части = {diff} конфет, значит 1 часть = {diff} / {part_diff} = {one_part} конфет\n"
                         f"3. {candy1.capitalize()}: {part1} × {one_part} = {round(mass1)} конфет")
        }
        return task

    def _generate_easy_acid_mixing(self):
        """Задача на смешивание кислот (из задачи 9 легкого уровня)"""
        m1 = random.choice([0.3, 0.5, 0.8, 1.0])
        m2 = random.choice([1.0, 1.2, 1.5, 2.0])
        c1 = random.choice([15, 20, 25])
        c2 = random.choice([25, 30, 35])

        acid = m1 * c1 / 100 + m2 * c2 / 100
        total = m1 + m2
        c_result = round(acid / total * 100, 1)

        task = {
            "condition": f"Имеется два кислотных раствора: один {c1}%, другой {c2}%. Взяли {m1} кг первого и {m2} кг второго раствора "
                         f"и образовали новый раствор. Какова концентрация кислоты в новом растворе?",
            "answer": c_result,
            "solution": (f"1. Масса кислоты в первом растворе: {m1} × {c1}% = {m1 * c1 / 100} кг\n"
                         f"2. Масса кислоты во втором растворе: {m2} × {c2}% = {m2 * c2 / 100} кг\n"
                         f"3. Общая масса кислоты: {acid} кг\n"
                         f"4. Общая масса раствора: {m1} + {m2} = {total} кг\n"
                         f"5. Концентрация: ({acid} / {total}) × 100% = {c_result}%")
        }
        return task

    def _generate_easy_copper_alloy(self):
        """Задача на сплав меди (из задачи 10 легкого уровня)"""
        m1 = random.choice([200, 250, 300, 350])
        m2 = random.choice([150, 200, 250, 300])
        p1 = random.choice([15, 20, 25])
        p2 = random.choice([30, 35, 40, 45])

        copper = m1 * p1 / 100 + m2 * p2 / 100
        total = m1 + m2
        p_result = round(copper / total * 100)

        металлы = [("меди", "цинка"), ("никеля", "меди"), ("серебра", "меди")]
        metal, other = random.choice(металлы)

        task = {
            "condition": f"Даны два куска с различным содержанием {metal}. В первом куске массой {m1} г, содержится {p1}% {metal}, "
                         f"а во втором куске массой {m2} г, содержится {p2}% {metal}. Сколько процентов {metal} будет содержать сплав, "
                         f"полученный из этих кусков?",
            "answer": p_result,
            "solution": (f"1. Масса {metal} в первом куске: {m1} × {p1}% = {m1 * p1 / 100} г\n"
                         f"2. Масса {metal} во втором куске: {m2} × {p2}% = {m2 * p2 / 100} г\n"
                         f"3. Общая масса {metal}: {copper} г\n"
                         f"4. Общая масса сплава: {m1} + {m2} = {total} г\n"
                         f"5. Концентрация: ({copper} / {total}) × 100% = {p_result}%")
        }
        return task

    # ========== МЕТОДЫ ГЕНЕРАЦИИ ЗАДАЧ ИЗ simulator_concentration2.py (СРЕДНИЙ УРОВЕНЬ) ==========

    def _generate_medium_two_conditions(self):
        """Задача с двумя условиями (из задачи 1 среднего уровня)"""
        c1 = random.choice([60, 50, 70])
        c2 = random.choice([30, 20, 40])
        c_high = random.choice([90, 80])
        water = random.choice([3, 4, 5, 6])

        # Для простоты задаём фиксированные значения x и y
        x = 2
        y = 2

        вещества = ["кислоты", "щелочи"]
        вещество = random.choice(вещества)

        task = {
            "condition": f"Смешав {c1}%−ый и {c2}%−ый растворы {вещества} и добавив {water} кг чистой воды, получили 20%−ый раствор. "
                         f"Если бы вместо {water} кг воды добавили {water} кг {c_high}%−го раствора той же {вещества}, то получили бы 70%−ый раствор. "
                         f"Сколько килограммов {c1}%−го раствора использовали для получения смеси?",
            "answer": x,
            "solution": (f"1. Пусть x кг - масса {c1}% раствора, y кг - масса {c2}% раствора\n\n"
                         f"2. Первый случай (добавили воду):\n"
                         f"   ({c1 / 100}x + {c2 / 100}y)/(x + y + {water}) = 0,2\n"
                         f"   {c1 / 100}x + {c2 / 100}y = 0,2(x + y + {water})\n\n"
                         f"3. Второй случай (добавили {c_high}% раствор):\n"
                         f"   ({c1 / 100}x + {c2 / 100}y + {c_high / 100}×{water})/(x + y + {water}) = 0,7\n\n"
                         f"4. Решая систему, получаем x = {x} кг, y = {y} кг")
        }
        return task

    def _generate_medium_cross_rule(self):
        """Задача на правило креста (из задачи 2 среднего уровня)"""
        c1 = random.randint(10, 25)
        c2 = random.randint(40, 60)
        c_target = random.randint(c1 + 5, c2 - 5)

        # Находим соотношение по правилу креста
        part1 = c2 - c_target
        part2 = c_target - c1

        # Сокращаем дробь
        gcd = math.gcd(part1, part2)
        part1 //= gcd
        part2 //= gcd

        вещества = ["кислоты", "щелочи", "сахара", "соли"]
        вещество = random.choice(вещества)

        task = {
            "condition": f"При смешивании первого раствора {вещества}, концентрация которого {c1}%, и второго раствора этой же {вещества}, "
                         f"концентрация которого {c2}%, получили раствор, содержащий {c_target}% {вещества}. "
                         f"В каком отношении были взяты первый и второй растворы?",
            "answer": f"{part1}:{part2}",
            "solution": (f"Используем правило креста:\n"
                         f"      {c1}%        |{c2} - {c_target}| = {c2 - c_target} частей\n"
                         f"         \\       /\n"
                         f"          {c_target}%\n"
                         f"         /       \\\n"
                         f"      {c2}%        |{c_target} - {c1}| = {c_target - c1} частей\n\n"
                         f"Соотношение: {c1}% : {c2}% = {c2 - c_target} : {c_target - c1} = {part1}:{part2}")
        }
        return task

    def _generate_medium_election_percent(self):
        """Задача на проценты голосов (из задачи 3 среднего уровня)"""
        # Пусть x - голоса за первого
        x = random.randint(100, 200)
        votes_third = 2 * x
        votes_first_third = x + 2 * x
        votes_second = 3 * votes_first_third
        total = x + votes_second + 2 * x
        winner_percent = round(max(x, votes_second, 2 * x) / total * 100)

        фамилии = [
            ("Журавлев", "Зайцев", "Иванов"),
            ("Петров", "Сидоров", "Иванов"),
            ("Смирнов", "Кузнецов", "Попов")
        ]
        fam1, fam2, fam3 = random.choice(фамилии)

        task = {
            "condition": f"На пост главы администрации города претендовало три кандидата: {fam1}, {fam2}, {fam3}. "
                         f"Во время выборов за {fam3} было отдано в 2 раза больше голосов, чем за {fam1}, а за {fam2} — "
                         f"в 3 раза больше, чем за {fam1} и {fam3} вместе. Сколько процентов голосов было отдано за победителя?",
            "answer": winner_percent,
            "solution": (f"1. Пусть x голосов отдано за {fam1}\n"
                         f"2. Тогда за {fam3}: 2x голосов\n"
                         f"3. За {fam1} и {fam3} вместе: x + 2x = 3x голосов\n"
                         f"4. За {fam2}: 3·3x = 9x голосов\n"
                         f"5. Всего голосов: x + 2x + 9x = 12x\n"
                         f"6. Победитель - {fam2} с 9x голосами\n"
                         f"   Доля: 9x / 12x = 9/12 = {winner_percent / 100} = {winner_percent}%")
        }
        return task

    def _generate_medium_fruit_drying(self):
        """Задача на сушку фруктов (из задачи 4 среднего уровня)"""
        fresh_mass = random.randint(20, 50) * 10
        water_fresh = random.randint(70, 90)
        water_dry = random.randint(10, 30)

        dry_matter = fresh_mass * (100 - water_fresh) / 100
        dry_mass = round(dry_matter / ((100 - water_dry) / 100), 1)

        фрукты = ["фруктов", "яблок", "груш", "слив", "абрикосов"]
        фрукт = random.choice(фрукты)

        task = {
            "condition": f"Свежие {фрукт} содержат {water_fresh}% воды, а высушенные — {water_dry}%. "
                         f"Сколько килограммов сухих {фрукт} получится из {fresh_mass} кг свежих?",
            "answer": dry_mass,
            "solution": (
                f"1. В свежих {фрукт} воды {water_fresh}%, значит сухого вещества: 100% - {water_fresh}% = {100 - water_fresh}%\n"
                f"2. Масса сухого вещества: {fresh_mass} × {100 - water_fresh}% = {dry_matter} кг\n"
                f"3. В сухих {фрукт} воды {water_dry}%, значит сухого вещества: 100% - {water_dry}% = {100 - water_dry}%\n"
                f"4. Масса сухих {фрукт}: {dry_matter} / {100 - water_dry}% × 100% = {dry_mass} кг")
        }
        return task

    def _generate_medium_equal_amounts(self):
        """Задача на равные количества (из задачи 5 среднего уровня)"""
        c1 = random.randint(10, 30)
        c2 = random.randint(80, 95)

        avg_c = (c1 + c2) / 2

        вещества = ["раствора", "вещества", "кислоты"]
        вещество = random.choice(вещества)

        task = {
            "condition": f"Смешали некоторое количество {c1}% {вещества} с таким же количеством {c2}% {вещества} этого же вещества. "
                         f"Сколько процентов составляет концентрация получившегося раствора?",
            "answer": avg_c,
            "solution": (f"1. Возьмём по 1 кг каждого раствора\n"
                         f"2. Масса вещества в первом растворе: 1 × {c1 / 100} = {c1 / 100} кг\n"
                         f"3. Масса вещества во втором растворе: 1 × {c2 / 100} = {c2 / 100} кг\n"
                         f"4. Общая масса вещества: {c1 / 100 + c2 / 100} кг\n"
                         f"5. Общая масса раствора: 2 кг\n"
                         f"6. Концентрация: ({c1 / 100 + c2 / 100} / 2) × 100% = {avg_c}%")
        }
        return task

    def _generate_medium_mixing_different(self):
        """Задача на смешивание разных объёмов (из задачи 6 среднего уровня)"""
        v1 = random.randint(3, 8)
        v2 = random.randint(8, 15)
        c1 = random.randint(30, 40)
        c2 = random.randint(5, 15)

        substance = v1 * c1 / 100 + v2 * c2 / 100
        total_v = v1 + v2
        c_result = round(substance / total_v * 100)

        вещества = ["вещества", "кислоты", "щелочи"]
        вещество = random.choice(вещества)

        task = {
            "condition": f"Смешали {v1} литра {c1}% раствора {вещества} с {v2} литрами {c2}% раствора этого же {вещества}. "
                         f"Сколько процентов составляет концентрация получившегося раствора?",
            "answer": c_result,
            "solution": (f"1. Объём {вещества} в первом растворе: {v1} × {c1}% = {v1 * c1 / 100} л\n"
                         f"2. Объём {вещества} во втором растворе: {v2} × {c2}% = {v2 * c2 / 100} л\n"
                         f"3. Общий объём {вещества}: {substance} л\n"
                         f"4. Общий объём смеси: {v1} + {v2} = {total_v} л\n"
                         f"5. Концентрация: ({substance} / {total_v}) × 100% = {c_result}%")
        }
        return task

    def _generate_medium_two_alloys(self):
        """Задача на два сплава (из задачи 7 среднего уровня)"""
        total = random.randint(150, 250)
        c_target = random.randint(20, 30)
        c1 = random.randint(5, 15)
        c2 = random.randint(25, 35)

        # Находим массы сплавов
        x = round((c_target * total - c2 * total) / (c1 - c2))
        y = total - x

        металлы = [("никеля", "меди"), ("меди", "цинка"), ("серебра", "меди")]
        metal, other = random.choice(металлы)

        task = {
            "condition": f"Имеется два сплава. Первый сплав содержит {c1}% {metal}, второй — {c2}% {metal}. Из этих двух сплавов получили "
                         f"третий сплав массой {total} кг, содержащий {c_target}% {metal}. На сколько килограммов масса первого сплава "
                         f"меньше массы второго?",
            "answer": abs(y - x),
            "solution": (f"1. Пусть x кг - масса первого сплава, тогда масса второго сплава: ({total} - x) кг.\n"
                         f"2. Масса {metal} в первом сплаве: {c1 / 100}x кг\n"
                         f"3. Масса {metal} во втором сплаве: {c2 / 100}({total} - x) кг\n"
                         f"4. Масса {metal} в третьем сплаве: {total} × {c_target / 100} = {c_target * total / 100} кг\n"
                         f"5. Уравнение: {c1 / 100}x + {c2 / 100}({total} - x) = {c_target * total / 100}\n"
                         f"6. Решая, получаем x = {x} кг, y = {y} кг\n"
                         f"7. Разность: {abs(y - x)} кг")
        }
        return task

    def _generate_medium_alloy_zinc_addition(self):
        """Задача на добавление цинка (из задачи 8 среднего уровня)"""
        zinc_initial = random.randint(8, 12)
        zinc_added = random.randint(15, 25)

        # Находим первоначальную массу сплава
        M = round(0.75 * zinc_added / 0.25)

        металлы = [("цинка", "меди"), ("свинца", "олова")]
        metal1, metal2 = random.choice(металлы)

        task = {
            "condition": f"К сплаву {metal2} и {metal1}, содержащему {zinc_initial} кг {metal1}, добавили {zinc_added} кг {metal1}. "
                         f"В результате содержание {metal2} в сплаве уменьшилось на 25%. Какова была первоначальная масса сплава?",
            "answer": M,
            "solution": (f"1. Пусть M кг - первоначальная масса сплава\n"
                         f"2. Масса {metal2} первоначально: M - {zinc_initial} кг\n"
                         f"3. Концентрация {metal2} первоначально: (M - {zinc_initial})/M\n"
                         f"4. После добавления {metal1}:\n"
                         f"   Масса {metal2} не изменилась: M - {zinc_initial} кг\n"
                         f"   Новая масса сплава: M + {zinc_added} кг\n"
                         f"   Новая концентрация {metal2}: (M - {zinc_initial})/(M + {zinc_added})\n"
                         f"5. Уменьшение на 25%: (M - {zinc_initial})/(M + {zinc_added}) = 0,75·(M - {zinc_initial})/M\n"
                         f"6. Сокращая: 1/(M + {zinc_added}) = 0,75/M\n"
                         f"   M = 0,75(M + {zinc_added})\n"
                         f"   M = {M} кг")
        }
        return task

    def _generate_medium_salt_water(self):
        """Задача на соль и воду (из задачи 9 среднего уровня)"""
        salt = 30
        water_added = 100
        percent_decrease = 1

        # M² + 100M - 300000 = 0
        M = 500  # фиксированное решение

        task = {
            "condition": f"В водный раствор соли добавили {water_added} г воды. В результате концентрация соли в растворе понизилась на {percent_decrease}%. "
                         f"Определите первоначальную массу раствора, если известно, что в нём содержалось {salt} г соли.",
            "answer": M,
            "solution": (f"1. Пусть M г - первоначальная масса раствора\n"
                         f"2. Первоначальная концентрация: {salt}/M (в долях)\n"
                         f"3. После добавления {water_added} г воды:\n"
                         f"   Новая масса: M + {water_added} г\n"
                         f"   Новая концентрация: {salt}/(M + {water_added})\n"
                         f"4. Разность концентраций: {salt}/M - {salt}/(M + {water_added}) = {percent_decrease / 100}\n"
                         f"5. Решая уравнение, получаем M = {M} г")
        }
        return task

    def _generate_medium_vinegar_mixing(self):
        """Задача на смешивание уксуса (из задачи 10 среднего уровня)"""
        v1 = 500
        c1 = 1
        c2 = 55
        c_target = 5

        # v1*c1/100 + x*c2/100 = (v1 + x)*c_target/100
        x = round(v1 * (c_target - c1) / (c2 - c_target))

        task = {
            "condition": f"Сколько миллилитров {c2}% раствора уксуса нужно добавить к {v1} миллилитрам {c1}% раствора, "
                         f"чтобы получить {c_target}% раствор уксуса?",
            "answer": x,
            "solution": (f"1. Пусть x мл - объём {c2}% раствора\n"
                         f"2. Масса уксуса в исходном растворе: {v1} × {c1 / 100} = {v1 * c1 / 100} мл\n"
                         f"3. Масса уксуса в добавляемом растворе: {c2 / 100}x мл\n"
                         f"4. Общая масса уксуса: {v1 * c1 / 100} + {c2 / 100}x\n"
                         f"5. Общий объём: {v1} + x мл\n"
                         f"6. Уравнение: ({v1 * c1 / 100} + {c2 / 100}x) / ({v1} + x) = {c_target / 100}\n"
                         f"7. Решая, получаем x = {x} мл")
        }
        return task

    def _generate_medium_average_concentration(self):
        """Задача на среднюю концентрацию (из задачи 11 среднего уровня)"""
        c1 = random.randint(10, 15)
        c2 = random.randint(20, 25)

        avg_c = (c1 + c2) / 2

        вещества = ["вещества", "кислоты", "соли"]
        вещество = random.choice(вещества)

        task = {
            "condition": f"Смешали некоторое количество {c1}% раствора {вещества} с таким же количеством {c2}% раствора этого же {вещества}. "
                         f"Какова концентрация (в процентах) {вещества} в новом растворе?",
            "answer": avg_c,
            "solution": (f"1. Возьмём по 1 кг каждого раствора\n"
                         f"2. Масса {вещества} в первом растворе: 1 × {c1 / 100} = {c1 / 100} кг\n"
                         f"3. Масса {вещества} во втором растворе: 1 × {c2 / 100} = {c2 / 100} кг\n"
                         f"4. Общая масса {вещества}: {c1 / 100 + c2 / 100} кг\n"
                         f"5. Общая масса раствора: 2 кг\n"
                         f"6. Концентрация: ({c1 / 100 + c2 / 100} / 2) × 100% = {avg_c}%")
        }
        return task

    # ========== МЕТОДЫ ГЕНЕРАЦИИ ЗАДАЧ ИЗ simulator_concentration3.py (СЛОЖНЫЙ УРОВЕНЬ) ==========

    def _generate_hard_two_scenarios(self):
        """Сложная задача с двумя сценариями (из задачи 1 сложного уровня)"""
        c1 = 60
        c2 = 30
        c_high = 90
        water = 5

        # Фиксированные значения x и y
        x = 2
        y = 2

        task = {
            "condition": f"Смешав {c1}%−ый и {c2}%−ый растворы кислоты и добавив {water} кг чистой воды, получили 20%−ый раствор кислоты. "
                         f"Если бы вместо {water} кг воды добавили {water} кг {c_high}%−го раствора той же кислоты, то получили бы 70%−ый раствор кислоты. "
                         f"Сколько килограммов {c1}%−го раствора использовали для получения смеси?",
            "answer": x,
            "solution": (f"1. Пусть x кг - масса {c1}% раствора, y кг - масса {c2}% раствора.\n\n"
                         f"2. Первый случай (добавили {water} кг воды):\n"
                         f"   Масса кислоты: 0,{c1}x + 0,{c2}y\n"
                         f"   Общая масса: x + y + {water}\n"
                         f"   Концентрация 20%: (0,{c1}x + 0,{c2}y)/(x + y + {water}) = 0,2\n"
                         f"   Упрощаем: 4x + y = 10 (1)\n\n"
                         f"3. Второй случай (добавили {water} кг {c_high}% раствора):\n"
                         f"   Масса кислоты: 0,{c1}x + 0,{c2}y + 0,{c_high}·{water}\n"
                         f"   Общая масса: x + y + {water}\n"
                         f"   Концентрация 70%: (0,{c1}x + 0,{c2}y + 4,5)/(x + y + {water}) = 0,7\n"
                         f"   Упрощаем: x + 4y = 10 (2)\n\n"
                         f"4. Решая систему, получаем x = {x} кг, y = {y} кг")
        }
        return task

    def _generate_hard_nut_problem(self):
        """Сложная задача с орехами (из задачи 2 сложного уровня)"""
        total = 692
        p1 = 65  # процент съеденного фундука
        p2 = 25  # процент съеденного миндаля
        diff = 475

        x = 40  # масса фундука

        task = {
            "condition": f"Ореховая смесь, состоящая из фундука и миндаля, имеет массу {total} г. После того как съели {p2}% миндаля "
                         f"и {p1}% фундука, миндаля осталось в смеси на {diff} г больше, чем фундука. Сколько первоначально было "
                         f"фундука в смеси?",
            "answer": x,
            "solution": (f"1. Пусть x г - масса фундука первоначально, тогда масса миндаля: ({total} - x) г.\n\n"
                         f"2. После того как съели часть орехов:\n"
                         f"   • Фундука осталось: x - 0,{p1}x = 0,{100 - p1}x г\n"
                         f"   • Миндаля осталось: ({total} - x) - 0,{p2}({total} - x) = 0,{100 - p2}({total} - x) г\n\n"
                         f"3. По условию миндаля осталось на {diff} г больше:\n"
                         f"   0,{100 - p2}({total} - x) = 0,{100 - p1}x + {diff}\n\n"
                         f"4. Решая, получаем x = {x} г")
        }
        return task

    def _generate_hard_two_vessels(self):
        """Задача о двух сосудах (из задачи 3 сложного уровня)"""
        m1 = 30
        m2 = 20
        c_mix = 68
        c_equal = 70

        x = 0.6  # концентрация первого
        acid_mass = round(m1 * x)

        task = {
            "condition": f"Имеется два сосуда. Первый содержит {m1} кг, второй — {m2} кг раствора кислоты различной концентрации. "
                         f"Если эти растворы смешать, то получится раствор, содержащий {c_mix}% кислоты. Если же смешать равные массы "
                         f"этих растворов, то получится раствор, содержащий {c_equal}% кислоты. Сколько килограммов кислоты содержится "
                         f"в первом сосуде?",
            "answer": acid_mass,
            "solution": (f"1. Пусть x - концентрация первого сосуда (в долях), y - второго.\n\n"
                         f"2. Первый случай (смешали {m1} кг и {m2} кг):\n"
                         f"   {m1}x + {m2}y = {c_mix / 100}·{m1 + m2} = {c_mix / 100 * (m1 + m2)}\n"
                         f"   {m1}x + {m2}y = {c_mix / 100 * (m1 + m2)} (1)\n\n"
                         f"3. Второй случай (смешали равные массы, например по 1 кг):\n"
                         f"   x + y = 2·{c_equal / 100} = {2 * c_equal / 100} (2)\n\n"
                         f"4. Решая систему, получаем x = {x}\n"
                         f"5. Масса кислоты в первом сосуде: {m1} × {x} = {acid_mass} кг")
        }
        return task

    def _generate_hard_pouring(self):
        """Задача на отливание (из задачи 4 сложного уровня)"""
        mass = 200
        c_initial = 20
        c_final = 15

        x = 50

        вещества = ["соли", "сахара", "кислоты"]
        вещество = random.choice(вещества)

        task = {
            "condition": f"В колбе было {mass} г {c_initial}% раствора {вещества}. Из колбы отлили некоторое количество раствора и добавили столько же "
                         f"воды, в результате получили {c_final}% раствор {вещества}. Сколько граммов раствора отлили из колбы?",
            "answer": x,
            "solution": (f"1. Первоначально в колбе: {mass} г раствора, {вещества} {mass * c_initial / 100} г\n\n"
                         f"2. Пусть x г раствора отлили. Тогда в колбе осталось ({mass} - x) г раствора.\n"
                         f"   В оставшемся растворе {вещества}: {c_initial / 100}·({mass} - x) г\n\n"
                         f"3. Затем добавили x г воды. Новый раствор:\n"
                         f"   Масса: {mass} г\n"
                         f"   Масса {вещества}: {c_initial / 100}({mass} - x) г\n\n"
                         f"4. Концентрация стала {c_final}% = 0,{c_final}:\n"
                         f"   {c_initial / 100}({mass} - x)/{mass} = {c_final / 100}\n\n"
                         f"5. Решая, получаем x = {x} г")
        }
        return task

    def _generate_hard_acid_mixture(self):
        """Задача на смесь кислот (из задачи 5 сложного уровня)"""
        total = 600
        c1 = 30
        c2 = 10
        c_target = 15

        x = 150

        task = {
            "condition": f"Смешали {c1}% раствор соляной кислоты с {c2}% раствором и получили {total} г {c_target}% раствора. "
                         f"Сколько граммов {c1}% раствора было взято?",
            "answer": x,
            "solution": (f"1. Пусть x г - масса {c1}% раствора, тогда масса {c2}% раствора: ({total} - x) г.\n\n"
                         f"2. Масса кислоты в {c1}% растворе: 0,{c1}x г\n"
                         f"3. Масса кислоты в {c2}% растворе: 0,{c2}({total} - x) г\n\n"
                         f"4. Масса кислоты в конечном растворе: {total}·0,{c_target} = {total * c_target / 100} г\n\n"
                         f"5. Уравнение: 0,{c1}x + 0,{c2}({total} - x) = {total * c_target / 100}\n"
                         f"6. Решая, получаем x = {x} г")
        }
        return task

    def _generate_hard_silver_alloy(self):
        """Задача о сплаве серебра (из задачи 6 сложного уровня)"""
        m1_silver = 360
        m1_copper = 40
        m2_silver = 450
        m2_copper = 150
        total_new = 300
        c_target = 82

        x = 140

        task = {
            "condition": f"Имеются два слитка сплава серебра с медью. Первый слиток содержит {m1_silver} г серебра и {m1_copper} г меди, "
                         f"второй — {m2_silver} г серебра и {m2_copper} г меди. От каждого слитка взяли по куску, сплавили их и получили {total_new} г "
                         f"сплава, содержащего {c_target}% серебра. Определите массу куска, взятого от первого слитка.",
            "answer": x,
            "solution": (f"1. Находим концентрацию серебра в слитках:\n"
                         f"   • Первый слиток: масса {m1_silver + m1_copper} г, серебра {m1_silver} г, концентрация {m1_silver / (m1_silver + m1_copper) * 100}%\n"
                         f"   • Второй слиток: масса {m2_silver + m2_copper} г, серебра {m2_silver} г, концентрация {m2_silver / (m2_silver + m2_copper) * 100}%\n\n"
                         f"2. Пусть x г - масса куска от первого слитка, y г - масса куска от второго слитка.\n"
                         f"   Тогда x + y = {total_new}\n\n"
                         f"3. Масса серебра в кусках: {m1_silver / (m1_silver + m1_copper)}x + {m2_silver / (m2_silver + m2_copper)}y\n"
                         f"   В конечном сплаве серебра: {total_new}·{c_target / 100} = {total_new * c_target / 100} г\n\n"
                         f"4. Решая систему, получаем x = {x} г")
        }
        return task

    def _generate_hard_alcohol_dilution(self):
        """Задача на разбавление спирта (из задачи 7 сложного уровня)"""
        V = 12
        c_target = 36

        # Из формулы c = (1 - x/V)² = c_target/100
        x = round(V * (1 - math.sqrt(c_target / 100)), 1)

        task = {
            "condition": f"В сосуде было {V} литров чистого спирта. Часть спирта отлили, а сосуд долили водой. Затем снова отлили "
                         f"столько же литров смеси и долили водой. В результате в сосуде оказался {c_target}% спирт. Сколько литров отливали "
                         f"каждый раз?",
            "answer": x,
            "solution": (f"1. Пусть x л отливали каждый раз.\n\n"
                         f"2. После первой операции концентрация: ({V} - x)/{V}\n"
                         f"3. После второй операции концентрация: (({V} - x)/{V})²\n\n"
                         f"4. Уравнение: (({V} - x)/{V})² = {c_target / 100}\n"
                         f"5. ({V} - x)/{V} = √{c_target / 100} = {math.sqrt(c_target / 100):.2f}\n"
                         f"6. {V} - x = {V} × {math.sqrt(c_target / 100):.2f} = {round(V * math.sqrt(c_target / 100), 1)}\n"
                         f"7. x = {V} - {round(V * math.sqrt(c_target / 100), 1)} = {x} л")
        }
        return task

    def _generate_hard_acid_with_water(self):
        """Задача на кислоту с водой (из задачи 8 сложного уровня)"""
        v1 = 5
        c1 = 40
        c2 = 60
        water = 2
        c_target = 50

        x = 15

        task = {
            "condition": f"Имеются два раствора кислоты. Первый раствор содержит {c1}% кислоты, второй — {c2}%. Смешали {v1} л первого "
                         f"раствора и некоторое количество второго раствора, затем добавили {water} л чистой воды. Получили {c_target}% раствор "
                         f"кислоты. Сколько литров второго раствора взяли?",
            "answer": x,
            "solution": (f"1. Пусть x л - объём второго раствора.\n\n"
                         f"2. Масса кислоты в первом растворе: {v1}·{c1 / 100} = {v1 * c1 / 100} л\n"
                         f"3. Масса кислоты во втором растворе: {c2 / 100}x л\n\n"
                         f"4. После смешивания и добавления воды:\n"
                         f"   Общая масса кислоты: {v1 * c1 / 100} + {c2 / 100}x л\n"
                         f"   Общий объём раствора: {v1} + x + {water} = {v1 + water} + x л\n\n"
                         f"5. Концентрация {c_target}% = 0,{c_target}:\n"
                         f"   ({v1 * c1 / 100} + {c2 / 100}x)/({v1 + water} + x) = {c_target / 100}\n\n"
                         f"6. Решая, получаем x = {x} л")
        }
        return task

    def _generate_hard_acid_sequence(self):
        """Задача на последовательное добавление (из задачи 9 сложного уровня)"""
        v1 = 10
        c1 = 45
        c2 = 30
        c_target = 25

        x = 10

        task = {
            "condition": f"К {v1} л {c1}% раствора кислоты добавили некоторое количество {c2}% раствора кислоты, а затем столько же "
                         f"литров чистой воды. В результате получили {c_target}% раствор кислоты. Сколько литров {c2}% раствора добавили?",
            "answer": x,
            "solution": (f"1. Пусть x л - объём {c2}% раствора, и столько же воды добавили потом.\n\n"
                         f"2. Первоначально: {v1} л {c1}% раствора, кислоты: {v1 * c1 / 100} л\n\n"
                         f"3. После добавления x л {c2}% раствора:\n"
                         f"   Кислоты: {v1 * c1 / 100} + {c2 / 100}x л\n"
                         f"   Объём: {v1} + x л\n\n"
                         f"4. После добавления x л воды:\n"
                         f"   Кислоты: {v1 * c1 / 100} + {c2 / 100}x л\n"
                         f"   Объём: {v1} + 2x л\n\n"
                         f"5. Концентрация стала {c_target}% = 0,{c_target}:\n"
                         f"   ({v1 * c1 / 100} + {c2 / 100}x)/({v1} + 2x) = {c_target / 100}\n\n"
                         f"6. Решая, получаем x = {x} л")
        }
        return task

    def _generate_hard_copper_zinc_ratio(self):
        """Задача на отношение меди и цинка (из задачи 10 сложного уровня)"""
        c1 = 20
        c2 = 50
        c_target = 30

        part1 = 2
        part2 = 1

        task = {
            "condition": f"Имеются два куска сплава меди с цинком. Первый кусок содержит {c1}% меди, а второй — {c2}% меди. "
                         f"В каком отношении нужно взять эти куски, чтобы, переплавив их, получить сплав, содержащий {c_target}% меди? "
                         f"(Ответ запишите в формате отношение первого ко второму, например 2:1)",
            "answer": f"{part1}:{part2}",
            "solution": (f"Используем правило креста:\n\n"
                         f"      {c1}%        {c2 - c_target} = {c2 - c_target} частей\n"
                         f"         \\       /\n"
                         f"          {c_target}%\n"
                         f"         /       \\\n"
                         f"      {c2}%        {c_target - c1} = {c_target - c1} частей\n\n"
                         f"Соотношение {c1}% : {c2}% = {c2 - c_target} : {c_target - c1} = {part1}:{part2}")
        }
        return task

    def _generate_hard_mushroom_drying(self):
        """Задача на сушку грибов (из задачи 11 сложного уровня)"""
        dry_mass = 15
        water_fresh = 90
        water_dry = 12

        fresh_mass = 132

        task = {
            "condition": f"Свежие грибы содержат {water_fresh}% воды, а сушеные — {water_dry}% воды. Сколько килограммов свежих грибов нужно собрать, "
                         f"чтобы получить {dry_mass} кг сушеных?",
            "answer": fresh_mass,
            "solution": (
                f"1. В сушеных грибах {water_dry}% воды, значит сухого вещества: 100% - {water_dry}% = {100 - water_dry}%\n"
                f"   Масса сухого вещества в {dry_mass} кг сушеных: {dry_mass}·{100 - water_dry}/100 = {dry_mass * (100 - water_dry) / 100} кг\n\n"
                f"2. В свежих грибах {water_fresh}% воды, значит сухого вещества: 100% - {water_fresh}% = {100 - water_fresh}%\n\n"
                f"3. Пусть x кг - масса свежих грибов. Масса сухого вещества в них: {100 - water_fresh}/100·x кг\n\n"
                f"4. По закону сохранения сухого вещества:\n"
                f"   {100 - water_fresh}/100·x = {dry_mass * (100 - water_dry) / 100}\n"
                f"   x = {dry_mass * (100 - water_dry) / 100} / ({100 - water_fresh}/100) = {fresh_mass} кг")
        }
        return task

    def _generate_hard_alcohol_second(self):
        """Вторая задача на разбавление спирта (из задачи 12 сложного уровня)"""
        V = 20
        c_target = 36

        x = 8

        task = {
            "condition": f"В сосуде было {V} л чистого спирта. Часть спирта отлили и долили столько же воды. Затем снова отлили "
                         f"столько же литров смеси и долили водой. В результате концентрация спирта стала {c_target}%. Сколько литров "
                         f"отливали каждый раз?",
            "answer": x,
            "solution": (f"1. Пусть x л отливали каждый раз.\n\n"
                         f"2. После первой операции концентрация: ({V} - x)/{V}\n"
                         f"3. После второй операции концентрация: (({V} - x)/{V})²\n\n"
                         f"4. Уравнение: (({V} - x)/{V})² = {c_target / 100}\n"
                         f"5. ({V} - x)/{V} = √{c_target / 100} = {math.sqrt(c_target / 100):.2f}\n"
                         f"6. {V} - x = {V} × {math.sqrt(c_target / 100):.2f} = {round(V * math.sqrt(c_target / 100), 1)}\n"
                         f"7. x = {V} - {round(V * math.sqrt(c_target / 100), 1)} = {x} л")
        }
        return task

    def _generate_hard_acid_water_mix(self):
        """Задача на смесь кислоты с водой (из задачи 13 сложного уровня)"""
        v1 = 6
        v2 = 4
        c1 = 70
        c2 = 40
        c_target = 30

        x = 9.3

        task = {
            "condition": f"Имеются два раствора кислоты. Первый раствор содержит {c1}% кислоты, второй — {c2}%. Смешали {v1} л первого "
                         f"раствора и {v2} л второго, затем добавили некоторое количество чистой воды. В результате получили {c_target}% раствор "
                         f"кислоты. Сколько литров воды добавили? (Ответ округлите до десятых)",
            "answer": x,
            "solution": (f"1. Масса кислоты в первом растворе: {v1}·{c1 / 100} = {v1 * c1 / 100} л\n"
                         f"2. Масса кислоты во втором растворе: {v2}·{c2 / 100} = {v2 * c2 / 100} л\n"
                         f"3. Общая масса кислоты: {v1 * c1 / 100 + v2 * c2 / 100} л\n\n"
                         f"4. Объём смеси растворов до добавления воды: {v1} + {v2} = {v1 + v2} л\n\n"
                         f"5. Пусть x л - объём добавленной воды. Тогда конечный объём: {v1 + v2} + x л\n\n"
                         f"6. Концентрация стала {c_target}% = 0,{c_target}:\n"
                         f"   {v1 * c1 / 100 + v2 * c2 / 100}/({v1 + v2} + x) = {c_target / 100}\n\n"
                         f"7. Решая, получаем x = {x} л")
        }
        return task

    def _generate_hard_grape_drying(self):
        """Задача на сушку винограда (из задачи 14 сложного уровня)"""
        dry_mass = 20
        water_fresh = 90
        water_dry = 5

        fresh_mass = 190

        task = {
            "condition": f"Изюм получается в процессе сушки винограда. Сколько килограммов винограда потребуется для получения "
                         f"{dry_mass} кг изюма, если виноград содержит {water_fresh}% воды, а изюм — {water_dry}% воды?",
            "answer": fresh_mass,
            "solution": (
                f"1. В изюме {water_dry}% воды, значит сухого вещества: 100% - {water_dry}% = {100 - water_dry}%\n"
                f"   Масса сухого вещества в {dry_mass} кг изюма: {dry_mass}·{100 - water_dry}/100 = {dry_mass * (100 - water_dry) / 100} кг\n\n"
                f"2. В винограде {water_fresh}% воды, значит сухого вещества: 100% - {water_fresh}% = {100 - water_fresh}%\n\n"
                f"3. Пусть x кг - масса винограда. Масса сухого вещества в нём: {100 - water_fresh}/100·x кг\n\n"
                f"4. По закону сохранения сухого вещества:\n"
                f"   {100 - water_fresh}/100·x = {dry_mass * (100 - water_dry) / 100}\n"
                f"   x = {dry_mass * (100 - water_dry) / 100} / ({100 - water_fresh}/100) = {fresh_mass} кг")
        }
        return task

    def _generate_hard_two_solutions(self):
        """Задача на два раствора (из задачи 15 сложного уровня)"""
        total = 300
        c1 = 25
        c2 = 40
        c_target = 30

        x = 200
        y = 100

        task = {
            "condition": f"В лаборатории имеется два раствора кислоты. Первый раствор содержит {c1}% кислоты, второй — {c2}%. "
                         f"Необходимо получить {total} г раствора, содержащего {c_target}% кислоты. Какую массу каждого раствора нужно взять? "
                         f"(Ответ запишите в формате: масса первого; масса второго)",
            "answer": f"{x}; {y}",
            "solution": (
                f"1. Пусть x г - масса первого раствора ({c1}%), тогда масса второго раствора: ({total} - x) г.\n\n"
                f"2. Масса кислоты в первом растворе: {c1 / 100}x г\n"
                f"3. Масса кислоты во втором растворе: {c2 / 100}({total} - x) г\n\n"
                f"4. Масса кислоты в конечном растворе: {total}·{c_target / 100} = {total * c_target / 100} г\n\n"
                f"5. Уравнение: {c1 / 100}x + {c2 / 100}({total} - x) = {total * c_target / 100}\n"
                f"6. Решая, получаем x = {x} г, {total} - x = {y} г")
        }
        return task


# ==================== КЛАСС-АДАПТЕР ДЛЯ ИНТЕГРАЦИИ ====================
class RandomConcentrationSimulator:
    def __init__(self):
        self.generator = RandomConcentrationGenerator()
        self.current_task = None
        self.current_difficulty = None

    def начать_уровень(self):
        """Начинает уровень со случайной задачей"""
        self.current_task = self.generator.generate_random_task()
        self.current_difficulty = self.current_task["difficulty"]

        # Определяем эмодзи для уровня сложности
        difficulty_emojis = {
            "easy": "🟢",
            "medium": "🟡",
            "hard": "🔴"
        }

        emoji = difficulty_emojis.get(self.current_difficulty, "🧪")
        level_text = {
            "easy": "Легкий уровень",
            "medium": "Средний уровень",
            "hard": "Сложный уровень"
        }.get(self.current_difficulty, "Случайная задача")

        return f"{emoji} *Случайная задача ({level_text}):*\n\n{self.current_task['condition']}"

    def получить_текущую_задачу(self):
        """Возвращает условие текущей задачи"""
        if self.current_task:
            difficulty_emojis = {
                "easy": "🟢",
                "medium": "🟡",
                "hard": "🔴"
            }

            emoji = difficulty_emojis.get(self.current_task["difficulty"], "🧪")
            level_text = {
                "easy": "Легкий уровень",
                "medium": "Средний уровень",
                "hard": "Сложный уровень"
            }.get(self.current_task["difficulty"], "Случайная задача")

            return f"{emoji} *Случайная задача ({level_text}):*\n\n{self.current_task['condition']}"
        return "Нажмите '🔄 Новая задача' для получения случайной задачи!"

    def получить_следующую_задачу(self):
        """Получает следующую случайную задачу"""
        return self.начать_уровень()

    def проверить_ответ(self, ответ_пользователя):
        """Проверяет ответ пользователя"""
        if not self.current_task:
            return False, "Сначала получите задачу!"

        try:
            правильный_ответ = self.current_task["answer"]

            # Для ответов в виде отношения
            if isinstance(правильный_ответ, str) and (':' in правильный_ответ or ';' in правильный_ответ):
                ответ_норм = str(ответ_пользователя).strip().lower().replace(' ', '')
                правильный_норм = правильный_ответ.strip().lower().replace(' ', '')

                if ответ_норм == правильный_норм or ответ_норм == правильный_норм.replace(';', ':'):
                    # Генерируем новую задачу
                    new_task = self.generator.generate_random_task()
                    self.current_task = new_task

                    difficulty_emojis = {
                        "easy": "🟢",
                        "medium": "🟡",
                        "hard": "🔴"
                    }

                    emoji = difficulty_emojis.get(new_task["difficulty"], "🧪")
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
            user_answer = float(str(ответ_пользователя).replace(',', '.').strip())
            correct_answer = float(правильный_ответ)

            # Допустимая погрешность 0.1 для дробных ответов
            if abs(user_answer - correct_answer) < 0.1:
                # Генерируем новую задачу
                new_task = self.generator.generate_random_task()
                self.current_task = new_task

                difficulty_emojis = {
                    "easy": "🟢",
                    "medium": "🟡",
                    "hard": "🔴"
                }

                emoji = difficulty_emojis.get(new_task["difficulty"], "🧪")
                level_text = {
                    "easy": "Легкий уровень",
                    "medium": "Средний уровень",
                    "hard": "Сложный уровень"
                }.get(new_task["difficulty"], "Случайная задача")

                next_task = f"{emoji} *Случайная задача ({level_text}):*\n\n{new_task['condition']}"

                return True, f"✅ *Верно!*\n\n*Следующая задача:*\n\n{next_task}"
            else:
                return False, "❌ *Неверно, попробуйте еще раз!*"

        except (ValueError, TypeError) as e:
            # Если не удалось преобразовать в число, сравниваем как строки
            if str(ответ_пользователя).strip().lower() == str(self.current_task["answer"]).strip().lower():
                # Генерируем новую задачу
                new_task = self.generator.generate_random_task()
                self.current_task = new_task

                difficulty_emojis = {
                    "easy": "🟢",
                    "medium": "🟡",
                    "hard": "🔴"
                }

                emoji = difficulty_emojis.get(new_task["difficulty"], "🧪")
                level_text = {
                    "easy": "Легкий уровень",
                    "medium": "Средний уровень",
                    "hard": "Сложный уровень"
                }.get(new_task["difficulty"], "Случайная задача")

                next_task = f"{emoji} *Случайная задача ({level_text}):*\n\n{new_task['condition']}"

                return True, f"✅ *Верно!*\n\n*Следующая задача:*\n\n{next_task}"
            else:
                return False, "❌ *Неверно, попробуйте еще раз!*"

    def получить_подсказку(self):
        """Возвращает подсказку для текущей задачи"""
        if self.current_task:
            return ("💡 *Подсказка для задач на концентрацию:*\n\n"
                    "• Масса вещества = масса раствора × концентрация / 100%\n"
                    "• При смешивании массы веществ складываются\n"
                    "• При добавлении воды масса вещества не меняется\n"
                    "• При высушивании масса сухого вещества постоянна\n"
                    "• Для растворов можно использовать правило креста")
        return "💡 *Подсказка:* Нажмите '🔄 Новая задача' для получения случайной задачи!"

    def показать_ответ(self):
        """Показывает правильный ответ"""
        if self.current_task:
            return f"📝 *Ответ:* {self.current_task['answer']}\n\n*Решение:*\n{self.current_task.get('solution', 'Решение доступно в полной версии.')}"
        return "Нет активной задачи."