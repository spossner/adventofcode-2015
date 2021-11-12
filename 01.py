class Solution:
    def solve(self, data):
        result = 0
        pos = 0
        for c in data:
            pos += 1
            if c == '(':
                result += 1
            elif c == ')':
                result -= 1
            if result == -1:
                return pos
        return -1

if __name__ == '__main__':
    s = Solution()
    assert s.solve(')') == 1
    assert s.solve('()())') == 5
    with open('01.txt') as f:
        print(s.solve(f.read()))