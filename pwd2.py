import string
import sys
import random
def generar_cadena_aleatoria(*args):
    caracteres_posibles = string.ascii_lowercase + string.ascii_letters + string.digits + string.punctuation
    xt = sys.argv[1] #argv es la longitud de la cadena aleatoria
    longitud = int(xt)
    # Generate at least two random digits to include in the string
    random_digits = random.choices(string.digits, k=2)
    
    # Ensure the string length is at least 2 characters longer than the specified length
    cadena_aleatoria = ''.join(random.choice(caracteres_posibles) for _ in range(longitud - 2))
    
    # Add the random digits at random positions in the string
    random_positions = random.sample(range(longitud - 2), 2)
    for i, digit in enumerate(random_digits):
        cadena_aleatoria = cadena_aleatoria[:random_positions[i]] + digit + cadena_aleatoria[random_positions[i]:]
    dig = random_digits 
    return cadena_aleatoria

# Ejemplo de uso con una longitud de contraseña de 10 caracteres (al menos 2 dígitos)
if len(sys.argv) < 2:
    print("Falta el tamaño de la cadena aleatoria")
    sys.exit()
lp = int(sys.argv[1])
if (lp < 4):
    print(sys.argv[1])
    sys.argv[1] = int(12)
    cadena_aleatoria = generar_cadena_aleatoria() 
    print("passwdx4 🔐:", cadena_aleatoria)
    sys.exit()
else:
    cadena_aleatoria = generar_cadena_aleatoria() 
    print("passwd 🔐:", cadena_aleatoria)
    print(len(cadena_aleatoria))
