class Solution:
    OFFSET = ((-1, -1), (0, -1), (1, -1),
              (-1, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1))

    def __init__(self):
        self.grid = []

    def solve(self, data, steps):
        for row in data:
            self.grid.append(list(map(lambda c: 0 if c == '.' else 1, list(row))))
        width = len(self.grid[0])
        height = len(self.grid)
        corners = ((0, 0), (width - 1, 0), (0, height - 1), (width - 1, height - 1))
        for x, y in corners:
            self.grid[y][x] = 1
        self.dump()
        for i in range(steps):
            new_state = [[0] * width for i in range(height)]
            for x, y in corners:
                new_state[y][x] = 1
            for y in range(height):
                for x in range(width):
                    if (x,y) in corners:
                        continue
                    count_adj_on = sum(self.adjacencies(x, y))
                    if self.grid[y][x] == 1:
                        new_state[y][x] = 1 if count_adj_on in (2, 3) else 0
                    else:
                        new_state[y][x] = 1 if count_adj_on == 3 else 0
            self.grid = new_state
            self.dump(i + 1)
        return self.grid

    def dump(self, i=None):
        print('Initial state:' if i is None else f"After {i} steps:")
        for row in self.grid:
            print("".join(list(map(lambda n: '#' if n == 1 else '.', row))))
        print()

    def adjacencies(self, cx, cy):
        for dx, dy in self.OFFSET:
            px = cx + dx
            py = cy + dy
            if px >= 0 and py >= 0 and px < len(self.grid[0]) and py < len(self.grid):
                yield self.grid[py][px]


if __name__ == '__main__':
    s = Solution()
    with open('18.txt') as f:
        result = s.solve(f.read().strip().splitlines(), 100)
        print(sum([sum(i) for i in result]))
