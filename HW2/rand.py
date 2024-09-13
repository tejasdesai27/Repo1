"""
This module provides functions for working with arrays, including 
randomly populating an array using system commands.
"""

import subprocess
"""
    This function uses the 'shuf' command from the shell to generate a random integer
    between 1 and 20 for each element of the input array.
"""

def random_array(arr):
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check= True)
        arr[i] = int(shuffled_num.stdout)
    return arr
