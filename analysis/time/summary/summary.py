import os
import pandas as pd
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
combined_csv_path = os.path.join(os.path.dirname(script_dir), "combined.csv")
map_json_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)), "map_to_group.json")

df = pd.read_csv(combined_csv_path)

with open(map_json_path, "r") as f:
    map_to_group = json.load(f)

df["Group"] = df["Map"].map(map_to_group)

numeric_cols = df.select_dtypes(include="number").columns
grouped = df.groupby("Group")[numeric_cols].mean().reset_index()

grouped["group_num"] = grouped["Group"].str.extract(r"(\d+)").astype(int)
grouped = grouped.sort_values("group_num").drop(columns="group_num")

grouped.to_csv("summary.csv", index=False)
