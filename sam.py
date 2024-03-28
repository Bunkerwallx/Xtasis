

import  pyfiglet
import  sys

texto = pyfiglet.print_figlet("\n Bunker",  font='slant', colors='blue')

intentos = 5
correct_password = "BunkerWallx500"

while intentos > 0:
    password = input("Ingresa tu ID: ")
    if password == correct_password:
        print("CORRECTO")
        break
    else:
        print("INCORRECTO")
        intentos -= 1
        if intentos == 0:
            print("Se acabaron tus intentos")




