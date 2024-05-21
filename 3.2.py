import random
def get_numbers_ticket(min_val, max_val, quantity):
    # Обмеження
    if min_val < 1 or max_val > 1000 or quantity < 1 or quantity > (max_val - min_val + 1):
        return []

    # Генерація унікальних чисел у заданому діапазоні
    Lottery_numbers = random.sample(range(min_val, max_val + 1), quantity)

    # Сортування
    Lottery_numbers.sort()
    return Lottery_numbers

# Виконання
result_numbers = get_numbers_ticket(1, 49, 6)
print(f"Ваші лотерейні числа:", result_numbers)
