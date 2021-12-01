class Solution:
    def solve(self, row, col):
        id = 1
        for i in range(1, row+col-1):
            id = id + i
        id = id + col - 1

        code = 20151125
        for i in range(id-1):
            code = (code * 252533) % 33554393

        return code


if __name__ == '__main__':
    s = Solution()
    print(s.solve(2, 1))
    print(s.solve(2, 3))
    print(s.solve(3, 4))
    print(s.solve(3010, 3019))
