#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualizar_boxplots(df):
    sns.set(style="whitegrid")
    kpi_columns = [
        'CD Identifica fuentes',
        'CD Copias',
        'CD Trabajo Colaborativo',
        'CD Verifica fuentes',
        'CD Realizo Investigaciones',
        'IndiceCompetenciasIndividual'
    ]
    
    for col in kpi_columns:
        plt.figure(figsize=(6, 4))
        sns.boxplot(y=df[col], color="skyblue")
        plt.title(f"{col}", fontsize=14)
        plt.ylabel(col, fontsize=12)
        plt.xlabel("")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    df = pd.read_excel("dt.xlsx")
    visualizar_boxplots(df)

