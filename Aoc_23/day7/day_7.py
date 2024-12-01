
""""
Thoughts, I need to sort this
having a diconary

"""
from copy import deepcopy

dic = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
ender ={(5,5):[],(4,1):[],(3,2):[],(3,1):[],(2,2):[],(2,1):[],(1,1):[]}

from collections import defaultdict

def main(file):
    for line in file:
        tup = line.split()
        copy = defaultdict(int)
        for char in tup[0]:
            copy[char] += 1
        maxi = max(copy.values())
        mini = min(copy.values())

        if len(copy.values())==3 and maxi == 2 and mini == 1: #bug that accured unlucky
            mini =2
        keyer = (maxi,mini)
        ender[keyer].append(tup)
    for e in ender.values():
        e.sort(reverse= True,key = lambda x: ([dic[c] for c in x[0]]))
    count = 1000
    sum = 0
    for e in ender.values():
        for b in e:
            sum += int(b[1])*count #bid*count
            count-=1
    print(sum)


if __name__ == '__main__':
    with open('day7.txt') as file:
        main(file.readlines())
