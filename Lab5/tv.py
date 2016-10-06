class TV(object):
    def __init__(self):
        self.kanal=1
        self.volym=4
        self.message=False
        self.program=1

    def hojVolym(self):
        if self.volym > 9:
            self.message="***** Det går ej att höja volymen ytterligare *****"
        else:
            self.volym += 1
            self.message="Volymen är nu "+str(self.volym)

    def sankVolym(self):
        if self.volym < 1:
            self.message="***** Det går ej att sänka volymen ytterligare *****"
        else:
            self.volym -= 1
            self.message="Volymen är nu "+str(self.volym)

    def bytKanal(self, kanalVal):
        self.kanal=kanalVal