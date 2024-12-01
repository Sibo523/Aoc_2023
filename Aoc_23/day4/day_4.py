
import re

def main():
    with open('../day3/day_3.txt') as file:
        sum = 0
        D = file.readlines()
       # array = [0]*len(D) #second shit
        for i,line in enumerate(D):
            sp = line[9:].split('|')
            man = set()
            woman = set()
            for n in re.finditer(r'\d+', sp[0]):
                man.add(n.group())
            for n in re.finditer(r'\d+', sp[1]):
                woman.add(n.group())
            i = len(woman & man)
            if i > 0:
                sum += 2**(i-1)

        print(sum)
if __name__ == '__main__':
    main()