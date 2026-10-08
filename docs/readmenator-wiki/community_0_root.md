# root

*Community 0 | 3 files | cohesion 1.00*

## Definition

This community groups 3 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `adn_a_binario`, `adn_a_codigo_maquina`, `base4_a_binario`, `base4_to_binary`, `base4_to_dna`, `binario_a_codigo_maquina`, `codificar_adn`, `crear_gif_adn`. Core file: `main3.py` (6 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `main.py` | py | utility | 3 | no |
| `main2.py` | py | utility | 3 | no |
| `main3.py` | py | utility | 6 | no |

## Key Symbols

- `base4_to_binary` (function, `main.py:4`) `def base4_to_binary(base4_string)`
- `base4_to_dna` (function, `main.py:11`) `def base4_to_dna(base4_string)`
- `plot_dna` (function, `main.py:18`) `def plot_dna(dna_string)`
- `codificar_adn` (function, `main2.py:3`) `def codificar_adn(secuencia)`
- `base4_a_binario` (function, `main2.py:23`) `def base4_a_binario(numero)`
- `binario_a_codigo_maquina` (function, `main2.py:26`) `def binario_a_codigo_maquina(numero)`
- `traducir_adn_a_colores` (function, `main3.py:2`) `def traducir_adn_a_colores(cadena_adn)`
- `obtener_numero_base_4` (function, `main3.py:15`) `def obtener_numero_base_4(cadena_adn)`
- `crear_gif_adn` (function, `main3.py:30`) `def crear_gif_adn(cadena_adn, colores)`
- `adn_a_binario` (function, `main3.py:50`) `def adn_a_binario(cadena_adn)`
- `adn_a_codigo_maquina` (function, `main3.py:60`) `def adn_a_codigo_maquina(cadena_adn)`
- `mostrar_resultados` (function, `main3.py:71`) `def mostrar_resultados(cadena_adn)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- No cross-community bridges recorded. This community is self-contained.

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `main.py`)? What purpose do they serve?
- What would break if the most connected file in root changed?
- Should root be split, given cohesion 1.00?

## Sources

- `main.py`
- `main2.py`
- `main3.py`
