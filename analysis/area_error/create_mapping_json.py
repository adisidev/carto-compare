import pandas as pd
import json

def human_readable(name):
    words = name.replace('_', ' ').split()
    new_words = []
    for word in words:
        if word.lower() == "by" or word[0].isdigit():
            new_words.append(word)
        else:
            new_words.append(word.capitalize())
    return " ".join(new_words)

df = pd.read_csv('combined.csv')

if 'Map' not in df.columns:
    raise ValueError("Column 'Map' not found in combined.csv.")

unique_maps = df['Map'].unique()
mapping = {name: human_readable(name) for name in unique_maps}

with open('mapping.json', 'w') as f:
    json.dump(mapping, f, indent=4)

print("Mapping file 'mapping.json' created successfully.")
