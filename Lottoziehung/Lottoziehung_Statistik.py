import random


def zufall(anzahl, auswahl):
    arr = []
    i = 0
    while len(arr) <= auswahl:
        arr.append(i)
        i = i + 1

    rand = []
    while len(rand) < anzahl:
        number = random.choice(arr)
        rand.append(number)
        arr.remove(number)
    return rand


def statistik(anzahl, auswahl):
    dic = {}
    for i in range(1, anzahl + 1):
        rand = zufall(1, auswahl)
        for value in rand:
            if value in dic:
                dic[value] = dic[value] + 1
            else:
                dic.update({value: 1})
    return dic


def ziehungGescheit(min, max, wieoft):
    lottozahlen = []
    for i in range(min, max + 1):
        lottozahlen.append(i)
    for i in range(wieoft):
        zufallszahl = random.randrange(0, max - min + 1)
        lastposition = len(lottozahlen) - i - 1
        lottozahlen[zufallszahl], lottozahlen[lastposition] = lottozahlen[lastposition], lottozahlen[zufallszahl]
    return lottozahlen[-wieoft:]


def stats(min, max, wieoft, anz_ziehungen=1000):
    stat_dict = {}
    for i in range(min, max + 1):
        stat_dict[i] = 0
    for i in range(anz_ziehungen):
        for elm in ziehungGescheit(min, max, wieoft):
            stat_dict[elm] += 1
    return stat_dict


if __name__ == '__main__':
    print(stats(1, 45, 6, 10000))
