""" 
Navigate toward the assignment folder in Anaconda.

Steps:
1. Create a virtual environment:
   (conda create --name sortenv python=3.10.0)
2. Activate the virtual environment:
   (conda activate sortenv)
3. To deactivate:
   (conda deactivate)
4. Install NumPy:
   (pip install numpy)
5. Open VS Code:
   (code .)
"""

# Importing library for numpy.sort
import numpy as np

def main():
    while True:
        try:
            # Taking input from the user
            user_input = input("Enter a list of numbers separated by spaces: ")    

            # Convert input to a list of integers
            num_list = list(map(int, user_input.split()))

            # Sort the list using numpy.sort()
            sorted_list = np.sort(num_list)

            # Printing the sorted list
            print("Sorted list:", sorted_list)
            
            break  # Exit loop after successful input
        
        except ValueError:
            print("Invalid input! Please enter only integers separated by spaces.")

if __name__ == "__main__":
    main()
