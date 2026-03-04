import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal

# Load CSV
df = pd.read_csv("review_papers.csv")

# Normalize the 'Usage of Gene annotation' column
df_clean = df.copy()
df_clean['Usage of Gene annotation'] = df_clean['Usage of Gene annotation'].astype(str).str.strip().str.capitalize()
df_clean['Impact Factor'] = pd.to_numeric(df_clean['Impact Factor'], errors='coerce')

# Run Kruskal–Wallis H-test
groups = [group['Impact Factor'].dropna().values for name, group in df_clean.groupby('Usage of Gene annotation')]
stat, p_value = kruskal(*groups)
print(f"Kruskal-Wallis H-test result: H={stat:.3f}, p={p_value:.4f}")

# Order categories
categories = ['Yes', 'No', 'Unknown']
df_clean['Usage of Gene annotation'] = pd.Categorical(df_clean['Usage of Gene annotation'], categories=categories)

# Create box plot
fig, ax = plt.subplots(figsize=(4, 4), facecolor='white')
ax.set_facecolor('white')

sns.boxplot(
    data=df_clean,
    x='Usage of Gene annotation',
    y='Impact Factor',
    order=categories,
    color='lightgray',
    width=0.6,
    fliersize=0,
    ax=ax
)

sns.stripplot(
    data=df_clean,
    x='Usage of Gene annotation',
    y='Impact Factor',
    order=categories,
    jitter=True,
    color='black',
    size=4,
    ax=ax,
    zorder=1
)

# Customize plot
ax.set_xlabel('Gene Annotation', fontsize=18, color='black')
ax.set_ylabel('Impact Factor', fontsize=18, color='black')
ax.tick_params(axis='x', labelrotation=0, labelsize=14, colors='black')
ax.tick_params(axis='y', labelsize=14, colors='black')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.grid(False)

# Export
plt.tight_layout()
plt.savefig("figure_l_boxplot.pdf", format="pdf")
plt.show()
