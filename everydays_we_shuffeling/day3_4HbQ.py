import math as m
import re
import timeit

def main():
    # Read the input board from the file
    board = list(open('C:\helper\day3.txt'))

    # Create a dictionary to store characters and their positions
    chars = {(r, c): [] for r in range(140) for c in range(140)
             if board[r][c] not in '01234566789.'}  # Dictionary for sign placements

    # Iterate through each row in the board
    for r, row in enumerate(board):
        # Find all matches of digits in the current row using regex
        for n in re.finditer(r'\d+', row):
            # Define the edge positions around the matched digit
            edge = {(r, c) for r in (r - 1, r, r + 1)           #set of the coordinated around each number, includes the number itself
                    for c in range(n.start() - 1, n.end() + 1)}  #n == the number that we found using regural expressions

            # Add the digit to the corresponding positions in the chars dictionary
            for o in edge & chars.keys(): #tuple of edge coordinated and rows and and overlaps the data
                chars[o].append(int(n.group()))   #fucking mad when it finds an overlap then it's go in the key o and adds the n found


    # Print the sum of all values in the chars dictionary and the sum of products for pairs with length 2
    print(sum(sum(p) for p in chars.values()),
          sum(m.prod(p) for p in chars.values() if len(p) == 2))

if __name__ == "__main__":
    # Measure the time taken for the main function to execute
    print(f'time took: {timeit.timeit(main, number=1)}')
