class Solution:
    TEXT = 1
    ESCAPE = 2
    HEX = 3
    HEX2 = 4

    def solve(self, data):
        if type(data) is not list:
            data = [data]

        total_mem = 0
        total_chars = 0

        for text in data:
            mem_count = 2 # starts and ends with "
            char_count = 0

            state = self.TEXT
            for c in text[1:-1]: # all text starts and ends with "
                mem_count += 1
                if state == self.TEXT:
                    if c == '\\':
                        state = self.ESCAPE
                    else:
                        char_count += 1
                elif state == self.ESCAPE:
                    if c == '"' or c == '\\':
                        char_count += 1
                        state = self.TEXT
                    elif c == 'x':
                        state = self.HEX
                elif state == self.HEX:
                    state = self.HEX2
                elif state == self.HEX2:
                    char_count += 1
                    state = self.TEXT
            total_mem += mem_count
            total_chars += char_count
        return (total_mem, total_chars)



if __name__ == '__main__':
    s = Solution()
    assert s.solve('"\\"\\""') == (6, 2)
    assert s.solve('""') == (2, 0)
    assert s.solve('"abc"') == (5, 3)
    assert s.solve('"aaa\\"aaa"') == (10, 7)
    assert s.solve('"\\x27"') == (6, 1)
    with open('08-dev.txt') as f:
         print(s.solve(f.read().splitlines()))
    with open('08.txt') as f:
         print(s.solve(f.read().splitlines()))
