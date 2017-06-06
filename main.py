import tkinter as tk

import random


class Dodaj():

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
                print(v_dat2)
                x = self.entry.get()
                self.entry.delete(0, "end")
                if (x.upper() in v_dat2) or (x == ""):
                    self.lab.config(text="Stanje: Beseda je že na seznamu!")
                else:
                    self.lab.config(text="Stanje: Besedo ste dodali na seznam!")
                    v_dat2.append(x)
                    print(x.upper(), file=dat)


def preberi_besede():
    '''Iz datoteke prebere besede in jih doda v seznam'''
    with open("besede.txt", "r") as dat:
        y = []
        for x in dat:
            beseda = x.replace("\n", "")
            y.append(beseda)
        return y

def izberi_besedo(seznam):
    '''Premmeša seznam in izbere element'''
    izbrana_beseda = seznam[random.randrange(0, len(seznam))]
    return izbrana_beseda


class Vislice:

    def __init__(self):
        okno = tk.Tk(className="Vislice")

        self.besede = preberi_besede()

        self.izbrana_beseda = izberi_besedo(self.besede)

        prikaz_besede = tk.Frame(okno)
        prikaz_besede.pack(side="top")
        prva_vrsta = tk.Frame(okno)
        prva_vrsta.pack(side="top")
        druga_vrsta = tk.Frame(okno)
        druga_vrsta.pack(side="top")
        tretja_vrsta = tk.Frame(okno)
        tretja_vrsta.pack(side="top")
        cetrta_vrsta = tk.Frame(okno)
        cetrta_vrsta.pack(side="top")
        stranski_gumbi = tk.Frame(okno)
        stranski_gumbi.pack(side="left")

        beseda = tk.Label(prikaz_besede, bd=50, width=100, text=str(self.izbrana_beseda))
        beseda.pack()

        gumb_dodaj = tk.Button(stranski_gumbi, text="Dodaj besedo", command=Dodaj)
        gumb_dodaj.pack()

        '''Postavitev gumbov s črkami v štiri vrste.'''
        gumba = tk.Button(prva_vrsta, text="A", height=2, width=2)
        gumba.pack(side="left")
        gumbb = tk.Button(prva_vrsta, text="B", height=2, width=2)
        gumbb.pack(side="left")
        gumbc = tk.Button(prva_vrsta, text="C", height=2, width=2)
        gumbc.pack(side="left")
        gumbch = tk.Button(prva_vrsta, text="Č", height=2, width=2)
        gumbch.pack(side="left")
        gumbd = tk.Button(prva_vrsta, text="D", height=2, width=2)
        gumbd.pack(side="left")
        gumbe = tk.Button(prva_vrsta, text="E", height=2, width=2)
        gumbe.pack(side="left")
        gumbf = tk.Button(prva_vrsta, text="F", height=2, width=2)
        gumbf.pack(side="left")
        gumbg = tk.Button(druga_vrsta, text="G", height=2, width=2)
        gumbg.pack(side="left")
        gumbh = tk.Button(druga_vrsta, text="H", height=2, width=2)
        gumbh.pack(side="left")
        gumbi = tk.Button(druga_vrsta, text="I", height=2, width=2)
        gumbi.pack(side="left")
        gumbj = tk.Button(druga_vrsta, text="J", height=2, width=2)
        gumbj.pack(side="left")
        gumbk = tk.Button(druga_vrsta, text="K", height=2, width=2)
        gumbk.pack(side="left")
        gumbl = tk.Button(druga_vrsta, text="L", height=2, width=2)
        gumbl.pack(side="left")
        gumbm = tk.Button(tretja_vrsta, text="M", height=2, width=2)
        gumbm.pack(side="left")
        gumbn = tk.Button(tretja_vrsta, text="N", height=2, width=2)
        gumbn.pack(side="left")
        gumbo = tk.Button(tretja_vrsta, text="O", height=2, width=2)
        gumbo.pack(side="left")
        gumbp = tk.Button(tretja_vrsta, text="P", height=2, width=2)
        gumbp.pack(side="left")
        gumbr = tk.Button(tretja_vrsta, text="R", height=2, width=2)
        gumbr.pack(side="left")
        gumbs = tk.Button(tretja_vrsta, text="S", height=2, width=2)
        gumbs.pack(side="left")
        gumbsh = tk.Button(cetrta_vrsta, text="Š", height=2, width=2)
        gumbsh.pack(side="left")
        gumbt = tk.Button(cetrta_vrsta, text="T", height=2, width=2)
        gumbt.pack(side="left")
        gumbu = tk.Button(cetrta_vrsta, text="U", height=2, width=2)
        gumbu.pack(side="left")
        gumbv = tk.Button(cetrta_vrsta, text="V", height=2, width=2)
        gumbv.pack(side="left")
        gumbz = tk.Button(cetrta_vrsta, text="Z", height=2, width=2)
        gumbz.pack(side="left")
        gumbzh = tk.Button(cetrta_vrsta, text="Ž", height=2, width=2)
        gumbzh.pack(side="left")

        okno.mainloop()



a = Vislice()



