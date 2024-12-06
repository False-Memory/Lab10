# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab10b.py

# TO DO 1: Copy the code from your lab10a.py file and paste here.
import numpy as np

def main():
    Array1 = np.array([20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49])
    print(Array1)
    
    Array2 = np.arange(20,50)
    print(Array2)
    
    Array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print("2D Array:\n", Array3)
    
    Array4 = np.array([[["January","February"],["March","April"],["May","June"]],[["July","August"],["September","October"],["November","December"]]])
    print("3D Array:\n", Array4)
    
    # TO DO 2: Reshape array1 reshapes array2 according to instructions given in readme.md file.
    Array1 = np.reshape(Array1,(5,6))
    Array2 = np.reshape(Array2,(2,3,5))
    print("Array1:\n", Array1)
    print("Array2:\n", Array2)
    # TO DO 3: Create array5 according to instructions given in readme.md file.
    Array5 = np.diag([45,7,61,8,9])
    print("Array5:\n", Array5)
    # TO DO 4: Create array6 according to instructions given in readme.md file.
    Array6 = np.random.randn(7,7)
    print("Array6:\n", Array6)

# TO DO 5: Run the script.

if __name__ == "__main__":
    main()