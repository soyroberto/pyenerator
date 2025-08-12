import string
import sys
import random
import argparse
import os
#word list from EFF
#https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
def cargar_lista_palabras(archivo_palabras="es.txt"):
    """
    Carga la lista de palabras desde el archivo EFF.
    
    Returns:
        list: Lista de palabras para generar passphrases
    """
    palabras = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(script_dir, archivo_palabras)
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            for linea in f:
                # El formato EFF es: número\tpalabra
                partes = linea.strip().split('\t')
                if len(partes) >= 2:
                    palabras.append(partes[1])
    except FileNotFoundError:
        # Lista de respaldo si no se encuentra el archivo EFF
        palabras = [
            "gato", "perro", "pila", "staple", "house", "water", "fire", "earth",
            "wind", "light", "noche", "moon", "sun", "star", "tree", "flower", "river",
            "mountain", "ocean", "forest", "desert", "cloud", "rain", "snow", "storm",
            "thunder", "rayo", "rainbow", "bridge", "castle", "tower", "garden",
            "field", "arena", "valley", "hill", "rock", "stone", "crystal", "diamond",
            "gold", "plata", "copper", "iron", "steel", "glass", "wood", "paper",
            "book", "pluma", "pencil", "brush", "paint", "color", "red", "blue", "green",
            "yellow", "naranja", "purple", "pink", "black", "white", "gray", "brown"
        ]
        print(f"Advertencia: No se encontró {archivo_palabras}, usando lista básica")
    
    return palabras

def generar_passphrase_xkcd(num_palabras=5, separador="-", incluir_numeros=False, incluir_simbolos=False, capitalizar=False):
    """
    Genera una passphrase estilo XKCD usando palabras aleatorias.
    
    Args:
        num_palabras (int): Número de palabras a usar
        separador (str): Carácter para separar las palabras
        incluir_numeros (bool): Si agregar números al final
        incluir_simbolos (bool): Si agregar símbolos al final
        capitalizar (bool): Si capitalizar la primera letra de cada palabra
    
    Returns:
        str: Passphrase generada
    """
    palabras = cargar_lista_palabras()
    
    # Seleccionar palabras aleatorias
    palabras_seleccionadas = random.sample(palabras, min(num_palabras, len(palabras)))
    
    # Capitalizar si se solicita
    if capitalizar:
        palabras_seleccionadas = [palabra.capitalize() for palabra in palabras_seleccionadas]
    
    # Unir con el separador
    passphrase = separador.join(palabras_seleccionadas)
    
    # Agregar números si se solicita
    if incluir_numeros:
        numeros = ''.join(random.choices(string.digits, k=2))
        passphrase += separador + numeros
    
    # Agregar símbolos si se solicita
    if incluir_simbolos:
        simbolos = ''.join(random.choices("!@#$%^&*", k=1))
        passphrase += separador + simbolos
    
    return passphrase

def generar_cadena_aleatoria(longitud, incluir_numeros=True, incluir_simbolos=True, incluir_especiales=True):
    """
    Genera una cadena aleatoria con opciones para incluir diferentes tipos de caracteres.
    (Función original mantenida para compatibilidad)
    """
    # Siempre incluir letras (minúsculas y mayúsculas)
    caracteres_posibles = string.ascii_letters
    
    # Agregar números si se solicita
    if incluir_numeros:
        caracteres_posibles += string.digits
    
    # Agregar símbolos si se solicita
    if incluir_simbolos:
        caracteres_posibles += "!@#$%^&*"
    
    # Agregar caracteres especiales si se solicita
    if incluir_especiales:
        caracteres_posibles += "()[]{}|\\:;\"'<>,.?/~`"
    
    # Verificar que tenemos al menos algunos caracteres para usar
    if not caracteres_posibles:
        caracteres_posibles = string.ascii_letters  # Fallback a solo letras
    
    # Generar la contraseña
    cadena_aleatoria = ''.join(random.choice(caracteres_posibles) for _ in range(longitud))
    
    return cadena_aleatoria

def main():
    parser = argparse.ArgumentParser(description='Generador de contraseñas con opciones personalizables y estilo XKCD')
    
    # Grupo mutuamente exclusivo para elegir el tipo de generación
    grupo_tipo = parser.add_mutually_exclusive_group()
    grupo_tipo.add_argument('--xkcd', action='store_true', help='Generar passphrase estilo XKCD con palabras')
    grupo_tipo.add_argument('longitud', nargs='?', type=int, help='Longitud de la contraseña (para modo tradicional)')
    
    # Opciones para modo tradicional
    parser.add_argument('--no-numeros', '--non', action='store_true', help='Excluir números de la contraseña')
    parser.add_argument('--no-simbolos', '--nos', action='store_true', help='Excluir símbolos de la contraseña')
    parser.add_argument('--no-especiales', '--noe', action='store_true', help='Excluir caracteres especiales de la contraseña')
    
    # Opciones para modo XKCD
    parser.add_argument('--palabras', type=int, default=5, help='Número de palabras para passphrase XKCD (default: 5)')
    parser.add_argument('--separador', default='-', help='Separador entre palabras (default: -)')
    parser.add_argument('--capitalizar', action='store_true', help='Capitalizar primera letra de cada palabra')
    parser.add_argument('--agregar-numeros', action='store_true', help='Agregar números al final de la passphrase')
    parser.add_argument('--agregar-simbolos', action='store_true', help='Agregar símbolos al final de la passphrase')
    
    args = parser.parse_args()
    
    if args.xkcd:
        # Modo XKCD
        passphrase = generar_passphrase_xkcd(
            num_palabras=args.palabras,
            separador=args.separador,
            incluir_numeros=args.agregar_numeros,
            incluir_simbolos=args.agregar_simbolos,
            capitalizar=args.capitalizar
        )
        
        print(f"passphrase 🔐: {passphrase}")
        print(f"Palabras: {args.palabras}")
        print(f"Separador: '{args.separador}'")
        
        extras = []
        if args.capitalizar:
            extras.append("capitalizado")
        if args.agregar_numeros:
            extras.append("números")
        if args.agregar_simbolos:
            extras.append("símbolos")
        
        if extras:
            print(f"Extras: {', '.join(extras)}")
        
    else:
        # Modo tradicional
        if args.longitud is None:
            parser.error("Debe especificar la longitud de la contraseña o usar --xkcd para modo passphrase")
        
        # Verificar longitud mínima
        if args.longitud < 4:
            print(f"Longitud mínima es 4, usando 12 en su lugar")
            args.longitud = 12
        
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

