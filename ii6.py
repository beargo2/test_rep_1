import random

def roll_dice(num_rolls):
    results = {}
    for _ in range(num_rolls):
        # Бросаем два кубика
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] = results.get(total, 0) + 1
    return results

# Запрашиваем количество бросков
rolls = int(input("Сколько раз бросить кубики? "))
stats = roll_dice(rolls)

# Выводим статистику
for total, count in sorted(stats.items()):
    print(f"Сумма {total}: {count} раз ({count / rolls * 100:.2f}%)")