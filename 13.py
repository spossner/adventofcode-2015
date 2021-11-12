import re
import itertools

class Solution:
    def solve(self, data):
        if type(data) is not list:
            data = [data]
        happiness_map = {}
        guests = set()
        guests.add('Seppo')
        r = re.compile('(\w+) would (\w).* (\d+) .*next to (\w+)')
        for row in data:
            m = r.match(row)
            src = m.group(1)
            guests.add(src)
            if not src in happiness_map:
                happiness_map[src] = {}
            points = happiness_map[src]
            points[m.group(4)] = int(m.group(3)) * (1 if m.group(2) == 'g' else -1)
            guests.add(m.group(4))

        # print(happiness_map)

        result = 0
        result_seating = None
        for seating in itertools.permutations(guests):
            n = len(seating)
            sum = 0
            for i, src in enumerate(seating):
                if not src in happiness_map:
                    continue
                happiness = happiness_map[src]
                l = seating[(i-1+n) % n]
                r = seating[(i+1) % n]
                if l in happiness:
                    sum += happiness[l]
                if r in happiness:
                    sum += happiness[r]
            # print(f"{seating} = {sum}")
            if sum > result:
                result = sum
                result_seating = seating
        return (result, result_seating)

if __name__ == '__main__':
    s = Solution()
    with open('13.txt') as f:
        print(s.solve(f.read().splitlines()))

