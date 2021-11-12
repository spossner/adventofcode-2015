class Solution:
    def solve(self, data):
        x = 0
        for c in data:
            if c == '(':
                x = x + 1
            if c == ')':
                x = x - 1
        return x


if __name__ == '__main__':
    s = Solution()
    assert s.solve('(())') == 0
    assert s.solve('()()') == 0
    assert s.solve('))(((((') == 3
    with open('01.txt') as f:
        print(s.solve(f.read()))