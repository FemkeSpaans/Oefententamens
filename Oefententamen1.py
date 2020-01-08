# Author: Femke Spaans
# Date: 03/01/2020
# Name: BI1a-Tinf Thematoets Linux Python I Voorbeeldtoets 2019/2020
# Version: 1

def main():
    naamBestand = "chr1.csv"
    aantal = aantal_genen(naamBestand)
    groter_gc_perc_dan(naamBestand)
    #gemiddelde_lengte(naamBestand, aantal)


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
    gc_perc = 50
    boven_vijftig = []
    bestand = open(naamBestand, "r")
    bestand.readline()
    for regel in bestand:
        positie = regel.strip().split(",")[5]
        boven_vijftig.append(float(positie))
    bestand.close()
    print(boven_vijftig)

    # if positie == gc_perc or positie >= gc_perc:
    # boven_vijftig.append(positie)
    # print(positie)


def gemiddelde_lengte(bestand, aantal):
    """
    :param bestand:
    :param aantal:
    :return:
    """


main()
