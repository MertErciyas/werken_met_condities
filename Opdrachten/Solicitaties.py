#Mert Erciyas 99058235
# Solicitatie print
print("----------------------------------------------")
print("|             Sollicitatieformulier          |")
print("----------------------------------------------")
print("|Er word een aantal relevante vragen gesteld |")
print("|Liefst invullen met eer en geweten          |")
print("|Als het blijkt dat u aan de citeria voldoet |")
print("|dan komt in aanmerking voor de sollicitatie |")
print("|Veel Succes!                                |")
print("----------------------------------------------")

personCompitence = ["0_personErvaring", "1_mboDiploma", "2_vrachtWagenRijbewijs", "3_bezittingHoed", "4_certificaat"]
personPhysical = ["0_naam", "1_haar", "2_lengte", "3_gewicht"]
distraction = ["0_sokken", "1_artiest", "2_pepsi", "3_eten"]
results = (personPhysical + personCompitence)  

# Vragen voor iedereen
naam = input("Wat is u naam?\n")
naam = True
personErvaring = int(input("Hoeveel jaar in praktijk ervaring heeft u in dieren-dressuur of jongleren of acrobatiek?\n"))
if personErvaring >= 3:
    personErvaring = True
elif personErvaring < 3:
    personErvaring = False
else:
    print("invalid input, exiting program")
    exit()
mboDiploma = int(input("Wat voor MBO diploma heeft u voor onderneming?\n"))
if mboDiploma >= 4:
    mboDiploma = True
elif mboDiploma < 4:
    mboDiploma = False
else:
    print("invalid input, exiting program")
    exit()
vrachtWagenRijbewijs = input("Heeft u een vrachtwagen rijbewijs?(J/N)\n")
if vrachtWagenRijbewijs == "J":
    vrachtWagenRijbewijs = True
elif vrachtWagenRijbewijs == "N":
    vrachtWagenRijbewijs = False
else:
    print("invalid input, exiting program")
    exit()
bezittingHoed = input("Bent u in bezit van een grote hoed? (J/N)\n")
if bezittingHoed == "J":
    bezittingHoed = True
elif bezittingHoed == "N":
    bezittingHoed = False
else:
    print("invalid input, exiting program")
    exit()
gender = input("Bent u een man of een vrouw?\n")
if gender == "man":
    haar = input("Hoelang is u snor?\n") # Vraag voor een man
    haar = True
elif gender == "vrouw":
    haar = input("hoelang is u krulhaar?\n") # Vraag voor een Vrouw
    haar = True
else:
    print("invalid input, exiting program")
    exit()
# Vragen voor iedereen
lengte = int(input("hoelang bent u?\n")) 
if lengte >= 180:
    lengte = True
elif lengte < 180:
    lengte = False
else:
    print("invalid input, exiting program")
    exit()
gewicht = int(input("Hoeveel weegt u?\n"))
if gewicht >= 90:
    gewicht = True
elif gewicht < 90:
    gewicht = False
certificaat = input("Heeft u een certificaat van Overleven met gevaarlijke personeel? (J/N)\n")
if certificaat == "J":
    certificaat = True
elif certificaat == "N":
    certificaat = False
# Vragen die niet uitmaken
sokken = input("Wat voor merk sokken draagt u graag?\n")
artiest = input("Wat is u favoriete artiest\n")
pepsi = input("Coca cola of Pepsi?\n   ")
eten = input("Wat is u favoriete eten?\n")

if naam == True and personErvaring == True and mboDiploma == True and vrachtWagenRijbewijs == True and bezittingHoed == True and haar == True and lengte == True and gewicht == True and certificaat == True:
    print("U bent aangenomen!")
else:
    print("U bent helaas niet angenomen")
