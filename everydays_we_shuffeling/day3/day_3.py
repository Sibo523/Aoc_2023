import timeit
def in_grid(grid, x,y):
    return 0 <= x < len(grid) and 0 <= y < len(grid)
def main():
    with open('C:\helper\day3.txt') as file:
        sum = 0
        d = file.readlines()
        temp = ""
        flag = False
        for num_line, line in enumerate(d):
            for num, c in enumerate(line):
                l =0
                if (c.isdigit()):
                    temp += c
                elif not temp == "":
                    x = len(temp)
                    for i in range(num-x-1, num +1):
                       for j in range (num_line-1,num_line+2): #num here is plus 1 from the end of the number pos
                           if in_grid(d,i,j):
                               if d[j][i] != '.' and not d[j][i].isdigit():
                                   flag = True
                    if flag:
                        sum +=int(temp)
                    temp = ""
                    flag = False
        print(sum)

if __name__ == '__main__':
    print(f'time took: {timeit.timeit(main, number=1)}')