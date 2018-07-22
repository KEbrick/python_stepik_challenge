# -*- coding: utf-8 -*-
# GC-состав является важной характеристикой геномных последовательностей и
# определяется как процентное соотношение суммы всех гуанинов и цитозинов к
# общему числу нуклеиновых оснований в геномной последовательности.
#
# Напишите программу, которая вычисляет процентное содержание символов G (гуанин)
# и C (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
#
# Например, в строке "acggtgttat" процентное содержание символов
# G и C равно , где 4 -- это количество символов G и C,  а 10 -- это длина строки.
#
# Sample Input:
# acggtgttat
#
# Sample Output:
# 40.0

a, c = input().upper(), 0
for i in a:
    if i == "C" or i == "G":
        c += 1
print((c / len(a)) * 100)