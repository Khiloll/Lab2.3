#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def replace_even_chars(sentence):
    modified_sentence = ""
    for i in range(len(sentence)):
        if i % 2 == 1:  # Проверяем индекс символа (четный индекс)
            modified_sentence += 'ы'
        else:
            modified_sentence += sentence[i]

    return modified_sentence

# Ввод предложения от пользователя
sentence = input("Введите предложение: ")

# Замена символов на четных позициях на 'ы'
result_sentence = replace_even_chars(sentence)
print(f"Предложение с замененными символами на четных позициях: {result_sentence}")
