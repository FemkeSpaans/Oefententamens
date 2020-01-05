# Author: Femke Spaans
# Date: 03/01/2020
# Name: BI1a-Tinf Thematoets Linux Python I Voorbeeldtoets 2019/2020
# Version: 1

def main():
    aantal_genen()
    # aantal_genen(bestandsnaam)
    # groter_gc_perc_dan(bestandsnaam, gc_perc=50)
    # gemiddelde_lengte(bestandsnaam)

def aantal_genen():
    """
    bestand openen,
    splitten op de komma,
    mogelijk in lijst zetten?
    aantal genen tellen
    :return:
    """
    aantal = 0
    bestand = open("chr1.csv", "r")
    for regel in bestand:
        positie = regel.split(",")[0]
        if positie[0:] == "Gene stable ID":
            aantal += 1
        aantal = len(positie)
    print(aantal)




def groter_gc_per_dan():
    pass

def gemiddelde_lengte():
    pass


main()
