import pandas as pd
import re

df = pd.read_csv("summary.csv")

latex_table = df.to_latex(index=False, escape=True, multirow=True, float_format="%.1f")

parts = latex_table.split('\\midrule', 1)

custom_header = r"""
\begin{tabular}{lrrr|rrr|rrr}
\toprule
\multirow{2}{*}{Group} & \multicolumn{3}{c}{Average Self-intersections} & \multicolumn{3}{c}{Average Overlap Intersections} & \multicolumn{3}{c}{Average Total} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}\cmidrule(lr){8-10}
                   & F4Carto & 5FCarto & FFB & F4Carto & 5FCarto & FFB & F4Carto & 5FCarto & FFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
