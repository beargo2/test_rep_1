def is_palindrome(text):
    # Приводим к нижнему регистру и убираем пробелы
    text = text.lower().replace(" ", "")
    # Сравниваем строку с её перевёрнутой версией
    return text == text[::-1]

# Запрашиваем строку у пользователя
user_input = input("Введите слово или фразу: ")
if is_palindrome(user_input):
    print("Это палиндром!")
else:
    print("Это не палиндром.")