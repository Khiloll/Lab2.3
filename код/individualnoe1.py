#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_letter_o(sentence):
    count = 0
    for letter in sentence:
        if letter.lower() == 'о':  # Проверяем каждую букву, игнорируя регистр
            count += 1
    return count

# Ввод предложения от пользователя
sentence = input("Введите предложение: ")

# Вычисление числа букв 'о' в предложении
letter_count = count_letter_o(sentence)
print(f"Число букв 'о' в предложении: {letter_count}")
