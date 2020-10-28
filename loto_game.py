from random import randint as ri


class Card:
    """
        Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
    расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
    --------------------------
        9 43 62          74 90
    2    27    75 78    82
       41 56 63     76      86
    --------------------------
    """
    card_rows = 3  # Количество строк в карточке
    card_cells = 9  # Количество клеток
    nums_in_row = 5  # Количество цифр в строке
    card = None  # По факту сама карточка
    space_mark = 0  # Метка для пробела между цифрами

    def __init__(self):

        # Запускаем генератор уникальных цифр и сохраняем полученный список
        uniques_numbers = self.numbers_generator(self.nums_in_row * self.card_rows, 1, 90)
        self.card = []
        for i in range(0, self.card_rows):
            # Сортируем числа в строке по возрастанию
            sort_num_in_rows = sorted(uniques_numbers[self.nums_in_row * i:self.nums_in_row * (i + 1)])
            # Указываем количество пробелов в строке и добавляем в случайное место на карточке
            empty_num_count = self.card_cells - self.nums_in_row
            for j in range(0, empty_num_count):
                index = ri(0, len(sort_num_in_rows))
                sort_num_in_rows.insert(index, self.space_mark)
            self.card += sort_num_in_rows

    def __str__(self):
        dotted_line = "--------------------------"
        line = dotted_line + "\n"
        for index, num in enumerate(self.card):
            # Если значение в списке равно нулю, то ставим двойной пробел
            if num == self.space_mark:
                line += "  "
            # Если значение меньше 10, то добавляем перед цифрой пробел
            elif num < 10:
                line += f" {str(num)}"
            else:
                line += str(num)

            if (index + 1) % self.card_cells == 0:
                line += "\n"
            else:
                line += " "
        return line + dotted_line

    def numbers_generator(self, count, min, max):
        """
        Функция для генерации уникальных случайных чисел в строке карточки
        count - сколько всего цифр должно быть создано для карточки (количество цифр в строке * количество строк)
        min - минимальное значение цифр
        max - максимальное значение цифр
        :return - возвращает список уникальных чисел
        """
        numbers = []
        # Пока длина списка меньше нужного количества цифр в карточке -> создаем цифры и проверяем на уникальность
        while len(numbers) < count:
            new_num = ri(min, max)
            if new_num not in numbers:
                numbers.append(new_num)
        return numbers


class GameSession():
    user_card = None

    def __init__(self):
        self.user_card = Card()
        self.computer_card = Card()
        self.barrels = Card.numbers_generator(Card(), 90, 1, 90)

    def play(self):
        barrel_number = self.barrels.pop()
        print(f"""
Новый бочонок: {barrel_number} (в мешке осталось {len(self.barrels)})
------ Карта игрока ------\n{self.user_card}
-------- Карта ИИ --------\n{self.computer_card}
        """)


# Проверяем генерацию карточки
test_card = Card()
print(test_card)

# Проверяем вывод информации на экран при загрузке сессии
test_session = GameSession()
test_session.play()