# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Create Series.
# Usage: ./lab10e.py

# TO DO 1: Import pandas module.
import pandas as pd
# TO DO 2: Create a series according to instructions given in readme.md file.
def main():
    data_values = ["<50","50-59","60-69","70-79","80-89","90-100"]
    series_list = pd.Series(data_values, index=["F","D","C","B","A","A+"])
    print("Series from List:\n", series_list)
# TO DO 3: Perform the operations on this series given in readme.md file.
    print("Values at Index 'C':", series_list["C"])
    print("Values at Index 'A+':", series_list["A+"])
    
    print(series_list["C"])
    
    print("* Operations on Series:") #Repeating Strings?
    print(series_list * 2)
# TO DO 4: Run the script.

if __name__ == "__main__":
    main()