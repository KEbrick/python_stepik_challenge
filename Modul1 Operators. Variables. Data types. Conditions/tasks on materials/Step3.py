# -*- coding: utf-8 -*-
# Напишите простой калькулятор, который считывает с пользовательского
# ввода три строки: первое число, второе число и операцию, после чего применяет
# операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.
#
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
#
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#
# Обратите внимание, что на вход программе приходят вещественные числа.
#
# Sample Input 1:
# 5.0
# 0.0
# mod
#
# Sample Output 1:
# Деление на 0!
#
# Sample Input 2:
# -12.0
# -8.0
# *
#
# Sample Output 2:
# 96.0
#
# Sample Input 3:
# 5.0
# 10.0
# /
#
# Sample Output 3:
# 0.5

a, b, operation = float(input()), float(input()), input()
if operation == "/" and b == 0 or operation == "mod" and b == 0 or operation == "div" and b == 0:
    print("Деление на 0!")
elif operation == "mod":
    print(int(a) % int(b))
elif operation == "/":
    print(a / b)
elif operation == "div":
    print(a // b)
elif operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "pow":
    print(a ** b)
