file = open('day18.txt').read().split('\n')
dic = {'U': (-1, 0),
       'D': (1, 0),
       'R': (0, 1),
       'L': (0, -1)}
edge = []
last_point = (0, 0)
summer = 0
for line in open('day18.txt'):
    direct, length, color = line.split()  # direction length of wall color of the edge
    color = color[2:-1]
    dr, dc = dic['RDLU'[int(color[-1])]]  # we pick the Char that we want to insert into the dic, the last number is the one we wants
    n = int(color[:-1], 16)  # we want the first 5, we now the number is hexa basis
    summer += n  # number plus this
    edge.append((last_point[0] + dr * n, last_point[1] + dc * n))
    last_point = (edge[-1])

A = abs(sum(
    edge[i][0] * (edge[i - 1][1] - edge[(i + 1) % len(edge)][1]) for i in range(len(edge)))) // 2  # shoe lace formula
i = A - summer // 2 + 1

print(i + summer)  # 92291468914147
