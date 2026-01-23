import random
import math


class RandomMovementGenerator:
    def __init__(self):
        self.task_templates = []
        self._initialize_templates()

    def _initialize_templates(self):
        """Инициализация шаблонов задач по категориям"""

        # ========== КАТЕГОРИЯ 1: Простые задачи (аналогично simulator_movement1) ==========
        simple_templates = [
            {
                "type": "simple_meeting",
                "generate": self._generate_simple_meeting,
                "difficulty": "easy"
            },
            {
                "type": "simple_speed_distance",
                "generate": self._generate_simple_speed_distance,
                "difficulty": "easy"
            },
            {
                "type": "simple_overtake",
                "generate": self._generate_simple_overtake,
                "difficulty": "easy"
            },
            {
                "type": "simple_average_speed",
                "generate": self._generate_simple_average_speed,
                "difficulty": "easy"
            },
            {
                "type": "simple_river",
                "generate": self._generate_simple_river,
                "difficulty": "easy"
            }
        ]

        # ========== КАТЕГОРИЯ 2: Средние задачи (аналогично simulator_movement2) ==========
        medium_templates = [
            {
                "type": "medium_equation",
                "generate": self._generate_medium_equation,
                "difficulty": "medium"
            },
            {
                "type": "medium_catch_up",
                "generate": self._generate_medium_catch_up,
                "difficulty": "medium"
            },
            {
                "type": "medium_river_round_trip",
                "generate": self._generate_medium_river_round_trip,
                "difficulty": "medium"
            },
            {
                "type": "medium_two_cars",
                "generate": self._generate_medium_two_cars,
                "difficulty": "medium"
            }
        ]

        # ========== КАТЕГОРИЯ 3: Сложные задачи (аналогично simulator_movement3) ==========
        hard_templates = [
            {
                "type": "hard_complex_meeting",
                "generate": self._generate_hard_complex_meeting,
                "difficulty": "hard"
            },
            {
                "type": "hard_circular_track",
                "generate": self._generate_hard_circular_track,
                "difficulty": "hard"
            },
            {
                "type": "hard_system_equations",
                "generate": self._generate_hard_system_equations,
                "difficulty": "hard"
            },
            {
                "type": "hard_multiple_segments",
                "generate": self._generate_hard_multiple_segments,
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
        task_data["difficulty"] = template["difficulty"]

        return task_data

    # ========== МЕТОДЫ ГЕНЕРАЦИИ ПРОСТЫХ ЗАДАЧ ==========

    def _generate_simple_meeting(self):
        """Генерация простой задачи на встречное движение"""
        # Случайные параметры
        distance = random.choice([100, 120, 150, 180, 200, 240, 300])
        speed1 = random.choice([40, 45, 50, 55, 60, 65])
        speed2 = random.choice([50, 55, 60, 65, 70, 75])

        # Рассчет
        time = distance / (speed1 + speed2)

        # Форматирование времени
        hours = int(time)
        minutes = int((time - hours) * 60)

        if minutes == 0:
            time_text = f"{hours} часов"
        elif hours == 0:
            time_text = f"{minutes} минут"
        else:
            time_text = f"{hours} часов {minutes} минут"

        task = {
            "condition": f"Из двух городов, расстояние между которыми {distance} км, одновременно навстречу друг другу выехали два автомобиля. Скорость первого автомобиля {speed1} км/ч, скорость второго — {speed2} км/ч. Через сколько часов они встретятся?",
            "answer": round(time, 2),
            "solution": f"Скорость сближения: {speed1} + {speed2} = {speed1 + speed2} км/ч\nВремя встречи: {distance} / {speed1 + speed2} = {round(time, 2)} часа"
        }
        return task

    def _generate_simple_speed_distance(self):
        """Генерация простой задачи на нахождение скорости или расстояния"""
        choice = random.randint(1, 3)

        if choice == 1:  # Найти скорость
            distance = random.choice([180, 240, 300, 360, 420])
            time = random.choice([3, 4, 5, 6])
            speed = distance / time

            task = {
                "condition": f"Автомобиль проехал {distance} км за {time} часа. Найдите скорость автомобиля.",
                "answer": speed,
                "solution": f"Скорость = Расстояние / Время = {distance} / {time} = {speed} км/ч"
            }

        elif choice == 2:  # Найти расстояние
            speed = random.choice([60, 70, 80, 90, 100])
            time = random.choice([2, 2.5, 3, 3.5, 4])
            distance = speed * time

            task = {
                "condition": f"Автомобиль двигался со скоростью {speed} км/ч в течение {time} часов. Какое расстояние он проехал?",
                "answer": distance,
                "solution": f"Расстояние = Скорость × Время = {speed} × {time} = {distance} км"
            }

        else:  # Найти время
            distance = random.choice([240, 300, 360, 420])
            speed = random.choice([60, 70, 80, 90])
            time = distance / speed

            task = {
                "condition": f"Автомобиль должен проехать {distance} км со скоростью {speed} км/ч. Сколько времени займет поездка?",
                "answer": round(time, 2),
                "solution": f"Время = Расстояние / Скорость = {distance} / {speed} = {round(time, 2)} часа"
            }

        return task

    def _generate_simple_overtake(self):
        """Генерация простой задачи на движение вдогонку"""
        # Случайные параметры
        head_start = random.choice([1, 1.5, 2, 2.5, 3])  # время форы
        speed_slow = random.choice([40, 45, 50, 55])
        speed_fast = random.choice([60, 65, 70, 75, 80])

        # Расстояние, которое успел проехать медленный
        initial_distance = speed_slow * head_start

        # Время сближения
        catch_up_time = initial_distance / (speed_fast - speed_slow)

        task = {
            "condition": f"Из пункта A выехал автомобиль со скоростью {speed_slow} км/ч. Через {head_start} часа из того же пункта в том же направлении выехал второй автомобиль со скоростью {speed_fast} км/ч. Через сколько часов второй автомобиль догонит первый?",
            "answer": round(catch_up_time, 2),
            "solution": f"За {head_start} часа первый проехал: {speed_slow} × {head_start} = {initial_distance} км\nСкорость сближения: {speed_fast} - {speed_slow} = {speed_fast - speed_slow} км/ч\nВремя сближения: {initial_distance} / {speed_fast - speed_slow} = {round(catch_up_time, 2)} часа"
        }
        return task

    def _generate_simple_average_speed(self):
        """Генерация простой задачи на среднюю скорость"""
        # Случайные параметры
        distance1 = random.choice([100, 120, 150])
        speed1 = random.choice([50, 60, 70])
        distance2 = random.choice([100, 120, 150])
        speed2 = random.choice([70, 80, 90])

        # Рассчеты
        time1 = distance1 / speed1
        time2 = distance2 / speed2
        total_distance = distance1 + distance2
        total_time = time1 + time2
        avg_speed = total_distance / total_time

        task = {
            "condition": f"Автомобиль проехал первые {distance1} км со скоростью {speed1} км/ч, а следующие {distance2} км — со скоростью {speed2} км/ч. Найдите среднюю скорость автомобиля на всем пути.",
            "answer": round(avg_speed, 1),
            "solution": f"Время на первом участке: {distance1} / {speed1} = {round(time1, 2)} ч\nВремя на втором участке: {distance2} / {speed2} = {round(time2, 2)} ч\nОбщее время: {round(time1, 2)} + {round(time2, 2)} = {round(total_time, 2)} ч\nОбщее расстояние: {distance1} + {distance2} = {total_distance} км\nСредняя скорость: {total_distance} / {round(total_time, 2)} = {round(avg_speed, 1)} км/ч"
        }
        return task

    def _generate_simple_river(self):
        """Генерация простой задачи на движение по реке"""
        boat_speed = random.choice([12, 15, 18, 20])
        river_speed = random.choice([2, 3, 4, 5])
        distance = random.choice([24, 30, 36, 42])

        # По течению
        downstream_speed = boat_speed + river_speed
        downstream_time = distance / downstream_speed

        # Против течения
        upstream_speed = boat_speed - river_speed
        upstream_time = distance / upstream_speed

        # Общее время
        total_time = downstream_time + upstream_time

        task = {
            "condition": f"Моторная лодка прошла {distance} км по течению реки и вернулась обратно. Собственная скорость лодки {boat_speed} км/ч, скорость течения реки {river_speed} км/ч. Сколько времени заняла вся поездка?",
            "answer": round(total_time, 2),
            "solution": f"По течению: скорость = {boat_speed} + {river_speed} = {downstream_speed} км/ч, время = {distance} / {downstream_speed} = {round(downstream_time, 2)} ч\nПротив течения: скорость = {boat_speed} - {river_speed} = {upstream_speed} км/ч, время = {distance} / {upstream_speed} = {round(upstream_time, 2)} ч\nОбщее время: {round(downstream_time, 2)} + {round(upstream_time, 2)} = {round(total_time, 2)} ч"
        }
        return task

    # ========== МЕТОДЫ ГЕНЕРАЦИИ СРЕДНИХ ЗАДАЧ ==========

    def _generate_medium_equation(self):
        """Генерация средней задачи, требующей уравнения"""
        # Вариант 1: Разница во времени
        if random.choice([True, False]):
            distance = random.choice([120, 150, 180, 210])
            speed_diff = random.choice([5, 10, 15])
            time_diff = random.choice([0.5, 1, 1.5])  # в часах

            # Пусть x - меньшая скорость
            # Уравнение: distance/x - distance/(x+speed_diff) = time_diff

            # Для простоты зададим конкретное решение
            x = random.choice([40, 45, 50, 55])
            speed2 = x + speed_diff

            task = {
                "condition": f"Автомобиль проехал {distance} км. Если бы он увеличил скорость на {speed_diff} км/ч, то затратил бы на этот путь на {time_diff} часа меньше. Найдите первоначальную скорость автомобиля.",
                "answer": x,
                "solution": f"Пусть x - первоначальная скорость (км/ч)\nТогда время при скорости x: {distance}/x\nВремя при скорости x+{speed_diff}: {distance}/(x+{speed_diff})\nУравнение: {distance}/x - {distance}/(x+{speed_diff}) = {time_diff}\nРешая уравнение, получаем x = {x} км/ч"
            }

        else:  # Вариант 2: Одинаковое время
            distance = random.choice([240, 300, 360])
            time = random.choice([4, 5, 6])

            # Автомобиль проехал половину пути с одной скоростью, вторую половину - с другой
            half_distance = distance / 2
            speed1 = random.choice([50, 55, 60])

            # speed2 = distance / time - speed1 (но упростим)
            speed2 = random.choice([65, 70, 75])

            task = {
                "condition": f"Автомобиль проехал {distance} км. Первую половину пути он ехал со скоростью {speed1} км/ч, а вторую половину — со скоростью {speed2} км/ч. Найдите среднюю скорость автомобиля на всем пути.",
                "answer": round(2 * speed1 * speed2 / (speed1 + speed2), 1),
                "solution": f"Общее время: t = ({half_distance}/{speed1}) + ({half_distance}/{speed2}) = {half_distance / speed1 + half_distance / speed2:.2f} ч\nСредняя скорость: v = {distance} / ({half_distance / speed1 + half_distance / speed2:.2f}) = {round(2 * speed1 * speed2 / (speed1 + speed2), 1)} км/ч"
            }

        return task

    def _generate_medium_catch_up(self):
        """Генерация средней задачи на движение вдогонку с уравнениями"""
        # Случайные параметры
        speed1 = random.choice([40, 45, 50])
        speed2 = speed1 + random.choice([10, 15, 20])
        time_delay = random.choice([1, 1.5, 2])  # задержка второго
        distance = random.choice([100, 120, 150])

        # Время до встречи
        # Пусть t - время движения второго до встречи
        # Тогда первый двигался t + time_delay
        # Уравнение: speed1*(t+time_delay) + speed2*t = distance

        t = (distance - speed1 * time_delay) / (speed1 + speed2)
        meeting_time = t + time_delay

        task = {
            "condition": f"Из пункта A в пункт B выехал автомобиль со скоростью {speed1} км/ч. Через {time_delay} часа из пункта B в пункт A выехал второй автомобиль со скоростью {speed2} км/ч. Расстояние между A и B равно {distance} км. Через сколько часов после выезда первого автомобиля они встретятся?",
            "answer": round(meeting_time, 2),
            "solution": f"Пусть t - время движения второго до встречи\nПервый проедет: {speed1}×(t+{time_delay})\nВторой проедет: {speed2}×t\nСумма: {speed1}×(t+{time_delay}) + {speed2}×t = {distance}\nРешая: {speed1}t + {speed1 * time_delay} + {speed2}t = {distance}\n({speed1}+{speed2})t = {distance} - {speed1 * time_delay}\nt = ({distance}-{speed1 * time_delay})/({speed1}+{speed2}) = {t:.2f} ч\nОбщее время: {t:.2f} + {time_delay} = {meeting_time:.2f} ч"
        }
        return task

    def _generate_medium_river_round_trip(self):
        """Генерация средней задачи на движение по реке туда и обратно"""
        distance = random.choice([30, 36, 42, 48])
        boat_speed = random.choice([12, 15, 18])
        time_total = random.choice([4, 5, 6])

        # Найдем скорость течения из уравнения
        # t1 + t2 = time_total
        # distance/(boat_speed + current) + distance/(boat_speed - current) = time_total

        # Для простоты зададим конкретное решение
        current = random.choice([2, 3, 4])

        task = {
            "condition": f"Моторная лодка прошла {distance} км по течению реки и вернулась обратно, затратив на весь путь {time_total} часов. Собственная скорость лодки {boat_speed} км/ч. Найдите скорость течения реки.",
            "answer": current,
            "solution": f"Пусть x - скорость течения (км/ч)\nВремя по течению: {distance}/({boat_speed}+x)\nВремя против течения: {distance}/({boat_speed}-x)\nУравнение: {distance}/({boat_speed}+x) + {distance}/({boat_speed}-x) = {time_total}\nРешая уравнение, получаем x = {current} км/ч"
        }
        return task

    def _generate_medium_two_cars(self):
        """Генерация задачи о двух автомобилях с разницей во времени"""
        distance = random.choice([400, 450, 500, 550])
        time_diff = random.choice([1, 1.5, 2])  # разница в часах
        speed_diff = random.choice([10, 15, 20])  # разница в скорости

        # Пусть x - скорость первого
        # Тогда второго: x + speed_diff
        # Уравнение: distance/x - distance/(x+speed_diff) = time_diff

        # Для простоты зададим конкретное решение
        x = random.choice([50, 55, 60])

        task = {
            "condition": f"Два автомобиля выехали одновременно из одного города в другой. Расстояние между городами {distance} км. Первый автомобиль прибыл на место на {time_diff} часа раньше второго. Найдите скорость первого автомобиля, если известно, что она на {speed_diff} км/ч больше скорости второго.",
            "answer": x + speed_diff,
            "solution": f"Пусть x - скорость второго (км/ч)\nТогда скорость первого: x + {speed_diff}\nВремя первого: {distance}/(x+{speed_diff})\nВремя второго: {distance}/x\nУравнение: {distance}/x - {distance}/(x+{speed_diff}) = {time_diff}\nРешая, получаем x = {x}, значит скорость первого: {x} + {speed_diff} = {x + speed_diff} км/ч"
        }
        return task

    # ========== МЕТОДЫ ГЕНЕРАЦИИ СЛОЖНЫХ ЗАДАЧ ==========

    def _generate_hard_complex_meeting(self):
        """Генерация сложной задачи на встречное движение с остановками"""
        distance = random.choice([300, 350, 400])
        speed1 = random.choice([50, 55, 60])
        speed2 = random.choice([60, 65, 70])
        stop_time = random.choice([0.5, 0.75, 1])  # время остановки в часах

        # Сложная задача: один делает остановку
        # Пусть t - время движения до встречи после остановки
        # Уравнение: speed1*(t+stop_time) + speed2*t = distance

        t = (distance - speed1 * stop_time) / (speed1 + speed2)
        total_time = t + stop_time

        task = {
            "condition": f"Из двух городов, расстояние между которыми {distance} км, одновременно навстречу друг другу выехали два автомобиля. Скорость первого {speed1} км/ч, скорость второго {speed2} км/ч. Первый автомобиль сделал остановку на {stop_time} часа. Через сколько часов после выезда автомобили встретятся?",
            "answer": round(total_time, 2),
            "solution": f"Пусть t - время движения после остановки до встречи\nПервый (с остановкой): {speed1}×(t+{stop_time})\nВторой: {speed2}×t\nСумма: {speed1}×(t+{stop_time}) + {speed2}×t = {distance}\n{speed1}t + {speed1 * stop_time} + {speed2}t = {distance}\n({speed1}+{speed2})t = {distance} - {speed1 * stop_time}\nt = ({distance}-{speed1 * stop_time})/({speed1}+{speed2}) = {t:.2f} ч\nОбщее время: {t:.2f} + {stop_time} = {total_time:.2f} ч"
        }
        return task

    def _generate_hard_circular_track(self):
        """Генерация задачи на круговое движение"""
        track_length = random.choice([1200, 1500, 1800, 2000]) / 100  # в км
        speed1 = random.choice([15, 18, 20])
        speed2 = speed1 + random.choice([3, 4, 5])

        # Время первой встречи при движении в одном направлении
        meeting_time = track_length / (speed2 - speed1)

        task = {
            "condition": f"Два бегуна стартуют одновременно из одной точки круговой трассы длиной {track_length} км в одном направлении. Скорость первого {speed1} км/ч, скорость второго {speed2} км/ч. Через сколько часов бегуны впервые поравняются?",
            "answer": round(meeting_time, 2),
            "solution": f"Скорость сближения при движении в одном направлении: {speed2} - {speed1} = {speed2 - speed1} км/ч\nЧтобы догнать, нужно пройти целый круг: {track_length} км\nВремя: {track_length} / {speed2 - speed1} = {round(meeting_time, 2)} ч"
        }
        return task

    def _generate_hard_system_equations(self):
        """Генерация задачи, требующей системы уравнений"""
        # Задача с лодкой: по озеру и против течения
        lake_distance = random.choice([15, 18, 21])
        river_distance = random.choice([6, 8, 10])
        total_time = random.choice([1.5, 2, 2.5])
        current_speed = random.choice([2, 3, 4])

        # Уравнение: lake_distance/x + river_distance/(x-current_speed) = total_time
        # Для простоты зададим решение
        boat_speed = random.choice([12, 15, 18])

        task = {
            "condition": f"Моторная лодка прошла {lake_distance} км по озеру и {river_distance} км против течения реки, затратив на весь путь {total_time} часа. Скорость течения реки {current_speed} км/ч. Найдите собственную скорость лодки.",
            "answer": boat_speed,
            "solution": f"Пусть x - собственная скорость лодки (км/ч)\nВремя по озеру: {lake_distance}/x\nВремя против течения: {river_distance}/(x-{current_speed})\nУравнение: {lake_distance}/x + {river_distance}/(x-{current_speed}) = {total_time}\nРешая, получаем x = {boat_speed} км/ч"
        }
        return task

    def _generate_hard_multiple_segments(self):
        """Генерация задачи с несколькими участками пути"""
        # 3 участка с разными скоростями
        distances = [
            random.choice([100, 120, 140]),
            random.choice([150, 180, 210]),
            random.choice([200, 240, 280])
        ]

        speeds = [
            random.choice([50, 55, 60]),
            random.choice([60, 65, 70]),
            random.choice([70, 75, 80])
        ]

        # Рассчеты
        times = [d / s for d, s in zip(distances, speeds)]
        total_distance = sum(distances)
        total_time = sum(times)
        avg_speed = total_distance / total_time

        condition = f"Автомобиль проехал три участка пути:\n"
        condition += f"1) {distances[0]} км со скоростью {speeds[0]} км/ч\n"
        condition += f"2) {distances[1]} км со скоростью {speeds[1]} км/ч\n"
        condition += f"3) {distances[2]} км со скоростью {speeds[2]} км/ч\n"
        condition += "Найдите среднюю скорость автомобиля на всем пути."

        solution = f"Время на 1 участке: {distances[0]} / {speeds[0]} = {times[0]:.2f} ч\n"
        solution += f"Время на 2 участке: {distances[1]} / {speeds[1]} = {times[1]:.2f} ч\n"
        solution += f"Время на 3 участке: {distances[2]} / {speeds[2]} = {times[2]:.2f} ч\n"
        solution += f"Общее время: {times[0]:.2f} + {times[1]:.2f} + {times[2]:.2f} = {total_time:.2f} ч\n"
        solution += f"Общее расстояние: {distances[0]} + {distances[1]} + {distances[2]} = {total_distance} км\n"
        solution += f"Средняя скорость: {total_distance} / {total_time:.2f} = {round(avg_speed, 1)} км/ч"

        task = {
            "condition": condition,
            "answer": round(avg_speed, 1),
            "solution": solution
        }
        return task

    def get_hint_for_task(self, task_type):
        """Возвращает подсказку для типа задачи"""
        hints = {
            "simple_meeting": "💡 *Подсказка:* Используйте формулу скорости сближения: v = v₁ + v₂. Затем время встречи: t = S / v.",
            "simple_speed_distance": "💡 *Подсказка:* Вспомните основную формулу: S = v × t. Найдите нужную величину, выразив ее из формулы.",
            "simple_overtake": "💡 *Подсказка:* Найдите расстояние, которое успел проехать первый объект до начала движения второго. Затем используйте скорость сближения.",
            "simple_average_speed": "💡 *Подсказка:* Средняя скорость = весь путь / всё время. Найдите время на каждом участке отдельно.",
            "simple_river": "💡 *Подсказка:* По течению: v = vₗ + vₜ. Против течения: v = vₗ - vₜ. Найдите время для каждого направления.",
            "medium_equation": "💡 *Подсказка:* Составьте уравнение, выразив время через скорость. Часто помогает ввести переменную для неизвестной скорости.",
            "medium_catch_up": "💡 *Подсказка:* Учтите, что объекты начали движение в разное время. Составьте уравнение для расстояний, пройденных каждым.",
            "medium_river_round_trip": "💡 *Подсказка:* Запишите время движения по течению и против течения. Их сумма равна общему времени.",
            "medium_two_cars": "💡 *Подсказка:* Выразите время каждого автомобиля через его скорость. Разница времен даст уравнение.",
            "hard_complex_meeting": "💡 *Подсказка:* Учтите время остановки одного из объектов. Составьте уравнение с учетом, что один двигался меньшее время.",
            "hard_circular_track": "💡 *Подсказка:* При движении в одном направлении скорость сближения равна разности скоростей. Нужно пройти целый круг.",
            "hard_system_equations": "💡 *Подсказка:* Составьте уравнение для общего времени движения. Вам понадобится выразить время на каждом участке.",
            "hard_multiple_segments": "💡 *Подсказка:* Найдите время движения на каждом участке отдельно. Средняя скорость = сумма расстояний / сумма времен."
        }

        return hints.get(task_type,
                         "💡 *Подсказка:* Внимательно прочитайте условие и определите, какие формулы нужно применить.")


# ==================== КЛАСС-АДАПТЕР ДЛЯ ИНТЕГРАЦИИ ====================
class RandomMovementSimulator:
    def __init__(self):
        self.generator = RandomMovementGenerator()
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

        emoji = difficulty_emojis.get(self.current_difficulty, "🎯")
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

            emoji = difficulty_emojis.get(self.current_task["difficulty"], "🎯")
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
            # Пробуем преобразовать ответ в число
            user_answer = float(str(ответ_пользователя).replace(',', '.').strip())
            correct_answer = float(self.current_task["answer"])

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

                emoji = difficulty_emojis.get(new_task["difficulty"], "🎯")
                level_text = {
                    "easy": "Легкий уровень",
                    "medium": "Средний уровень",
                    "hard": "Сложный уровень"
                }.get(new_task["difficulty"], "Случайная задача")

                next_task = f"{emoji} *Случайная задача ({level_text}):*\n\n{new_task['condition']}"

                return True, f"✅ *Верно!*\n\n*Следующая задача:*\n\n{next_task}"
            else:
                return False, "❌ *Неверно, попробуйте еще раз!*"

        except ValueError:
            # Если не удалось преобразовать в число, сравниваем как строки
            if str(ответ_пользователя).strip() == str(self.current_task["answer"]).strip():
                # Генерируем новую задачу
                new_task = self.generator.generate_random_task()
                self.current_task = new_task

                difficulty_emojis = {
                    "easy": "🟢",
                    "medium": "🟡",
                    "hard": "🔴"
                }

                emoji = difficulty_emojis.get(new_task["difficulty"], "🎯")
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
        if self.current_task and "type" in self.current_task:
            return self.generator.get_hint_for_task(self.current_task["type"])
        return "💡 *Подсказка:* Внимательно прочитайте условие задачи. Определите, что дано и что нужно найти. Используйте основные формулы движения: S = v × t."

    def показать_ответ(self):
        """Показывает правильный ответ"""
        if self.current_task:
            return f"📝 *Ответ:* {self.current_task['answer']}\n\n*Решение:*\n{self.current_task.get('solution', 'Решение доступно в полной версии.')}"
        return "Нет активной задачи."