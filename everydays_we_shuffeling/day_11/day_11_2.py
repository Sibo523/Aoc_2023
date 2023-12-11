
def main(file):
    f = file.split('\n')
    new_lines = []
    bruy = []
    for index,line in enumerate(f):
        new_lines.append(line)
        if all(ch == '.' for ch in line):
            bruy.append(index)
    transpose = list(zip(*new_lines))
    new_lines.clear()
    brux = []
    for index,line in enumerate(transpose):
        new_lines.append(line)
        if all(ch == '.' for ch in line):
            brux.append(index)
    transpose = list(zip(*new_lines))

    dic = []
    for y,line in enumerate(transpose):
        for x,char in enumerate(line):
            if char == '#':
                tempx =0
                tempy = 0
                for i in brux:
                    if i < x:
                        tempx+= 999999
                for i in bruy:
                    if i < y:
                        tempy += 999999
                dic.append((y+tempy,x+tempx))
    sum = 0
    for index,val in enumerate(dic):
        for i in dic[index+1:]:
            sum+= abs(val[0]-i[0])+abs(val[1]-i[1])

    print(sum)

if __name__ == '__main__':
    with open('day_11.txt') as file:
        main(file.read())