class Solution:
    def solve(self, data):
        floor = 0
        position = 0
        for c in data:
            position = position + 1
            if c == '(':
                floor = floor + 1
            if c == ')':
                floor = floor - 1
            if floor == -1:
                break

        return position


if __name__ == '__main__':
    s = Solution()
    assert s.solve('))(((((') == 1
    assert s.solve('())(((((') == 3
    with open('01.txt') as f:
        print(s.solve(f.read()))