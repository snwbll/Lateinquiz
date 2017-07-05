# -*- coding: utf-8 -*-

# Modul für die Konjugationen

import random
from kivy.properties import ObjectProperty

######################################################################################################################


class Konjugationen(object):
    """
    Wählt zufällig eine Konjugation aus und erstellt, korrigiert oder vervollständigt sie.
    """
    ##################################################################################################################

    def __init__(self):
        self.get_PPA(self.PS[random.randint(0, len(self.PS) - 1)])
        self.get_kon("Indikativ Präsens", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
            self.AP[random.randint(0, len(self.AP) - 1)])

    def change_kon(self, next_kon):
        self.erstepssg = ""
        self.zweitepssg = ""
        self.drittepssg = ""
        self.erstepspl = ""
        self.zweitepspl = ""
        self.drittepspl = ""

        if next_kon == "Indikativ Präsens":
            self.get_kon("Indikativ Präsens", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif next_kon == "Konjunktiv Präsens":
            self.get_kon("Konjunktiv Präsens", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif next_kon == "Indikativ Imperfekt":
            self.get_kon("Indikativ Imperfekt", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif next_kon == "Konjunktiv Imperfekt":
            self.get_kon("Konjunktiv Imperfekt", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif next_kon == "Indikativ Futur I":
            self.get_kon("Indikativ Futur I", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])

    def get_PPA(self, person):
        self.colorN = [1, 1, 1, 1]
        self.colorG = [1, 1, 1, 1]
        self.colorD = [1, 1, 1, 1]
        self.colorA = [1, 1, 1, 1]
        self.colorAB = [1, 1, 1, 1]
        self.klasse = "PPA, m/f"
        self.wort = self.Beispiele[random.randint(0, len(self.Beispiele) - 1)]
        if person == "Singular":
            self.person = "Singular"
            self.NOM = "ns"
            i = random.randint(1, 2)
            if i == 1:
                self.GEN = self.PPAListSg[1]
            else:
                self.GEN = ""
            i = random.randint(1, 2)
            if i == 1:
                self.DAT = self.PPAListSg[2]
            else:
                self.DAT = ""
            i = random.randint(1, 2)
            if i == 1 and self.DAT != self.PPAListSg[2]:
                self.AKK = self.PPAListSg[3]
            else:
                self.AKK = ""
            i = random.randint(1, 2)
            if i == 1 and self.DAT != self.PPAListSg[2]:
                self.ABL = self.PPAListSg[4]
            else:
                self.ABL = ""
        elif person == "Plural":
            self.person = "Plural"
            i = random.randint(1, 2)
            if i == 1:
                self.NOM = self.PPAListPl[0]
            else:
                self.NOM = ""
            i = random.randint(1, 2)
            if i == 1:
                self.GEN = self.PPAListPl[1]
            else:
                self.GEN = ""
            i = random.randint(1, 2)
            if i == 1 and self.GEN != self.PPAListPl[1]:
                self.DAT = self.PPAListPl[2]
            else:
                self.DAT = ""
            i = random.randint(1, 2)
            if i == 1:
                self.AKK = self.PPAListPl[3]
            else:
                self.AKK = ""
            i = random.randint(1, 2)
            if i == 1 and self.NOM != self.PPAListPl[0]:
                self.ABL = self.PPAListPl[4]
            else:
                self.ABL = ""

    def next_kon(self, kon):
        if kon == "PPA, m/f":
            self.get_PPA(self.PS[random.randint(0, len(self.PS) - 1)])
        elif kon == "Indikativ Präsens":
            self.get_kon("Indikativ Präsens", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif kon == "Konjunktiv Präsens":
            self.get_kon("Konjunktiv Präsens", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif kon == "Indikativ Imperfekt":
            self.get_kon("Indikativ Imperfekt", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif kon == "Konjunktiv Imperfekt":
            self.get_kon("Konjunktiv Imperfekt", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])
        elif kon == "Indikativ Futur I":
            self.get_kon("Indikativ Futur I", self.Konjun[random.randint(0, len(self.Konjun) - 1)],
                         self.AP[random.randint(0, len(self.AP) - 1)])

    def loesung(self, klasse, kon, akpa):
        if klasse == "PPA, m/f":
            if self.NOM == "ns":
                v = self.PPAListSg
            else:
                v = self.PPAListPl
            self.NOM = v[0]
            self.GEN = v[1]
            self.DAT = v[2]
            self.AKK = v[3]
            self.ABL = v[4]
        else:
            if klasse == "Indikativ Präsens":
                if kon == "a" or kon == "e":
                    if akpa == "aktiv":
                        v = self.IPaeA
                    else:
                        v = self.IPaeP
                elif kon == "i":
                    if akpa == "aktiv":
                        v = self.IPiA
                    else:
                        v = self.IPiP
                elif kon == "kons":
                    if akpa == "aktiv":
                        v = self.IPkonsA
                    else:
                        v = self.IPkonsP

            elif klasse == "Konjunktiv Präsens":
                if akpa == "aktiv":
                    v = self.KPaeikonsA
                else:
                    v = self.KPaeikonsP

            elif klasse == "Indikativ Imperfekt":
                if akpa == "aktiv":
                    v = self.IIaeikonsA
                else:
                    v = self.IIaeikonsP

            elif klasse == "Konjunktiv Imperfekt":
                if akpa == "aktiv":
                    v = self.KIaeikonsA
                else:
                    v = self.KIaeikonsP

            elif klasse == "Indikativ Futur I":
                if kon == "a" or kon == "e":
                    if akpa == "aktiv":
                        v = self.IFaeA
                    else:
                        v = self.IFaeP
                elif kon == "i" or kon == "kons":
                    if akpa == "aktiv":
                        v = self.IFikonsA
                    else:
                        v = self.IFikonsP

            self.erstepssg = v[0]
            self.zweitepssg = v[1]
            self.drittepssg = v[2]
            self.erstepspl = v[3]
            self.zweitepspl = v[4]
            self.drittepspl = v[5]

    def get_kon(self, klasse, konjugation, akpa):
        self.erstepssg = ""
        self.zweitepssg = ""
        self.drittepssg = ""
        self.erstepspl = ""
        self.zweitepspl = ""
        self.drittepspl = ""
        self.colorESG = [1, 1, 1, 1]
        self.colorZSG = [1, 1, 1, 1]
        self.colorDSG = [1, 1, 1, 1]
        self.colorEPL = [1, 1, 1, 1]
        self.colorZPL = [1, 1, 1, 1]
        self.colorDPL = [1, 1, 1, 1]
        # auswählen der konjugation
        if klasse == "Indikativ Präsens":
            self.naechste_kon = "Konjunktiv Präsens"
            if konjugation == "a" or konjugation == "e":
                if akpa == "aktiv":
                    k = self.IPaeA
                else:
                    k = self.IPaeP
            elif konjugation == "i":
                if akpa == "aktiv":
                    k = self.IPiA
                else:
                    k = self.IPiP
            elif konjugation == "kons":
                if akpa == "aktiv":
                    k = self.IPkonsA
                else:
                    k = self.IPkonsP

        elif klasse == "Konjunktiv Präsens":
            self.naechste_kon = "Indikativ Imperfekt"
            if akpa == "aktiv":
                k = self.KPaeikonsA
            else:
                k = self.KPaeikonsP


        elif klasse == "Indikativ Imperfekt":
            self.naechste_kon = "Konjunktiv Imperfekt"
            if akpa == "aktiv":
                k = self.IIaeikonsA
            else:
                k = self.IIaeikonsP

        elif klasse == "Konjunktiv Imperfekt":
            self.naechste_kon = "Indikativ Futur I"
            if akpa == "aktiv":
                k = self.KIaeikonsA
            else:
                k = self.KIaeikonsP

        elif klasse == "Indikativ Futur I":
            self.naechste_kon = "Indikativ Präsens"
            if konjugation == "a" or konjugation == "e":
                if akpa == "aktiv":
                    k = self.IFaeA
                else:
                    k = self.IFaeP
            elif konjugation == "i" or konjugation == "kons":
                if akpa == "aktiv":
                    k = self.IFikonsA
                else:
                    k = self.IFikonsP

        # Beispielwörter
        if klasse == "Indikativ Präsens":
            if konjugation == "a":
                self.beispieleins = self.IPBeispiele[0]
                self.beispiel = self.IPBeispiele[1]
            elif konjugation == "e":
                self.beispieleins = self.IPBeispiele[2]
                self.beispiel = self.beispieleins
            elif konjugation == "i":
                self.beispieleins = self.IPBeispiele[3]
                self.beispiel = self.beispieleins
            else:
                self.beispieleins = self.IPBeispiele[4]
                self.beispiel = self.beispieleins

        elif klasse == "Konjunktiv Präsens":
            if konjugation == "a":
                self.beispieleins = self.KPBeispiele[0]
                self.beispiel = self.beispieleins
            elif konjugation == "e":
                self.beispieleins = self.KPBeispiele[1]
                self.beispiel = self.beispieleins
            elif konjugation == "i":
                self.beispieleins = self.KPBeispiele[2]
                self.beispiel = self.beispieleins
            else:
                self.beispieleins = self.KPBeispiele[3]
                self.beispiel = self.beispieleins

        elif klasse == "Indikativ Imperfekt":
            if konjugation == "a":
                self.beispieleins = self.IIBeispiele[0]
                self.beispiel = self.beispieleins
            elif konjugation == "e":
                self.beispieleins = self.IIBeispiele[1]
                self.beispiel = self.beispieleins
            elif konjugation == "i":
                self.beispieleins = self.IIBeispiele[2]
                self.beispiel = self.beispieleins
            else:
                self.beispieleins = self.IIBeispiele[3]
                self.beispiel = self.beispieleins

        elif klasse == "Konjunktiv Imperfekt":
            if konjugation == "a":
                self.beispieleins = self.KIBeispiele[0]
                self.beispiel = self.beispieleins
            elif konjugation == "e":
                self.beispieleins = self.KIBeispiele[1]
                self.beispiel = self.beispieleins
            elif konjugation == "i":
                self.beispieleins = self.KIBeispiele[2]
                self.beispiel = self.beispieleins
            else:
                self.beispieleins = self.KIBeispiele[3]
                self.beispiel = self.beispieleins

        elif klasse == "Indikativ Futur I":
            if konjugation == "a":
                self.beispieleins = self.IFBeispiele[0]
                self.beispiel = self.beispieleins
            elif konjugation == "e":
                self.beispieleins = self.IFBeispiele[1]
                self.beispiel = self.beispieleins
            elif konjugation == "i":
                self.beispieleins = self.IFBeispiele[2]
                self.beispiel = self.beispieleins
            else:
                self.beispieleins = self.IFBeispiele[3]
                self.beispiel = self.beispieleins

        i = random.randint(1, 2)
        if i == 1:
            self.erstepssg = k[0]
        else:
            self.erstepssg = ""
        i = random.randint(1, 2)
        if i == 1:
            self.zweitepssg = k[1]
        else:
            self.zweitepssg = ""
        i = random.randint(1, 2)
        if i == 1:
            self.drittepssg = k[2]
        else:
            self.drittepssg = ""
        i = random.randint(1, 2)
        if i == 1:
            self.erstepspl = k[3]
        else:
            self.erstepspl = ""
        i = random.randint(1, 2)
        if i == 1 and self.erstepspl != k[3]:
            self.zweitepspl = k[4]
        else:
            self.zweitepspl = ""
        i = random.randint(1, 2)
        if i == 1:
            self.drittepspl = k[5]
        else:
            self.drittepspl = ""

        self.konjugation = konjugation
        self.klasse = klasse
        self.aktivpassiv = akpa

    def richtig_kon(self):
        with open("data/statistiken.txt") as f:
            lines = f.readlines()
        current = lines[2]
        new = int(current) + 1
        lines[2] = (str(new) + "\n")
        with open("data/statistiken.txt", "w") as f:
            f.writelines(lines)

    def falsch_kon(self):
        with open("data/statistiken.txt") as f:
            lines = f.readlines()
        current = lines[3]
        new = int(current) + 1
        lines[3] = (str(new) + "\n")
        with open("data/statistiken.txt", "w") as f:
            f.writelines(lines)


    ##################################################################################################################


    beispieleins = ObjectProperty(None)
    beispiel = ObjectProperty(None)
    wort = ObjectProperty(None)
    person = ObjectProperty(None)
    klasse = ObjectProperty(None)
    konjugation = ObjectProperty(None)
    aktivpassiv = ObjectProperty(None)
    NOM = ObjectProperty(None)
    GEN = ObjectProperty(None)
    DAT = ObjectProperty(None)
    AKK = ObjectProperty(None)
    ABL = ObjectProperty(None)
    colorN = ObjectProperty(None)
    colorG = ObjectProperty(None)
    colorD = ObjectProperty(None)
    colorA = ObjectProperty(None)
    colorAB = ObjectProperty(None)
    colorESG = ObjectProperty(None)
    colorZSG = ObjectProperty(None)
    colorDSG = ObjectProperty(None)
    colorEPL = ObjectProperty(None)
    colorZPL = ObjectProperty(None)
    colorDPL = ObjectProperty(None)
    erstepssg = ObjectProperty(None)
    zweitepssg = ObjectProperty(None)
    drittepssg = ObjectProperty(None)
    erstepspl = ObjectProperty(None)
    zweitepspl = ObjectProperty(None)
    drittepspl = ObjectProperty(None)
    naechste_kon = ObjectProperty(None)

    ##################################################################################################################

    Konjun = ["a", "e", "i", "kons"]
    PS = ["Singular", "Plural"]
    AP = ["aktiv", "passiv"]
    Beispiele = ["lauda", "mone", "audie", "rege", "capie"]
    PPAListSg = ["ns", "ntis", "nti", "ntem", "nte"]
    PPAListPl = ["ntes", "ntium", "ntibus", "ntes", "ntibus"]
    IPaeA = ["o", "s", "t", "mus", "tis", "nt"]
    IPaeP = ["or", "ris", "tur", "mur", "mini", "ntur"]
    IPiA = ["o", "s", "t", "mus", "tis", "unt"]
    IPiP = ["or", "ris", "tur", "mur", "mini", "untur"]
    IPkonsA = ["o", "is", "it", "imus", "itis", "unt"]
    IPkonsP = ["or", "eris", "itur", "imur", "imini", "untur"]
    IPBeispiele = ["laud", "lauda", "mone", "audi", "reg"]
    KPaeikonsA = ["m", "s", "t", "mus", "tis", "nt"]
    KPaeikonsP = ["r", "ris", "tur", "mur", "mini", "ntur"]
    KPBeispiele = ["laude", "mone", "audi", "reg"]

    IIaeikonsA = ["bam", "bas", "bat", "bamus", "batis", "bant"]
    IIaeikonsP = ["bar", "baris", "batur", "bamur", "bamini", "bantur"]
    IIBeispiele = ["lauda", "mone", "audie", "rege"]

    KIaeikonsA = ["rem", "res", "ret", "remus", "retis", "rent"]
    KIaeikonsP = ["rer", "reris", "retur", "remur", "remini", "rentur"]
    KIBeispiele = ["lauda", "mone", "audi", "rege"]

    IFaeA = ["bo", "bis", "bit", "bimus", "bitis", "bunt"]
    IFaeP = ["bor", "beris", "bitur", "bimur", "bimini", "buntur"]
    IFikonsA = ["am", "es", "et", "emus", "etis", "ent"]
    IFikonsP = ["ar", "eris", "etur", "emur", "emini", "entur"]
    IFBeispiele = ["lauda", "mone", "audi", "reg"]