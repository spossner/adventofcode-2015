import copy

with open("22.txt") as f:
    lines = f.readlines()

lines = list(map(lambda x: x.strip(), lines))
boss_hp = int(lines[0].split(":")[1])
boss_damage = int(lines[1].split(":")[1])

playerStart = {"Hit Points": 50
    , "Mana": 500
    , "Armor": 0
    , "Active Spells": []
    , "Mana spent": 0
               }

bossStart = {"Hit Points": boss_hp
    , "Damage": boss_damage}

outcome = 10000000  # 'infinity'
stateStack = [(playerStart, bossStart)]


def updateSpells(state):
    (player, boss) = state
    activeSpells = player["Active Spells"]
    newActive = []

    shieldOff = True
    for (spell, remaining) in activeSpells:

        if spell == "Shield":
            player["Armor"] = 7
            shieldOff = False

        elif spell == "Poison":
            boss["Hit Points"] -= 3

        elif spell == "Recharge":
            player["Mana"] += 101

        if remaining > 1:
            newActive.append((spell, remaining - 1))

    if shieldOff:
        player["Armor"] = 0

    player["Active Spells"] = newActive

    return (player, boss)


def bossTurn(state):
    global outcome
    (player, boss) = updateSpells(state)

    if boss["Hit Points"] <= 0:
        res = player["Mana spent"]
        if res < outcome:
            outcome = res

    damage_dealt = max([1, boss["Damage"] - player["Armor"]])
    player["Hit Points"] -= damage_dealt

    if player["Hit Points"] > 0:
        stateStack.append((player, boss))


# of course it is implied that the player is able to win
def playerTurn(state):
    global outcome

    spells = [("Magic Missile", 53)
        , ("Drain", 73)
        , ("Shield", 113)
        , ("Poison", 173)
        , ("Recharge", 229)
              ]

    (player, boss) = updateSpells(state)

    # hard mode
    player["Hit Points"] -= 1

    if player["Hit Points"] <= 0:
        return

    if player["Mana spent"] > outcome:
        return

    if boss["Hit Points"] <= 0:
        res = player["Mana spent"]
        if res < outcome:
            outcome = res
        return

    nextStates = []

    for (spell, cost) in spells:

        playerNext = copy.deepcopy(player)
        bossNext = copy.deepcopy(boss)

        if cost > playerNext["Mana"]:
            continue

        activeSpells = list(map(lambda a: a[1], playerNext["Active Spells"]))

        if spell in activeSpells:
            continue

        if spell == "Magic Missile":
            bossNext["Hit Points"] -= 4

        elif spell == "Drain":
            bossNext["Hit Points"] -= 4
            playerNext["Hit Points"] += 2

        elif spell == "Shield":
            playerNext["Active Spells"].append(("Shield", 6))

        elif spell == "Poison":
            playerNext["Active Spells"].append(("Poison", 6))

        elif spell == "Recharge":
            playerNext["Active Spells"].append(("Recharge", 5))
            # recharge = True

        playerNext["Mana"] -= cost
        playerNext["Mana spent"] += cost

        # check boss hitpoints
        if bossNext["Hit Points"] <= 0:
            res = playerNext["Mana spent"]
            if res < outcome:
                outcome = res

        else:
            bossTurn((playerNext, bossNext))


while stateStack != []:
    playerTurn(stateStack.pop())

print(outcome)
