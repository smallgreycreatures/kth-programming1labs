def tal_av_fil():
    # Frågar användaren efter en sökväg och returnerar filens innehåll som en lista
    while True:
        sökväg = input("Ange filnamn: ")
        try:
            fil = open(sökväg, "r")
            break
        except FileNotFoundError:
            print("Filen "+sökväg+" kan inte hittas, försök igen!")
    ls = []
    for line in fil:
        if not line.startswith("#"):
            ls.append(int(line))
    fil.close()
    print("Laddade in ", len(ls), " tal.")
    return ls

print (tal_av_fil())