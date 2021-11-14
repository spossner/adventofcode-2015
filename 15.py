import collections


class Solution:
    def __init__(self):
        self.ingredients = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
        self.properties = set()
        self.items = list()

    def splits(self, amount, count):
        if count <= 1:
            yield [amount]
        else:
            for i in range(amount + 1):
                for subsplit in self.splits(amount - i, count - 1):
                    yield [i] + subsplit

    def calculate_score(self, quantities):
        score = 1

        calories = sum(quantities[item] * self.ingredients[item]['calories'] for item in quantities)
        if calories != 500:
            return 0

        print(f"combination {quantities} ends up in 500 calories with {self.ingredients}")

        for p in self.properties:
            property_score = sum(quantities[item] * self.ingredients[item][p] for item in quantities)

            if property_score > 0:
                score *= property_score
            else:
                score = 0
                break

        return score

    def solve(self, data):
        if type(data) is not list:
            data = [data]

        for row in data:
            name, values = row.split(':')
            values = map(lambda x: x.strip(), values.split(','))
            for ingredient in values:
                n, v = ingredient.split(' ')
                self.ingredients[name][n] = int(v)
                self.properties.add(n)

        self.properties.remove('calories')
        self.items = list(sorted(self.ingredients.keys()))

        best_score = 0
        best_quantities = None

        for split in self.splits(100, len(self.items)):
            quantities = dict(zip(self.items, split))
            score = self.calculate_score(quantities)

            if score > best_score:
                best_score = score
                best_quantities = quantities

        print(best_score)
        print(best_quantities)


if __name__ == '__main__':
    s = Solution()
    with open('15.txt') as f:
        s.solve(f.read().splitlines())
