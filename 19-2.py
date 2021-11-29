import collections


class Solution:
    def solve(self, data):
        self.ops = collections.defaultdict(list)
        for instruction in data[:-2]:
            src, dest = instruction.split(' => ')
            self.ops[src].append(dest)
        self.word = data[-1]

        visited = set()
        nodes = collections.deque()
        nodes.append('e')
        steps = 0

        while len(nodes) > 0:
            for i in range(len(nodes)):
                node = nodes.popleft()
                if node == self.word:
                    return steps
                for word in self.next_molecules(node):
                    if not word in visited:
                        visited.add(word)
                        nodes.append(word)
            # print(nodes)
            steps += 1
            print(f"{steps} steps with deque of len {len(nodes)}")




    def next_molecules(self, word):
        result = set()
        for i in range(len(word)):
            if word[i] == self.word[i]:
                continue
            if word[i] in self.ops:
                for dest in self.ops[word[i]]:
                    new_word = word[:i]+dest+word[i+1:]
                    if self.is_legal(new_word):
                        result.add(new_word)
            if i < len(word)-1:
                src = word[i:i+2]
                if src in self.ops:
                    for dest in self.ops[src]:
                        new_word = word[:i] + dest + word[i + 2:]
                        if self.is_legal(new_word):
                            result.add(new_word)
        return result

    def is_legal(self, word):
        if len(word) > len(self.word):
            return False
        i = 0
        while i <  len(word):
            if word[i] == self.word[i]:
                i += 1
            elif word[i] in self.ops or (i < len(word)-1 and word[i:i+2] in self.ops):
                #print(f"{word} can be continued at position {i}")
                return True
            else:
                # no match and no replacement found at position i
                return False


if __name__ == '__main__':
    s = Solution()
    with open('19.txt') as f:
        result = s.solve(f.read().strip().splitlines())
        print(result)