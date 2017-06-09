import tkinter as tk
import random

def preberi_besede():
    '''Iz datoteke prebere besede in jih doda v seznam'''
    with open("besede.txt", "r") as dat:
        y = []
        for x in dat:
            beseda = x.replace("\n", "")
            y.append(beseda)
        return y

seznam_besed = preberi_besede()
tezavnost = ""


class Wind:

    def __init__(self):
        master = tk.Tk(className="vislice")

        naslov = tk.Label(master, text="Vislice", font=("Courier", 30), borderwidth=75)
        naslov.grid(columnspan=5, rowspan=2)
        lahko_text = tk.Label(text="(Izpolnjen en samoglasnik in en soglasnik ali dva soglasnika.)")
        lahko_text.grid(row=2, column=4)
        srednje_text = tk.Label(text="(Izpolnjen en soglasnik.)")
        srednje_text.grid(row=3, column=4, sticky="w")
        tezko_text = tk.Label(text="(Celotna beseda ostane zakrita.)")
        tezko_text.grid(row=4, column=4, sticky="w")

        izberi_t = tk.Label(master, text="Izberite težavnost:", font=("Courier", 13))
        izberi_t.grid(row=3, column=1)

        lahko = tk.Button(master, text="Lahko", height=1, width=10, command=self.stopnja_l)
        lahko.grid(row=2, column=3)
        self.lahko_lab = tk.Label(master, text="     ")
        self.lahko_lab.grid(row=2, column=2)

        srednje = tk.Button(master, text="Srednje", height=1, width=10, command=self.stopnja_s)
        srednje.grid(row=3, column=3)
        self.srednje_lab = tk.Label(master, text="     ")
        self.srednje_lab.grid(row=3, column=2)

        tezko = tk.Button(master, text="Tezko", height=1, width=10, command=self.stopnja_t)
        tezko.grid(row=4, column=3)
        self.tezko_lab = tk.Label(master, text="     ")
        self.tezko_lab.grid(row=4, column=2)

        self.tez = ""

        prazno = tk.Label(master, text=" ")
        prazno.grid(row=5, column=4)
        zacni = tk.Button(master, text="Začni igro", height=1, width=10, command=self.zacni)
        zacni.grid(row=6, column=3)
        gumb_dodaj = tk.Button(master, text="Dodaj besedo", command=Dodaj)
        gumb_dodaj.grid(row=6, column=4)


        master.mainloop()

    def stopnja_l(self):
        self.lahko_lab.config(text=" ✔ ")
        self.srednje_lab.config(text="   ")
        self.tezko_lab.config(text="   ")
        self.tez = "l"

    def stopnja_s(self):
        self.lahko_lab.config(text="   ")
        self.srednje_lab.config(text=" ✔ ")
        self.tezko_lab.config(text="   ")
        self.tez = "s"

    def stopnja_t(self):
        self.lahko_lab.config(text="   ")
        self.srednje_lab.config(text="  ")
        self.tezko_lab.config(text=" ✔ ")
        self.tez = "t"

    def zacni(self):
        global tezavnost
        if self.tez == "l":
            tezavnost = "l"
            Vislice()
        elif self.tez == "s":
            tezavnost = "s"
            Vislice()
        elif self.tez == "t":
            tezavnost = "t"
            Vislice()



class Dodaj:

    def __init__(self):
        wind = tk.Tk(className="Dodaj besedo")
        text = tk.Label(wind, text="Vpišite besedo, ki jo želite dodati:")
        text.grid()
        self.entry = tk.Entry(wind)
        self.entry.grid(row=1)
        but = tk.Button(wind, text="Dodaj", command=self.dodaj_v_slovar)
        but.grid(column=1, row=1)
        self.lab = tk.Label(wind, text="Stanje:")
        self.lab.grid(row=2, columnspan=2, sticky="w")


    def dodaj_v_slovar(self):
        v_dat2 = []
        with open("besede.txt", "a") as dat:
            with open("besede.txt", "r") as dat2:
                for i in dat2:
                    v_dat2.append(i.replace("\n", ""))
                x = self.entry.get()
                self.entry.delete(0, "end")
                if (x.upper() in v_dat2) or (x == ""):
                    self.lab.config(text="Stanje: Beseda je že na seznamu!")
                else:
                    self.lab.config(text="Stanje: Besedo ste dodali na seznam!")
                    v_dat2.append(x)
                    print(x.upper(), file=dat)


