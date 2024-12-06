# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Create Arrays.
# Usage: ./lab10a.py
import numpy as np

def main():
    # TO DO 1: Create array1 and array2 according to instructions given in readme.md file.
    Array1 = np.array([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
    print(Array1)
    Array2 = np.arange(20,50)
    print(Array2)
    # TO DO 2: Create array3 according to instructions given in readme.md file.
    
    Array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("2D Array:\n", Array3)
    
    # TO DO 3: Create array4 according to instructions given in readme.md file.
    
    Array4 = np.array([[["January","February"],["March","April"],["May","June"]],[["July","August"],["September","October"],["November","December"]]])
    print("3D Array:\n", Array4)

if __name__ == "__main__":
    main()