class Solution:
    def solve(self, data):
        if type(data) is not list:
            data = [data]

        total_mem = 0
        total_chars = 0

        for text in data:
            mem_count = 2  # starts and ends with "
            char_count = 0

            for c in text:
                char_count += 1
                mem_count += 1
                if c in ('\\', '"'):
                    mem_count += 1

            total_mem += mem_count
            total_chars += char_count

        return (total_mem, total_chars)


if __name__ == '__main__':
    s = Solution()
    assert s.solve('""') == (6, 2)
    assert s.solve('"abc"') == (9, 5)
    assert s.solve('"aaa\\"aaa"') == (16, 10)
    assert s.solve('"\\x27"') == (11, 6)
    with open('08-dev.txt') as f:
        result = s.solve(f.read().splitlines())
        print(f"{result} -> {result[0] - result[1]}")
    with open('08.txt') as f:
        result = s.solve(f.read().splitlines())
        print(f"{result} -> {result[0] - result[1]}")
