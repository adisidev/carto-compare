import pandas as pd
import sys

def filter_csv_by_suffix(input_csv, column_name, regex, name_):
    df = pd.read_csv(input_csv)

    filtered_df = df[df[column_name].str.contains(regex, na=False)]
    
    filtered_df.to_csv(name_, index=False)

if __name__ == "__main__":
    input_csv = "similarity.csv"
    column_name = " altered_map"
    
    filter_csv_by_suffix(input_csv, column_name, r'^.*_\d+\.geojson$', "f4carto_raw.csv")
    
    filter_csv_by_suffix(input_csv, column_name, r'.*_5FCarto\.geojson$', "5fcarto_raw.csv")
    
    filter_csv_by_suffix(input_csv, column_name, r'.*_flow_based\.geojson$', "flow_based_raw.csv")
    
