from functools import reduce
from itertools import combinations
from operator import mul


class Solution:
    def solve(self, data, num_groups):
        wts = [int(x) for x in data]
        group_size = sum(wts) // num_groups
        for i in range(len(wts)):
            qes = [reduce(mul, c) for c in combinations(wts, i) if sum(c) == group_size]
            if qes:
                return min(qes)


if __name__ == '__main__':
    s = Solution()

    # l = [1, 2, 3, 4]
    # print(list(s.buckets(l)))
    # l = [1, 2, 3, 4, 5]
    # print(list(s.subset_sum(l, 5)))

    # with open('24-dev.txt') as f:
    #    print(s.solve(f.read().strip().splitlines(), 3))

    with open('24.txt') as f:
        data = f.read().strip().splitlines()
        print(s.solve(data, 3))
        print(s.solve(data, 4))
