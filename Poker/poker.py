import random

hand = []
hand_suit = []
hand_type = []

stats = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a Kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a Kind": 0,
    "Two Pair": 0,
    "Pair": 0,
    "High Card": 0
}


def getcards(min, max, num):
    cards = []
    for i in range(min, max + 1):
        cards.append(i)
    for j in range(num):
        rand = random.randrange(0, max - min + 1)
        last_pos = len(cards) - 1 - j
        cards[rand], cards[last_pos] = cards[last_pos], cards[rand]
    return cards[-num:]


def card_suit(index):
    index %= 4
    if index == 0:
        return 'Diamonds'
    elif index == 1:
        return 'Spades'
    elif index == 2:
        return 'Hearts'
    elif index == 3:
        return 'Clubs'


def card_number(index):
    index %= 13
    return index


def card_type(index):
    type = index + 2
    if type == 11:
        return "Jack"
    if type == 12:
        return "Queen"
    if type == 13:
        return "King"
    if type == 14:
        return "Ace"
    return type


def checkforpairs(values):
    combos = [n for n in values if values.count(n) > 1]
    single_combos = list(set(combos))
    return len(combos), single_combos


def check_combinations(symbols, values):
    orders = False
    if symbols.count(symbols[0]) == len(symbols):
        symbols.sort()
        if values[0] == values[-1] - 4 and values[-1] == 12:
            stats["Royal Flush"] += 1
            orders = True
        elif values[0] == values[-1] - 4:
            stats["Straight Flush"] += 1
            orders = True
        elif not orders:
            stats["Flush"] += 1
    if checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) == 1:
        stats["Four of a Kind"] += 1
        orders = True
    elif checkforpairs(values)[0] == 5 and len(checkforpairs(values)[1]) >= 2:
        stats["Full House"] += 1
        orders = True
    elif checkforpairs(values)[0] == 3:
        stats["Three of a Kind"] += 1
        orders = True
    elif checkforpairs(values)[0] == 4 and len(checkforpairs(values)[1]) >= 2:
        stats["Two Pair"] += 1
        orders = True
    elif checkforpairs(values)[0] == 2:
        stats["Pair"] += 1
        orders = True
    values.sort()
    if values[0] == values[-1] - 4 and len(checkforpairs(values)[1]) == 0:
        stats["Straight"] += 1
        orders = True
    if not orders:
        stats["High Card"] += 1


if __name__ == "__main__":
    for x in range(10000):
        yourCards = getcards(1, 52, 5)
        for i in yourCards:
            hand_type.append(card_number(i))
            hand_suit.append(card_suit(i))
            hand.append([card_type(card_number(i)), card_suit(i)])
        check_combinations(hand_suit, hand_type)
        hand_type = []
        hand_suit = []
    print(stats)
