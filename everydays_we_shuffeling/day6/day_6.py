
import numpy
import math
def winning_races(total_time, record_distance):
    root1 = ((total_time + ((total_time**2 -4*record_distance)**(1/2)))/2 - 0.05)
    root2 = ((total_time - ((total_time**2 -4*record_distance)**(1/2)))/2 + 0.05)
    return math.floor(root1)-math.ceil(root2) + 1
def main(file):
    time = [int(i) for i in file[0].split() if i.isdigit()]
    distance = [int(i) for i in file[1].split() if i.isdigit()]
    list = []
    for i in range(len(time)):
        min_s = int(distance[i]/time[i])
        list.append(winning_races(int(time[i]),int(distance[i])))
    print(numpy.prod(list))

if __name__ == '__main__':
    with open('day_6.txt') as file:
        main(file.readlines())








































































