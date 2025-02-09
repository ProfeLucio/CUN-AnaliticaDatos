#!/usr/bin/env python3
import pandas as pd
import statsmodels.api as sm

def modelo_regresion_lineal(df):
    # Transformaciones básicas para el modelo
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
    
    # Definir variable dependiente (Y) y las independientes (X)
    y = df["IndiceCompetenciasIndividual"]
    X = df[["AcompanamientoFamiliar", "Estrato", "internet_bin", "DiasPorSemana", "TieneDispositivos"]]
    
    # Eliminar filas con valores nulos
    df_model = pd.concat([X, y], axis=1).dropna()
    X = df_model.drop("IndiceCompetenciasIndividual", axis=1)
    y = df_model["IndiceCompetenciasIndividual"]
    
    # Agregar la constante (intercepto)
    X = sm.add_constant(X)
    
    # Ajustar el modelo con mínimos cuadrados ordinarios (OLS)
    modelo = sm.OLS(y, X).fit()
    print(modelo.summary())
    return modelo

if __name__ == "__main__":
    df = pd.read_excel("dt.xlsx")
    print("Tamaño del DataFrame original:", df.shape)
    modelo = modelo_regresion_lineal(df)

