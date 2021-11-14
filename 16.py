import re


class Solution:
    def solve(self, data):
        if type(data) is not list:
            data = [data]

        r_sue = re.compile('Sue (\d+): (.*)')
        aunts = [{}] * 500
        for row in data:
            no, values = r_sue.match(row).groups()
            id = int(no)-1
            properties = {'no': no}
            for value in values.split(','):
                name, count = value.strip().split(':')
                properties[name.strip()] = int(count.strip())
            aunts[id] = properties
        metrics_str = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

        metrics = {}
        for metric in metrics_str.splitlines():
            name, value = metric.split(':')
            metrics[name.strip()] = int(value.strip())

        for k, v in metrics.items():
            aunts = list(filter(lambda a: self.matches(a, k, v), aunts))
        print(aunts)

    def matches(self, aunt, metric, value):
        if not metric in aunt:
            return True
        a_value = aunt[metric]
        if metric in ('cats', 'trees'):
            return True if a_value > value else False
        elif metric in ('pomeranians', 'goldfish'):
            return True if a_value < value else False
        else:
            return a_value == value


if __name__ == '__main__':
    s = Solution()
    with open('16.txt') as f:
        s.solve(f.read().splitlines())
