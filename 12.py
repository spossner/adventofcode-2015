import json


class Solution:
    def solve(self, data):
        j = json.loads(data)
        return self.count_nums(j)

    def count_nums(self, element):
        if element is None:
            return 0
        if type(element) == int:
            return int(element)
        if type(element) == str:
            return 0
        if type(element) == list:
            return sum(map(lambda x: self.count_nums(x), element))
        if type(element) == dict:
            values = list(element.values())
            return self.count_nums(values) if not "red" in values else 0
        raise Exception(f"unknown type {type(element)}")


if __name__ == '__main__':
    s = Solution()
    assert s.solve('[1,2,3]') == 6
    assert s.solve('{"a":2,"b":4}') == 6
    assert s.solve('[[[3]]]') == 3
    assert s.solve('{"a":{"b":4},"c":-1}') == 3
    assert s.solve('{"a":[-1,1]}') == 0
    assert s.solve('[-1,{"a":1}]') == 0
    assert s.solve('[]') == 0
    assert s.solve('{}') == 0
    with open('12.txt', 'r') as f:
        print(s.solve(f.read()))

