#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def matriz_correlacion(df):
    # Seleccionar variables de interés para la correlación
    variables_interes = ['acceso_internet', 'IndiceCompetenciasIndividual', 'dispositivos', 
                         'uso_TIC_acad', 'educacion_num', 'backup', 'pensamiento', 
                         'DiasPorSemana', 'tipo_conexion_num', 'TieneAlgunaRed', 'Estrato']
    
    df_corr = df[variables_interes].dropna()
    matriz_corr = df_corr.corr()
    
    print("Matriz de Correlación:")
    print(matriz_corr)
    
    plt.figure(figsize=(12, 10))
    sns.heatmap(matriz_corr, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    plt.title("Matriz de Correlación entre Variables Clave")
    plt.show()

if __name__ == "__main__":
    # Cargar datos
    df = pd.read_excel("dt.xlsx")
    
    # Realizar las transformaciones necesarias
    df['acceso_internet'] = df["¿Cuenta con acceso a internet en su hogar?"].str.strip().str.lower().map({
        "si": 1, "sí": 1, "no": 0
    })
    df["IndiceCompetenciasIndividual"] = pd.to_numeric(df["IndiceCompetenciasIndividual"], errors="coerce")
    df['dispositivos'] = df["TieneDispositivos"].str.strip().str.lower().map({
        "sí": 1, "si": 1, "no": 0
    })
    uso_tic_mapping = {
        "nunca": 0,
        "casi nunca": 1,
        "ocasionalmente": 2,
        "casi siempre": 3,
        "siempre": 4
    }
    df['uso_TIC_acad'] = df["Comparto información con profesores relacionados con mis labores escolares (tareas, búsqueda de información, realización de presentaciones, entre otras)"]\
                         .str.strip().str.lower().map(uso_tic_mapping)
    educacion_mapping = {
        "primaria": 1,
        "secundaria": 2,
        "técnico": 3,
        "profesional": 4,
        "postgrado": 5
    }
    df['educacion_num'] = df["Nivel de escolaridad del acudiente"].str.strip().str.lower().map(educacion_mapping)
    df['backup'] = df["Realizas copias de seguridad de la información que consideras relevante"]\
                   .str.strip().str.lower().map(uso_tic_mapping)
    df['pensamiento'] = df["Verifica las fuentes de información para ayudar a reconocer y comprender el punto de vista o la parcialidad que hay detrás de una información concreta"]\
                        .str.strip().str.lower().map(uso_tic_mapping)
    df["DiasPorSemana"] = pd.to_numeric(df["DiasPorSemana"], errors="coerce")
    df['Estrato'] = pd.to_numeric(df['Estrato'], errors='coerce')
    df["TieneAlgunaRed"] = df["TieneAlgunaRed"].str.strip().str.lower().map({
        "sí": 1, "si": 1, "no": 0
    })
    tipo_conexion_mapping = {
        "Red Banda ancha ADSL mediante un cable modem wifi": 1,
        "Red Banda ancha HFC mediante un cable modem wifi": 2,
        "Red de banda ancha satelital": 3,
        "No sabe": 4,
        "Red banda ancha móvil a través de celular": 5,
        "Red banda ancha fibra óptica": 6
    }
    df["tipo_conexion_num"] = df["El tipo de acceso a internet en su hogar es:"].map(tipo_conexion_mapping)
    
    matriz_correlacion(df)

