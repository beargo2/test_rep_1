import random
import string


def generate_password(length):
    # Определяем набор символов
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols

    # Генерируем пароль
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


# Запрашиваем длину пароля
length = int(input("Введите длину пароля: "))
print("Ваш пароль:", generate_password(length))