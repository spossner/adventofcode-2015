import collections
import functools
import re


class Solution:
    def add_node(self, nodes, no, name) -> int:
        if not name in nodes:
            nodes[name] = no
            no = no << 1
        return no

    def solve(self, data):
        if type(data) is not list:
            data = [data]
        edges = {}
        node_no = 0x1
        nodes = {} # name -> bit
        re_route = re.compile('(\w+) to (\w+) = (\d+)')
        for route in data:
            m = re_route.match(route)
            if not m:
                raise Exception(f"syntax error: {route}")
            (src, dest, distance) = m.groups()
            if not src in edges:
                edges[src] = {}
            edges[src][dest] = int(distance)
            if not dest in edges:
                edges[dest] = {}
            edges[dest][src] = int(distance)
            node_no = self.add_node(nodes, node_no, src)
            node_no = self.add_node(nodes, node_no, dest)

        print(edges)
        aim = functools.reduce(lambda x, y : x | y, nodes.values())
        results = []
        for start in edges.keys():
            print(f"\n\nCHECKING start {start}")
            deq = collections.deque()
            deq.append((start, nodes[start], 0, start)) # (node, visited, costs, path)
            while len(deq) > 0:
                for i in range(len(deq)):
                    (node, visited, costs, path) = deq.popleft()
                    if visited == aim:
                        print(f"FOUND {path} for {costs}")
                        results.append((path, costs))
                        continue
                    if not node in edges:
                        print(f"no more edges from {path}")
                        continue # dead end
                    for (dest, distance) in edges[node].items():
                        if (visited & nodes[dest]) == 0:
                            print(f"processing {node} with {visited} and {costs} costs so far")
                            print(f"{node}: next node {dest} with costs {distance}")
                            deq.append((dest, visited | nodes[dest], costs+distance, path+">"+dest))
                        else:
                            print(f"{dest} already visited in {path}")
        return results

if __name__ == '__main__':
    s = Solution()
    with open('09.txt') as f:
        result = s.solve(f.read().splitlines())
        print(result)
        print(functools.reduce(lambda x, y: x if x[1] > y[1] else y, result))
