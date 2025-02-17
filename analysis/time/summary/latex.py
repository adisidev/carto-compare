import pandas as pd
import re

df = pd.read_csv("summary.csv")

latex_table = df.to_latex(index=False, escape=True, multirow=True, float_format="%.3f")

parts = latex_table.split('\\midrule', 1)

custom_header = r"""
\begin{tabular}{lccc|ccc}
\toprule
\multirow{2}{*}{Group} & \multicolumn{3}{c}{Average Time} & \multicolumn{3}{c}{\shortstack{Average Max Relative Area \\ Error at Time}} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}
                     & F4Carto & 5FCarto & FFB & F4Carto & 5FCarto & FFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
