import pandas as pd
import re

df = pd.read_csv("summary.csv")

latex_table = df.to_latex(index=False, escape=True, multirow=True, float_format="%.6f")

parts = latex_table.split('\\midrule', 1)

custom_header = r"""\begin{tabular}{lccc}
\toprule
Group & \multicolumn{3}{c}{\shortstack{Average Minimum Max Relative Area Error\\Among First 100 Iterations*}} \\
\cmidrule(lr){2-4}
     & F4Carto & 5FCarto & BFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
