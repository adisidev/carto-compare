import pandas as pd
import json
import os

df = pd.read_csv("time_and_area_error_comparison.csv")

df = df.rename(columns={
    "mapname": "Map",
    "5FCarto_time_at_n": "5FCarto_time",
    "flow_based_time_at_n": "flow_based_time",
    "F4Carto_min_relative_area_error_reached": "F4Carto_max_relative_area_error_at_time",
    "5FCarto_max_relative_area_error_at_n": "5FCarto_max_relative_area_error_at_time",
    "flow_based_max_relative_area_error_at_n": "flow_based_max_relative_area_error_at_time",
})

df = df[[
    "Map",
    "F4Carto_time",
    "5FCarto_time",
    "flow_based_time",
    "F4Carto_max_relative_area_error_at_time",
    "5FCarto_max_relative_area_error_at_time",
    "flow_based_max_relative_area_error_at_time",
]]

df["F4Carto_max_relative_area_error_at_time"] = df["F4Carto_max_relative_area_error_at_time"].round(3)
df["5FCarto_max_relative_area_error_at_time"] = df["5FCarto_max_relative_area_error_at_time"].round(3)
df["flow_based_max_relative_area_error_at_time"] = df["flow_based_max_relative_area_error_at_time"].round(3)
df["F4Carto_time"] = df["F4Carto_time"].round(3)
df["5FCarto_time"] = df["5FCarto_time"].round(3)
df["flow_based_time"] = df["flow_based_time"].round(3)

df = df[df["Map"] != "concentric_circles"]

mapping_path = os.path.join(os.path.dirname(os.getcwd()), "mapping.json")
with open(mapping_path, 'r') as f:
    mapping = json.load(f)

df["Map"] = df["Map"].apply(lambda x: mapping.get(x, x))

df = df.sort_values(by="Map")

df.to_csv("combined.csv", index=False)
