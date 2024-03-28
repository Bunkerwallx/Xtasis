import subprocess
import requests
import time
import platform
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64
import pyfiglet
import random

# Impresión del texto con estilo
texto = pyfiglet.print_figlet("Bunker", font='slant', colors='blue')

# Generación segura de la clave de encriptación
key = get_random_bytes(32)  # Clave de encriptación
cipher = AES.new(key, AES.MODE_ECB)  # Crea un nuevo objeto cifrado AES

# Contraseña original (debería solicitarse al usuario o almacenarse de manera segura)
original_password = b'BunkerWallx500'

# Encripta la contraseña original
encrypted_password = cipher.encrypt(pad(original_password, AES.block_size))
print("Contraseña encriptada: ", base64.b64encode(encrypted_password))

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
time.sleep(4)

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



# Función para verificar la conexión a Internet
def verificar_conexion_internet():
    try:
        request = requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

# Verificación de la conexión a Internet
if verificar_conexion_internet():
    print("Conexión a Internet establecida.")
else:
    print("Sin conexión a Internet. Verifica tu conexión.")

# Lista de paquetes a verificar e instalar si es necesario
paquetes_a_verificar = ["pop", "numpy", "pandas", "matplotlib", "sys", "os", "requests", "pyfiglet", "pycryptodome"]

def verificar_paquetes():
    paquetes_faltantes = []
    for paquete in paquetes_a_verificar:
        try:
            __import__(paquete)
        except ImportError:
            paquetes_faltantes.append(paquete)
    return paquetes_faltantes

def instalar_paquetes(paquetes):
    for paquete in paquetes:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", {}paquete])
            print(f"Paquete '{paquete}' instalado correctamente.")
        except subprocess.CalledProcessError:
            print(f"No se pudo instalar el paquete '{paquete}'.")

# Verificar paquetes faltantes e instalarlos si es necesario
paquetes_faltantes = verificar_paquetes()
if paquetes_faltantes:
    print("Los siguientes paquetes no están instalados:")
    for paquete in paquetes_faltantes:
        print(f"- {paquete}")
    print("\nInstalando los paquetes faltantes...")
    instalar_paquetes(paquetes_faltantes)
else:
    print("Todos los paquetes están instalados correctamente.")
