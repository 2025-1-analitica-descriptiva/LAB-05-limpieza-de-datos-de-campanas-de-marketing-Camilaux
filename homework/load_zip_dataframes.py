import pandas as pd


import zipfile
from pathlib import Path


def load_zip_dataframes():
    output_dir = Path("files/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Leer datos de archivos ZIP
    input_dir = Path("files/input")

    # Lista para almacenar todos los dataframes
    all_data = []

    # Leer cada archivo ZIP en el directorio de entrada
    for zip_file in input_dir.glob("*.zip"):
        with zipfile.ZipFile(zip_file, 'r') as zf:
            for filename in zf.namelist():
                if filename.endswith('.csv'):
                    with zf.open(filename) as file:
                        df = pd.read_csv(file)
                        all_data.append(df)
    return output_dir,all_data