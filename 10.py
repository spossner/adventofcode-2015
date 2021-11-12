class Solution:
    def solve(self, data):
        last_char = None
        result = ''
        count = 0
        for c in data:
            if last_char is not None and last_char != c:
                result += f"{count}{last_char}"
                last_char = None

            if last_char == None:
                last_char = c
                count = 1
            elif last_char == c:
                count += 1
        if last_char is not None:
            result += f"{count}{last_char}"
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.solve('1') == '11'
    assert s.solve('11') == '21'
    assert s.solve('21') == '1211'
    assert s.solve('1211') == '111221'
    text = '1113222113'
    for i in range(50):
        text = s.solve(text)
    # print(text)
    print(len(text))


