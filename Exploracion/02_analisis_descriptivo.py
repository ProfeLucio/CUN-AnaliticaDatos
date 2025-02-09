#!/usr/bin/env python3
import pandas as pd

def analisis_descriptivo(df):
    # Definir las columnas cuantitativas de interés
    columnas_cuantitativas = [
        'Edad del acudiente',
        '¿Cuántas personas viven en tu hogar?',
        'IndiceCompetenciasIndividual',
        'DiasPorSemana'
    ]
    
    df_num = df[columnas_cuantitativas]
    
    print("=== Estadísticas descriptivas ===")
    print(df_num.describe())
    
    # Calcular media, mediana y moda para cada columna
    for col in columnas_cuantitativas:
        serie = df[col].dropna()
        media = serie.mean()
        mediana = serie.median()
        moda = serie.mode().values  # Puede haber más de un valor modal
        print(f"\n--- {col} ---")
        print(f"Media: {media:.2f}")
        print(f"Mediana: {mediana}")
        print(f"Moda(s): {moda}")

if __name__ == "__main__":
    df = pd.read_excel("dt.xlsx")
    analisis_descriptivo(df)

