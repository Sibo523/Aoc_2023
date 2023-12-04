
import re

def main():
    with open('day_3.txt') as file:
        sum = 0
        D = file.readlines()
        array = [0]*len(D)
        for i,line in enumerate(D):
            i = 0
            sp = line[9:].split('|')
            # print(sp)
            man = set()
            woman = set()
            for n in re.finditer(r'\d+', sp[0]):
                man.add(n.group())
            for n in re.finditer(r'\d+', sp[1]):
                woman.add(n.group())

            for o in woman&man:
                # print(o , end = " ")
                i+=1        # amounts of wins
            # print("")
            # print(i)
            # for j in range(i+1,2*i+2): # adds one's in every next spot for i times
            #     if(j > len(array)):
            #     array[j]+=1
            if i > 0:
                sum += 2**(i-1)


        print(sum)
if __name__ == '__main__':
    main()