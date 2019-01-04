ponedeljek = {}
torek = {}
sreda = {}
cetrtek = {}
petek = {}
sobota = {}
nedelja = {}


while True:

    dan = raw_input("Vpisite dan: ")
    jed = raw_input("Vpisite jed: ")
    cena = raw_input("Vpisite ceno: ")
    konec = raw_input("Ali ste koncali z urejanjem: (da/ne) ")

    if dan == "ponedeljek":
        ponedeljek[jed] = cena

    elif dan == "torek":
        torek[jed] = cena

    elif dan == "sreda":
        sreda[jed] = cena

    elif dan == "cetrtek":
        cetrtek[jed] = cena

    elif dan == "petek":
        petek[jed] = cena

    elif dan == "sobota":
        sobota[jed] = cena

    elif dan == "nedelja":
        nedelja[jed] = cena

    if konec == "da":
        break

for k, v in ponedeljek.iteritems():
    print "Ponedeljek:"
    print (k) + " " + (v) + "EUR"

for k, v in torek.iteritems():
    print "Torek:"
    print (k) + " " + (v) + "EUR"

for k, v in sreda.iteritems():
    print "Sreda:"
    print (k) + " " + (v) + "EUR"

for k, v in cetrtek.iteritems():
    print "Cetrtek:"
    print (k) + " " + (v) + "EUR"

for k, v, in petek.iteritems():
    print "Petek:"
    print (k) + " " + (v) + "EUR"

for k, v, in sobota.iteritems():
    print "Sobota:"
    print (k) + " " + (v)+ "EUR"

for k, v in nedelja.iteritems():
    print "Nedelja:"
    print (k) + " " + (v) + "EUR"

meni_file = open("Tedenski meni" + ".txt", "w+")
meni_file.write("Tedeski meni \n")

for k, v in ponedeljek.iteritems():
    if konec == "da":
        meni_file.write("Ponedeljek: \n" + k + " " + v + " " + "EUR" + "\n")
for k, v in torek.iteritems():
    if konec == "da":
        meni_file.write("Torek: \n" + k + " " + v + " " + "EUR" + "\n" )

for k, v in sreda.iteritems():
    if konec == "da":
        meni_file.write("Sreda: \n" + k + " " + v + " " + "EUR" + "\n")

for k, v in cetrtek.iteritems():
    if konec == "da":
        meni_file.write("Cetrtek: \n" + k + " " + v + " " + "EUR" + "\n")

for k, v, in petek.iteritems():
    if konec == "da":
        meni_file.write("Petek: \n" + k + " " + v + " " + "EUR" + "\n")

for k, v, in sobota.iteritems():
    if konec == "da":
        meni_file.write("Sobota: \n" + k + " " + v + " " + "EUR" + "\n")

for k, v in nedelja.iteritems():
    if konec == "da":
        meni_file.write("Nedelja: \n" + k + " " + v + " " + "EUR" + "\n")


meni_file.close()