# 🔢 Verificador de Paridad - Máquina de Turing

## 📝 Descripción
Esta implementación de una Máquina de Turing determina si una cadena binaria contiene un número par o impar de unos (1's). La máquina procesa la entrada y devuelve un resultado visual indicando la paridad.

## ⚙️ Funcionamiento
La máquina opera siguiendo estos principios:
- Inicia en el estado q0 (paridad par)
- Cambia entre estados q0 y q1 según encuentra 1's
- Mantiene el mismo estado al encontrar 0's
- El estado final determina la paridad:
  - q0 (0) = número par de 1's
  - q1 (1) = número impar de 1's

## 🎯 Características
- Interfaz gráfica moderna y responsiva
- Visualización en tiempo real de la cinta
- Validación de entrada instantánea
- Retroalimentación visual del resultado
- Tema oscuro con acentos de color

## 🔧 Tabla de Transiciones
| Estado | Símbolo | Escribir | Movimiento | Siguiente Estado |
|--------|---------|----------|------------|------------------|
| q0     | 0       | 0        | R          | q0              |
| q0     | 1       | 1        | R          | q1              |
| q0     | B       | 0        | S          | qf              |
| q1     | 0       | 0        | R          | q1              |
| q1     | 1       | 1        | R          | q0              |
| q1     | B       | 1        | S          | qf              |

## 📋 Requisitos
- Python 3.x
- Tkinter (incluido en Python)

## 🚀 Uso
1. Ejecute el script:
```bash
python main.py
```

2. Ingrese una cadena binaria en el campo de texto
3. El programa validará automáticamente la entrada
4. Presione "Verificar Paridad" para ver el resultado

## 🎨 Interfaz
- Campo de entrada con validación en tiempo real
- Visualización de la cinta de la máquina de Turing
- Indicador de paridad codificado por colores:
  - Verde: Número par de 1's
  - Azul: Número impar de 1's

## 📊 Ejemplos
```
Entrada: 1101
Resultado: Impar (3 unos)

Entrada: 11011
Resultado: Par (4 unos)

Entrada: 1111
Resultado: Par (4 unos)
```

## 🔍 Notas Técnicas
- La máquina usa un símbolo 'B' para marcar el final de la cinta
- El movimiento está restringido a derecha (R) y parada (S)
- El estado 'qf' es el estado final de aceptación