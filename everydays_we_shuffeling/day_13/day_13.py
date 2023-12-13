def find_mirror(grid_lines):
    for index in range(1,len(grid_lines)): #index is the mirror
        above = grid_lines[:index] #turns out you can [::-1] to reverse
        below = grid_lines[index:]
        above.reverse()
        #match the lengths the rest considered a match
        above = above[:len(below)]
        below = below[:len(above)]
        if below == above:
            return index

    return 0

def main(file):
    total = 0
    for block in file:
        grid_lines = block.splitlines()
        total += 100*find_mirror(grid_lines)
        total += find_mirror(list(zip(*grid_lines)))
    print(total)








if __name__ == '__main__':
    with open('day_13.txt') as file:
        main(file.read().split('\n\n'))