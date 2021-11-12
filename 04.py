import hashlib


class Solution:
    def solve(self, data):
        i = 0
        while True:
            s = f"{data}{i}".encode('utf-8')
            n = hashlib.md5(s).hexdigest()
            # PART 2 -> 6 zeros
            if n.startswith('000000'):
                break
            i += 1

        return i


if __name__ == '__main__':
    s = Solution()
    # assert s.solve('abcdef') == 609043
    # assert s.solve('pqrstuv') == 1048970
    print(s.solve('iwrupvqb'))
