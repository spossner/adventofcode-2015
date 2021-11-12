import re
from collections import deque


class Solution:
    def __init__(self, registers={}):
        self.registers = registers

    def set_value(self, dest, value):
        self.registers[dest] = value & 0xffff

    def get_value(self, value) -> int:
        try:
            return int(value) & 0xffff
        except ValueError:
            if value in self.registers:
                return self.registers[value]
            else:
                return None  # not set

    def solve(self, data):
        if type(data) is not list:
            data = [data]

        cmds = deque(data)

        r1 = re.compile('(.+) -> (.*)')
        r_binary = re.compile('(.+) (\w+) (.+)')
        r_unary = re.compile('NOT (\w+)')
        r_assign = re.compile('(\d+)')
        while len(cmds) > 0:
            for i in range(len(cmds)):
                cmd = cmds.popleft().rstrip()
                # print(cmd)
                m_cmd = r1.match(cmd)
                dest = m_cmd.group(2)
                ops = m_cmd.group(1)
                m = r_binary.match(ops)
                if m:
                    op = m.group(2)
                    o1 = self.get_value(m.group(1))
                    o2 = self.get_value(m.group(3))
                    if o1 is not None and o2 is not None:
                        if op == 'OR':
                            self.set_value(dest, o1 | o2)
                        elif op == 'AND':
                            self.set_value(dest, o1 & o2)
                        elif op == 'LSHIFT':
                            self.set_value(dest, o1 << o2)
                        elif op == 'RSHIFT':
                            self.set_value(dest, o1 >> o2)
                        else:
                            print(f"syntax error {op}: command not found")
                            raise Exception('unknown command ' + op)
                        print(f"{dest} := {o1} {op} {o2} = {self.registers[dest]}")
                    else:
                        cmds.append(cmd)  # keep that circuit

                else:
                    m = r_unary.match(ops)
                    if m:
                        o1 = self.get_value(m.group(1))
                        if o1 is not None:
                            self.set_value(dest, ~o1)
                            print(f"{dest} := NOT {o1} = {self.registers[dest]}")
                        else:
                            cmds.append(cmd)  # keep that circuit
                    else:
                        ops = self.get_value(ops)
                        if ops is not None:
                            if dest == 'b':
                                print("overwrite b assignment")
                                ops = 956
                            self.set_value(dest, ops)
                            print(f"{dest} := {ops} = {self.registers[dest]}")
                        else:
                            cmds.append(cmd)  # keep that circuit
        return self.registers


if __name__ == '__main__':
    # s = Solution()
    # with open('07-dev.txt') as f:
    #      states = s.solve(f.readlines())
    #      assert states['d'] == 72

    # with open('07.txt') as f:
    #     s.solve(f.readlines())
    #     print(s.registers)
    #     print(f"first run: {s.get_value('a')}")
    s2 = Solution({'b': 956})
    with open('07.txt') as f:
        s2.solve(f.readlines())
        print(s2.registers)
        print(f"second run: {s2.get_value('a')}")
