import datetime
import calendar

def get_day_of_week(day: int, month: int, year: int) -> str:
    """Определяет день недели для заданной даты."""
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    day_index = datetime.date(year, month, day).weekday()
    return days[day_index]

def is_leap_year(year: int) -> bool:
    """Определяет, является ли год високосным."""
    return calendar.isleap(year)

def calculate_age(day: int, month: int, year: int) -> int:
    """Вычисляет возраст пользователя."""
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def display_date_as_stars(day: int, month: int, year: int):
    """Выводит дату в формате дд мм гггг, цифры отображаются звёздочками."""
    digits = {
        '0': [
            " *** ",
            "*   *",
            "*   *",
            "*   *",
            " *** "
        ],
        '1': [
            "  *  ",
            " **  ",
            "  *  ",
            "  *  ",
            "*****"
        ],
        '2': [
            " *** ",
            "*   *",
            "  ** ",
            " *   ",
            "*****"
        ],
        '3': [
            " *** ",
            "*   *",
            "  ** ",
            "*   *",
            " *** "
        ],
        '4': [
            "   * ",
            "  ** ",
            " * * ",
            "*****",
            "   * "
        ],
        '5': [
            "*****",
            "*    ",
            "**** ",
            "    *",
            "**** "
        ],
        '6': [
            " ****",
            "*    ",
            "**** ",
            "*   *",
            " *** "
        ],
        '7': [
            "*****",
            "    *",
            "   * ",
            "  *  ",
            " *   "
        ],
        '8': [
            " *** ",
            "*   *",
            " *** ",
            "*   *",
            " *** "
        ],
        '9': [
            " *** ",
            "*   *",
            " ****",
            "    *",
            "**** "
        ]
    }

    date_str = f"{day:02d} {month:02d} {year}"
    rows = ["" for _ in range(5)]

    for char in date_str:
        if char == " ":
            for i in range(5):
                rows[i] += "   "
        else:
            for i in range(5):
                rows[i] += digits[char][i] + "  "

    for row in rows:
        print(row)

if __name__ == "__main__":
    try:
        day = int(input("Введите день вашего рождения (1-31): "))
        month = int(input("Введите месяц вашего рождения (1-12): "))
        year = int(input("Введите год вашего рождения: "))

        print("\nОпределение данных о дате рождения...")
        day_of_week = get_day_of_week(day, month, year)
        leap_year = is_leap_year(year)
        age = calculate_age(day, month, year)

        print(f"Вы родились в {day_of_week}.")
        print(f"Год рождения {'високосный' if leap_year else 'не високосный'}.")
        print(f"Ваш возраст: {age} лет.")

        print("\nДата рождения в формате электронного табло:")
        display_date_as_stars(day, month, year)
    except ValueError:
        print("Ошибка: введены некорректные данные.")
