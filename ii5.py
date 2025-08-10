def analyze_text(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    return word_count, char_count

# Запрашиваем текст
text = input("Введите текст: ")
words, chars = analyze_text(text)

# Выводим результаты
print(f"Количество слов: {words}")
print(f"Количество символов (с пробелами): {chars}")
print(f"Средняя длина слова: {chars / words if words > 0 else 0:.2f}")