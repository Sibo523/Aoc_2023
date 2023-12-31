file = open('day18.txt').read().split('\n')
dic = {'U': (-1, 0),
       'D': (1, 0),
       'R': (0, 1),
       'L': (0, -1)}
edge = []
last_point = (0, 0)
summer = 0
for line in file:
    direct, length, color = line.split()  # direction length of wall color of the edge
    to_y, to_x = dic[direct]
    summer += int(length)
    sy, sx = last_point  # starting x and starting y
    edge.append((sy + to_y * int(length), sx + to_x * int(length), color[:-1]))
    last_point = (edge[-1][0], edge[-1][1])

A = abs(sum(edge[i][0] * (edge[i - 1][1] - edge[(i + 1) % len(edge)][1]) for i in range(len(edge)))) // 2
i = A - summer // 2 + 1

print(i + summer)
