# A5.2 – computeSales

Programa en Python que lee un catálogo de productos y un registro de ventas (ambos en formato JSON) y calcula el costo total de todas las ventas.

## Estructura del proyecto

```
A01656679_A5.2/
├── src/
│   └── computeSales.py
├── tests/
│   ├── inputs/
│   │   ├── product_list.json
│   │   ├── tc1_sales.json
│   │   ├── tc2_sales.json
│   │   └── tc3_sales.json
│   └── results/
│       ├── tc1/
│       │   └── sales_report.txt
│       ├── tc2/
│       │   └── sales_report.txt
│       └── tc3/
│           └── sales_report.txt
├── quality/
│   ├── flake8_output.txt
│   └── pylint_output.txt
└── README.md
```

## Uso

```bash
python src/computeSales.py <catálogo_productos.json> <registro_ventas.json>
```

### Ejemplo

```bash
python src/computeSales.py tests/inputs/product_list.json tests/inputs/tc1_sales.json
```

## Casos de prueba

| Caso | Archivo de ventas          | Resultado                        |
|------|----------------------------|----------------------------------|
| TC1  | `tests/inputs/tc1_sales.json` | `tests/results/tc1/sales_report.txt` |
| TC2  | `tests/inputs/tc2_sales.json` | `tests/results/tc2/sales_report.txt` |
| TC3  | `tests/inputs/tc3_sales.json` | `tests/results/tc3/sales_report.txt` |

Todos los casos de prueba comparten el mismo catálogo de productos: `tests/inputs/product_list.json`.

## Calidad de código

- **flake8**: Sin errores ni advertencias (`quality/flake8_output.txt`).
- **pylint**: Calificación 10.00/10 (`quality/pylint_output.txt`).
