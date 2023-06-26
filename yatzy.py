from random import randint
from collections import Counter
from os import environ

dice = lambda: randint(1, 6)


class player:
    def __init__(self, name):
        self.name = name
        self.minutes = dict.fromkeys(
            [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "pair",
                "two pairs",
                "triple number",
                "four number",
                "small straight",
                "large straight",
                "full house",
                "random",
                "Yatzy",
            ],
            None,
        )

    def roll(self):
        self.row = [dice() for i in range(5)]
        self.potential()
        for i in self.options:
            if self.minutes[i] != None:
                continue
            print(i + ":" + str(self.options[i]))

    def potential(self):
        c = Counter(self.row)
        self.options = {str(i): i * self.row.count(i) for i in range(1, 7)}
        self.options.update(
            {
                "pair": max([i * c[i] if c[i] == 2 else 0 for i in range(1, 7)]),
                "two pairs": max(
                    [
                        i * c[i] + j * c[j] if c[i] >= 2 <= c[j] else 0
                        for i in range(1, 7)
                        for j in range(1, 7)
                        if i != j
                    ]
                ),
                "triple number": max(
                    [i * c[i] if c[i] == 3 else 0 for i in range(1, 7)]
                ),
                "four number": max([i * c[i] if c[i] == 4 else 0 for i in range(1, 7)]),
                "small straight": 15 if set(range(1, 6)) == set(self.row) else 0,
                "large straight": 20 if set(range(2, 7)) == set(self.row) else 0,
                "full house": sum(self.row)
                if len(c) == 2 and set((2, 3)) == set(c.values())
                else 0,
                "random": sum(self.row),
                "Yatzy": 50 if len(set(self.row)) == 1 else 0,
            }
        )

    def mark(self, choice):
        while self.minutes[choice] != None:
            print("You can't choose that.")
            choice = input(
                "Which point in minutes do you want to fill in? You can only select those whose value is None.: "
            )
        self.minutes[choice] = self.options[choice]

    def change(self, l):
        for i in l:
            self.row[i] = dice()
        self.potential()
        for i in self.options:
            if self.minutes[i] != None:
                continue
            print(i + ":" + str(self.options[i]))

    def final(self):
        self.score = sum(self.minutes.values)


p = player(environ.get("USERNAME"))
t = 0
while t < 15:
    t += 1
    p.roll()
    print(p.row)
    for i in range(2):
        if int(input("shall we take the throw already? 1 or 0: ")):
            break
        x = int(input("Throw all or just some 1 or 0: "))
        if x:
            p.roll()
            print(p.row)
        else:
            p.change(
                [
                    int(i) - 1
                    for i in input(
                        "Enter the rerolled dice 1-5 separated by a space: "
                    ).split()
                ]
            )
            print(p.row)
    for i in p.minutes:
        print(i + ":" + str(p.minutes[i]))
    p.mark(
        input(
            "Which point in minutes do you want to fill in? You can only select those whose value is None.: "
        )
    )

    print()
p.final()
print(p.score)
