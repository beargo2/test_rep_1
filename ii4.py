import random

# Загадываем число
number = random.randint(1, 100)
attempts = 0

print("Я загадал число от 1 до 100. Попробуй угадать!")
while True:
    guess = int(input("Ваш вариант: "))
    attempts += 1
    if guess < number:
        print("Слишком мало!")
    elif guess > number:
        print("Слишком много!")
    else:
        print(f"Поздравляю! Вы угадали число {number} за {attempts} попыток!")
        break