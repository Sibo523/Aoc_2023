
def printi(mapy):
    for i in mapy:
        for j in i:
            print(j, end = "")
        print("")

def main(file):
    f = file.split('\n')
    new_lines = []
    for i,line in enumerate(f):
        new_lines.append(line)
        if all(ch == '.' for ch in line):
            new_lines.append('.'*len(line))
    transpose = list(zip(*new_lines))
    new_lines.clear()
    for line in transpose:
        new_lines.append(line)
        if all(ch == '.' for ch in line):
            new_lines.append('.'*len(line))
    transpose = list(zip(*new_lines))
    dic = []
    for y,line in enumerate(transpose):
        for x,char in enumerate(line):
            if char == '#':
                dic.append((y,x))
    sum = 0
    for index,val in enumerate(dic):
        for i in dic[index+1:]:
            sum+= abs(val[0]-i[0])+abs(val[1]-i[1])

    print(sum)












if __name__ == '__main__':
    with open('day_11.txt') as file:
        main(file.read())