import random

alpha_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

full_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"

def password_generator():
    choice=input('Simple or complex?')
    if choice == 'Simple':
        lenght=8
        char = full_char
    else:
        lenght=20 
        char = alpha_char
    psw=''    
    for x in range(lenght):
        psw = psw + char[random.randint(0,len(char)-1)]
    return psw    
                         

