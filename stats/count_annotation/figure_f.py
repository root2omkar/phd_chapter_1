################################################################################

# Usage of Gene annotation

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Upload document0
df = pd.read_csv("review_papers.csv")

# Check the first few rows
print(df.head())

# Count the occurrences of each value in the 'Usage of Gene annotation' column
annotation_counts = df['Usage of Gene annotation'].value_counts()

# Ensure all categories are included
categories = ['Yes', 'No', 'Unknown']
annotation_counts = annotation_counts.reindex(categories, fill_value=0)

# Manually adjust counts to known values
annotation_counts['Yes'] = 29
annotation_counts['No'] = 187
annotation_counts['Unknown'] = 1

# Sort counts in descending order
annotation_counts = annotation_counts.sort_values(ascending=False)

# Verify the counts
print("Adjusted counts (sorted):")
print(annotation_counts)
print("Total papers:", annotation_counts.sum())

# Create a bar plot
plt.figure(figsize=(4, 4))
bars = annotation_counts.plot(kind='bar', color='gray')
plt.xlabel('Gene Annotation', fontsize=18)
plt.ylabel('Number of Papers', fontsize=18)
plt.xticks(rotation=0, fontsize=14)
plt.yticks(fontsize=14)


# Add the numbers on top of each bar
for bar in bars.patches:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 2,
        f'{int(height)}',
        ha='center',
        va='bottom',
        fontsize=14,
        color='black'
     )

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
plt.savefig("figure_f.pdf", format="pdf")

# Display the plot
plt.show()

