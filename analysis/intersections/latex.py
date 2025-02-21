import pandas as pd

df = pd.read_csv('combined.csv')
latex_table = df.to_latex(index=False, escape=True, multirow=True)

parts = latex_table.split('\\midrule', 1)
if len(parts) < 2:
    raise ValueError("Could not find '\\midrule' in the generated LaTeX table.")

custom_header = r"""
\begin{tabular}{lrrr|rrr|rrr}
\toprule
\multirow{2}{*}{Map} & \multicolumn{3}{c}{Self-intersections} & \multicolumn{3}{c}{Overlap Intersections} & \multicolumn{3}{c}{Total} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}
                   & F4Carto & 5FCarto & BFB & F4Carto & 5FCarto & BFB & F4Carto & 5FCarto & BFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
