"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import datetime


def clean_date(date_str):
    # List of possible date formats
    date_formats = [
        "%Y-%m-%d",  # Year-Month-Day
        "%d-%m-%Y",  # Day-Month-Year
        "%m-%d-%Y",  # Month-Day-Year
        "%Y/%m/%d",  # Year/Month/Day
        "%d/%m/%Y",  # Day/Month/Year
        "%m/%d/%Y",  # Month/Day/Year
    ]

    cleaned_date = None
    for fmt in date_formats:
        try:
            cleaned_date = datetime.datetime.strptime(date_str, fmt).date()
            break  # Stop loop if a valid date is found
        except ValueError:
            continue  # Continue to next format if parsing fails

    return cleaned_date

def clean_numeric_column(column):
    column = column.astype(str)
    column = column.str.replace('$', '').str.replace(',', '')
    column = pd.to_numeric(column, errors='coerce')
    column = column.dropna()
    return column



def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", encoding="utf-8")
    
    df_copia = df.drop_duplicates()
    df_copia = df_copia.dropna()
    df_copia = df_copia.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    df_copia['sexo'] = df_copia['sexo'].str.lower().str.strip()
    
    df_copia['idea_negocio'] = df_copia['idea_negocio'].str.rstrip() 
    df_copia['idea_negocio'] = df_copia['idea_negocio'].str.replace('-', '') 
    df_copia['idea_negocio'] = df_copia['idea_negocio'].str.replace('_', ' ') 
    df_copia['idea_negocio'] = df_copia['idea_negocio'].str.replace('  ', ' ') 
    df_copia['idea_negocio'] = df_copia['idea_negocio'].str.replace(' ', '')  
    df_copia['idea_negocio'] = df_copia['idea_negocio'].str.lower() 
    
    df_copia['tipo_de_emprendimiento'] = df_copia['tipo_de_emprendimiento'].str.lower().str.strip()
    
    df_copia['barrio'] = df_copia['barrio'].str.rstrip()  # Eliminar espacios en blanco al principio y al final
    df_copia['barrio'] = df_copia['barrio'].str.replace(r'[-_]', ' ', regex=True)  # Reemplazar guiones y guiones bajos con espacios
    df_copia['barrio'] = df_copia['barrio'].str.replace('  ', ' ', regex=True)
    df_copia['barrio'] = df_copia['barrio'].str.replace('santo domingo savio ', 'santo domingo savio', regex=True)
    df_copia['barrio'] = df_copia['barrio'].str.replace('cabecera san antonio ', 'cabecera san antonio', regex=True)
    df_copia['barrio'] = df_copia['barrio'].str.replace('playon de los ', 'playon de los', regex=True)
    df_copia['barrio'] = df_copia['barrio'].str.rstrip() 
    
    df_copia['fecha_de_beneficio'] = df_copia['fecha_de_beneficio'].apply(clean_date)
    
    df_copia['monto_del_credito'] = clean_numeric_column(df_copia['monto_del_credito'])
    
    
    df_copia['línea_credito'] = df_copia['línea_credito'].str.lower()
    df_copia['línea_credito'] = df_copia['línea_credito'].str.rstrip()
    df_copia['línea_credito'] = df_copia['línea_credito'].str.replace('-', '') 
    df_copia['línea_credito'] = df_copia['línea_credito'].str.replace('_', ' ')
    df_copia['línea_credito'] = df_copia['línea_credito'].str.replace(' ', '') 
    
    
    
    return df_copia
