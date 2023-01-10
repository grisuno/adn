import matplotlib.pyplot as plt
import pandas as pd

def base4_to_binary(base4_string):
  base4_digits = {'0': '00', '1': '01', '2': '10', '3': '11'}
  binary_string = ''
  for base4_digit in base4_string:
    binary_string += base4_digits[base4_digit]
  return binary_string

def base4_to_dna(base4_string):
  base4_digits = {'0': 'A', '1': 'C', '2': 'G', '3': 'T'}
  dna_string = ''
  for base4_digit in base4_string:
    dna_string += base4_digits[base4_digit]
  return dna_string

def plot_dna(dna_string):
  colors = {'A': 'yellow', 'C': 'red', 'G': 'green', 'T': 'transparent'}
  dna_data = pd.DataFrame({'Base': list(dna_string)})
  dna_data['Color'] = dna_data['Base'].apply(lambda x: colors[x])
  dna_data.plot(kind='scatter', x='Base', y='Base', c='Color', s=100, title='Representación gráfica de ADN')
  plt.show()

dna_string = input('Ingrese la cadena de ADN: ')
base4_string = base4_to_binary(dna_string)
binary_string = base4_to_binary(base4_string)

print(f'Cadena de ADN: {dna_string}')
print(f'Cadena de ADN codificada en base 4: {base4_string}')
print(f'Cadena de binario: {binary_string}')
plot_dna(dna_string)
