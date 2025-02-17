import pandas as pd
import json
import os

df_4f = pd.read_csv("f4carto.csv")
df_5f = pd.read_csv("5fcarto.csv")
df_fb = pd.read_csv("flow_based.csv")

df_fb.rename(columns=lambda x: x if x=="Map" else "flow_based_" + x, inplace=True)

merged_df = pd.merge(df_5f, df_4f, on="Map", suffixes=('_5fcarto', '_f4carto'))

merged_df = pd.merge(merged_df, df_fb, on="Map")

merged_df.rename(columns={
    "self-intersections_5fcarto": "5FCarto_self-intersections",
    "overlap intersections_5fcarto": "5FCarto_overlap intersections",
    "self-intersections_f4carto": "F4Carto_self-intersections",
    "overlap intersections_f4carto": "F4Carto_overlap intersections",
    "self-intersections_flow_based": "flow_based_self-intersections",
    "overlap intersections_flow_based": "flow_based_overlap intersections"
}, inplace=True)

merged_df["5FCarto_total"] = merged_df["5FCarto_self-intersections"] + merged_df["5FCarto_overlap intersections"]
merged_df["F4Carto_total"] = merged_df["F4Carto_self-intersections"] + merged_df["F4Carto_overlap intersections"]
merged_df["flow_based_total"] = merged_df["flow_based_self-intersections"] + merged_df["flow_based_overlap intersections"]

merged_df = merged_df[[
    "Map",
    "F4Carto_self-intersections", "5FCarto_self-intersections", "flow_based_self-intersections",
     "F4Carto_overlap intersections",  "5FCarto_overlap intersections", "flow_based_overlap intersections",
     "F4Carto_total", "5FCarto_total", "flow_based_total"
]]

merged_df = merged_df[merged_df["Map"] != "concentric_circles"]

merged_df.iloc[:, 1:] = merged_df.iloc[:, 1:].round(6)

mapping_path = os.path.join(os.path.dirname(os.getcwd()), "mapping.json")
with open(mapping_path, 'r') as f:
    mapping = json.load(f)

merged_df["Map"] = merged_df["Map"].apply(lambda x: mapping.get(x, x))

merged_df = merged_df.sort_values(by="Map")

merged_df.to_csv("combined.csv", index=False)
