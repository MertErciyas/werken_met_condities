
a = "De kaas die u bedoelt is"
wacka = True

kaasGeel = input("is kaas geel?\n")
if kaasGeel == "ja":
    kaasGat = input("zitten gaten in?\n")
    if kaasGat == "ja":
        kaasDuur = input("is kaas duur?\n")
        if kaasDuur == "ja":
            print(a,"Emmathaler")
        elif kaasDuur == "nee":
            print(a,"leerdammer")
        else:
            print("invalid input, exiting program")
            exit()
    elif kaasGat == "nee":
        kaasHard = input("is de kaas hard?\n")  
        if kaasHard == "ja":
            print(a,"Pammigiano Reggiano")        
        elif kaasHard == "nee":
            print(a,"Goudsekaas")
        else:
            print("invalid input, exiting program")
            exit()
    else:
        print("invalid input, exiting program")
        exit()
elif kaasGeel == "nee":
    kaasSchimmel = input("heeft de kaas blauwe schimmel?\n")
    if kaasSchimmel == "ja":
        kaasKorst = input("heeft de kaas korst?\n")
        if kaasKorst == "ja":
            print(a,"Blue de Rachbaron")
        elif kaasKorst == "nee":
            print(a,"Founme d'Ambert")
        else:
            print("invalid input, exiting program")
            exit()
    elif kaasSchimmel == "nee":
        korstKaas = input("heeft de kaas korst?\n")
        if korstKaas == "ja":
            print(a,"Camembert")
        elif korstKaas == "nee":
            print(a,"Mozzarella")
        else:
            print("invalid input, exiting program")
            exit()
    else:
        print("invalid input, exiting program")
        exit()
  
    wacka=True
else:
    wacka = False
    exit()