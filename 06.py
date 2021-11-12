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
                    new_state = 0
                    if mode == 'n' or (mode == 'e' and grid[y][x] == 0):
                        new_state = 1
                    grid[y][x] = new_state
        return sum([sum(i) for i in grid])

if __name__ == '__main__':
    s = Solution()
    assert s.solve('turn on 0,0 through 999,999') == 1000000
    assert s.solve('turn on 0,0 through 2,2') == 9
    assert s.solve(['turn on 0,0 through 999,999', 'turn off 0,0 through 2,2']) == 1000000-9
    assert s.solve(['turn on 0,0 through 999,999', 'toggle 0,0 through 2,2']) == 1000000-9
    with open('06.txt') as f:
        print(s.solve(f.readlines()))
