# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Create Data Frames.
# Usage: ./lab10f.py

import pandas as pd

def main():
# TO DO 1: Create dataframe from provided dictionaries in readme.md file.
    data = {
        'Name': ["Apple","Carrot","Radish","Okra","Potato"],
        'Shape': ["","","Round","Thin","Blob"],
        'Price':[2.1, 1.3, 3.0, 3.5, 3.0]
        }
    
    df = pd.DataFrame(data)
    print("DataFrame created from dictionary:\n", df)
    
# TO DO 2: create a data frame provided in dataframe.jpg file.
    jpg_data = {
        'Subject': ["Maths","English","Urdu","Science"],
        'Student Name': ["A","B","C","D"],
        'Student Marks': [22,344,55,77]
        }
    dj = pd.DataFrame(jpg_data)
    print("DataFrame created from JPG:\n", dj)
# TO DO 3: Run the script.
if __name__ == "__main__":
    main()