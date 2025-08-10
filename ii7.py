def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    # Запрашиваем число
    num = int(input("Введите число для вычисления факториала: "))
    if num < 0:
        print("Факториал не определён для отрицательных чисел.")
    else:
        result = factorial(num)
        print(f"Факториал числа {num} равен {result}")
except ValueError:
    print("Пожалуйста, введите целое число.")