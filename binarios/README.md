# 🧮 Sumador Binario - Máquina de Turing

## 📝 Descripción
Esta implementación de una Máquina de Turing realiza sumas de números binarios. La máquina procesa una entrada en formato "10+n=" y calcula la suma, mostrando el resultado tanto en binario como en decimal.

## ⚙️ Funcionamiento
La máquina opera siguiendo estos principios:
- Valida el formato de entrada "número+número="
- Procesa el primer número (debe comenzar con "10")
- Valida el operador "+"
- Procesa el segundo número
- Verifica el símbolo "=" final
- Calcula y muestra el resultado

## 🎯 Características
- Interfaz gráfica moderna y responsiva
- Visualización en tiempo real de la cinta
- Validación de entrada instantánea
- Conversión automática entre binario y decimal
- Retroalimentación visual del proceso

## 🔧 Tabla de Transiciones
| Estado | Símbolo | Escribir | Movimiento | Siguiente Estado |
|--------|---------|----------|------------|------------------|
| q0     | 1       | 1        | R          | q1              |
| q1     | 0       | 0        | R          | q2              |
| q2     | +       | +        | R          | q3              |
| q3     | 0,1     | 0,1      | R          | q3              |
| q3     | =       | =        | R          | q4              |
| q4     | ''      | ''       | S          | q5              |

## 📋 Requisitos
- Python 3.x
- Tkinter (incluido en Python)

## 🚀 Uso
1. Ejecute el script:
```bash
python main.py
```

2. Ingrese una expresión en el formato "10+n="
3. El programa validará automáticamente la entrada
4. Presione "Calcular" para ver el resultado

## 🎨 Interfaz
- Campo de entrada con validación en tiempo real
- Visualización animada de la cinta
- Indicadores de estado del proceso
- Resultados codificados por colores:
  - Verde: Operación exitosa
  - Rojo: Error en el proceso

## 📊 Ejemplos
```
Entrada: 10+1=
Resultado: 11 (binario) = 3 (decimal) ✅

Entrada: 10+11=
Resultado: 101 (binario) = 5 (decimal) ✅

Entrada: 10+100=
Resultado: 110 (binario) = 6 (decimal) ✅
```

## 🔍 Notas Técnicas
- El primer número debe comenzar con "10"
- Acepta cualquier número binario después del "+"
- La entrada debe terminar con "="
- La suma se realiza en decimal y se convierte a binario
- El movimiento está restringido a derecha (R) y parada (S)

## 🎮 Estados
- q0: Estado inicial, espera "1"
- q1: Ha leído "1", espera "0"
- q2: Ha leído "10", espera "+"
- q3: Procesando segundo número
- q4: Ha leído "=", prepara resultado
- q5: Estado de aceptación

## ⚡ Funcionalidades Especiales
1. Procesamiento de Entrada
   - Validación de formato
   - Verificación de números binarios
   - Control de sintaxis

2. Visualización del Proceso
   - Movimiento del cabezal en tiempo real
   - Estado actual de la máquina
   - Contenido de la cinta

3. Cálculo y Resultados
   - Extracción de números
   - Conversión binario-decimal
   - Presentación dual del resultado

## 🎯 Casos de Uso
- Aprendizaje de aritmética binaria
- Demostración de máquinas de Turing
- Práctica de conversiones numéricas
- Validación de expresiones matemáticas