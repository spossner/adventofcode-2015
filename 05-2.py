class Solution:
    def solve(self, data):
        if type(data) is not list:
            data = [data]

        nice_count = 0

        for text in data:
            print(text)
            triple = False
            pair = False
            pairs = {}
            for i in range(len(text)):
                if i > 1:
                    if not triple and text[i-2] == text[i]:
                        triple = True
                if not pair and i > 0:
                    p = text[i-1:i+1]
                    if p in pairs:
                        if pairs[p] < i-2:
                            pair = True
                    else:
                        pairs[p] = i-1

            if pair and triple:
                nice_count += 1
        return nice_count


if __name__ == '__main__':
    s = Solution()
    assert s.solve('qjhvhtzxzqqjkmpb') == 1
    assert s.solve('xxyxx') == 1
    assert s.solve('uurcxstgmygtbstg') == 0
    assert s.solve('ieodomkazucvgmuy') == 0
    with open('05.txt') as f:
        print(s.solve(f.readlines()))
