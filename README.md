# kobo-bpm-check-list
Extractor automático de KoboToolbox con Python (limpieza de datos y mapeo de etiquetas) + Tablero de control en Power BI para visualización de cumplimiento (CUMPLE/NO CUMPLE) del proceso BPM en una empresa regulada.
# 📊 Sistema de Extracción y Visualización KoboToolbox (BPM)

Este proyecto automatiza el ciclo de vida de los datos de inspecciones BPM (Buenas Prácticas de Manufactura): desde la extracción directa de la API de KoboToolbox hasta la visualización de indicadores clave en Power BI.

## 🚀 Características del Proyecto
*   **Extracción Automatizada:** Script en Python que conecta con la API v2 de KoboToolbox.
*   **Limpieza de Datos:** Transformación de encabezados técnicos a formatos legibles.
*   **Seguridad y Privacidad:** 
    *   **Anonimización:** Las preguntas reales han sido sustituidas por etiquetas genéricas (Pregunta 1, Pregunta 2, etc.) para proteger la confidencialidad del proceso.
    *   **Mapeo de Respuestas:** Conversión de códigos técnicos (`A`/`R`) a etiquetas de cumplimiento (`CUMPLE`/`NO CUMPLE`).
*   **Filtros Inteligentes:** Procesamiento de datos a partir de fechas específicas (Abril 2026).
*   **Dashboard de Control:** Visualización interactiva en Power BI para el análisis de cumplimiento por áreas.

## 🛠️ Stack Tecnológico
*   **Python 3.x** (Librerías: `pandas`, `requests`, `openpyxl`)
*   **KoboToolbox API v2**
*   **Power BI Desktop**
*   **Excel** (como base de datos intermedia)

## 📁 Estructura del Repositorio
*   `main.py`: Script principal de extracción y limpieza.
*   `requirements.txt`: Librerías necesarias para ejecutar el código.
*   `BPM_Dashboard_Demo.pbix`: Archivo de Power BI con el tablero de control.
*   `data_demo.xlsx`: Ejemplo de la estructura de datos generada (datos anonimizados).

## 🔧 Configuración
1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Configura tu `TOKEN` de KoboToolbox en la variable de entorno o directamente en el script (solo para uso local).
3. Ejecuta el script:
   ```bash
   python main.py
   ```

---
> **Nota Ética:** Los datos y preguntas mostrados en este repositorio son **ficticios y con fines demostrativos**. Se han modificado para proteger la propiedad intelectual y los resultados operativos de la organización original.
