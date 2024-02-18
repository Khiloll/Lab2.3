#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fix_word(word):
    # Переставляем буквы в слове для исправления ошибки
    # Меняем местами вторую и третью букву в слове (индексы 1 и 2)
    corrected_word = list(word)
    corrected_word[1], corrected_word[2] = corrected_word[2], corrected_word[1]
    corrected_word = ''.join(corrected_word)

    return corrected_word

# Заданное ошибочное слово
wrong_word = "иинформация"

# Исправленное слово
corrected_word = fix_word(wrong_word)
print(f"Ошибка исправлена: {corrected_word}")
