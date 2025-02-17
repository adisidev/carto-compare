import pandas as pd
import sys
import re


def process_csv(input_csv, column_to_remove, column_to_rename, fill_word, output_csv, remove_from_second_last_underscore=False):
    df = pd.read_csv(input_csv)

    if column_to_remove in df.columns:
        df.drop(columns=[column_to_remove], inplace=True)
    else:
        print(f"Column '{column_to_remove}' not found. Skipping removal.", file=sys.stderr)

    if column_to_rename in df.columns:
        df.rename(columns={column_to_rename: "Map"}, inplace=True)
    else:
        print(f"Column '{column_to_rename}' not found.", file=sys.stderr)
        sys.exit(1)

    def modify_map(s):
        if remove_from_second_last_underscore:
            # Remove from the second last underscore onward.
            # This regex captures everything up to the second last underscore.
            new_s = re.sub(r'^(.*)_[^_]+_[^_]+$', r'\1', s)
            return new_s
        else:
            # Remove from the last underscore onward.
            new_s = re.sub(r'_(?!.*_).*$', '', s)
            return new_s

    df["Map"] = df["Map"].apply(modify_map)

    df["algorithm"] = fill_word

    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    column_to_remove = "base_map"    # Column name to remove
    column_to_rename = " altered_map"       # Column name to rename to "map_name"

    # ============================
    input_csv = "f4carto_raw.csv"         # Filename of the CSV
    fill_word = "f4carto"             # Word to fill the new "algorithm" column
    output_csv = "f4carto.csv"           # Name of the output file
    # ============================

    process_csv(input_csv, column_to_remove, column_to_rename, fill_word, output_csv)
    
    input_csv = "5fcarto_raw.csv"         # Filename of the CSV
    fill_word = "5fcarto"             # Word to fill the new "algorithm" column
    output_csv = "5fcarto.csv"           # Name of the output file
    # ============================

    process_csv(input_csv, column_to_remove, column_to_rename, fill_word, output_csv)
    
    input_csv = "flow_based_raw.csv"         # Filename of the CSV
    fill_word = "flow_based"             # Word to fill the new "algorithm" column
    output_csv = "flow_based.csv"           # Name of the output file
    # ============================

    process_csv(input_csv, column_to_remove, column_to_rename, fill_word, output_csv, remove_from_second_last_underscore=True)
