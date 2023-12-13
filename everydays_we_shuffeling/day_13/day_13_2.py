def find_mirror(grid_lines):
    for index in range(1,len(grid_lines)): #index is the mirror
        above = grid_lines[:index][::-1]
        below = grid_lines[index:]

        above = above[:len(below)]
        below = below[:len(above)]
        #every missmatch adds 1
        c = sum(above[i][index] != below[i][index] for i in range(len(above)) for index in range(len(above[i]))) # c  = for every right thing
        if c == 1: #can be precisely 1 cause there's a smudge
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