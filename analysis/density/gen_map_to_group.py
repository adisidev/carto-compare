import pandas as pd
import json

df = pd.read_csv("combined.csv")

map_to_group = dict(zip(df["Map"], df["Group"]))

with open("map_to_group.json", "w") as f:
    json.dump(map_to_group, f, indent=4)
