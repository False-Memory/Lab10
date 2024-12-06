# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Slice 2D NumPy Arrays.
# Usage: ./lab10d.py
import numpy as np
# TO DO 1: Create an array according to instructions given in readme.md file.
def main():
    # Creating a 2D NumPy array
    arr_2d = np.array([[10, 20, 30, 40, 50],[60, 70, 80, 90, 100],[110, 120, 130, 140, 150],[160, 170, 180, 190, 200]])
    print(arr_2d)
    
# TO DO 2: Perform the operations on this array given in readme.md file.
    slice_1 = arr_2d[:2,-3:]
    print(slice_1)
    
    slice_2 = arr_2d[1:3,1:3]
    print(slice_2)
    
    slice_3 = arr_2d[::2,::2]
    print(slice_3)
# TO DO 3: Run the script.

if __name__ =='__main__':
    main()