

def Hash(line):
    total =0
    return [total := ((total +ord(i))*17)%256 for i in line][-1]
def main(file):
    arr = [{} for i in range(256)]
    for line in file:
        if '-' in line:
            line = line.split('-')
            arr[Hash(line[0])].pop(line[0],None) #if it doesn't exist doesn't do anything
        else:
            line = line.split('=')
            arr[Hash(line[0])][line[0]] = int(line[1])
    print(sum(arr[i][j]*(i+1)*(index+1) for i in range(len(arr)) for index,j in enumerate(arr[i]))) #210906
if __name__ == '__main__':
    with open ('day_15.txt') as file:
        main(file.read().split(','))