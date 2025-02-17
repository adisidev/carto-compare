import pandas as pd

df = pd.read_csv('combined.csv')
latex_table = df.to_latex(index=False, escape=True, multirow=True, float_format="%.6f")

parts = latex_table.split('\\midrule', 1)
if len(parts) < 2:
    raise ValueError("Could not find '\\midrule' in the generated LaTeX code.")

custom_header = r"""\begin{tabular}{lccc}
\toprule
Map & \multicolumn{3}{c}{\shortstack{Minimum Max Relative Area Error\\Among First 100 Iterations*}} \\
\cmidrule(lr){2-4}
     & F4Carto & 5FCarto & FFB \\
\midrule
"""

final_latex = custom_header + parts[1]

with open("latex.tex", "w") as f:
    f.write(final_latex)
