# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Daniel Tian
# Date: December 06th, 2024
# Purpose: Slice NumPy Arrays.
# Usage: ./lab10c.py
import numpy as np

def main():
    # TO DO 1: Create numArray according to instructions given in readme.md file.
    numArray = np.random.randint(1,101, size=100)
    print(numArray)
    
    sub_array1 = numArray[0:10]
    print(sub_array1)
    
    sub_array2 = numArray[-10:]
    print(sub_array2)
    
    sub_array3 = numArray[21:51]
    print(sub_array3)
    
    # TO DO 2: Perform the operations on numArray given in readme.md file.
    numArray[50:65] = 101
    print(numArray)

# TO DO 3: Run the script.
if __name__ == "__main__":
    main()
