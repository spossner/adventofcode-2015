class Solution:
    OFFSETS = {
        '^': (0,-1),
        'v': (0,1),
        '<': (-1,0),
        '>': (1,0),
    }
    def solve(self, data):
        visited = set()
        visited.add((0, 0))
        pos = [(0,0), (0,0)]
        for i, c in enumerate(data):
            (dx, dy) = self.OFFSETS[c]
            p = pos[i % 2]
            pos[i % 2] = (p[0] + dx, p[1] + dy)
            visited.add(pos[i % 2])

        return len(visited)


if __name__ == '__main__':
    s = Solution()
    assert s.solve('^>') == 3
    assert s.solve('^>v<') == 3
    assert s.solve('^v^v^v^v^v') == 11
    with open('03.txt') as f:
        print(s.solve(f.read()))
