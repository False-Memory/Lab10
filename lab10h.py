# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Create Histograms.
# Usage: ./lab10h.py

# TO DO 1: Import pandas and matplotlib modules.
import matplotlib.pyplot as plt
import pandas as pd

# TO DO 2: Draw histogram of the data from movies database.
def main():
    movies_df = pd.read_csv('imdb_top_250.csv')
    
    years = movies_df['Year']
    sorted_years = years.sort_values()
    year_counts = sorted_years.value_counts().sort_index()
    unique_years = year_counts.index[:10]
    counts = year_counts.values[:10]
    plt.bar(unique_years, counts)
    plt.xlabel('Years')
    plt.ylabel('Number of Movies')
    plt.title('Number of Movies per Year (First 10 Years)')
    plt.xticks(rotation=45)
    plt.show()

# TO DO 3: Perform the operations provided in readme.md file on this data.

# TO DO 4: Run the script.
if __name__ == "__main__":
    main()