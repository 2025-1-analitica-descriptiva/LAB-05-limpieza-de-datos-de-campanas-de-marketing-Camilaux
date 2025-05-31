"""
Escriba el codigo que ejecute la accion solicitada.
"""

# pylint: disable=import-outside-toplevel

from homework.clean_client_data import clean_client_data
from homework.clean_campaign_dataframe import clean_campaign_dataframe
from homework.clean_economics_data import clean_economics_data
from homework.combine_dataframes import combine_dataframes
from homework.generate_csv_files import generate_csv_files
from homework.load_zip_dataframes import load_zip_dataframes

def clean_campaign_data():
    """
    En esta tarea se le pide que limpie los datos de una campaña de
    marketing realizada por un banco, la cual tiene como fin la
    recolección de datos de clientes para ofrecerls un préstamo.

    La información recolectada se encuentra en la carpeta
    files/input/ en varios archivos csv.zip comprimidos para ahorrar
    espacio en disco.

    Usted debe procesar directamente los archivos comprimidos (sin
    descomprimirlos). Se desea partir la data en tres archivos csv
    (sin comprimir): client.csv, campaign.csv y economics.csv.
    Cada archivo debe tener las columnas indicadas.

    Los tres archivos generados se almacenarán en la carpeta files/output/.

    client.csv:
    - client_id
    - age
    - job: se debe cambiar el "." por "" y el "-" por "_"
    - marital
    - education: se debe cambiar "." por "_" y "unknown" por pd.NA
    - credit_default: convertir a "yes" a 1 y cualquier otro valor a 0
    - mortage: convertir a "yes" a 1 y cualquier otro valor a 0

    campaign.csv:
    - client_id
    - number_contacts
    - contact_duration
    - previous_campaing_contacts
    - previous_outcome: cmabiar "success" por 1, y cualquier otro valor a 0
    - campaign_outcome: cambiar "yes" por 1 y cualquier otro valor a 0
    - last_contact_day: crear un valor con el formato "YYYY-MM-DD",
        combinando los campos "day" y "month" con el año 2022.

    economics.csv:
    - client_id
    - const_price_idx
    - eurobor_three_months



    """
    # Crear directorio de salida si no existe
    output_dir, all_data = load_zip_dataframes()
    
    # Combinar todos los dataframes
    combined_data = combine_dataframes(all_data)

    # Limpiar y transformar los datos para client.csv
    client_data = clean_client_data(combined_data)

    # Limpiar y transformar los datos para campaign.csv
    campaign_data = clean_campaign_dataframe(combined_data)

    # Limpiar y transformar los datos para economics.csv
    economics_data = clean_economics_data(combined_data)

    # Guardar los dataframes en archivos CSV
    generate_csv_files(output_dir, client_data, campaign_data, economics_data)

    return

if __name__ == "__main__":
    clean_campaign_data()
