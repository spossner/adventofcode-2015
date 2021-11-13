import re
import itertools


class Solution:
    def solve(self, data, time):
        if type(data) is not list:
            data = [data]

        reindeers = {}
        r = re.compile('(\w+) can fly (\d+) .* (\d+) seconds.* (\d+) seconds.*')
        for row in data:
            m = r.match(row)
            # [   0  ,    1    ,   2  ,   3                 ,    4    ,   5    ]
            # [ speed, duration, pause, block=duration+pause, distance, points ]
            reindeers[m.group(1)] = [int(m.group(2)) ,int(m.group(3)), int(m.group(4)), int(m.group(3))+int(m.group(4)), 0.0, 0]

        print(reindeers)
        leader = (0, set())
        for i in range(time):
            for name, reindeer in reindeers.items():
                d_in_block = (i % reindeer[3])
                if d_in_block < reindeer[1]: # this reindeer is running at the moment
                    reindeer[4] += reindeer[0]
                if reindeer[4] == leader[0]:
                    leader[1].add(name)
                elif reindeer[4] > leader[0]:
                    leader = (reindeer[4], set())
                    leader[1].add(name)


            for l in leader[1]:
                reindeers[l][5] += 1
            print(f"{i+1}: current leader: {leader}")
            print(reindeers)
            # distance = int(time/block) * speed * duration + (min(time % block, duration) * speed)


if __name__ == '__main__':
    s = Solution()
    with open('14.txt') as f:
       print(s.solve(f.read().splitlines(), 2503))
