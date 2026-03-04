import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mannwhitneyu

# Load CSV
df = pd.read_csv("review_papers.csv")

# Set seaborn style
sns.set_theme(style="white")

# Normalize 'Outgroup selection'
df_clean = df.copy()
df_clean['Outgroup selection'] = df_clean['Outgroup selection'].astype(str).str.strip().str.capitalize()
df_clean['Impact Factor'] = pd.to_numeric(df_clean['Impact Factor'], errors='coerce')

# Statistical test
grouped = df_clean.groupby('Outgroup selection')['Impact Factor']
if len(grouped) == 2:
    group1, group2 = [group.dropna() for _, group in grouped]
    stat, p_value = mannwhitneyu(group1, group2, alternative='two-sided')
    print(f"Mann–Whitney U test result: U={stat:.3f}, p={p_value:.4f}")
else:
    print("Unexpected number of groups for Mann–Whitney U test.")

# Create box plot with stripplot overlay
plt.figure(figsize=(4, 4))
ax = plt.gca()

sns.boxplot(
    data=df_clean,
    x='Outgroup selection',
    y='Impact Factor',
    order=sorted(df_clean['Outgroup selection'].unique()),
    color='lightgray',
    width=0.6,
    fliersize=0,
    ax=ax
)

sns.stripplot(
    data=df_clean,
    x='Outgroup selection',
    y='Impact Factor',
    order=sorted(df_clean['Outgroup selection'].unique()),
    jitter=True,
    color='black',
    size=4,
    ax=ax,
    zorder=1
)

# Customize labels
ax.set_xlabel('Outgroup', fontsize=18)
ax.set_ylabel('Impact Factor', fontsize=18)
ax.tick_params(axis='x', labelrotation=0, labelsize=14)
ax.tick_params(axis='y', labelsize=14)

# Aesthetics
plt.grid(False)
ax.set_facecolor('white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Export
plt.tight_layout()
plt.savefig("figure_j_boxplot.pdf", format="pdf")
plt.show()
