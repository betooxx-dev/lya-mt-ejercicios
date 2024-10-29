# 🔍 Validador de Patrón 'abb' - Máquina de Turing

## 📝 Descripción
Esta implementación de una Máquina de Turing verifica si una cadena de entrada mantiene el patrón específico 'abb'. La máquina procesa la entrada y determina si cumple con este patrón, proporcionando retroalimentación visual del proceso.

## ⚙️ Funcionamiento
La máquina opera siguiendo estos principios:
- Busca secuencias que terminan en 'abb'
- Procesa la entrada de izquierda a derecha
- Acepta múltiples ocurrencias del patrón
- El estado final (q3) indica si la cadena termina correctamente

## 🎯 Características
- Interfaz gráfica moderna y responsiva
- Visualización en tiempo real de la cinta
- Validación de entrada instantánea
- Retroalimentación visual del resultado
- Tema consistente con otros ejercicios

## 🔧 Tabla de Transiciones
| Estado | Símbolo | Escribir | Movimiento | Siguiente Estado |
|--------|---------|----------|------------|------------------|
| q0     | a       | a        | R          | q1              |
| q1     | b       | b        | R          | q2              |
| q2     | b       | b        | R          | q3              |
| q3     | a       | a        | R          | q1              |

## 📋 Requisitos
- Python 3.x
- Tkinter (incluido en Python)

## 🚀 Uso
1. Ejecute el script:
```bash
python main.py
```

2. Ingrese una cadena usando solo las letras 'a' y 'b'
3. El programa validará automáticamente la entrada
4. Presione "Validar" para ver el resultado

## 🎨 Interfaz
- Campo de entrada con validación en tiempo real
- Visualización de la cinta de la máquina de Turing
- Indicador de validación codificado por colores:
  - Verde: Cadena válida (mantiene el patrón 'abb')
  - Rojo: Cadena inválida

## 📊 Ejemplos
```
Entrada: abb
Resultado: Válida ✅

Entrada: abbabb
Resultado: Válida ✅

Entrada: abba
Resultado: Inválida ❌

Entrada: abbabbabb
Resultado: Válida ✅
```

## 🔍 Notas Técnicas
- La máquina usa un símbolo ' ' para marcar el final de la cinta
- Solo acepta los símbolos 'a' y 'b' como entrada válida
- El estado 'q3' es el estado de aceptación
- El movimiento está restringido a derecha (R)

## 🎮 Estados
- q0: Estado inicial, espera una 'a'
- q1: Ha encontrado una 'a', espera primera 'b'
- q2: Ha encontrado primera 'b', espera segunda 'b'
- q3: Estado de aceptación (patrón completado)

## ⚡ Funcionalidades Especiales
1. Validación en Tiempo Real
   - Verifica la entrada mientras el usuario escribe
   - Resalta errores inmediatamente
   - Habilita/deshabilita el botón según la entrada

2. Visualización de la Cinta
   - Muestra el contenido actual de la cinta
   - Resalta la posición del cabezal
   - Actualiza en tiempo real durante el proceso

3. Feedback Visual
   - Mensajes claros y descriptivos
   - Colores intuitivos para resultados
   - Indicadores de estado del proceso

## 🎯 Casos de Uso
- Validación de patrones en cadenas
- Demostración de autómatas finitos
- Aprendizaje de máquinas de Turing
- Práctica de reconocimiento de patrones