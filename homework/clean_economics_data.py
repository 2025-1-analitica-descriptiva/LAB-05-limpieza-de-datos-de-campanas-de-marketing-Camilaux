def clean_economics_data(combined_data):
    economics_data = combined_data[['client_id', 'cons_price_idx', 'euribor_three_months']].copy()
    return economics_data