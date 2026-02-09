# A01656679 - Pruebas de Software y Aseguramiento de Calidad

Repo con las entregas de la materia. Cada carpeta dentro de `A01656679_A4.2/` corresponde a un ejercicio distinto de la actividad 4.2.

Los tres programas estan hechos en Python y la restriccion principal es que **no se pueden usar librerias ni funciones built-in** para los calculos (nada de `math`, `statistics`, `sorted()`, `bin()`, `hex()`, etc). Todo se implemento desde cero.

## Como correr los programas

Los tres funcionan igual: se les pasa un archivo de texto como argumento y generan un archivo de resultados + salida en consola.

```bash
# P1 - Estadisticas descriptivas
python A01656679_A4.2/P1/source/computeStatistics.py <archivo.txt>

# P2 - Conversion a binario y hexadecimal
python A01656679_A4.2/P2/source/convertNumbers.py <archivo.txt>

# P3 - Conteo de palabras
python A01656679_A4.2/P3/source/wordCount.py <archivo.txt>
```

Los casos de prueba estan en la carpeta `tests/` de cada ejercicio, por ejemplo:

```bash
cd A01656679_A4.2/P1/source
python computeStatistics.py ../tests/TC1.txt
```

## P1 - Compute Statistics

Lee numeros de un archivo (uno por linea) y calcula count, mean, median, mode, desviacion estandar y varianza. Para la mediana use merge sort propio y la raiz cuadrada la saque con Newton-Raphson. Si una linea tiene algo que no es numero, la ignora con un warning y sigue.

Se probo con 7 test cases (desde 400 enteros hasta 12769 numeros enormes con datos invalidos). Los resultados coinciden con la referencia del profesor.

Resultados en `A01656679_A4.2/P1/results/`.

## P2 - Converter

Lee numeros enteros y los convierte a binario y hex usando divisiones sucesivas. Los negativos se manejan con complemento a dos (10 bits para binario, 40 bits para hex, igual que DEC2BIN y DEC2HEX de Excel). Datos invalidos salen como `#VALUE!`.

4 test cases, incluyendo uno con negativos y otro con datos basura mezclados (ABC, ERR, VAL). Resultados en `A01656679_A4.2/P2/results/`.

## P3 - Count Words

Cuenta frecuencia de palabras en un archivo de texto. El ordenamiento es por frecuencia descendente y luego alfabetico (con merge sort propio, sin usar `sorted()`). El conteo usa un dict basico sin `collections.Counter`.

Los archivos de referencia del profesor estan generados con tablas dinamicas de Excel asi que el formato no es identico, pero los conteos y el Grand Total si coinciden exacto.

5 test cases, desde 100 hasta 5000 palabras. Resultados en `A01656679_A4.2/P3/results/`.

## PyLint

Los tres programas pasan pylint con **10.00/10**. Lo unico que se deshabilito es `invalid-name` porque los nombres de archivo usan camelCase (`computeStatistics.py`, `convertNumbers.py`, `wordCount.py`) pero el enunciado lo pide asi.

```bash
pip install pylint
python -m pylint A01656679_A4.2/P1/source/computeStatistics.py
python -m pylint A01656679_A4.2/P2/source/convertNumbers.py
python -m pylint A01656679_A4.2/P3/source/wordCount.py
```

## Estructura

```
A01656679_A4.2/
  P1/
    source/computeStatistics.py
    tests/TC1.txt ... TC7.txt
    results/StatisticsResults_TC1.txt ... TC7.txt
  P2/
    source/convertNumbers.py
    tests/TC1.txt ... TC4.txt
    results/ConvertionResults_TC1.txt ... TC4.txt
  P3/
    source/wordCount.py
    tests/TC1.txt ... TC5.txt
    results/WordCountResults_TC1.txt ... TC5.txt
```

Cada carpeta `results/` tambien tiene un `pylint_output.txt` con la evidencia del analisis estatico.

## Reportes individuales

Los reportes detallados de cada ejercicio (decisiones de implementacion, verificacion de resultados, etc) estan en:

- `P1_Reporte.md`
- `P2_Reporte.md`
- `P3_Reporte.md`
