import pandas as pd
import json
import os

df = pd.read_csv("results_best_out_of_100.csv")

df = df.rename(columns={
    "mapname": "Map",
    "5FCarto_min_relative_area_error_reached": "5FCarto",
    "F4Carto_min_relative_area_error_reached": "F4Carto",
    "flow_based_min_relative_area_error_reached": "Flow Based"
})

df = df[["Map", "F4Carto", "5FCarto", "Flow Based"]]

df = df[df["Map"] != "concentric_circles"]

df = df.round(6)

mapping_path = os.path.join(os.path.dirname(os.getcwd()), "mapping.json")
with open(mapping_path, 'r') as f:
    mapping = json.load(f)

df["Map"] = df["Map"].apply(lambda x: mapping.get(x, x))

df = df.sort_values(by="Map")

df.to_csv("combined.csv", index=False)
