def generate_csv_files(output_dir, client_data, campaign_data, economics_data):
    # Guardar client.csv
    client_data.to_csv(output_dir / 'client.csv', index=False)
    # Guardar campaign.csv
    campaign_data.to_csv(output_dir / 'campaign.csv', index=False)
    # Guardar economics.csv
    economics_data.to_csv(output_dir / 'economics.csv', index=False)
    print("Archivos generados en:", output_dir)