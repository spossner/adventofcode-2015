import itertools


class Solution:
    WEAPONS = {
        'Dagger': (8, 4, 0),
        'Shortsword': (10, 5, 0),
        'Longsword': (40, 7, 0),
        'Greataxe': (74, 8, 0)
    }

    ARMOR = {
        'None': (0, 0, 0),
        'Leather': (13, 0, 1),
        'Chainmail': (31, 0, 2),
        'Splintmail': (53, 0, 3),
        'Bandedmail': (75, 0, 4),
        'Platemail': (102, 0, 5)
    }

    RINGS = {
        'None': (0, 0, 0),
        'None2': (0, 0, 0),
        'Damage +1': (25, 1, 0),
        'Damage +2': (50, 2, 0),
        'Damage +3': (100, 3, 0),
        'Defense +1': (20, 0, 1),
        'Defense +2': (40, 0, 2),
        'Defense +3': (80, 0, 3)
    }

    def simulate(self, attacker, defender): # [Hit, Damage, Armor], [Hit, Damage, Armor]
        data = (attacker, defender)
        next_player = 0
        while True:
            d = data[next_player][1] - data[1-next_player][2]
            data[1-next_player][0] -= d
            if data[1-next_player][0] <= 0:
                return next_player
            print(data)
            next_player = 1 - next_player

    def solve(self, hitpoints, defender):
        result = 100000
        for w in self.WEAPONS.values(): # choose 1 weapon
            for a in self.ARMOR.values(): # choose 0 or 1 ARMOR (first armor us None)
                for r in itertools.combinations(self.RINGS.values(), 2): # will do the single ones duplicated..
                    attacker = [hitpoints, w[1] + r[0][1] + r[1][1], a[2] + r[0][2] + r[1][2]]
                    costs = w[0] + a[0] + r[0][0] + r[1][0]
                    if self.simulate(attacker, list(defender)) == 0 and costs < result:
                        result = costs
        return result


    def solve2(self, hitpoints, defender):
        result = 0
        for w in self.WEAPONS.values(): # choose 1 weapon
            for a in self.ARMOR.values(): # choose 0 or 1 ARMOR (first armor us None)
                for r in itertools.combinations(self.RINGS.values(), 2): # will do the single ones duplicated..
                    attacker = [hitpoints, w[1] + r[0][1] + r[1][1], a[2] + r[0][2] + r[1][2]]
                    costs = w[0] + a[0] + r[0][0] + r[1][0]
                    if self.simulate(attacker, list(defender)) == 1 and costs > result:
                        result = costs
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.solve(100, (103, 9, 2)))
    print(s.solve2(100, (103, 9, 2)))
