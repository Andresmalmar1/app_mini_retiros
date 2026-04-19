# 💰 Planificación de Mini Retiros y Retiro Final

Aplicación en Python para calcular cuánto necesitas invertir **mensualmente extra** en **dos fondos separados** para financiar mini retiros y un retiro final, considerando la inflación para mantener tu poder adquisitivo.

## 🎯 Qué hace

Esta aplicación te ayuda a planificar financieramente tu retiro considerando:

- **Fondo de Mini Retiros**: Calcula la inversión mensual necesaria para financiar retiros periódicos de 6 meses cada uno
- **Fondo de Retiro Final**: Calcula la inversión mensual necesaria para financiar 20 años de retiro completo
- **Inflación**: Ajusta todos los cálculos para mantener el poder adquisitivo
- **Proyección Anual**: Muestra el saldo de cada fondo por año con las inversiones calculadas

## 📊 Funcionalidades

- Calcula montos necesarios ajustados por inflación para mini retiros (6 meses) y retiro final (20 años)
- **Muestra la asignación de tu inversión actual entre ambos fondos**
- **Determina los montos mensuales EXTRA requeridos** para cada fondo por separado
- Muestra una proyección anual detallada con saldo de cada fondo por año
- Interfaz moderna y fácil de usar
- Resultados en pesos mexicanos

## 📋 Requisitos

- Python 3.8 o superior
- Tkinter (incluido con Python)

## 🚀 Instalación

1. Navega al directorio del proyecto:

```bash
cd C:\Users\andre\OneDrive\Proyectos_GitHub_Copilot\app_mini_retiros
```

2. Ejecuta la aplicación:

```bash
python mini_retiros_app.py
```

## 📖 Uso

### Paso 1: Ingresa tus datos personales y financieros

1. **Monto actual para gastos fijos**: Cuánto necesitas actualmente para cubrir tus gastos mensuales
2. **Edad actual**: Tu edad actual
3. **Monto invertido hoy**: Dinero que ya tienes invertido
4. **Tasa de inflación (%)**: Inflación anual esperada (ej: 4%)
5. **Tasa de rendimiento (%)**: Rendimiento anual esperado de tus inversiones (ej: 8%)

### Paso 2: Configura tu plan de retiros

1. **Edad del primer mini retiro**: A qué edad quieres hacer tu primer mini retiro
2. **Duración mini retiro (meses)**: Cuántos meses cubrirá cada mini retiro (por defecto: 6)
3. **Total de mini retiros**: Cuántos mini retiros planeas hacer
4. **Frecuencia (años)**: Cada cuántos años harás un mini retiro
5. **Edad retiro final**: A qué edad harás tu retiro final
6. **Duración retiro final (años)**: Cuántos años cubrirá tu retiro final (por defecto: 20)

### Paso 3: Calcula y analiza

1. **Presiona "Calcular Plan Financiero"**
2. **Revisa los resultados**:
   - Monto necesario para cada mini retiro (6 meses ajustados por inflación)
   - Monto necesario para el retiro final (20 años ajustados por inflación)
   - **Asignación de tu inversión actual** entre mini retiros y retiro final
   - **Monto mensual extra requerido para el fondo de mini retiros**
   - **Monto mensual extra requerido para el fondo de retiro final**
3. **Analiza la tabla de proyección**: Muestra año a año el saldo de cada fondo con las inversiones calculadas

## 📊 Ejemplo de Uso

**Datos de entrada:**
- Gastos mensuales: $15,000 MXN
- Edad actual: 30 años
- Inversión actual: $0
- Inflación: 4%
- Rendimiento: 8%
- Primer mini retiro: 50 años
- Duración mini retiro: 6 meses
- Total mini retiros: 5
- Frecuencia: 2 años
- Retiro final: 65 años
- Duración retiro final: 20 años

**Resultados calculados:**
- Monto por mini retiro: Aproximadamente $108,000 MXN (ajustado por inflación)
- Monto retiro final: Aproximadamente $540,000 MXN (ajustado por inflación)
- Asignación inversión actual - Mini retiros: $0 MXN
- Asignación inversión actual - Retiro final: $0 MXN
- Monto mensual extra - Mini retiros: Aproximadamente $1,200 MXN
- Monto mensual extra - Retiro final: Aproximadamente $2,800 MXN

## 🎨 Interfaz de Usuario

La aplicación cuenta con una interfaz moderna y organizada:

- **Panel izquierdo**: Campos de entrada organizados en filas compactas
- **Panel derecho**: Tabla de proyección anual con saldo de cada fondo
- **Resultados destacados**: Muestra claramente las dos inversiones mensuales requeridas
  - **Sección inferior**: Botón de cálculo y **resultados destacados**

- **Panel derecho**: Tabla de proyección anual con evolución detallada del saldo

- **Sección de resultados mejorada**:
  - Caja destacada con fondo azul
  - Tres resultados principales en cajas separadas
  - Inversión mensual requerida en caja prominente con fondo azul
  - Fuentes más grandes y colores diferenciados

- **Diseño responsive**: La ventana se puede redimensionar para adaptarse a diferentes tamaños de pantalla

## 💡 Ejemplo de uso

Imagina que actualmente necesitas $15,000 mensuales para tus gastos, tienes 30 años, ya tienes $50,000 invertidos, esperas 4% de inflación y 8% de rendimiento. Quieres hacer mini retiros cada 2 años empezando a los 50 años (total 5 mini retiros) y un retiro final a los 65 años.

La aplicación calculará:
- Monto por mini retiro: ~$25,000 (ajustado por inflación)
- Monto retiro final: ~$35,000 (ajustado por inflación)
- Inversión mensual: ~$2,500

## 🔧 Características técnicas

- **Cálculos financieros precisos**: Usa fórmulas de valor presente y futuro
- **Ajuste por inflación**: Todos los montos se ajustan para mantener poder adquisitivo
- **Proyección detallada**: Tabla anual con evolución del saldo
- **Interfaz moderna**: Diseño intuitivo con colores diferenciados
- **Validaciones**: Verifica que los datos sean lógicos y positivos
- **Formato MXN**: Muestra todos los montos en pesos mexicanos

## 📈 Fórmulas utilizadas

- **Monto futuro con inflación**: `monto_actual × (1 + inflación)^años`
- **Valor presente**: `monto_futuro ÷ (1 + tasa_mensual)^meses`
- **Inversión mensual**: Resuelve la ecuación de anualidad para el valor presente requerido

## 🤝 Contribución

Si encuentras errores o tienes sugerencias de mejora, por favor crea un issue o envía un pull request.