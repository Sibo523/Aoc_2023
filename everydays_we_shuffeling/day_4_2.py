import timeit
import re
from collections import defaultdict
def main():
    with open('day_3.txt') as file:
        # sum = 0
        D = file.readlines()
        array = defaultdict(int)

        for l_num,line in enumerate(D):
            array[l_num] += 1
            sp = line[9:].split('|')
            man = set()
            woman = set()
            for n in re.finditer(r'\d+', sp[0]):
                man.add(n.group())
            for n in re.finditer(r'\d+', sp[1]):
                woman.add(n.group())
            i = len(woman & man) #amount of overlaps -> wins

            for j in range (i): #runs the amoung of wins
                array[l_num+1+j] +=array[l_num] #all the next index's should be summed with the current value in the box

        print(sum(array.values()))# sum all the values in the end :)
        
if __name__ == '__main__':
    print(f'time took: {timeit.timeit(main, number=1)}')
