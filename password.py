import random
import base64
LETTERS = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"] # password's all letter
NUMBERS = [1,2,3,4,5,6,7,8,9] # password's all number
OTHERS = ["`","-","=","[","]",'\\',";","'",".",",","/","~","!","@","#","$","%","^","&","*","(",")","_","+","{","}","|",":","\"","<",">","?"] # password's all fuhao

def create_password(byte: int):
    password = ""
    letter_byte = random.randrange(0,byte)
    number_byte = random.randrange(0,byte-letter_byte)
    other_byte = byte-letter_byte-number_byte
    print(letter_byte,number_byte,other_byte)
    for _ in range(letter_byte):
        password += random.choice(LETTERS)
    for _ in range(number_byte):
        password += str(random.choice(NUMBERS))
    for _ in range(other_byte):
        password += random.choice(OTHERS)
    return password



print(create_password(9))