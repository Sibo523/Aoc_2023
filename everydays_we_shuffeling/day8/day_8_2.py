
from math import gcd

def main(file):  # remember to split ', ' for the keys to the next thing
    instruction, maper = file.split('\n\n')
    # O(n) lines in file
    Dict = dict((x, y[1:-1]) for x, y in (line.split(' = ')
                                          for line in maper.split('\n')))
    #O(n)
    list = [i for i in Dict.keys() if i[-1] == 'A']

    real_counter = 0
    prod = 1
    for cur in list:
        real_counter = 0
        while not cur[-1] == 'Z' :
            ch = instruction[counter]
            left, right = Dict[cur].split(', ')
            cur = left if ch == 'L' else right
            instruction = instruction[1:] + instruction[0] #used the elegent way described in part 1
            real_counter += 1
        prod =prod * real_counter// gcd(prod,real_counter)
    print(prod)


if __name__ == '__main__':
    with open('day8.txt') as file:
        main(file.read())