def izberi_besedo(seznam):
    '''Premmeša seznam in izbere element'''
    if seznam == []:
        Konec()
    izbrana_beseda = seznam[random.randrange(0, len(seznam))]
    seznam_besed.remove(izbrana_beseda)
    return list(izbrana_beseda)

def beseda_v_(beseda):
    '''Ustvari seznam _-jev dolžine izbrane besede'''
    x = []
    for _ in range(len(beseda)):
        x.append("_")
    return x


class Vislice:
    '''Igra vislic'''

    def izpolni(self, x):
        '''Izpolni 2 črki v besedi za lahko stopnjo in eno črko za srednjo stopnjo'''
        sam_so = ["A", "E", "I", "O", "U"]
        if x == "l":
            stevec = 0
            y = 2
            if "A" or "E" or "I" or "O" or "U" in self.izbrana_beseda:
                y = 1
                for i in self.izbrana_beseda:
                    if i in sam_so:
                        samoglasnik = i
                        break
                for j in range(len(self.izbrana_beseda)):
                    if self.izbrana_beseda[j] == samoglasnik:
                        self.izbrana_beseda_[j] = samoglasnik
            while stevec != y:
                stevec += 1
                for k in self.izbrana_beseda[::-1]:
                    if k not in sam_so:
                        sam_so.append(k)
                        soglasnik = k
                        break
                for l in range(len(self.izbrana_beseda)):
                    if self.izbrana_beseda[l] == soglasnik:
                        self.izbrana_beseda_[l] = soglasnik
                soglasnik = ""
        elif x == "s":
            for i in self.izbrana_beseda:
                if i in sam_so:
                    continue
                else:
                    for j in range(len(self.izbrana_beseda)):
                        if self.izbrana_beseda[j] == i:
                            self.izbrana_beseda_[j] = i
                break
        elif x == "t":
            pass


    def preveri_crko(self, x, gumb):
        '''Preveri ali je ugibana črka v besedi'''
        if x in self.izbrana_beseda:
            if self.stevec > 8 or self.izbrana_beseda == self.izbrana_beseda_:
                return
            for i in range(len(self.izbrana_beseda)):
                if self.izbrana_beseda[i] == x:
                    self.izbrana_beseda_[i] = x
                    self.beseda.config(text=" ".join(self.izbrana_beseda_))
            gumb.config(bg="green")
            if self.izbrana_beseda == self.izbrana_beseda_:
                self.napis.config(text="Čestitke, preživeli ste!")
        else:
            if gumb in self.g_mbi or self.izbrana_beseda == self.izbrana_beseda_:
                return
            if self.stevec < 9:
                self.g_mbi.append(gumb)
                gumb.config(bg="red")
                self.stevec += 1
                self.zivljenja.config(text="Število napačnih poskusov: " + str(self.stevec) + "/9")
            if self.stevec == 9:
                self.beseda.config(text=" ".join(self.izbrana_beseda))
                self.napis.config(text="Ni vam uspelo, bili ste obešeni!")

    def __init__(self):

        self.main = tk.Tk()

        self.izbrana_beseda = izberi_besedo(seznam_besed)
        self.izbrana_beseda_ = beseda_v_(self.izbrana_beseda)
        self.izpolni(tezavnost)
        self.stevec = 0

        self.g_mbi = []

        self.napis = tk.Label(self.main, text=" ", font=("Courier", 10))
        self.napis.grid(row=1, columnspan=3)

        self.zivljenja = tk.Label(self.main, text="Število napačnih poskusov: 0/9", font=("Courier", 10))
        self.zivljenja.grid(row=1, column=3)

        self.beseda = tk.Label(self.main, text=" ".join(self.izbrana_beseda_), font=("Courier", 20), borderwidth=75)
        self.beseda.grid(row=0, columnspan=3)

        '''Postavitev gumbov v 5x5 kvadrat'''
        frame_gumbi = tk.Frame(self.main)
        frame_gumbi.grid(row=0, column=3)

        self.gumba = tk.Button(
            frame_gumbi, text="A", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("A", self.gumba))
        self.gumba.grid()
        self.gumbb = tk.Button(
            frame_gumbi, text="B", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("B", self.gumbb))
        self.gumbb.grid(row=0, column=1)
        self.gumbc = tk.Button(
            frame_gumbi, text="C", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("C", self.gumbc))
        self.gumbc.grid(row=0, column=2)
        self.gumbcc = tk.Button(
            frame_gumbi, text="Č", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("Č", self.gumbcc))
        self.gumbcc.grid(row=0, column=3)
        self.gumbd = tk.Button(
            frame_gumbi, text="D", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("D", self.gumbd))
        self.gumbd.grid(row=0, column=4)
        self.gumbe = tk.Button(
            frame_gumbi, text="E", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("E", self.gumbe))
        self.gumbe.grid(row=1)
        self.gumbf = tk.Button(
            frame_gumbi, text="F", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("F", self.gumbf))
        self.gumbf.grid(row=1, column=1)
        self.gumbg = tk.Button(
            frame_gumbi, text="G", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("G", self.gumbg))
        self.gumbg.grid(row=1, column=2)
        self.gumbh = tk.Button(
            frame_gumbi, text="H", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("H", self.gumbh))
        self.gumbh.grid(row=1, column=3)
        self.gumbi = tk.Button(
            frame_gumbi, text="I", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("I", self.gumbi))
        self.gumbi.grid(row=1, column=4)
        self.gumbj = tk.Button(
            frame_gumbi, text="J", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("J", self.gumbj))
        self.gumbj.grid(row=2)
        self.gumbk = tk.Button(
            frame_gumbi, text="K", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("K", self.gumbk))
        self.gumbk.grid(row=2, column=1)
        self.gumbl = tk.Button(
            frame_gumbi, text="L", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("L", self.gumbl))
        self.gumbl.grid(row=2, column=2)
        self.gumbm = tk.Button(
            frame_gumbi, text="M", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("M", self.gumbm))
        self.gumbm.grid(row=2, column=3)
        self.gumbn = tk.Button(
            frame_gumbi, text="N", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("N", self.gumbn))
        self.gumbn.grid(row=2, column=4)
        self.gumbo = tk.Button(
            frame_gumbi, text="O", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("O", self.gumbo))
        self.gumbo.grid(row=3)
        self.gumbp = tk.Button(
            frame_gumbi, text="P", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("P", self.gumbp))
        self.gumbp.grid(row=3, column=1)
        self.gumbr = tk.Button(
            frame_gumbi, text="R", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("R", self.gumbr))
        self.gumbr.grid(row=3, column=2)
        self.gumbs = tk.Button(
            frame_gumbi, text="S", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("S", self.gumbs))
        self.gumbs.grid(row=3, column=3)
        self.gumbss = tk.Button(
            frame_gumbi, text="Š", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("Š", self.gumbss))
        self.gumbss.grid(row=3, column=4)
        self.gumbt = tk.Button(
            frame_gumbi, text="T", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("T", self.gumbt))
        self.gumbt.grid(row=4)
        self.gumbu = tk.Button(
            frame_gumbi, text="U", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("U", self.gumbu))
        self.gumbu.grid(row=4, column=1)
        self.gumbv = tk.Button(
            frame_gumbi, text="V", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("V", self.gumbv))
        self.gumbv.grid(row=4, column=2)
        self.gumbz = tk.Button(
            frame_gumbi, text="Z", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("Z", self.gumbz))
        self.gumbz.grid(row=4, column=3)
        self.gumbzz = tk.Button(
            frame_gumbi, text="Ž", width=3, font=("Courier", 15), command=lambda: self.preveri_crko("Ž", self.gumbzz))
        self.gumbzz.grid(row=4, column=4)


class Konec():

    def __init__(self):
        root = tk.Tk()

        konec_igre = tk.Label(root, text="Konec igre, uganili ste vse besede!", font=("Courier", 50))
        konec_igre.grid()



wind = Wind()


