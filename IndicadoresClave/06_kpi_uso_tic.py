#!/usr/bin/env python3
import pandas as pd

def calcular_kpi_uso_tic(df):
    # a) Porcentaje que usa TIC en actividades académicas
    col_uso_tic = "Comparto información con profesores relacionados con mis labores escolares (tareas, búsqueda de información, realización de presentaciones, entre otras)"
    valores_positivos = ["Siempre", "Casi Siempre"]
    kpi10 = (df[col_uso_tic].isin(valores_positivos).sum() / len(df)) * 100

    # b) Frecuencia promedio de uso de internet (días/semana)
    df["DiasPorSemana"] = pd.to_numeric(df["DiasPorSemana"], errors="coerce")
    kpi11 = df["DiasPorSemana"].mean()

    print("----- KPI Uso de TIC -----")
    print(f"KPI 10. Porcentaje que usa TIC en actividades académicas: {kpi10:.2f}%")
    print(f"KPI 11. Frecuencia promedio de uso de internet (días/semana): {kpi11:.2f}")

if __name__ == "__main__":
    df = pd.read_excel("dt.xlsx")
    calcular_kpi_uso_tic(df)

