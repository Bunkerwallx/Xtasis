

import  pyfiglet
import  sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import platform

texto = pyfiglet.print_figlet("\n Bunker",  font='slant', colors='blue')


key = get_random_bytes(16) # Clave de encriptación
cipher = AES.new(key, AES.MODE_ECB) # Crea un nuevo objeto cifrado AES

# Contraseña original
original_password = b'BunkerWallx500'

# Encripta la contraseña original
encrypted_password = cipher.encrypt(pad(original_password, AES.block_size))
print("Contraseña encriptada: ", base64.b64encode(encrypted_password))

# Ahora puedes verificar la contraseña ingresada por el usuario
for _ in range(5):
    input_password = input("Ingresa tu ID: ").encode()

    # Encripta la contraseña ingresada por el usuario
    encrypted_input_password = cipher.encrypt(pad(input_password, AES.block_size))
    
    if encrypted_input_password == encrypted_password:
        print("CORRECTO")
        break
    else:
        print("INCORRECTO")
else:
        print("Se acabaron tus intentos")


def identificar_sistema_operativo():
    sistema_operativo = platform.system()
    if sistema_operativo == 'Windows':
        return 'Windows'
    elif sistema_operativo == 'Linux':
        return 'Linux'
    elif sistema_operativo == 'Darwin':
        return 'macOS'
    else:
        return 'No se puede identificar el sistema operativo'

print(identificar_sistema_operativo())