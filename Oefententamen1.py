# Author: Femke Spaans
# Date: 03/01/2020
# Name: BI1a-Tinf Thematoets Linux Python I Voorbeeldtoets 2019/2020
# Version: 1

def main():
    naamBestand = "chr1.csv"
    aantal = aantal_genen(naamBestand)
    groter_gc_perc_dan(naamBestand)
    gemiddelde_lengte(naamBestand, aantal)


def aantal_genen(naamBestand):
    """
    bestand openen,
    splitten op de komma,
    mogelijk in lijst zetten?
    aantal genen tellen
    :return: bestand
    """
    aantal = 0
    bestand = open(naamBestand, "r")
    bestand.readline()
    for regel in bestand:
        positie = regel.split(",")[0]
        aantal += 1
    print(aantal)
    bestand.close()
    return aantal


def groter_gc_perc_dan(naamBestand):
    """
    :param: bestand
    :return:
    """
    bestand = open(naamBestand, "r")
    bestand.readline()
    for regel in bestand:
        regel = regel.strip().split(",")
        positie = regel[-1]
        if float(positie) >= 50:
            print(regel[0])
    bestand.close()


def gemiddelde_lengte(naamBestand, aantal):
    """
    :param bestand:
    :param aantal:
    :return:
    """
    bestand = open(naamBestand, "r")
    bestand.readline()
    start = 0
    eind = 0
    for regel in bestand:
        regel = regel.strip().split(",")
        start = int(regel) [-3]
        eind = int(regel)[-2]
    lengte = eind - start
    print(lengte)





main()
