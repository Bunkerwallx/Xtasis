

import  pyfiglet
import  sys

texto = pyfiglet.print_figlet("\n Bunker",  font='slant', colors='blue')


def check_password():
    # Establecer la contraseña correcta y el número de intentos
    correct_password = "Bunker"
    attempts = 5

    # Bucle para verificar la contraseña
    for i in range(attempts):
        # Solicitar la contraseña al usuario
        user_password = input("INGRESA TU PASSWORD: ")

        # Comprobar si la contraseña es correcta
        if user_password == correct_password:
            print("¡CORRECTO! Has ingresado la contraseña correcta.")
            return
        else:
            print("INCORRECTO. Te quedan {} intentos.".format(attempts - i - 1))

    # Si se agotan todos los intentos, informar al usuario
    print("Se acabaron tus intentos.")

# Llamar a la función para ejecutarla
check_password()







