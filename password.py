import base64
import random

LETTERS = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c",
           "v", "b", "n", "m"]  # password's all letter
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # password's all number
SYMBOLS = ["`", "-", "=", "[", "]", '\\', ";", "'", ".", ",", "/", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(",
           ")",
           "_", "+", "{", "}", "|", ":", "\"", "<", ">", "?"]  # password's all symbol


def create_password(byte, letter_byte, number_byte, symbol_byte):
    if letter_byte == "random":
        letter_byte = random.randrange(0, byte)
    if number_byte == "random":
        number_byte = random.randrange(0, byte - letter_byte)
    if symbol_byte == "random":
        symbol_byte = byte - letter_byte - number_byte

    password = r""
    for _ in range(letter_byte):
        password += random.choice(LETTERS)
    for _ in range(number_byte):
        password += str(random.choice(NUMBERS))
    for _ in range(symbol_byte):
        password += random.choice(SYMBOLS)
    lst = list(password)
    random.shuffle(lst)
    shuffle = r""
    for i in lst:
        shuffle += i
    return shuffle


def base64_write(password, filename):
    with open(filename, mode="wb") as file:
        file.write(bytes(base64.b64encode(bytes(password))))


def ask_bool(question) -> bool:
    answer = input(question)
    if answer == "Y" or answer == "y":
        return True
    elif answer == "Y" or answer == "y":
        return False
    else:
        raise ValueError()


def ask_number(question, default):
    a = input(question)
    if a == "":
        print(f"Use default:{default}")
        return default
    else:
        return int(a)
