import collections
import re


class Solution:
    def solve(self, data, target=150):
        if type(data) is not list:
            data = [data]
        buckets = []
        for row in data:
            buckets.append(int(row))
        print(buckets)
        d = collections.deque()
        result = set()
        d.append((target, list(range(len(buckets))), []))
        while (len(d) > 0):
            for i in range(len(d)):
                l, b, used = d.popleft()
                # print(l,b)

                if l == 0:
                    used.sort()
                    result.add(tuple(used))
                    #print(f"found candidate")

                if l <= 0:
                    continue


                for j in range(len(b)):
                    e = buckets[b[j]]
                    if l >= e:
                        new_buckets = b[:j]+b[j+1:]
                        # print(f"using {b[j]} from {b} - going on with {new_buckets}")
                        d.append((l-e, new_buckets, used+[b[j]]))
            print(len(b))
        return result

if __name__ == '__main__':
    s = Solution()
    with open('17.txt') as f:
        result = s.solve(f.read().strip().splitlines(), 150)
        print(len(result), ':',  result)
        min_count = 150
        bucket_count = 0
        for solution in result:
            if len(solution) < min_count:
                min_count = len(solution)
                bucket_count = 1
            elif len(solution) == min_count:
                bucket_count += 1
        print(min_count,' with ', bucket_count)

