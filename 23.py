import re
import itertools

class Solution:
    def solve(self, data):
        if type(data) is not list:
            data = [data]
        r = {'a': 1, 'b': 0}
        ptr = 0
        while ptr >= 0 and ptr < len(data):
            op = data[ptr]
            cmd = op[:3]
            arg = op[4:]
            print(cmd, arg)
            if cmd == 'inc':
                r[arg] = r[arg] + 1
            elif cmd == 'hlf':
                r[arg] = r[arg] >> 1
            elif cmd == 'tpl':
                r[arg] = r[arg] * 3
            elif cmd == 'jmp':
                ptr = eval(f"ptr {arg}")
                continue
            elif cmd == 'jie':
                arg = arg.split(',')
                if r[arg[0]] % 2 == 0:
                    ptr = eval(f"ptr {arg[1]}")
                    continue
            elif cmd == 'jio':
                arg = arg.split(',')
                if r[arg[0]] == 1:
                    ptr = eval(f"ptr {arg[1]}")
                    continue
            ptr += 1
        return r

if __name__ == '__main__':
    s = Solution()
    #with open('23-dev.txt') as f:
    #   print(s.solve(f.read().strip().splitlines()))
    with open('23.txt') as f:
       print(s.solve(f.read().strip().splitlines()))

