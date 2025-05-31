import pandas as pd


def clean_client_data(combined_data):
    client_data = combined_data[['client_id', 'age', 'job', 'marital', 'education', 'credit_default', 'mortgage']].copy()
    client_data['job'] = client_data['job'].str.replace('.', '').str.replace('-', '_')
    client_data['education'] = client_data['education'].str.replace('.', '_').replace('unknown', pd.NA)
    client_data['credit_default'] = client_data['credit_default'].apply(lambda x: 1 if x == 'yes' else 0)
    client_data['mortgage'] = client_data['mortgage'].apply(lambda x: 1 if x == 'yes' else 0)
    return client_data