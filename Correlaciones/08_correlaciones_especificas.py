#!/usr/bin/env python3
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

def calcular_correlacion(df, var1, var2, label1, label2):
    data = df[[var1, var2]].dropna()
    if len(data) < 2:
        print(f"No hay suficientes datos para calcular la correlación entre {label1} y {label2}.")
        print("-" * 50)
        return np.nan, np.nan
    corr, p_value = pearsonr(data[var1], data[var2])
    print(f"Correlación entre {label1} y {label2}:")
    print(f"  Coeficiente de Pearson: {corr:.3f}")
    print(f"  Valor p: {p_value:.3f}")
    print("-" * 50)
    return corr, p_value

if __name__ == "__main__":
    df = pd.read_excel("dt.xlsx")
    
    # Realizar las mismas transformaciones que en el heatmap
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
    
    print("----- Correlaciones Específicas -----")
    calcular_correlacion(df, "acceso_internet", "IndiceCompetenciasIndividual",
                         "Acceso a Internet", "Índice de Competencias Digitales")
    calcular_correlacion(df, "dispositivos", "uso_TIC_acad",
                         "Disponibilidad de Dispositivos", "Uso de TIC Académicas")
    calcular_correlacion(df, "educacion_num", "backup",
                         "Nivel Educativo del Acudiente", "Realización de Copias de Seguridad")
    calcular_correlacion(df, "educacion_num", "pensamiento",
                         "Nivel Educativo del Acudiente", "Pensamiento Crítico Digital")
    calcular_correlacion(df, "DiasPorSemana", "IndiceCompetenciasIndividual",
                         "Frecuencia de Uso de Internet", "Índice de Competencias Digitales")
    calcular_correlacion(df, "CD Trabajo Colaborativo", "CD Realizo Investigaciones",
                         "Uso de Herramientas Colaborativas", "Realización de Investigaciones Digitales")
    calcular_correlacion(df, "TieneAlgunaRed", "uso_TIC_acad",
                         "Presencia en Redes Sociales", "Uso de TIC Académicas")
    calcular_correlacion(df, "tipo_conexion_num", "IndiceCompetenciasIndividual",
                         "Tipo de Conexión a Internet", "Índice de Competencias Digitales")
    # Adicional: Influencia del Nivel de Formación del Acudiente
    calcular_correlacion(df, "educacion_num", "IndiceCompetenciasIndividual",
                         "Nivel Educativo del Acudiente", "Índice de Competencias Digitales")
    calcular_correlacion(df, "educacion_num", "backup",
                         "Nivel Educativo del Acudiente", "Realización de Copias de Seguridad")
    calcular_correlacion(df, "educacion_num", "pensamiento",
                         "Nivel Educativo del Acudiente", "Pensamiento Crítico Digital")
    calcular_correlacion(df, "Estrato", "IndiceCompetenciasIndividual",
                         "Estrato Socioeconómico", "Índice de Competencias Digitales")

