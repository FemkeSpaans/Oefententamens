# Femke Spaans
# 13/11/2019
# uitwerking tentamen blok 1


def main():
    genen_per_chr(18)
    alle_genen()


def genen_per_chr(chromo):
    aantal = 0
    aantal_p = 0
    aantal_q = 0
    bestand = open("gene_with_protein_product.txt", "r", encoding="utf8")
    for regel in bestand:
        positie = regel.split("\t")[7]
        if positie[0:2] == chromo:
            aantal += 1
            if positie[2] == "p":
                aantal_p += 1
            if positie[2] == "q":
                aantal_q += 1
    return aantal_p, aantal_q
    print(aantal)


def alle_genen():
    lijst = ["01", "02", "03"]
    for c in lijst:
        p, q = genen_per_chr(c)
        print("aantal p =", p, "aantal q =", q)


main()
