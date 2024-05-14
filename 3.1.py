# Перше завдання
from datetime import datetime
def get_days_from_today(date):
    # Перевірка на неправильний формат дати
    try:
        # Створення об'єкта datetime з конкретною датою
        specific_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return "Incorrect date format! Please write date in such format 'YYYY-MM-DD'."

    # Створення об'єкта datetime з поточною датою
    current_date = datetime.now()

    # Обчислення різниці
    difference = current_date.toordinal() - specific_date.toordinal()

    return difference

date = '2024-01-10'
get_days_from_today(date)














