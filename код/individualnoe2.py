def check_sequence(words_sequence):
    for word in words_sequence:
        if "жи" in word or "ши" in word:
            print(f'Слово "{word}" правильно содержит буквосочетание "жи" или "ши"')
        else:
            print(f'Слово "{word}" не содержит буквосочетание "жи" или "ши"')

# Заданная последовательность слов
input_words_sequence = ["жираф", "мышь", "книга", "свижа"]

# Вызываем функцию для проверки последовательности слов
check_sequence(input_words_sequence)