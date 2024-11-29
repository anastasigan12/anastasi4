def transform_number(n):
    # Перевіряємо, що число трицифрове
    if not (100 <= abs(n) <= 999):
        raise ValueError("Число повинно бути трицифровим")
    
    # Перетворюємо число на рядок для роботи з символами
    n_str = str(abs(n))
    
    # Переставляємо цифри: останню переносимо на початок
    new_number = n_str[-1] + n_str[:-1]
    
    # Перетворюємо назад у число
    return int(new_number)

# Приклад використання
number = 657
result = transform_number(number)
print("Результат:", result)

import math

def calculate_y(x):
    # Перевірка на коректність значення x
    if x == 0 or abs(x) % (math.pi / 2) == 0:
        raise ValueError("Некоректне значення x, ділення на нуль неможливе")
    
    # Константа sin(18°), переводимо градуси у радіани
    sin_18 = math.sin(math.radians(18))
    
    # Обчислення чисельника
    numerator = (math.sin(3 * x + math.pi) ** 3) * (2 ** (1 - x))
    
    # Обчислення знаменника
    denominator = math.tan(abs(x)) * sin_18
    
    # Обчислення логарифмічного доданку
    log_part = (1 / 3) * math.log2(abs(x))
    
    # Повний вираз
    y = (numerator / denominator) + log_part
    return y

# Приклад використання
x = 2  # Задайте значення x
try:
    result = calculate_y(x)
    print(f"Результат для x = {x}: y = {result}")
except ValueError as e:
    print(f"Помилка: {e}")

def is_palindrome(n):
    # Перевіряємо, що число чотиризначне
    if not (1000 <= abs(n) <= 9999):
        raise ValueError("Число повинно бути чотиризначним")
    
    # Перетворюємо число у рядок
    n_str = str(abs(n))
    
    # Порівнюємо число з його оберненим рядком
    return n_str == n_str[::-1]

# Приклад використання
number = 4224  
result = is_palindrome(number)
print(f"Число {number} є паліндромом: {result}")
