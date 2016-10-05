import os
from tv import TV

program=["", "Music is life", "Har du tur i kärlek?", "Pengar är inte allt", "Vem vill inte bli miljonär?" ]
kanaler=["", "Tv 1", "Tv 2", "Tv 3", "Tv 4"]


def ladda():
    #Laddar kanal och volyminställningar från settings.conf
    fil = open("settings.conf", "r")
    lines = fil.readlines()
    for line in lines:
        if line.startswith("TV1-volume:"):
            tv1.volym=int((line.split(":")[1]))
            fil.close()
        if line.startswith("TV1-kanal:"):
            tv1.kanal=int((line.split(":")[1]))
            fil.close()
        if line.startswith("TV2-volume:"):
            tv2.volym=int((line.split(":")[1]))
            fil.close()
        if line.startswith("TV2-kanal:"):
            tv2.kanal=int((line.split(":")[1]))
            fil.close()
    return

def cls():
    #Rensa skärmen
    print ("\n" * 50)

def spara():
    #Sparar kanal och volyminställningar till filen settings.conf
    fil = open("settings.conf", "w")
    fil.write("TV1-volume:"+str(tv1.volym)+"\n")
    fil.write("TV1-kanal:"+str(tv1.kanal)+"\n")
    fil.write("TV2-volume:"+str(tv2.volym)+"\n")
    fil.write("TV2-kanal:"+str(tv2.kanal)+"\n")
    fil.close()

    return
def meny(menu_level=0, alternativ=3):
    # Innehåller all menyhantering

    while True:
        cls()
        display()
        print("***Välkommen till TV-simulatorn, vi har två TV-apparater som kan användas i simuleringen***")
        print("1. VardagsrumsTV")
        print("2. Köks TV")
        print("3. Avsluta")
        try:
            menyval = input("Välj:")
            if 0 < int(menyval) <= alternativ:
                if menyval == "1":
                    while menyval == "1":
                        cls()
                        display()
                        print("Du styr nu vardagsrums-TV:n")
                        print("1. Byt kanal")
                        print("2. Höj volymen")
                        print("3. Sänk volymen")
                        print("4. Åter till huvudmenyn")
                        vmeny=input("Välj")
                        if vmeny =="4":
                            menyval=0
                        elif vmeny == "1":
                            cls()
                            display()
                            print("Välj kanal:")
                            for i in range(1, len(kanaler)):
                                print(str(i)+". ", kanaler[i], program[i])
                            while True:
                                kanalbyte=int(input())
                                if kanalbyte in range(1, len(kanaler)):
                                    tv1.bytKanal(kanalbyte)
                                    break
                                else:
                                    print("Fel val, försök igen")

                        elif vmeny == "2":
                            tv1.hojVolym()
                        elif vmeny == "3":
                            tv1.sankVolym()
                        else:
                            print("Fel val, försök igen")
                            vmeny=0
                elif menyval == "2":
                    while menyval == "2":
                        cls()
                        display()
                        print("Du styr nu köks-TV:n")
                        print("1. Byt kanal")
                        print("2. Höj volymen")
                        print("3. Sänk volymen")
                        print("4. Åter till huvudmenyn")
                        vmeny=input("Välj")
                        if vmeny =="4":
                            menyval=0
                        elif vmeny == "1":
                            cls()
                            display()
                            print("Välj kanal:")
                            for i in range(1, len(kanaler)):
                                print(str(i)+". ", kanaler[i], program[i])
                            while True:
                                kanalbyte=int(input())
                                if kanalbyte in range(1, len(kanaler)):
                                    tv2.bytKanal(kanalbyte)
                                    break
                                else:
                                    print("Fel val, försök igen")

                        elif vmeny == "2":
                            tv2.hojVolym()
                        elif vmeny == "3":
                            tv2.sankVolym()
                        else:
                            print("Fel val, försök igen")
                            vmeny=0

                elif int(menyval) == alternativ:
                    return False
                else:
                    print("Välj ett alternativ mellan 1 och ", alternativ)
        except ValueError:
            print("Fel val. Försök igen.")
    return False

def display(prompt_message=""):
    # Visar meddelanden från TV-apparaterna, t.ex. vad som sänds och eventuella meddelanden
    cls()
    print("På vardagsrums-TV:n visas ", kanaler[int(tv1.kanal)], "med programmet:", program[int(tv1.kanal)])
    if tv1.message != 0:
        print(tv1.message)
        tv1.message == 0
    print("På köks-TV:n visas ", kanaler[tv2.kanal], "med programmet:", program[int(tv2.kanal)])

    if tv2.message != 0:
        print(tv2.message)
        tv2.message == 0
    return

run=True
tv1=TV()
tv1.program=program[1]
tv1.kanal=1
tv2=TV()
tv2.program=program[2]
tv2.kanal=2
ladda()
while run:
    run = meny()


#Updatera inställningsfil
print("Avslutar")
spara()