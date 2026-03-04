################################################################################

# Type of data

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn3

# Assuming you upload "review_papers.csv", load it0
df = pd.read_csv("review_papers.csv")

# Check the first few rows
print(df.head())

# Replace NaNs with empty string to avoid errors
df['Type of data used'] = df['Type of data used'].fillna('')

# Create set membership flags
df['uses_nucleotides'] = df['Type of data used'].str.contains('Nucleotides', case=False)
df['uses_amino_acids'] = df['Type of data used'].str.contains('Amino Acids', case=False)
df['uses_unknown'] = df['Type of data used'].str.contains('Unknown', case=False)

# Create sets of indices for each category
set_nucleotides = set(df[df['uses_nucleotides']].index)
set_amino_acids = set(df[df['uses_amino_acids']].index)
set_unknown = set(df[df['uses_unknown']].index)

# Create a Venn diagram
plt.figure(figsize=(5, 5))
venn = venn3([set_nucleotides, set_amino_acids, set_unknown],
             set_labels=('Nucleotides', 'Amino Acids', 'Unknown'),
             set_colors=('gray', 'lightgray', 'darkgray'),
             alpha=0.5)

# Customize patch outlines
for patch in venn.patches:
    if patch:
        patch.set_edgecolor('black')
        patch.set_linewidth(1)

# Increase font size of labels and manually reposition to avoid overlap
label_offsets = [(0,0), (0.25, -0.05), (0.15, 0)]  # x, y offsets for each label
for i, label in enumerate(venn.set_labels):
    if label:
        label.set_fontsize(16)
        x, y = label.get_position()
        dx, dy = label_offsets[i]
        label.set_position((x + dx, y + dy))

# Increase font size of subset labels
for label in venn.subset_labels:
    if label:
        label.set_fontsize(14)
        
# Export the plot as PDF
plt.tight_layout()
plt.savefig("figure_e.pdf", format="pdf")

# Show the plot
plt.show()

