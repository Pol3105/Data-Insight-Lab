# Data-Insight-Lab 📊

> **Dashboard Interactivo de Análisis de Datos construido con Python y Streamlit.** Incluye análisis exploratorio de datos (EDA), visualizaciones dinámicas y seguimiento de KPIs usando Pandas.

---

## 🚀 Sobre este Proyecto (Mi viaje en Datos)

¡Bienvenido a mi portafolio! **Este es mi primer proyecto en el campo del Análisis de Datos.** Representa el punto de partida de mi camino hacia la ciencia de datos. Mi objetivo era ir más allá de las hojas de cálculo estáticas y construir una **herramienta interactiva en vivo** que consuma datos financieros en tiempo real. Aunque es solo el comienzo, demuestra mi capacidad para integrar APIs, manejar DataFrames y crear interfaces de usuario amigables.

**Próximamente:** Estaré añadiendo constantemente proyectos más complejos a este repositorio a medida que domine SQL, Machine Learning y un análisis estadístico más profundo.

---

## 🛠️ Cómo lo construí (Paso a paso)

Este proyecto fue construido utilizando un proceso iterativo para asegurar robustez y usabilidad:

### 1. Configuración del Entorno
Configuré un entorno de desarrollo en la nube utilizando **GitHub Codespaces**, asegurando un espacio de trabajo limpio y reproducible con Python.

### 2. Extracción de Datos (ETL)
En lugar de utilizar archivos CSV estáticos, implementé una conexión a la **API de Yahoo Finance** (`yfinance`). Esto permite que el dashboard obtenga datos del mercado de valores en tiempo real, haciendo que la herramienta sea útil para el análisis de mercado actual.

### 3. Procesamiento de Datos con Pandas
Utilicé `pandas` para estructurar los datos JSON crudos en DataFrames, manejando fechas y limpiando valores faltantes para preparar el conjunto de datos para su visualización.

### 4. Visualización Interactiva
Elegí **Plotly** sobre librerías estáticas (como Matplotlib) para crear gráficos de velas (Candlestick) interactivos. Esto permite a los usuarios hacer zoom, desplazarse y pasar el cursor sobre puntos de datos específicos para ver los precios de apertura/cierre.

### 5. Interfaz de Usuario (UI/UX)
Usando **Streamlit**, construí una barra lateral para las entradas del usuario. Implementé:
* **Menús desplegables** para una selección rápida de activos populares (Apple, Bitcoin, etc.).
* **Validación de entrada** y manejo de errores (bloques Try/Except) para evitar que la aplicación se cierre si se introduce un símbolo inválido.

---

## 💻 Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **Framework Web:** Streamlit
* **Manipulación de Datos:** Pandas
* **Visualización de Datos:** Plotly Graph Objects
* **API:** yfinance

---

## ⚙️ Cómo ejecutarlo localmente

Si deseas clonar este repositorio y ejecutar el dashboard en tu máquina:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Pol3105/Data-Insight-Lab.git](https://github.com/Pol3105/Data-Insight-Lab.git)
    cd Data-Insight-Lab
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install streamlit pandas yfinance plotly
    ```

3.  **Ejecutar la aplicación:**
    ```bash
    streamlit run app.py
    ```

---

*Creado con ❤️ por Pablo Rejon Camacho*
