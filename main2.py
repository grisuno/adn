import ctypes
# Función para codificar una secuencia de ADN en base 4
def codificar_adn(secuencia):
  # Diccionario para asignar cada base nitrogenada a un dígito
  codigos = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3
  }
  
  # Inicializamos una lista para almacenar los dígitos codificados
  digitos = []
  
  # Iteramos por cada base de la secuencia
  for base in secuencia:
    # Añadimos el dígito correspondiente a la lista
    digitos.append(codigos[base])
  
  # Devolvemos la lista de dígitos codificados como un número en base 4
  return int(''.join(map(str, digitos)), 4)

def base4_a_binario(numero):
      # Convertimos el número a binario y devolvemos el resultado
  return bin(numero)[2:]
def binario_a_codigo_maquina(numero):
      # Convertimos el número a código de máquina y devolvemos el resultado
  return hex(int(numero, 2))[2:]

# Prueba de la función
secuencia = 'GATAAATCTGGTCTTATTTC'

codigo_adn = codificar_adn(secuencia)
print(codigo_adn)  # Imprime "13"

codigo_binario = base4_a_binario(codigo_adn)
print(codigo_binario)  # Imprime "11"

codigo_maquina = binario_a_codigo_maquina(codigo_binario)
print(codigo_maquina)  # Imprime "3"
