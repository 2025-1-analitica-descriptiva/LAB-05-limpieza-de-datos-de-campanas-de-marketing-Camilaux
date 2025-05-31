import pandas as pd


def clean_campaign_dataframe(combined_data):
    campaign_data = combined_data[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'day', 'month']].copy()
    campaign_data['previous_outcome'] = campaign_data['previous_outcome'].apply(lambda x: 1 if x == 'success' else 0)
    campaign_data['campaign_outcome'] = campaign_data['campaign_outcome'].apply(lambda x: 1 if x == 'yes' else 0)

    # Convertir nombres de meses a números
    month_map = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    campaign_data['month_num'] = campaign_data['month'].str.lower().map(month_map)

    # Crear fechas usando componentes numéricos (más eficiente)
    campaign_data['last_contact_date'] = pd.to_datetime(dict(
        year=2022,
        month=campaign_data['month_num'],
        day=campaign_data['day']
    ))

    # Seleccionar las columnas finales para campaign.csv
    campaign_data = campaign_data[['client_id', 'number_contacts', 'contact_duration', 'previous_campaign_contacts', 'previous_outcome', 'campaign_outcome', 'last_contact_date']]
    return campaign_data