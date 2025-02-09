#!/usr/bin/env python3
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def evaluar_modelo(modelo):
    residuos = modelo.resid
    ajustados = modelo.fittedvalues

    # Gráfico de Residuos vs. Valores Ajustados
    plt.figure(figsize=(6, 4))
    plt.scatter(ajustados, residuos, alpha=0.5)
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel("Valores Ajustados")
    plt.ylabel("Residuos")
    plt.title("Residuos vs. Valores Ajustados")
    plt.show()

    # Histograma de los residuos
    plt.figure(figsize=(6, 4))
    plt.hist(residuos, bins=30, alpha=0.7, color='gray')
    plt.title("Distribución de Residuos")
    plt.xlabel("Residuos")
    plt.ylabel("Frecuencia")
    plt.show()

if __name__ == "__main__":
    # Para evaluar el modelo se vuelve a cargar y transformar el conjunto de datos.
    df = pd.read_excel("dt.xlsx")
    df["AcompanamientoFamiliar"] = df["Acudiente en la institución educativa"].apply(lambda x: 1 if pd.notna(x) else 0)
    df["Estrato"] = pd.to_numeric(df["Estrato"], errors="coerce")
    df["internet_bin"] = df["¿Cuenta con acceso a internet en su hogar?"].str.strip().str.lower().map({
        "si": 1, "sí": 1, "no": 0
    })
    df["DiasPorSemana"] = pd.to_numeric(df["DiasPorSemana"], errors="coerce")
    df["TieneDispositivos"] = df["TieneDispositivos"].str.strip().str.lower().map({
        "sí": 1, "si": 1, "no": 0
    })
    df["IndiceCompetenciasIndividual"] = pd.to_numeric(df["IndiceCompetenciasIndividual"], errors="coerce")
    
    y = df["IndiceCompetenciasIndividual"]
    X = df[["AcompanamientoFamiliar", "Estrato", "internet_bin", "DiasPorSemana", "TieneDispositivos"]]
    df_model = pd.concat([X, y], axis=1).dropna()
    X = df_model.drop("IndiceCompetenciasIndividual", axis=1)
    y = df_model["IndiceCompetenciasIndividual"]
    X = sm.add_constant(X)
    
    modelo = sm.OLS(y, X).fit()
    evaluar_modelo(modelo)

