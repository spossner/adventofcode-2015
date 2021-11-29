class Solution:
    def solve(self, goal):
        size = int(goal/10)+1
        counts = [0] * size
        for n in range(1, size):
            step = n * 11
            counter = 0
            for i in range(n, size, n):
                counts[i] += step
                counter += 1
                if counter >= 50:
                    break
        #print(counts)
        for i in range(size):
            if counts[i] >= goal:
                return i
        return -1


if __name__ == '__main__':
    s = Solution()

    # assert s.solve(10) == 1
    # assert s.solve(30) == 2
    # assert s.solve(40) == 3
    # assert s.solve(60) == 4
    # assert s.solve(70) == 4
    # assert s.solve(80) == 6
    # assert s.solve(120) == 6
    # assert s.solve(130) == 8
    # assert s.solve(150) == 8
    print(s.solve(29000000))