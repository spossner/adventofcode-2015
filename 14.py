import re
import itertools

class Solution:
    def solve(self, data, time):
        if type(data) is not list:
            data = [data]

        result = (0, None)
        r = re.compile('(\w+) can fly (\d+) .* (\d+) seconds.* (\d+) seconds.*')
        for row in data:
            m = r.match(row)
            src = m.group(1)
            speed = int(m.group(2))
            duration = int(m.group(3))
            pause = int(m.group(4))
            block = duration+pause
            distance = int(time/block) * speed * duration + (min(time % block, duration) * speed)
            if distance > result[0]:
                result = (distance, src)
        return result


if __name__ == '__main__':
    s = Solution()
    # assert s.solve('Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.', 100) == (176.0, 'Rudolph')
    # assert s.solve('Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.', 165) == (176.0, 'Rudolph')
    assert s.solve('Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.', 173) == (176.0, 'Rudolph')
    assert s.solve('Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.', 177) == (264.0, 'Rudolph')
    assert s.solve('Rudolph can fly 22 km/s for 8 seconds, but then must rest for 165 seconds.', 181) == (352.0, 'Rudolph')
    with open('14.txt') as f:
       print(s.solve(f.read().splitlines(), 2503))

