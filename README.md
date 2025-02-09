# Proyecto de Análisis de Competencias Digitales en Estudiantes

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar la influencia del **acompañamiento familiar** y la **escolaridad del acudiente** en el desarrollo de competencias digitales en estudiantes de 10º y 11º grado en instituciones públicas de Buenaventura. A través del uso de **Python en Google Colab**, se han desarrollado diversos scripts para la **exploración, visualización y modelado de datos**.

El estudio está basado en el análisis de **indicadores clave de desempeño (KPI)**, correlaciones entre variables y modelos estadísticos como la **regresión lineal múltiple**.

## Estructura del Proyecto
El repositorio contiene los siguientes archivos de código fuente, organizados según las distintas fases del análisis:

### 📂 1. Carga y Preparación de Datos
- `01_carga_datos.py`: Carga y preprocesamiento del archivo de datos `dt.xlsx`, incluyendo limpieza de valores nulos y transformación de variables categóricas en numéricas.

### 📊 2. Exploración y Análisis Descriptivo
- `02_analisis_descriptivo.py`: Cálculo de estadísticos básicos (media, mediana, moda) para comprender la distribución de variables clave.
- `03_visualizacion_boxplot.py`: Genera gráficos de caja (boxplots) para visualizar la distribución de los KPI de competencias digitales.

### 🔢 3. Cálculo de Indicadores Clave de Desempeño (KPI)
- `04_kpi_familia_acceso.py`: Cálculo de KPI relacionados con el nivel educativo del acudiente, acompañamiento familiar y acceso a internet.
- `05_kpi_competencias_tic.py`: Medición de indicadores de competencia digital, incluyendo verificación de fuentes, copias de seguridad y pensamiento crítico.
- `06_kpi_uso_tic.py`: Evaluación del uso de herramientas TIC en entornos académicos y frecuencia de acceso a internet.

### 🔗 4. Análisis de Correlaciones
- `07_matriz_correlacion.py`: Construcción de la matriz de correlación entre variables clave, visualizada con un heatmap.
- `08_correlaciones_especificas.py`: Evaluación de correlaciones particulares entre variables de interés (ej. acceso a internet vs. competencias digitales, acompañamiento familiar vs. desarrollo de TIC).

### 📈 5. Modelado Estadístico: Regresión Lineal
- `09_regresion_lineal.py`: Implementación de un modelo de regresión lineal múltiple para predecir el impacto del acompañamiento familiar y otras variables en el índice de competencias digitales.
- `10_evaluacion_modelo.py`: Análisis de residuos del modelo de regresión para evaluar su ajuste y cumplimiento de supuestos estadísticos.

## 🛠️ Requisitos y Configuración
Para ejecutar los scripts, asegúrate de contar con las siguientes librerías instaladas en tu entorno de Google Colab o local:

```bash
pip install pandas numpy matplotlib seaborn openpyxl statsmodels
```

Además, el archivo `dt.xlsx` debe estar cargado en el entorno de ejecución.

## 🚀 Uso de los Scripts
Cada script está diseñado para ejecutarse de manera independiente, pero se recomienda seguir el orden numerado para obtener una interpretación coherente de los datos. Puedes ejecutar los archivos en Colab con:

```python
%run nombre_del_script.py
```

## 🤝 Contacto y Contribuciones
Si deseas aportar mejoras al análisis o tienes dudas sobre los scripts, puedes contactarnos o contribuir con mejoras en **GitHub**.

