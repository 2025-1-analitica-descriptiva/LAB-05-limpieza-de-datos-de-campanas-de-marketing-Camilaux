import pandas as pd


def combine_dataframes(all_data):
    if all_data:
        combined_data = pd.concat(all_data, ignore_index=True)
    return combined_data