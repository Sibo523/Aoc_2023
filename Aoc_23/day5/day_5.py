import re, timeit
def endy(i,next_section,D):

    if i == len(next_section) - 1:
        return  len(D)
    return next_section[i + 1] - 2
def found(section, end, D , seed):
    for line in range(section, end):  # goes over the lines to check
        res = [int(i) for i in D[line].split() if i.isdigit()]  # I now every line num
        if res[1] < seed < res[1] + res[2]:
            dif = res[1] - res[0]
            seed -= dif
            return seed
    return seed
def main():
    with open('day_5.txt')as file:
        D = file.readlines()
        min_val = 10**30
        next_section = []
        for index,i in enumerate(D[1:]): #skip on the first line
            if i[0].isalpha():
                next_section.append(index+2) #know what line in the D we are :)

        for seed in re.finditer(r'\d+', D[0]): #runs on all seeds
            seed = int(seed.group())                                    #seed is a number that I want to check
            for num_sec,section in enumerate(next_section): # runs on every section
                end = endy(num_sec,next_section,D)  #gives the sections radius
                seed = found(section,end,D , seed)  #converts the seed to new thing
            if(seed < min_val): min_val = seed #update min_val after every number

        print(min_val)
if __name__ == '__main__':
    print(f'time took: {timeit.timeit(main, number=1)}')