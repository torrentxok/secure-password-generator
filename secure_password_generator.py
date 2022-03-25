from random import *


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину одного пароля: '))
add_digits = input('Включить цифры? (д = да, н = нет): ').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет): ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет): ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет): ').strip()
remove_badsymbol = input('Исключить символы il1Lo0O? (д = да, н = нет): ').strip()

if add_digits.lower()=='д':
    chars += digits
if add_lowercase.lower()=='д':
    chars += lowercase_letters
if add_uppercase.lower()=='д':
    chars += uppercase_letters
if add_punctuation.lower()=='д':
    chars += punctuation
if remove_badsymbol.lower()=='д':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')


for _ in range(n):
    print(generate_password(length, chars))