import pandas as pd
import re

df = pd.read_csv("summary.csv")

latex_table = df.to_latex(index=False, escape=True, multirow=True, float_format="%.2f")

parts = latex_table.split('\\midrule', 1)

custom_header = r"""
\begin{tabular}{lccc|ccc|ccc}
\toprule
\multirow{2}{*}{Group} & \multicolumn{3}{c}{Average Fréchet Distance} & \multicolumn{3}{c}{Average Hausdorff Distance} & \multicolumn{3}{c}{Average Symmetric Difference} \\
\cmidrule(lr){2-10}
                   & F4Carto & 5FCarto & FFB & F4Carto & 5FCarto & FFB & F4Carto & 5FCarto & FFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
