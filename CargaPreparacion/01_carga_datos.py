#!/usr/bin/env python3
import pandas as pd

def cargar_datos():
    """
    Carga el archivo Excel 'dt.xlsx' y realiza una limpieza básica de columnas.
    """
    try:
        df = pd.read_excel("dt.xlsx")
        # Opcional: quitar espacios en los nombres de columnas
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print("Error al cargar el archivo:", e)
        return None

if __name__ == "__main__":
    df = cargar_datos()
    if df is not None:
        print("Datos cargados correctamente. Muestra de los primeros registros:")
        print(df.head())

