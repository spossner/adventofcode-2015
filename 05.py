class Solution:
    VOWELS = ('a','e','i','o','u')
    BLACK_LIST = (
        'ab', 'cd', 'pq', 'xy'
    )
    def solve(self, data):
        if type(data) is not list:
            data = [data]

        nice_count = 0

        for text in data:
            vowels = 0
            pair = False
            illegal = False
            for i in range(len(text)):
                if i > 0:
                    if text[i-1:i+1] in self.BLACK_LIST:
                        illegal = True
                        break
                    if not pair and text[i-1] == text[i]:
                        pair = True
                if text[i] in self.VOWELS:
                    vowels += 1

            if not illegal and pair and vowels >= 3:
                nice_count += 1
        return nice_count


if __name__ == '__main__':
    s = Solution()
    assert s.solve('ugknbfddgicrmopn') == 1
    assert s.solve('aaa') == 1
    assert s.solve('jchzalrnumimnmhp') == 0
    assert s.solve('haegwjzuvuyypxyu') == 0
    assert s.solve('dvszwmarrgswjxmb') == 0
    with open('05.txt') as f:
        print(s.solve(f.readlines()))
