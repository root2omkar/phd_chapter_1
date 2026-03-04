################################################################################

# F.A.I.R. Compliance

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload document0
df = pd.read_csv("review_papers.csv")

# Check the first few rows
print(df.head())

# Set seaborn style
sns.set_theme(style="white")

# List of FAIR principle columns
fair_columns = [
    'Data available online',
    'Data is accessible',
    'Data is current',
    'Data is interoperable',
    'Data is findable',
    'Data is reusable'
]

# Normalize: strip whitespace and convert to lowercase
df_clean = df.copy()
for col in fair_columns:
    df_clean[col] = df_clean[col].astype(str).str.strip().str.lower()

# Check if all FAIR principles are 'yes'
df_clean['Follows FAIR'] = df_clean[fair_columns].apply(
    lambda row: all(val == 'yes' for val in row),
    axis=1
)

# Count how many follow and how many do not
counts = df_clean['Follows FAIR'].value_counts().rename({True: 'Yes', False: 'No'})

# Create a bar plot with white background and visible border
fig, ax = plt.subplots(figsize=(4, 4), facecolor='white')
ax.set_facecolor('white')

# Plot bars
bars = ax.bar(counts.index, counts.values, color='gray')

# Add count labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.01 * max(counts.values),
        f'{int(height)}',
        ha='center',
        va='bottom',
        fontsize=14,
        color='black'
    )

# Customize labels and title
ax.set_xlabel('F.A.I.R. compliance', fontsize=18, color='black')
ax.set_ylabel('Number of Papers', fontsize=18, color='black')
ax.tick_params(axis='x', labelrotation=0, labelsize=14, colors='black')
ax.tick_params(axis='y', labelsize=14, colors='black')

# Remove grid lines
plt.grid(False)

# Show only X and Y axes (bottom and left spines), hide others
ax = plt.gca()
ax.set_facecolor('white')  # Set background to white
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

# Export the plot as PDF
plt.tight_layout()
plt.savefig("figure_h.pdf", format="pdf")

# Display the plot
plt.show()

