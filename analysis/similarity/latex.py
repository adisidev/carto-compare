import pandas as pd

df = pd.read_csv('combined.csv')
latex_table = df.to_latex(index=False, escape=True, multirow=True, float_format="%.2f")

parts = latex_table.split('\\midrule', 1)

custom_header = r"""
\begin{tabular}{lccc|ccc|ccc}
\toprule
\multirow{2}{*}{Map} & \multicolumn{3}{c}{Fréchet Distance} & \multicolumn{3}{c}{Hausdorff Distance} & \multicolumn{3}{c}{Symmetric Difference} \\
\cmidrule(lr){2-10}
                   & F4Carto & 5FCarto & BFB & F4Carto & 5FCarto & BFB & F4Carto & 5FCarto & BFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
