from sodapy import Socrata
import pandas as pd

def generate_sample_data(departamento, n):
    client = Socrata("www.datos.gov.co",
                    "axzd54LGExmtlbjuS4Zl3l8zY",
                    username="j.riveros1@utp.edu.co",
                    password="7E1088ro239515?")

    results = client.get("gt2j-8ykr", limit=2000)
    results_df = pd.DataFrame.from_records(results)

    departamento_data = results_df[results_df['departamento_nom'] == departamento.upper()]

    if n > len(departamento_data):
        print(f"-------------------------------------------------------------------------------------\n!!!!!!!!!!!!!!!ADVERTENCIA!!!!!!!!!!!!!!!!!!!!!!!!!!\nEl DataFrame solo tiene {len(departamento_data)} filas. No se pueden seleccionar {n} filas.\nSe mostrarán los {len(departamento_data)} datos disponibles.\n-------------------------------------------------------------------------------------")
        n = len(departamento_data)
    
    sample_data = departamento_data.iloc[:n].copy()
    
    sample_data.reset_index(drop=True, inplace=True)

    #Imputar en la columna de pais_viajo_1_nom los valores nulos con Colombia
    sample_data['pais_viajo_1_nom'].fillna('COLOMBIA', inplace=True)

    
    return sample_data