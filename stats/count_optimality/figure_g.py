################################################################################

# OPTIMALITY CRITERIA

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from upsetplot import from_indicators, UpSet

# Upload document
df = pd.read_csv("review_papers.csv")

# Check the first few rows
print(df.head())

# Define mapping of full names to abbreviations
method_abbrev_map = {
    "Maximum Likelihood": "ML",
    "Bayesian Inference": "BI",
    "Parsimony": "P",
    "Neighbor Joining": "NJ",
    "UPGMA": "UPGMA",
    "CGR (Chaos Game Representation)": "CGR",
    "Unknown": "Unknown"
}

# Define the methods of interest in full and abbreviated forms
full_methods = list(method_abbrev_map.keys())
abbrev_methods = [method_abbrev_map[m] for m in full_methods]

# Create boolean indicator columns using the full names
for method in full_methods:
    df[method_abbrev_map[method]] = df["Optimality criteria used"].fillna("").apply(lambda x: method in x)

# Create the UpSet data from abbreviated indicator columns
upset_data = from_indicators(abbrev_methods, df)

# Create and customize the UpSet plot
plt.figure(figsize=(1, 1))

upset = UpSet(
    upset_data,
    subset_size='count',
    show_counts=True,
    sort_by='cardinality',
    sort_categories_by='input',
    facecolor='gray'
)
upset_plot = upset.plot()

# Customize bar label font size and color
for ax in plt.gcf().get_axes():
    for text in ax.texts:
        text.set_fontsize(18)
        text.set_color('black')


# Customize label font size
plt.gca().tick_params(labelsize=18, colors='black')

# Customize Y-axis label
plt.gca().set_ylabel("Number of Papers", fontsize=18, color='black')

# Show only X and Y axes in black, hide other borders
for ax in plt.gcf().get_axes():
    for spine_name, spine in ax.spines.items():
        if spine_name in ['left', 'bottom']:
            spine.set_visible(True)
            spine.set_color('black')
        else:
            spine.set_visible(False)

# Remove grid lines
plt.grid(False)

# Export the plot as PDF
plt.tight_layout()
plt.savefig("figure_g.pdf", format="pdf")

# Display the plot
plt.show()

