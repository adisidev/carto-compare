import pandas as pd

def generate_latex_table(csv_file):
    df = pd.read_csv(csv_file)
    
    df['GroupNum'] = df['Group'].str.extract(r'(\d+)').astype(int)
    header = r"""\begin{tabular}{lcccc}
\toprule
Map & Group & Min Density & Max Density & Ratio \\
\midrule
"""
    table_lines = [header]
    
    for group_name, group_df in df.groupby("Group"):
        n = len(group_df)
        group_df = group_df.reset_index(drop=True)
        for i, row in group_df.iterrows():
            if i == 0:
                group_cell = r"\multirow{" + f"{n}" + r"}{*}{" + f"{group_name}" + r"}"
            else:
                group_cell = ""
            line = f"{row['Map']} & {group_cell} & {row['Min Density']:.3f} & {row['Max Density']:.2f} & {row['Ratio']:.1f} \\\\"
            table_lines.append(line)
        # Add a horizontal line after each group
        table_lines.append(r"\midrule")
    
    footer = r"""\bottomrule
\end{tabular}"""
    table_lines.append(footer)
    
    return "\n".join(table_lines)

if __name__ == '__main__':
    latex_table = generate_latex_table("combined.csv")
    
    with open("latex.tex", "w") as f:
      f.write(latex_table)
