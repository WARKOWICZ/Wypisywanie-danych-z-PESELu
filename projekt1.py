game_running = True
while game_running == True:
    pesel = input("Witaj. Proszę podaj swój PESEL: ")
    while len(pesel) != 11:
        print('Pesel ma mieć 11 cyfr')
        pesel = input('Wpisz swój pesel: ')


    # ROK

    if pesel[0] == "0":
        if pesel[1] == "0":
            print("Twój rok urodzenia to: 20" + str(pesel[0]) + str(pesel[1]))
    if pesel[0] == "9":
        print("Twój rok urodzenia to: 19" + str(pesel[0]) + str(pesel[1]))
    if pesel[0] == "8":
        print("Twój rok urodzenia to: 18" + str(pesel[0]) + str(pesel[1]))

    # MIESIĄC
    miesiąc = {"1": "Styczeń", "2": "Luty", "3": "Marzec", "4": "Kwiecień", "5": "Maj", "6": "Czerwiec", "7": "Lipiec",
               "8": "Sierpień", "9": "Wrzesień"}
    # 2000-2099
    if pesel[2] == "2" or pesel[2] == "3":
        print("Twój miesiąc urodzenia to: " + miesiąc[pesel[3]])

    # 1800-1899
    if pesel[2] == "8" or pesel[2] == "9":
        print("Twój miesiąc urodzenia to: " + miesiąc[pesel[3]])

    # 1900-1999
    if pesel[2] == "0" or pesel[2] == "1":
        print("Twój miesiąc urodzenia to: " + miesiąc[pesel[3]])

    # DZIEŃ
    print("Twój dzień urodzenia to: " + pesel[4] + pesel[5])

    # KOBIETA CZY MĘŻCZYZNA

    if pesel[9] == "1":
        print("Jesteś mężczyzną")
    if pesel[9] == "3":
        print("Jesteś mężczyzną")
    if pesel[9] == "5":
        print("Jesteś mężczyzną")
    if pesel[9] == "7":
        print("Jesteś mężczyzną")
    if pesel[9] == "9":
        print("Jesteś mężczyzną")
    if pesel[9] == "0":
        print("Jesteś kobietą")
    if pesel[9] == "2":
        print("Jesteś kobietą")
    if pesel[9] == "4":
        print("Jesteś kobietą")
    if pesel[9] == "6":
        print("Jesteś kobietą")
    if pesel[9] == "8":
        print("Jesteś kobietą")

    wybor = input("Chcesz sprawdzić kolejny pesel? 1) TAK / 2) NIE: ")
    if wybor == "1":
        pass
    elif wybor == "2":
        print("Dziękuje, do widzenia")
        break