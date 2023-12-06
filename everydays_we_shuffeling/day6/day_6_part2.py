

import numpy,re,math

def winning_races(total_time, record_distance):
    root1 = ((total_time + ((total_time**2 -4*record_distance)**(1/2)))/2 - 0.05)
    root2 = ((total_time - ((total_time**2 -4*record_distance)**(1/2)))/2 + 0.05)
    return math.floor(root1)-math.ceil(root2) + 1
def main(file):
    times = re.findall(r'\d+', file[0])
    distance = re.findall(r'\d+', file[1])
    time = ''.join(times)
    dist = ''.join(distance)
    print(winning_races(int(time),int(dist)))

if __name__ == '__main__':
    with open('day_6.txt') as file:
        main(file.readlines())