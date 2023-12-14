"""
My idea is taking solution for part 1 and when I find the same grid layout then I came back to the same place,
meaning that there's no reason to keep calculating the grids casue I have all of them in my array
just need to pick the right one, using the final (number - start)%(end-start)+start
I changed cycle to a version I saw in someone's else solution that looks much cleaner
"""
grid = tuple(open('day_14.txt').read().splitlines())
def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple(
            "#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)


cache = {grid}
array = [grid]

end = 0 # the end of the loop

while True:
    end += 1
    cycle()
    if grid in cache:
        break
    cache.add(grid)
    array.append(grid)

first = array.index(grid)
grid = array[(1000000000 - first) % (end - first) + first]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))