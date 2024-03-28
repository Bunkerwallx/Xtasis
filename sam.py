

import  pyfiglet
import  sys

texto = pyfiglet.print_figlet("\n Bunker",  font='slant', colors='blue')

intentos =  5
passwd_correcto = "Bunker"

while intentos > 0:
	passwd = input(" Ingresa tu ID : ")
	if passwd == passwd_correcto:
		print("ID correcto")
		break
    ...:         break
    ...:     else:
    ...:         print("ID incorrecto")
    ...:         intentos -= 1
    ...:      if intentos == 0:






