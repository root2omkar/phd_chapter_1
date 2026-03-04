################################################################################

# Root Usage

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you upload "review_papers.csv", load it0
df = pd.read_csv("review_papers.csv")

# Check the first few rows
print(df.head())

# Set seaborn style
sns.set_theme(style="white")

# Count the occurrences of each value in the 'Rooted trees' column
counts = df['Rooted trees'].value_counts().reindex(["Yes", "No", "Unknown"], fill_value=0)

# Sort in descending order
counts = counts.sort_values(ascending=False)

# Create a grayscale bar plot with white background
fig, ax = plt.subplots(figsize=(4, 4), facecolor='white')  # Set figure background
ax.set_facecolor('white')  # Set axes background

bars = ax.bar(counts.index, counts.values, color='gray')

# Add total count labels on top of each bar
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

# Customize the plot
ax.set_xlabel('Root', fontsize=18, color='black')
ax.set_ylabel('Number of Papers', fontsize=18, color='black')
ax.tick_params(axis='x', labelrotation=0, labelsize=14, colors='black')
ax.tick_params(axis='y', labelsize=14, colors='black')


# Remove grid lines
plt.grid(False)

# Show only X and Y axes 
ax = plt.gca()
ax.set_facecolor('white')  # Set background to white
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

# Export the plot as PDF
plt.tight_layout()
plt.savefig("figure_b.pdf", format="pdf")

# Display plot
plt.show()
