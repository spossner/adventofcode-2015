class Solution:
    OFFSETS = {
        '^': (0,-1),
        'v': (0,1),
        '<': (-1,0),
        '>': (1,0),
    }
    def solve(self, data):
        pos = (0, 0)
        visited = set()
        visited.add(pos)
        for c in data:
            (dx, dy) = self.OFFSETS[c]
            pos = (pos[0] + dx, pos[1] + dy)
            visited.add(pos)

        return len(visited)


if __name__ == '__main__':
    s = Solution()
    assert s.solve('>') == 2
    assert s.solve('^>v<') == 4
    assert s.solve('^v^v^v^v^v') == 2
    with open('03.txt') as f:
        print(s.solve(f.read()))
