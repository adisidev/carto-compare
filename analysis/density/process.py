import pandas as pd
import json
import os

df = pd.read_csv("density.csv")

df["Ratio"] = df["Max Density"] / df["Min Density"]

df["Map"] = df["Map"].apply(lambda x: x.replace(".csv", ""))

df = df[df["Map"] != "concentric_circles"]

mapping_path = os.path.join(os.path.dirname(os.getcwd()), "mapping.json")
with open(mapping_path, 'r') as f:
    mapping = json.load(f)

df["Map"] = df["Map"].apply(lambda x: mapping.get(x, x))

df = df.sort_values(by="Map")

df.to_csv("density_processed.csv", index=False)