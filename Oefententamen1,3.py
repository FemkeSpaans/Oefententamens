# Author: Femke Spaans
# Date: 03/01/2020
# Name: BI1a-Tinf Thematoets Linux Python I Voorbeeldtoets 2019/2020
# Version: 2


def main():
    aantal_genen()
    groter_gc_per_dan()
    # groter_gc_perc_dan(bestandsnaam, gc_perc=50)
    # gemiddelde_lengte(bestandsnaam)


def aantal_genen():
    """
    bestand openen,
    aantal genen tellen
    """
    try:
        file = open("chr1.csv")
        file.readline()
        numline = len(file.readlines())
        print("The number of genes in this file:", numline)
    except FileNotFoundError:
        print("This file does not exist in this directory")


def groter_gc_per_dan():
    """
    bestand openen,
    genen laten zien met een GC% hoger dan 50
    """
    file = open("chr1.csv")
    file.readline()
    for row in file:
        if row[5] == 50 and if row[5] => 50 :
            print(row)



def gemiddelde_lengte():
    pass


main()
