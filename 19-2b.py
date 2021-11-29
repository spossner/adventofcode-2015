import random


class Solution:
    def solve(self, data):
        ops = [(l.split()[-1], l.split()[0]) for l in data if "=>" in l]
        ops.sort(key=lambda x: len(x[0]))

        tries = 1
        while True:
            medicine = data[-1].strip()
            random.shuffle(ops)
            print(f"Try {tries}...")
            tries += 1
            total = 0
            while medicine != 'e':
                replaced = False
                for lhs, rhs in ops:
                    if lhs in medicine:
                        medicine = medicine.replace(lhs, rhs, 1)
                        total += 1
                        replaced = True
                        break
                if not replaced:
                    break
            if medicine == 'e':
                return total


if __name__ == '__main__':
    s = Solution()
    with open('19.txt') as f:
        result = s.solve(f.read().strip().splitlines())
        print(result)