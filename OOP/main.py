
class Firma:
    pass

class Abteilung:
    pass

class Person:
    def __init__(self, vorname, nachname, geburtstag, geschlecht, email):
        self.vorname = vorname
        self.nachname = nachname
        self.geburtstag = geburtstag
        self.geschlecht = geschlecht
        self.email = email

    def __str__(self):
        return "{0} {1}, geb. am {2}, {3}, E-Mail: {4}".format(
            self.vorname, self.nachname, self.geburtstag, self.geschlecht, self.email)


class Mitarbeiter(Person):
    def __init__(self, vorname, nachname, geburtstag, geschlecht, email, mitarbeiterId, gehalt):
        super().__init__(vorname, nachname, geburtstag, geschlecht, email)
        self.mitarbeiterId = mitarbeiterId
        self.gehalt = gehalt

    def __str__(self):
        person = super().__str__()
        return "M-ID: {0}, {1}, Gehalt: {2}".format(self.mitarbeiterId, person, self.gehalt)


class Abteilungsleiter(Person):
    def __init__(self, vorname, nachname, geburtstag, geschlecht, email, abteilungsId, gehalt):
        super().__init__(vorname, nachname, geburtstag, geschlecht, email)
        self.abteilungsId = abteilungsId
        self.gehalt = gehalt

    def __str__(self):
        person = super().__str__()
        return "A-ID: {0}, {1}, Gehalt: {2}".format(self.abteilungsId, person, self.gehalt)


if __name__ == '__main__':
    p1 = Person("Leonardo", "Djurdjevic", "männlich", "20.03.2004", "ldjurdjevictsn.at")
    p2 = Person("Melihgazi", "Esen", "männlich", "06.01.2004", "meesen@tsn.at")
    p3 = Person("Mert", "Cetinkaya", "weiblich", "04.02.2004", "mcetinkaya@tsn.at")
    p4 = Person("Luca", "Dietz", "weiblich", "19.07.2004", "ldietz@tsn.at")
    p5 = Person("Kristof", "Csölle", "männlich", "31.12.2002", "kcsoelle@tsn.at")
    p6 = Person("Noel", "Klapeer", "männlich", "09.02.2004", "nklapeer@tsn.at")
    p7 = Person("Jakob", "Resch", "männlich", "22.07.2004", "jresch@tsn.at")
    p8 = Person("Noah", "Muigg", "männlich", "17.04.2004", "nklapeer@tsn.at")
    p9 = Person("Niklas", "Sillaber", "männlich", "")

    a1 = Abteilungsleiter(p1.vorname, p1.nachname, p1.geschlecht, p1.geburtstag, p1.email, 1, 5000)
    a2 = Abteilungsleiter(p3.vorname, p3.nachname, p3.geschlecht, p3.geburtstag, p3.email, 2, 4500)
    a3 = Abteilungsleiter(p7.vorname, p7.nachname, p7.geschlecht, p7.geburtstag, p7.email, 2, 4400)

    print(a1)
