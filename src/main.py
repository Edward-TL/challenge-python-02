# Resolve the problem!!
import string

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    import random

    password = ""
    PasswordSize = random.randrange(8,16)
    
    #Para asegurar que se cumplan las 4 condiciones:
    Missing = [1,1,1,1]
    
    for slot in range(0, PasswordSize):

        #En el caso de que alguna condicion y aún se puede agregar:    
        if sum(Missing) < (PasswordSize-len(password)):
            RollTheDice = random.randrange(0,4)             
        else:
            for check in range(0, len(Missing)):
                if Missing[check] == 1:
                    RollTheDice = check
            #Se usa el 'len' para que check sea una variable de tipo int
            #Así puede interactuar con el apartado "if"


        if RollTheDice == 0:
            Number = chr(47 + random.randrange(1,10))
            password = password + Number
            Missing[0] = 0

        elif RollTheDice == 1:
            Uppercase = chr(64+ random.randrange(1,27))
            password = password + Uppercase
            Missing[1] = 0

        elif RollTheDice == 2:
            Lowercase = chr(96+ random.randrange(1,27))
            password = password + Lowercase
            Missing[2] = 0

        else:
            password = password + random.choice(SYMBOLS)
            Missing[3] = 0
            pass
    
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
