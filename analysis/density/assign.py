import pandas as pd

df = pd.read_csv("density_processed.csv")

df = df.sort_values(by="Ratio")

df["Group"] = ["Group " + str(i//8 + 1) for i in range(len(df))]

df = df.round(6)

df = df[["Map", "Group", "Min Density", "Max Density", "Ratio"]]

df.to_csv("combined.csv", index=False)


