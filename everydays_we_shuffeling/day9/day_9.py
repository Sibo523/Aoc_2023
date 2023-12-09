import re

def next(line):
    diffs = [(line[i])-(line[i-1]) for i in range(1,len(line))]
    if any(x != 0 for x in line):
        return next(diffs) + line[-1]
    return 0

def main(file_content):
    lines = [list(map(int, re.split('\s+', line.strip()))) for line in file_content.split('\n')]
    total_sum = 0
    for line in lines:
        total_sum += next(line)
    print(total_sum)    #1901217887

if __name__ == '__main__':
    with open('day_9.txt') as file:
        main(file.read())
