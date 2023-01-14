from PIL import Image, ImageDraw, ImageSequence
def traducir_adn_a_colores(cadena_adn):
    # Diccionario para asignar colores a las bases nitrogenadas
    colores = {"A": "rojo", "T": "verde", "C": "azul", "G": "amarillo"}
    # Inicializar cadena de colores vacía
    cadena_colores = ""
    # Recorrer cada base nitrogenada de la cadena de ADN
    for base in cadena_adn:
        # Añadir el color correspondiente a la cadena de colores
        cadena_colores += colores[base] + "-"
    # Eliminar el último caracter (guion)
    cadena_colores = cadena_colores[:-1]
    # Devolver la cadena de colores
    return cadena_colores
def obtener_numero_base_4(cadena_adn):
    # Diccionario para asignar valores numéricos a las bases nitrogenadas
    valores = {"A": 0, "T": 1, "C": 2, "G": 3}
    # Inicializar número en base 4 vacío
    numero_base_4 = 0
    # Recorrer cada base nitrogenada de la cadena de ADN
    for i, base in enumerate(cadena_adn):
        # Calcular el valor numérico de la base nitrogenada
        valor = valores[base]
        # Añadir el valor numérico a la representación en base 4
        numero_base_4 += valor * 4 ** (len(cadena_adn) - i - 1)
    # Devolver el número en base 4
    return numero_base_4


def crear_gif_adn(cadena_adn, colores):
    # Crear una lista vacía para almacenar las imágenes del GIF
    imagenes = []
    # Crear una imagen en blanco para dibujar la cadena de ADN
    imagen = Image.new("RGB", (1000, 100), (255, 255, 255))
    dibujo = ImageDraw.Draw(imagen)
    # Recorrer cada base nitrogenada de la cadena de ADN
    x = 10
    for base in cadena_adn:
        # Obtener el color correspondiente a la base nitrogenada
        color = colores[base]
        # Dibujar un rectángulo con el color correspondiente
        dibujo.rectangle([x, 10, x + 50, 90], fill=color)
        x += 60
    # Agregar la imagen a la lista de imágenes del GIF
    imagenes.append(imagen)
    # Crear el GIF a partir de la lista de imágenes
    gif = Image.new("RGB", (1000, 100), (255, 255, 255))
    gif.save("adn.gif", save_all=True, append_images=imagenes, duration=1000, loop=0)

def adn_a_binario(cadena_adn):
    # Diccionario para asignar valores binarios a las bases nitrogenadas
    valores = {"A": "00", "T": "01", "C": "10", "G": "11"}
    # Inicializar cadena de bits vacía
    cadena_bits = ""
    # Recorrer cada base nitrogenada de la cadena de ADN
    for base in cadena_adn:
        # Añadir el valor binario correspondiente a la cadena de bits
        cadena_bits += valores[base]
    return cadena_bits
def adn_a_codigo_maquina(cadena_adn):
    # Convertir la cadena de ADN a binario
    cadena_bits = adn_a_binario(cadena_adn)
    # Inicializar cadena de código de máquina vacía
    codigo_maquina = ""
    # Recorrer cada bit de la cadena binaria
    for bit in cadena_bits:
        # Convertir cada bit a código de máquina
        codigo_maquina += chr(int(bit, 2))
    return codigo_maquina

def mostrar_resultados(cadena_adn):
    # Traducir ADN a colores
    colores = traducir_adn_a_colores(cadena_adn)
    print(f"Cadena de ADN en colores: {colores}")
    
    print(f"Cadena de ADN en colores: {colores}")
    # Obtener representación numérica en base 4
    numero_base_4 = obtener_numero_base_4(cadena_adn)
    crear_gif_adn(cadena_adn, numero_base_4)
    print(f"Representación numérica en base 4: {numero_base_4}")
    # Convertir ADN a binario
    cadena_bits = adn_a_binario(cadena_adn)
    print(f"Cadena de ADN en binario: {cadena_bits}")
    # Convertir ADN a código de máquina
    codigo_maquina = adn_a_codigo_maquina(cadena_adn)
    print(f"Cadena de ADN en código de")

cadena_adn = "GGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCCAGTGGTATCC"
mostrar_resultados(cadena_adn)
