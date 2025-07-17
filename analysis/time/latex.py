import pandas as pd

pd.set_option('display.max_colwidth', None)

df = pd.read_csv('combined.csv')
latex_table = df.to_latex(index=False, escape=True, multirow=True, float_format="%.3f")

parts = latex_table.split('\\midrule', 1)
if len(parts) < 2:
    raise ValueError("Could not find '\\midrule' in the generated LaTeX code.")

custom_header = r"""
\begin{tabular}{lccc|ccc}
\toprule
\multirow{2}{*}{Map} & \multicolumn{3}{c}{Time (s)} & \multicolumn{3}{c}{\shortstack{Maximum Relative Area \\ Error at Termination}} \\
\cmidrule(lr){2-4}\cmidrule(lr){5-7}
                     & F4Carto & 5FCarto & BFB & F4Carto & 5FCarto & BFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
