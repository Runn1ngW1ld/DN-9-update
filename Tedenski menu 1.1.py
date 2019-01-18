teden = {
    "ponedeljek": {},
    "torek": {},
    "sreda": {},
    "cetrtek": {},
    "petek": {},
    "sobota": {},
    "nedelja": {}
}

while True:

    dan_v_tednu = raw_input("Vpisite dan, ki bi ga radi uredili: ")
    jed = raw_input("Vpisite ime jedi: ")
    cena = raw_input("Vpisite ceno jedi: ") + " EUR" + "\n"
    konec = raw_input("Ali ste koncali z urejanjem:(da/ne) ")

    if dan_v_tednu == "ponedeljek".lower():
        teden["ponedeljek"] = jed + " " + cena
    elif dan_v_tednu == "torek".lower():
        teden["torek"] = jed + " " + cena
    elif dan_v_tednu == "sreda".lower():
        teden["sreda"] = jed + " " + cena
    elif dan_v_tednu == "cetrtek".lower():
        teden["cetrtek"] = jed + " " + cena
    elif dan_v_tednu == "petek".lower():
        teden["petek"] = jed + " " + cena
    elif dan_v_tednu == "sobota".lower():
        teden["sobota"] = jed + " " + cena
    elif dan_v_tednu == "nedelja".lower():
        teden["nedelja"] = jed + " " + cena

    if konec == "da":
        menu_file = open("Tedenski menu.txt", "w+")
        menu_file.write("Tedenski meni: \n")

        menu_file.write("Ponedeljek:\n")
        menu_file.write(str(teden["ponedeljek"]))

        menu_file.write("Torek:\n")
        menu_file.write(str(teden["torek"]))

        menu_file.write("Sreda:\n")
        menu_file.write(str(teden["sreda"]))

        menu_file.write("Cetrtek:\n")
        menu_file.write(str(teden["cetrtek"]))

        menu_file.write("Petek:\n")
        menu_file.write(str(teden["petek"]))

        menu_file.write("Sobota:\n")
        menu_file.write(str(teden["sobota"]))

        menu_file.write("Nedelja:\n")
        menu_file.write(str(teden["nedelja"]))

        menu_file.close()
        break

print "Ponedeljek:"
print teden["ponedeljek"]
print "Torek:"
print teden["torek"]
print "Sreda:"
print teden["sreda"]
print "Cetrtek:"
print teden["cetrtek"]
print "Petek:"
print teden["petek"]
print "Sobota:"
print teden["sobota"]
print "Nedelja:"
print teden["nedelja"]


