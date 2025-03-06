def proviryator(string):
    for i in range(len(password)):
        if password[i] in string:
            return True



password = input()
crypto_level = 0
if len(password) >= 8:
    crypto_level +=1
if proviryator(string="qwertyuiopasdfghjklzxcvbnm"):
    crypto_level +=1
if proviryator(string="qwertyuiopasdfghjklzxcvbnm".upper()):
    crypto_level +=1
if proviryator(string="! \" # $ % & ' ( ) * +"):
    crypto_level +=1
print(crypto_level)