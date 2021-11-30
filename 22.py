import collections
import copy
import json


class Spell:
    SPELLS = {                                    #   0     1      2       3     4        5                6
        'MISSLE': ('MISSLE', 53, 4, 0, 0, 0, 0),  # name, costs, damage, heal, mana, armor-increase, effect-duration
        'DRAIN': ('DRAIN', 73, 2, 2, 0, 0, 0),
        'SHIELD': ('SHIELD', 113, 0, 0, 0, 7, 6),
        'POISON': ('POISON', 173, 3, 0, 0, 0, 6),
        'RECHARGE': ('RECHARGE', 229, 0, 0, 101, 0, 5)
    }


class Game:
    def __init__(self, player_points, mana, boss_points, damage):
        self.player = player_points
        self.mana = mana
        self.boss = boss_points
        self.damage = damage
        self.effects = {}
        self.mana_spent = 0

    def is_finished(self):
        return self.player <= 0 or self.boss <= 0

    def is_dead(self):
        return self.player <= 0

    def has_won(self):
        return self.boss <= 0

    def get_armor(self):
        return Spell.SPELLS['SHIELD'][5] if 'SHIELD' in self.effects else 0

    def dump_status(self):
        print(f'- Player has {self.player} hit points, {self.get_armor()} armor, {self.mana} mana')
        print(f'- Boss has {self.boss} hit points')
        print(f'{self.effects}')

    def cast(self, spell):
        if self.is_finished():
            return

        print(f'Player casts {spell[0]}', end='')
        self.mana -= spell[1] # take costs
        self.mana_spent += spell[1]
        if spell[6] == 0:
            self.boss -= spell[2]
            self.player += spell[3]
            print(f', dealing {spell[2]} damage and {spell[3]} healing')
        else:
            self.effects[spell[0]] = spell[6] # NAME -> turns_left
            print('.')

    def attack(self):
        if self.is_finished():
            return

        d = max(self.damage - self.get_armor(), 1)
        print(f'Boss attacks for {d} damage.')
        self.player -= d

    def decrease(self):
        if self.is_finished():
            return
        self.player -= 1

    def process_effects(self):
        if self.is_finished():
            return

        if len(self.effects) == 0:
            return

        for name in self.effects.keys():
            e = Spell.SPELLS[name]
            self.boss -= e[2]  # process damage
            self.mana += e[4] # process mana
            # ignore armor
            self.effects[name] = self.effects[name] - 1
            # print(f"{name}, timer is now {self.effects[name]}")

        new_effects = {k: v for k, v in self.effects.items() if v > 0}
        if len(self.effects) != len(new_effects):
            # print(f"dropped at least 1 effect: {self.effects} vs {new_effects}")
            self.effects = new_effects

    def __str__(self):
        return f'<{self.player} ({self.mana_spent}) || {self.boss}>'



class Solution:
    def __init__(self, hitpoints, mana, boss_points, damage):
        self.init_state = Game(hitpoints, mana, boss_points, damage)
        self.active_effects = {}

    def solve(self):
        results = []
        d = collections.deque()
        d.append(self.init_state)

        count = 0
        while len(d) > 0 and count < 10:
            for i in range(len(d)):
                state = d.popleft()

                for spell in Spell.SPELLS.values():
                    if spell[1] > state.mana:
                        continue

                    new_state = copy.deepcopy(state)
                    print(f'-- Player turn --')
                    new_state.decrease()
                    new_state.dump_status()
                    new_state.process_effects()
                    if spell[0] in state.effects:
                        continue
                    new_state.cast(spell)

                    if new_state.is_finished():
                        if new_state.is_dead():
                            print(f'LOST - ignore this path')
                        elif new_state.has_won():
                            print(f'WON - this is a candidate')
                            results.append(new_state)
                        continue

                    print(f'-- Boss turn --')
                    new_state.dump_status()
                    new_state.process_effects()
                    new_state.attack()

                    if new_state.is_finished():
                        if new_state.is_dead():
                            print(f'LOST - ignore this path')
                        elif new_state.has_won():
                            print(f'WON - this is a candidate')
                            results.append(new_state)
                        continue

                    d.append(new_state)
            count += 1
        return results

if __name__ == '__main__':
    #s = Solution(10, 250, 13, 8)
    #print(s.solve())

    #s = Solution(10, 250, 14, 8)
    #print(s.solve())

    s = Solution(50, 500, 51, 9)
    result = s.solve()
    for r in result:
        print(r)
