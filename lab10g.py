# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Create data frame from CSV file.
# Usage: ./lab10g.py
import pandas as pd
import matplotlib.pyplot as plt

def main():
# TO DO 1: create a new data frame from the link of csv file provided in readme.md file.
    movie_df = pd.read_csv('imdb_top_250.csv')
    print(movie_df)
# TO DO 2: Perform the operations provided in readme.md file on this data frame.

    print("Print the First 10 rows of the DataFrame", movie_df.head(10))
    print("Print the Last 10 rows of the DataFrame", movie_df.tail(10))
    
    year = movie_df["Year"]
    print("The Earliest Movie is from the Year:",min(year))
    print("The Latest Movie is from the Year:",max(year))
    
    unique_genre = movie_df["Genre"].unique()
    print(f"Unique Genres: {unique_genre}")
    
    non_usa_movies = movie_df[movie_df['Origin'] != 'USA'].shape[0]
    print(f"Number of movies not made in the USA: {non_usa_movies}")
    
    top10_movies = movie_df.sort_values(by='IMDB rating', ascending=False).head(10)
    print("Top 10 Highest-Rated Movies:")
    print(top10_movies)
    
    movie_df['Decade'] = movie_df['Year'].apply(get_decade) #adds the decade column to the DataFrame
    rating_decade = movie_df.groupby('Decade')['IMDB rating'].mean().reset_index()
    print(rating_decade)
    
    #Scatter Plot
    plt.figure(figsize=(10,6))
    plt.scatter(rating_decade['Decade'], rating_decade['IMDB rating'], color='blue', alpha=0.7)
    plt.title("Average Movie Ratings by Decade")
    plt.xlabel('Decade')
    plt.ylabel('Average Rating')
    plt.grid(True)
    plt.show()
    
# TO DO 3: Run the script.
def get_decade(year):
    return(year //10)*10

if __name__ == "__main__":
    main()