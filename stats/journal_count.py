################################################################################

# Number of Unique journals

################################################################################

import pandas as pd

# Load the CSV file
file_path = "review_papers.csv"
df = pd.read_csv(file_path)

# Get unique non-null names from the "Journal/Book" column and sort them
unique_journals = sorted(df["Journal/Book"].dropna().unique())

# Count the number of unique names
unique_count = len(unique_journals)

# Print the count and the sorted journal names
print(f"Total number of unique journal names: {unique_count}")
for journal in unique_journals:
    print(journal)
