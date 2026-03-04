################################################################################

# Type of analysis

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from upsetplot import from_memberships, UpSet

# Assuming you upload "review_papers.csv", load it0
df = pd.read_csv("review_papers.csv")

# Check the first few rows
print(df.head())


# Column containing methods
method_col = "Single-gene analysis, Multi-gene analysis, or Whole genome analysis"

# Parse methods into lists
def parse_methods(cell):
    if pd.isna(cell) or cell.strip().lower() == "unknown":
        return ["Unknown"]
    return [m.strip() for m in cell.split(",")]

# Create method combinations
memberships = df[method_col].apply(parse_methods)
upset_data = from_memberships(memberships)

# Plot
plt.figure(figsize=(5, 5))

# Create a grayscale UpSet plot
upset = UpSet(
    upset_data,
    subset_size='count',
    show_counts=True,
    sort_by='degree',
    facecolor='gray'  # Set bar color to gray
)
upset_plot = upset.plot()


# Customize bar label font size and color
for ax in plt.gcf().get_axes():
    for text in ax.texts:
        text.set_fontsize(14)
        text.set_color('black')


# Customize label font size
plt.gca().tick_params(labelsize=14, colors='black')

# Customize Y-axis label
plt.gca().set_ylabel("Number of Papers", fontsize=14, color='black')

# Remove grid lines and set axis line colors to black
for ax in plt.gcf().get_axes():
    ax.grid(False)
    for spine_name, spine in ax.spines.items():
        if spine_name in ['left', 'bottom']:
            spine.set_visible(True)
            spine.set_color('black')     # Make axis lines black
        else:
            spine.set_visible(False)

# Export the plot as PDF
plt.tight_layout()
plt.savefig("figure_d.pdf", format="pdf")

# Display the plot
plt.show()


