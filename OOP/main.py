class Firma:
    def __init__(self, firmenname, abteilungen):
        self.firmenname = firmenname
        self.abteilungen = abteilungen

    def __str__(self):
        abteilungString = ""
        for a in self.abteilungen:
            abteilungString += a.__str__() + "\n"
        return "{0} \n\n{1}".format(self.firmenname, abteilungString)

    def zaehleMitarbeiter(self):
        anzahl = 0
        for a in self.abteilungen:
            anzahl += a.zaehlePersonen()
        return "Anzahl der Mitarbeiter: {0}".format(anzahl)

    def zaehleAbteilungen(self):
        return "Anzahl der Abteilungen: {0}".format(len(self.abteilungen))

    def staerksteAbteilung(self):
        anzahlPersonen = self.abteilungen[0].zaehlePersonen()
        for a in self.abteilungen:
            if a.zaehlePersonen() > anzahlPersonen:
                anzahlPersonen = a.zaehlePersonen()
        return "Die staerkste Abteilung ist: {0}".format(anzahlPersonen)

    def anteilGeschlechter(self):
        anzahlMaenner = 0
        anzahlFrauen = 0
        for a in self.abteilungen:
            anzahlMaenner += a.anzahlGeschlechter()[0]
            anzahlFrauen += a.anzahlGeschlechter()[1]
        prozentMaenner = (anzahlMaenner / (anzahlMaenner + anzahlFrauen)) * 100
        prozentFrauen = (anzahlFrauen / (anzahlMaenner + anzahlFrauen)) * 100
        return "Anteil Männer und Frauen im Unternehmen: {0} - {1}".format(prozentMaenner, prozentFrauen)


class Abteilung:
    def __init__(self, abteilungsname, abteilungsleiter, personen):
        self.abteilungsname = abteilungsname
        self.abteilungsleiter = abteilungsleiter
        self.mitarbeiter = personen

    def __str__(self):
        mitarbeiterString = ""
        for m in self.mitarbeiter:
            mitarbeiterString += m.__str__() + "\n\t\t"
        return "Name der Abteilung: {0} \n\t Leiter: {1} {2}\n\t Mitarbeiter: \n\t\t{3}\n".format(
            self.abteilungsname, self.abteilungsleiter.vorname, self.abteilungsleiter.nachname, mitarbeiterString)

    def zaehlePersonen(self):
        return len(self.mitarbeiter) + 1

    def anzahlGeschlechter(self):
        frauen = 0
        maenner = 0
        for m in self.mitarbeiter:
            if m.geschlecht == "männlich":
                maenner += 1
            elif m.geschlecht == "weiblich":
                frauen += 1
        return maenner, frauen


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
    m1 = Mitarbeiter("Melihgazi", "Esen", "männlich", "06.01.2004", "meesen@tsn.at", 1, 1100)
    m2 = Mitarbeiter("Luca", "Dietz", "weiblich", "19.07.2004", "ldietz@tsn.at", 2, 1300)
    m3 = Mitarbeiter("Kristof", "Csölle", "männlich", "31.12.2002", "kcsoelle@tsn.at", 3, 900)
    m4 = Mitarbeiter("Noel", "Klapeer", "männlich", "09.02.2004", "nklapeer@tsn.at", 4, 1400)
    m5 = Mitarbeiter("Noah", "Muigg", "männlich", "17.04.2004", "nklapeer@tsn.at", 5, 1000)
    m6 = Mitarbeiter("Niklas", "Sillaber", "männlich", "19.09.2003", "nsillaber@tsn.at", 6, 1200)

    a1 = Abteilungsleiter("Leonardo", "Djurdjevic", "männlich", "20.03.2004", "ldjurdjevictsn.at", 1, 5000)
    a2 = Abteilungsleiter("Mert", "Cetinkaya", "weiblich", "04.02.2004", "mcetinkaya@tsn.at", 2, 4500)
    a3 = Abteilungsleiter("Jakob", "Resch", "männlich", "22.07.2004", "jresch@tsn.at", 3, 4400)

    mitarbeiterAbteilung1 = [m1, m2]
    mitarbeiterAbteilung2 = [m3, m4]
    mitarbeiterAbteilung3 = [m5, m6]

    abteilung1 = Abteilung("IT-Abteilung", a1, mitarbeiterAbteilung1)
    abteilung2 = Abteilung("Reinigungskräfte", a2, mitarbeiterAbteilung2)
    abteilung3 = Abteilung("Büro", a3, mitarbeiterAbteilung3)

    listAbteilungen = [abteilung1, abteilung2, abteilung3]

    firma = Firma("Pfusch GmbH", listAbteilungen)

    print(firma)
    print(firma.zaehleMitarbeiter())
    print(firma.zaehleAbteilungen())
    print(firma.staerksteAbteilung())
    print(firma.anteilGeschlechter())