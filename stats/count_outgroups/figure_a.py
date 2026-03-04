################################################################################

# Outgroup Usage

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("review_papers.csv")

# Show first few rows
print(df.head())

# Set seaborn theme
sns.set_theme(style="white")

# Count 'Yes' and 'No' in the 'Outgroup selection' column
outgroup_counts = df['Outgroup selection'].value_counts()
yes_count = outgroup_counts.get('Yes', 0)
no_count = outgroup_counts.get('No', 0)

print(f"Number of papers with Outgroup selection 'Yes': {yes_count}")
print(f"Number of papers with Outgroup selection 'No': {no_count}")

# Plot settings
fig, ax = plt.subplots(figsize=(4, 4), facecolor='white')
ax.set_facecolor('white')

# Plot bars
bars = ax.bar(outgroup_counts.index, outgroup_counts.values, color='gray')

# Axis labels
ax.set_xlabel('Outgroup', fontsize=18, color='black')
ax.set_ylabel('Number of Papers', fontsize=18, color='black')
ax.tick_params(axis='x', labelrotation=0, labelsize=14, colors='black')
ax.tick_params(axis='y', labelsize=14, colors='black')


# Add value labels
for i, count in enumerate(outgroup_counts.values):
    plt.text(i, count + 0.5, str(count), ha='center', va='bottom', fontsize=14, color='black')

# Show X and Y axes
ax = plt.gca()
ax.set_facecolor('white')  # Set background to white
plt.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

# Export to PDF
plt.tight_layout()
plt.savefig("figure_a.pdf", format="pdf")

# Display the plot
plt.show()
