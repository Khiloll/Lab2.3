#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_letters(sentence):
    result = [char for char in sentence if char in ['м', 'и', 'н']]
    return result

# Заданное предложение
input_sentence = "Пример заданного предложения, содержащего буквы 'м', 'и', 'н'."

# Вызываем функцию для поиска букв и выводим результат
found_letters = find_letters(input_sentence)
print("Найденные буквы: ", found_letters)
