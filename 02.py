class Solution:
    def solve(self, data):
        if type(data) is not list:
            data = [data]
        sum = 0

        for box in data:
            (l, w, h) = map(lambda x: int(x), box.split('x'))
            areas = [l * w, w * h, h * l]
            areas.sort()
            (a1, a2, a3) = areas
            sum += (a1 << 1) + (a2 << 1) + (a3 << 1) + a1

        return sum

    def solve2(self, data):
        if type(data) is not list:
            data = [data]
        sum = 0

        for box in data:
            sides = list(map(lambda x: int(x), box.split('x')))
            sides.sort()
            (l1, l2, l3) = sides
            sum += (l1 << 1) + (l2 << 1) + (l1 * l2 * l3)

        return sum


if __name__ == '__main__':
    s = Solution()
    # PART 1
    # assert s.solve('2x3x4') == 58
    # assert s.solve('1x1x10') == 43

    # PART 2
    assert s.solve2('2x3x4') == 34
    assert s.solve2('1x1x10') == 14
    with open('02.txt') as f:
        print(s.solve2(f.readlines()))
