import re


class Solution:
    def solve(self, data):
        if type(data) is not list:
            data = [data]

        r = re.compile('(.+)\s+(\d+),(\d+) through (\d+),(\d+)')
        grid = [[0] * 1000 for i in range(1000)]
        for cmd in data:
            m = r.match(cmd)
            mode = m.group(1)[-1] # n -> on | f -> off | e -> toggle
            sx = int(m.group(2))
            sy = int(m.group(3))
            ex = int(m.group(4))
            ey = int(m.group(5))
            for y in range(sy, ey+1):
                for x in range(sx, ex+1):
                    state = grid[y][x]
                    if mode == 'n':
                        state += 1
                    elif mode == 'f' and state > 0:
                        state -= 1
                    elif mode == 'e':
                        state += 2
                    grid[y][x] = state
        return sum([sum(i) for i in grid])

if __name__ == '__main__':
    s = Solution()
    assert s.solve('turn on 0,0 through 0,0') == 1
    assert s.solve(['toggle 0,0 through 999,999']) == 2000000
    with open('06.txt') as f:
        print(s.solve(f.readlines()))
