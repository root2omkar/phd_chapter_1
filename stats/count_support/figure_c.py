################################################################################

# Branch support metrics

################################################################################

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you upload "review_papers.csv", load it0
df = pd.read_csv("review_papers.csv")

# Check the first few rows
print(df.head())

# Define the exact categories (including composite ones) in desired order
data = {
    'Branch support metrics': ['Bootstrap', 'Posterior Probabilities', 'Goodman Bremer', 'Unknown'],
    'Count': [
        sum(1 for _, row in df.iterrows() if row['Branch support metrics'] == 'Bootstrap'),
        sum(1 for _, row in df.iterrows() if row['Branch support metrics'] == 'Posterior Probabilities'),
        sum(1 for _, row in df.iterrows() if row['Branch support metrics'] == 'Goodman Bremer'),
        sum(1 for _, row in df.iterrows() if row['Branch support metrics'] == 'Unknown')
    ]
}
df_counts = pd.DataFrame(data)

# Sort the DataFrame by Count in ascending order
df_counts = df_counts.sort_values(by='Count', ascending=False)

# Create the bar plot
plt.figure(figsize=(5, 5))
ax = plt.gca()  # Get current Axes
bars = ax.bar(df_counts['Branch support metrics'], df_counts['Count'], color='gray')

# Add total count above each bar
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.5, int(yval),
            ha='center', va='bottom', fontsize=15)

# Customize the plot
ax.set_xlabel('Branch Support Metrics', fontsize=16)
ax.set_ylabel('Number of Papers', fontsize=16)
ax.set_xticklabels(df_counts['Branch support metrics'], rotation=45, ha='right', fontsize=15, color='black')
ax.tick_params(axis='y', labelsize=16, color='black')

# Remove grid lines
ax.grid(False)

# Show X and Y axes 
ax = plt.gca()
ax.set_facecolor('white')  # Set background to white
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

# Export the plot as PDF
plt.tight_layout()
plt.savefig("figure_c.pdf", format="pdf")

# Display the plot
plt.show()

