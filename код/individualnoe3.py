#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def insert_letter(word, letter_to_insert):
    for i, char in enumerate(word):
        if char == 'и':
            word = word[:i+1] + letter_to_insert + word[i+1:]
            break
    return word

# Заданное слово и буква для вставки
input_word = "пример."  # Пример заданного слова
inserted_letter = "а"  # Буква для вставки

# Вызываем функцию для вставки буквы после первой буквы "и" в слове
resulting_word = insert_letter(input_word, inserted_letter)
print("Результат:", resulting_word)
