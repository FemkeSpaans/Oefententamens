# Author: Femke Spaans
# Date: 03/01/2020
# Name: BI1a-Tinf Thematoets Linux Python I Voorbeeldtoets 2019/2020
# Version: 2

import csv

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
    counter = 0
    with open ('chr1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            counter += row[0]
        length = len(counter)
        print(length)



def groter_gc_per_dan():
    pass

def gemiddelde_lengte():
    pass


main()
