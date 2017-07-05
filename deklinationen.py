# -*- coding: utf-8 -*-

# Modul für die Deklinationen

import random
from kivy.properties import ObjectProperty


##################################################################################################################

class Deklinationen(object):
    """
    Wählt zufällig eine Deklination aus und erstellt, korrigiert oder vervollständigt sie.
    """

    ##################################################################################################################

    def __init__(self):
        self.get_dek(random.randint(1,3))

    def get_dek(self, dek):
        # wählt eine zufällige Deklination aus und füllt manche textinputs
        if dek == 1:
            self.v = self.Deklination_a
            self.klasse = "a - Deklination, femininum"
            self.check = 1
        elif dek == 2:
            self.v = self.Deklination_o_m
            self.klasse = "o - Deklination, maskulinum"
            self.check = 2
        elif dek == 3:
            self.v = self.Deklination_o_n
            self.klasse = "o - Deklination, neutrum"
            self.check = 3
        elif dek == 4:
            self.v = self.Deklination_kons_m
            self.klasse = "kons. Deklination, maskulinum"
            self.check = 4
        elif dek == 5:
            self.v = self.Deklination_kons_n
            self.klasse = "kons. Deklination, neutrum"
            self.check = 5
        elif dek == 6:
            self.v = self.Deklination_u_m
            self.klasse = "u - Deklination, maskulinum"
            self.check = 6
        elif dek == 7:
            self.v = self.Deklination_u_n
            self.klasse = "u - Deklination, neutrum"
            self.check = 7
        elif dek == 8:
            self.v = self.Deklination_e
            self.klasse = "e - Deklination, femininum"
            self.check = 8
        elif dek == 9:
            self.v = self.Deklination_i_n
            self.klasse = "i - Deklination, neutrum"
            self.check = 9
        elif dek == 10:
            self.v = self.Deklination_i_f
            self.klasse = "i - Deklination, femininum"
            self.check = 10
        else:
            self.v = self.Deklination_a
            self.klasse = "a - Deklination, femininum"
            self.check = 1

        self.NS = self.v[0]
        self.NP = self.v[1]
        self.GS = self.v[2]
        self.GP = self.v[3]
        self.DS = self.v[4]
        self.DP = self.v[5]
        self.AKS = self.v[6]
        self.AKP = self.v[7]
        self.ABS = self.v[8]
        self.ABP = self.v[9]

        a = random.randint(0, 1)
        b = random.randint(0, 1)
        c = random.randint(0, 1)
        d = random.randint(0, 1)
        e = random.randint(0, 1)
        f = random.randint(0, 1)
        g = random.randint(0, 1)
        h = random.randint(0, 1)
        i = random.randint(0, 1)
        j = random.randint(0, 1)

        if a == 1:
            if self.check == 4:
                self.NS = "xx"
            else:
                self.NS = ""
        if b == 1:
            self.NP = ""
        if c == 1:
            self.GS = ""
        if d == 1:
            self.GP = ""
        if e == 1:
            self.DS = ""
        if f == 1:
            self.DP = ""
        if g == 1:
            if self.check == 5:
                self.AKS = "xx"
            else:
                self.AKS = ""
        if h == 1:
            self.AKP = ""
        if i == 1:
            self.ABS = ""
        if j == 1:
            self.ABP = ""

    def next_dek(self):
        # wählt eine zufällige deklination aus, die als nächstes kommen soll
        self.colorNS = [1, 1, 1, 1]
        self.colorNP = [1, 1, 1, 1]
        self.colorGS = [1, 1, 1, 1]
        self.colorGP = [1, 1, 1, 1]
        self.colorDS = [1, 1, 1, 1]
        self.colorDP = [1, 1, 1, 1]
        self.colorAKS = [1, 1, 1, 1]
        self.colorAKP = [1, 1, 1, 1]
        self.colorABS = [1, 1, 1, 1]
        self.colorABP = [1, 1, 1, 1]
        self.random = True
        self.get_dek(random.randint(1, 10))

    def loesung(self, dek):
        if dek == "a - Deklination, f":
            self.v = self.Deklination_a
        elif dek == "o - Deklination, m":
            self.v = self.Deklination_o_m
        elif dek == "o - Deklination, n":
            self.v = self.Deklination_o_n
        elif dek == "kons. Deklination, m":
            self.v = self.Deklination_kons_m
        elif dek == "kons. Deklination, n":
            self.v = self.Deklination_kons_n
        elif dek == "u - Deklination, m":
            self.v = self.Deklination_u_m
        elif dek == "u - Deklination, n":
            self.v = self.Deklination_u_n
        elif dek == "e - Deklination, f":
            self.v = self.Deklination_e
        elif dek == "i - Deklination, n":
            self.v = self.Deklination_i_n
        elif dek == "i - Deklination, f":
            self.v = self.Deklination_i_f

        self.NS = self.v[0]
        self.NP = self.v[1]
        self.GS = self.v[2]
        self.GP = self.v[3]
        self.DS = self.v[4]
        self.DP = self.v[5]
        self.AKS = self.v[6]
        self.AKP = self.v[7]
        self.ABS = self.v[8]
        self.ABP = self.v[9]

    def check_dek(self, NS, NP, GS, GP, DS, DP, AKS, AKP, ABS, ABP):
        # bekommt die texte der textinputs und vergleicht sie mit den Lösungen
        false_color = [.8, 0, 0, 1]
        right_color = [0, .8, 0, 1]
        if self.check == 1:
            checklist = self.Deklination_a
        elif self.check == 2:
            checklist = self.Deklination_o_m
        elif self.check == 3:
            checklist = self.Deklination_o_n
        elif self.check == 4:
            checklist = self.Deklination_kons_m
        elif self.check == 5:
            checklist = self.Deklination_kons_n
        elif self.check == 6:
            checklist = self.Deklination_u_m
        elif self.check == 7:
            checklist = self.Deklination_u_n
        elif self.check == 8:
            checklist = self.Deklination_e
        elif self.check == 9:
            checklist = self.Deklination_i_n
        elif self.check == 10:
            checklist = self.Deklination_i_f

        else:
            checklist = self.Deklination_a

        # kontrolliert die einzelnen antworten
        if str(NS) == str(checklist[0]):
            self.colorNS = right_color
            self.richtig_dek()
        else:
            self.colorNS = false_color
            self.falsch_dek()
        if str(NP) == str(checklist[1]):
            self.colorNP = right_color
            self.richtig_dek()
        else:
            self.colorNP = false_color
            self.falsch_dek()
        if str(GS) == str(checklist[2]):
            self.colorGS = right_color
            self.richtig_dek()
        else:
            self.colorGS = false_color
            self.falsch_dek()
        if str(GP) == str(checklist[3]):
            self.colorGP = right_color
            self.richtig_dek()
        else:
            self.colorGP = false_color
            self.falsch_dek()
        if str(DS) == str(checklist[4]):
            self.colorDS = right_color
            self.richtig_dek()
        else:
            self.colorDS = false_color
            self.falsch_dek()
        if str(DP) == str(checklist[5]):
            self.colorDP = right_color
            self.richtig_dek()
        else:
            self.colorDP = false_color
            self.falsch_dek()
        if str(AKS) == str(checklist[6]):
            self.colorAKS = right_color
            self.richtig_dek()
        else:
            self.colorAKS = false_color
            self.falsch_dek()
        if str(AKP) == str(checklist[7]):
            self.colorAKP = right_color
            self.richtig_dek()
        else:
            self.colorAKP = false_color
            self.falsch_dek()
        if str(ABS) == str(checklist[8]):
            self.colorABS = right_color
            self.richtig_dek()
        else:
            self.colorABS = false_color
            self.falsch_dek()
        if str(ABP) == str(checklist[9]):
            self.colorABP = right_color
            self.richtig_dek()
        else:
            self.colorABP = false_color
            self.falsch_dek()

    def richtig_dek(self):
        with open("data/statistiken.txt") as f:
            lines = f.readlines()
        current = lines[2]
        new = int(current) + 1
        lines[2] = (str(new) + "\n")
        with open("data/statistiken.txt", "w") as f:
            f.writelines(lines)

    def falsch_dek(self):
        with open("data/statistiken.txt") as f:
            lines = f.readlines()
        current = lines[3]
        new = int(current) + 1
        lines[3] = (str(new) + "\n")
        with open("data/statistiken.txt", "w") as f:
            f.writelines(lines)

    colorNS = ObjectProperty(None)
    colorNP = ObjectProperty(None)
    colorGS = ObjectProperty(None)
    colorGP = ObjectProperty(None)
    colorDS = ObjectProperty(None)
    colorDP = ObjectProperty(None)
    colorAKS = ObjectProperty(None)
    colorAKP = ObjectProperty(None)
    colorABS = ObjectProperty(None)
    colorABP = ObjectProperty(None)
    klasse = ObjectProperty(None)
    NS = ObjectProperty(None)
    NP = ObjectProperty(None)
    GS = ObjectProperty(None)
    GP = ObjectProperty(None)
    DS = ObjectProperty(None)
    DP = ObjectProperty(None)
    AKS = ObjectProperty(None)
    AKP = ObjectProperty(None)
    ABS = ObjectProperty(None)
    ABP = ObjectProperty(None)

    ##################################################################################################################

    Deklination_a = ["a", "ae", "ae", "arum", "ae", "is", "am", "as", "a", "is"]
    Deklination_o_m = ["us", "i", "i", "orum", "o", "is", "um", "os", "o", "is"]
    Deklination_o_n = ["um", "a", "i", "orum", "o", "is", "um", "a", "o", "is"]
    Deklination_kons_m = ["xx", "es", "is", "um", "i", "ibus", "em", "es", "e", "ibus"]
    Deklination_kons_n = ["xx", "a", "is", "um", "i", "ibus", "xx", "a", "e", "ibus"]
    Deklination_u_m = ["us", "us", "us", "uum", "ui", "ibus", "um", "us", "u", "ibus"]
    Deklination_u_n = ["u", "ua", "us", "uum", "u", "ibus", "u", "ua", "u", "ibus"]
    Deklination_e = ["es", "es", "ei", "erum", "ei", "ebus", "em", "es", "e", "ebus"]
    Deklination_i_n = ["e", "a", "is", "um", "i", "ibus", "e", "ia", "i", "ibus"]
    Deklination_i_f = ["is", "es", "is", "ium", "i", "ibus", "im", "es", "i", "ibus"]
