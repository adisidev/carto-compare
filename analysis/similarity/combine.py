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
    "frechet distance_f4carto": "f4carto_frechet distance",
    "frechet distance_5fcarto": "5fcarto_frechet distance",
    "frechet distance_flow_based": "flow_based_frechet distance",
    "hausdorff distance_f4carto": "f4carto_hausdorff distance",
    "hausdorff distance_5fcarto": "5fcarto_hausdorff distance",
    "hausdorff distance_flow_based": "flow_based_hausdorff distance",
    "symmetric difference_f4carto": "f4carto_symmetric difference",
    "symmetric difference_5fcarto": "5fcarto_symmetric difference",
    "symmetric difference_flow_based": "flow_based_symmetric difference"
}, inplace=True)


merged_df = merged_df[[
    "Map",
    "f4carto_frechet distance", "5fcarto_frechet distance", "flow_based_frechet distance",
    "f4carto_hausdorff distance", "5fcarto_hausdorff distance", "flow_based_hausdorff distance",
    "f4carto_symmetric difference", "5fcarto_symmetric difference", "flow_based_symmetric difference"
]]

merged_df.iloc[:, 1:] = merged_df.iloc[:, 1:].round(2)

merged_df = merged_df[merged_df["Map"] != "concentric_circles"]

mapping_path = os.path.join(os.path.dirname(os.getcwd()), "mapping.json")
with open(mapping_path, 'r') as f:
    mapping = json.load(f)

merged_df["Map"] = merged_df["Map"].apply(lambda x: mapping.get(x, x))

merged_df = merged_df.sort_values(by="Map")

merged_df.to_csv("combined.csv", index=False)
