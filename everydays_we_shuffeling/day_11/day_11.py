
def main(file):
    new_lines = file.split('\n')
    bruy = [index for index,line in enumerate(new_lines) if all(ch == '.' for ch in line)] #list of all columns that worth more
    transpose = list(zip(*new_lines))

    brux = [index for index,line in enumerate(transpose) if all(ch == '.' for ch in line)] #list of all columns that worth more
    new_lines = list(zip(*transpose))

    dic = [] #stores all galaxyies with the updated cords
    pad_worth = 1 #how much padding for each non galaxy place
    for y,line in enumerate(new_lines):
        for x,char in enumerate(line):
            if char == '#':
                tempx = pad_worth*len([i for i in brux if i < x])
                tempy = pad_worth * len([i for i in bruy if i < y])
                dic.append((y+tempy,x+tempx))
    """"
    sum all pairs possible, start from the first galaxy runs on all over galaxies 
    the reason for dic[index+1:] is so it won't sum up the pairs that been considered 
    """
    print(sum([abs(val[0]-i[0])+abs(val[1]-i[1]) for index,val in enumerate(dic) for i in dic[index+1:]]))
    #678728808158

if __name__ == '__main__':
    with open('day_11.txt') as file:
        main(file.read())