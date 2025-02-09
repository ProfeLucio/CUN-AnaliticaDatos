#!/usr/bin/env python3
import pandas as pd

def calcular_kpi_competencias(df):
    # a) Índice de Competencias Digitales
    skill_cols = [
        "CD Identifica fuentes", 
        "CD Copias", 
        "CD Trabajo Colaborativo", 
        "CD Verifica fuentes", 
        "CD Realizo Investigaciones"
    ]
    # Convertir las columnas a numérico
    for col in skill_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    
    # Suma de habilidades por fila y cálculo del índice
    df["suma_habilidades"] = df[skill_cols].sum(axis=1)
    puntaje_max = len(skill_cols) * 4
    kpi7 = (df["suma_habilidades"].sum() / (len(df) * puntaje_max)) * 100

    # b) Porcentaje con pensamiento crítico digital
    valores_positivos = ["Siempre", "Casi Siempre"]
    kpi8 = (df["Verifica las fuentes de información para ayudar a reconocer y comprender el punto de vista o la parcialidad que hay detrás de una información concreta"]
            .isin(valores_positivos).sum() / len(df)) * 100

    # c) Porcentaje que realiza copias de seguridad
    kpi9 = (df["Realizas copias de seguridad de la información que consideras relevante"]
            .isin(valores_positivos).sum() / len(df)) * 100

    print("----- KPI Competencias Digitales -----")
    print(f"KPI 7. Índice de Competencias Digitales: {kpi7:.2f}%")
    print(f"KPI 8. Porcentaje con pensamiento crítico digital: {kpi8:.2f}%")
    print(f"KPI 9. Porcentaje que realiza copias de seguridad: {kpi9:.2f}%")

if __name__ == "__main__":
    df = pd.read_excel("dt.xlsx")
    calcular_kpi_competencias(df)
