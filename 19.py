import collections


class Solution:
    def solve(self, data):
        ops = collections.defaultdict(list)
        for instruction in data[:-2]:
            src, dest = instruction.split(' => ')
            ops[src].append(dest)
        word = data[-1]
        result = set()
        for i in range(len(word)):
            if word[i] in ops:
                for dest in ops[word[i]]:
                    result.add(word[:i]+dest+word[i+1:])
            if i < len(word)-1:
                src = word[i:i+2]
                if src in ops:
                    for dest in ops[src]:
                        result.add(word[:i] + dest + word[i + 2:])
        print(result)
        return len(result)

if __name__ == '__main__':
    s = Solution()
    with open('19-dev.txt') as f:
        result = s.solve(f.read().strip().splitlines())
        print(result)
