class Solution:
    ILLEGAL_CHARS = set(map(lambda c: ord(c), ('i', 'o', 'l')))
    SKIP_ONE_CHARS = set(map(lambda c: ord(c), ('h', 'n', 'k')))

    def solve(self, data):
        # if type(data) is not list:
        #     data = [data]
        #
        # for letters in data:
        letters = list(map(lambda c: ord(c), data))
        self.increment(letters) # initial increment
        while not self.check_password(letters):
            candidate_found = False
            while not candidate_found:
                candidate_found = self.increment(letters)
            # print(f"candidate found: {letters}")

        return self.dump_letters(letters)

    def dump_letters(self, letters):
        return "".join(map(lambda x:chr(x), letters))

    def check_password(self, letters):
        # print(f"checking {self.dump_letters(letters)}")
        if len(letters) != 8:
            return False

        skip_next = False
        sequence_found = False
        pairs_count = 0
        for i, c in enumerate(letters):
            if c in self.ILLEGAL_CHARS:
                return False

            if not sequence_found:
                if i >= len(letters) - 2:
                    return False  # can not find a sequence anymore
                if letters[i + 1] == letters[i] + 1 and letters[i + 2] == letters[i] + 2:
                    sequence_found = True
            if skip_next:
                skip_next = False
            elif pairs_count < 2:
                if i < len(letters) - 1:
                    if letters[i] == letters[i + 1]:
                        pairs_count += 1
                        skip_next = True
                else:
                    return False  # can not find a pair anymore
        return sequence_found and pairs_count >= 2

    def increment(self, letters, i=None):
        if i is None:
            i = len(letters) - 1
        if i < 0:
            raise Exception('huch... rolling over first letter')
        candidate_found = False
        if letters[i] in self.SKIP_ONE_CHARS:
            letters[i] = letters[i] + 2
        elif letters[i] == 122:  # ord('z') = 122
            letters[i] = 97  # ord('a') = 97
            candidate_found = self.increment(letters, i - 1)
        else:
            letters[i] = letters[i] + 1
        return candidate_found or self.check_potential_candidate(letters, i)

    def check_potential_candidate(self, letters, i) -> bool:
        return self.check_sequence(letters, i - 2) or self.check_sequence(letters, i - 1) or self.check_sequence(letters, i) or self.check_pair(
            letters, i - 1) or self.check_pair(letters, i)

    def check_sequence(self, letters, start) -> bool:
        if start < 0 or start > len(letters) - 3:
            return False
        return letters[start] == letters[start + 1] + 1 and letters[start] == letters[start + 2] + 2

    def check_pair(self, letters, start) -> bool:
        if start < 0 or start > len(letters) - 2:
            return False
        return letters[start] == letters[start + 1]


if __name__ == '__main__':
    s = Solution()
    # assert s.solve('abcdffaa') is True
    # assert s.check_password('hijklmmn') is False
    # assert s.check_password('abbceffg') is False
    # assert s.check_password('abbcegjk') is False
    # assert s.solve('abcdefgh') == 'abcdffaa'
    # assert s.solve('ghijklmn') == 'ghjaabcc'
    # print(s.solve('cqjxjnds'))
    print(s.solve('cqjxxyzz'))
