import string
import sys
import random
import argparse

def generar_cadena_aleatoria(longitud, incluir_numeros=True, incluir_simbolos=True, incluir_especiales=True):
    """
    Genera una cadena aleatoria con opciones para incluir diferentes tipos de caracteres.
    
    Args:
        longitud (int): Longitud de la contraseña
        incluir_numeros (bool): Si incluir números (0-9)
        incluir_simbolos (bool): Si incluir símbolos de puntuación
        incluir_especiales (bool): Si incluir caracteres especiales
    
    Returns:
        str: Contraseña generada
    """
    # Siempre incluir letras (minúsculas y mayúsculas)
    caracteres_posibles = string.ascii_letters
    
    # Agregar números si se solicita
    if incluir_numeros:
        caracteres_posibles += string.digits
    
    # Agregar símbolos si se solicita
    if incluir_simbolos:
        caracteres_posibles += "!@#$%^&*-_=+"
    
    # Agregar caracteres especiales si se solicita
    if incluir_especiales:
        caracteres_posibles += "()[]{}|\\:;<>,.?/~"
    
    # Verificar que tenemos al menos algunos caracteres para usar
    if not caracteres_posibles:
        caracteres_posibles = string.ascii_letters  # Fallback a solo letras
    
    # Generar la contraseña
    cadena_aleatoria = ''.join(random.choice(caracteres_posibles) for _ in range(longitud))
    
    return cadena_aleatoria

def main():
    parser = argparse.ArgumentParser(description='Generador de contraseñas con opciones personalizables')
    parser.add_argument('longitud', type=int, help='Longitud de la contraseña')
    parser.add_argument('--no-numeros', '--non', action='store_true', help='Excluir números de la contraseña')
    parser.add_argument('--no-simbolos', '--nos', action='store_true', help='Excluir símbolos de la contraseña')
    parser.add_argument('--no-especiales', '--noe', action='store_true', help='Excluir caracteres especiales de la contraseña')
    
    args = parser.parse_args()
    
    # Verificar longitud mínima
    if args.longitud < 4:
        print(f"Longitud mínima es 4, usando 13 en su lugar")
        args.longitud = 13
    
    # Determinar qué tipos de caracteres incluir
    incluir_numeros = not args.no_numeros
    incluir_simbolos = not args.no_simbolos
    incluir_especiales = not args.no_especiales
    
    # Generar la contraseña
    cadena_aleatoria = generar_cadena_aleatoria(
        args.longitud, 
        incluir_numeros, 
        incluir_simbolos, 
        incluir_especiales
    )
    
    # Mostrar información sobre los tipos de caracteres incluidos
    tipos_incluidos = []
    if incluir_numeros:
        tipos_incluidos.append("números")
    if incluir_simbolos:
        tipos_incluidos.append("símbolos")
    if incluir_especiales:
        tipos_incluidos.append("especiales")
    
    print(f"passwd 🔐: {cadena_aleatoria}")
    print(f"Longitud: {len(cadena_aleatoria)}")
    print(f"Tipos incluidos: {', '.join(tipos_incluidos) if tipos_incluidos else 'solo letras'}")

if __name__ == "__main__":
    main()

