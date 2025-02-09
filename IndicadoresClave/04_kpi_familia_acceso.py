#!/usr/bin/env python3
import pandas as pd

def calcular_kpi_familia_acceso(df):
    # a) Nivel educativo del acudiente
    educacion_mapping = {
        "Básica": 1,
        "Secundaria": 2,
        "Técnica": 3,
        "Universitaria": 4
    }
    df["educacion_num"] = df["Nivel de escolaridad del acudiente"].map(educacion_mapping)
    if df["educacion_num"].notnull().sum() > 0:
        kpi1 = df["educacion_num"].sum() / df["educacion_num"].notnull().sum()
    else:
        kpi1 = None

    # b) Porcentaje de acompañamiento familiar
    acompanamiento_count = df["Acudiente en la institución educativa"].notna().sum()
    kpi2 = (acompanamiento_count / len(df)) * 100

    # c) Tamaño promedio del hogar
    df["personas_hogar"] = pd.to_numeric(df["¿Cuántas personas viven en tu hogar?"], errors="coerce")
    kpi3 = df["personas_hogar"].mean()

    print("----- KPI Familia y Acceso -----")
    if kpi1 is not None:
        print(f"KPI 1. Nivel educativo promedio del acudiente: {kpi1:.2f}")
    else:
        print("KPI 1. No se pudo calcular el nivel educativo.")
    print(f"KPI 2. Porcentaje de acompañamiento familiar: {kpi2:.2f}%")
    print(f"KPI 3. Tamaño promedio del hogar: {kpi3:.2f}")

if __name__ == "__main__":
    df = pd.read_excel("dt.xlsx")
    calcular_kpi_familia_acceso(df)

