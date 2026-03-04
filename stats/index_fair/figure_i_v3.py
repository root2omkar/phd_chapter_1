import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mannwhitneyu

# Load CSV
df = pd.read_csv("review_papers.csv")

# FAIR principle columns
fair_columns = [
    'Data available online',
    'Data is accessible',
    'Data is current',
    'Data is interoperable',
    'Data is findable',
    'Data is reusable'
]

# Normalize responses
df_clean = df.copy()
for col in fair_columns:
    df_clean[col] = df_clean[col].astype(str).str.strip().str.lower()

# Compute FAIR compliance
df_clean['Follows FAIR'] = df_clean[fair_columns].apply(
    lambda row: all(val == 'yes' for val in row),
    axis=1
)
df_clean['Follows FAIR Label'] = df_clean['Follows FAIR'].map({True: 'Yes', False: 'No'})

# Convert impact factor to numeric
df_clean['Impact Factor'] = pd.to_numeric(df_clean['Impact Factor'], errors='coerce')

# Mann–Whitney U test
group_yes = df_clean[df_clean['Follows FAIR']]['Impact Factor'].dropna()
group_no = df_clean[~df_clean['Follows FAIR']]['Impact Factor'].dropna()

if len(group_yes) > 0 and len(group_no) > 0:
    stat, p_value = mannwhitneyu(group_yes, group_no, alternative='two-sided')
    print(f"Mann–Whitney U test result: U={stat:.3f}, p={p_value:.4f}")
else:
    print("Not enough data for statistical test.")

# Create box plot with individual points
fig, ax = plt.subplots(figsize=(4, 4), facecolor='white')
ax.set_facecolor('white')

sns.boxplot(
    data=df_clean,
    x='Follows FAIR Label',
    y='Impact Factor',
    order=['Yes', 'No'],
    color='lightgray',
    width=0.6,
    fliersize=0,
    ax=ax
)

sns.stripplot(
    data=df_clean,
    x='Follows FAIR Label',
    y='Impact Factor',
    order=['Yes', 'No'],
    jitter=True,
    color='black',
    size=4,
    ax=ax,
    zorder=1
)

# Formatting
ax.set_xlabel('F.A.I.R. Compliance', fontsize=18, color='black')
ax.set_ylabel('Impact Factor', fontsize=18, color='black')
ax.tick_params(axis='x', labelrotation=0, labelsize=14, colors='black')
ax.tick_params(axis='y', labelsize=14, colors='black')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.grid(False)

# Export
plt.tight_layout()
plt.savefig("figure_i_boxplot.pdf", format="pdf")
plt.show()
