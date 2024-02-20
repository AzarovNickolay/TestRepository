def word_multiplier(word: str, num: int) -> str:
    word = word.capitalize()
    return word * num

word = input('Введите слово: ')
num = int(input('Введите количество повторений: '))

print(word_multiplier(word, num))