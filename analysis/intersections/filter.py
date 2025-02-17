import pandas as pd
import sys
import re

def process_csv(input_csv, fill_word, output_csv, remove_from_second_last_underscore=False):
    df = pd.read_csv(input_csv)
  
    df.rename(columns={"map_name": "Map"}, inplace=True)

    def modify_map(s):
        if remove_from_second_last_underscore:
            new_s = re.sub(r'^(.*)_[^_]+_[^_]+$', r'\1', s)
            return new_s
        else:
            new_s = re.sub(r'_(?!.*_).*$', '', s)
            return new_s

    df["Map"] = df["Map"].apply(modify_map)

    df["algorithm"] = fill_word

    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    # ============================
    input_csv = "f4carto_raw.csv"         # Filename of the CSV
    fill_word = "f4carto"             # Word to fill the new "algorithm" column
    output_csv = "f4carto.csv"           # Name of the output file
    # ============================

    process_csv(input_csv, fill_word, output_csv)
    
    input_csv = "5fcarto_raw.csv"         # Filename of the CSV
    fill_word = "5fcarto"             # Word to fill the new "algorithm" column
    output_csv = "5fcarto.csv"           # Name of the output file
    # ============================

    process_csv(input_csv, fill_word, output_csv)
    
    input_csv = "flow_based_raw.csv"         # Filename of the CSV
    fill_word = "flow_based"             # Word to fill the new "algorithm" column
    output_csv = "flow_based.csv"           # Name of the output file
    # ============================

    process_csv(input_csv, fill_word, output_csv, remove_from_second_last_underscore=True)
