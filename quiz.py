# -*- coding: utf-8 -*-

# Modul für das Quiz

import random
from kivy.properties import ObjectProperty


##################################################################################################################


class Entry:
    """
    Definiert die Zugehörigkeit der Vokabeln (deutsch oder latein)
    """

    ##################################################################################################################

    def __init__(self, deutsch, latein):
        self.deutsch = deutsch
        self.latein = latein


##################################################################################################################


class Quiz(object):
    """"
    Generiert zufällige Lateinfragen.
    """
    c = 1
    # sorgt dafür, dass niemals 3 gleiche Vokabeln nacheinander kommen (siehe "get_quiz_question()")
    rep = [110, 120, 130, 140]

    ##################################################################################################################

    def __init__(self):
        """
        Beginnt mit der Auswahl der Vokabeln.
        """
        self.get_quiz_question(0)

    def statusc(self, s):
        if s == 1:
            self.lektionsstatusc = "Lektion 1"
        elif s == 2:
            self.lektionsstatusc = "Lektion 2"
        elif s == 3:
            self.lektionsstatusc = "Lektion 3"
        elif s == 4:
            self.lektionsstatusc = "Lektion 4"
        elif s == 5:
            self.lektionsstatusc = "Lektion 5"
        elif s == 51:
            # gemische Lektionen
            self.lektionsstatusc = "1 - 5"
        elif s == 6:
            self.lektionsstatusc = "Lektion 6"
        elif s == 7:
            self.lektionsstatusc = "Lektion 7"
        elif s == 8:
            self.lektionsstatusc = "Lektion 8"
        elif s == 9:
            self.lektionsstatusc = "Lektion 9"
        elif s == 10:
            self.lektionsstatusc = "Lektion 10"
        elif s == 61:
            self.lektionsstatusc = "6 - 10"
        elif s == 11:
            self.lektionsstatusc = "Lektion 11"
        elif s == 12:
            self.lektionsstatusc = "Lektion 12"
        elif s == 13:
            self.lektionsstatusc = "Lektion 13"
        elif s == 14:
            self.lektionsstatusc = "Lektion 14"
        elif s == 15:
            self.lektionsstatusc = "Lektion 15"
        elif s == 71:
            self.lektionsstatusc = "11 - 15"
        elif s == 16:
            self.lektionsstatusc = "Lektion 16"
        elif s == 17:
            self.lektionsstatusc = "Lektion 17"
        elif s == 18:
            self.lektionsstatusc = "Lektion 18"
        elif s == 19:
            self.lektionsstatusc = "Lektion 19"
        elif s == 20:
            self.lektionsstatusc = "Lektion 20"
        elif s == 81:
            self.lektionsstatusc = "16 - 20"

    def get_quiz_question(self, mode):
        """
        Wählt zufällige Vokabeln aus den vorgegeben Lektionen aus, von denen 1 richtig und 3 falsch sind.
        """
        if self.c == 1:
            self.Vokabeln = self.Lektion_1
        elif self.c == 2:
            self.Vokabeln = self.Lektion_2
        elif self.c == 3:
            self.Vokabeln = self.Lektion_3
        elif self.c == 4:
            self.Vokabeln = self.Lektion_4
        elif self.c == 5:
            self.Vokabeln = self.Lektion_5
        elif self.c == 51:
            self.Vokabeln = self.Lektionen1bis5
        elif self.c == 6:
            self.Vokabeln = self.Lektion_6
        elif self.c == 7:
            self.Vokabeln = self.Lektion_7
        elif self.c == 8:
            self.Vokabeln = self.Lektion_8
        elif self.c == 9:
            self.Vokabeln = self.Lektion_9
        elif self.c == 10:
            self.Vokabeln = self.Lektion_10
        elif self.c == 61:
            self.Vokabeln = self.Lektionen6bis10
        elif self.c == 11:
            self.Vokabeln = self.Lektion_11
        elif self.c == 12:
            self.Vokabeln = self.Lektion_12
        elif self.c == 13:
            self.Vokabeln = self.Lektion_13
        elif self.c == 14:
            self.Vokabeln = self.Lektion_14
        elif self.c == 15:
            self.Vokabeln = self.Lektion_15
        elif self.c == 71:
            self.Vokabeln = self.Lektionen11bis15
        elif self.c == 16:
            self.Vokabeln = self.Lektion_16
        elif self.c == 71:
            self.Vokabeln = self.Lektionen11bis15
        elif self.c == 17:
            self.Vokabeln = self.Lektion_17
        elif self.c == 18:
            self.Vokabeln = self.Lektion_18
        elif self.c == 19:
            self.Vokabeln = self.Lektion_19
        elif self.c == 20:
            self.Vokabeln = self.Lektion_20
        elif self.c == 81:
            self.Vokabeln = self.Lektionen16bis20

        if mode == 1:

            # gesuchte Vokabel (Frage)
            a_a = random.randint(0, len(self.Vokabeln) - 1)
            self.a = str(self.Vokabeln[a_a].deutsch)

            # richtige Vokabel
            self.b = str(self.Vokabeln[a_a].latein)

            # falsche Vokabeln
            j_a = random.randint(0, len(self.Vokabeln) - 1)
            self.j = str(self.Vokabeln[j_a].latein)

            k_a = random.randint(0, len(self.Vokabeln) - 1)
            self.k = str(self.Vokabeln[k_a].latein)

            l_a = random.randint(0, len(self.Vokabeln) - 1)
            self.l = str(self.Vokabeln[l_a].latein)

            # falls mehrere gleiche Vokabeln vorkommen wird neu ausgewählt
            if a_a == j_a or a_a == k_a or a_a == l_a or j_a == a_a or j_a == k_a or j_a == l_a or k_a == l_a or k_a == a_a or k_a == j_a or l_a == a_a or l_a == k_a or l_a == j_a:
                self.get_quiz_question(1)

            else:
                self.rep.append(a_a)
                if len(self.rep) > 4:
                    self.rep.remove(self.rep[0])

                if self.rep[0] == self.rep[1] or self.rep[0] == self.rep[2] or self.rep[0] == self.rep[3] or self.rep[
                    1] == self.rep[3] or self.rep[2] == self.rep[3] or self.rep[1] == self.rep[2] or self.rep[2] == \
                        self.rep[1] or self.rep[2] == self.rep[0]:
                    self.get_quiz_question(1)

                else:
                    # verteilung der Antworten
                    list = [self.b, self.j, self.k, self.l]

                    self.e = random.randint(0, len(list) - 1)
                    self.vokabel_one = list[self.e]
                    list.remove(list[self.e])

                    self.f = random.randint(0, len(list) - 1)
                    self.vokabel_two = list[self.f]
                    list.remove(list[self.f])

                    self.g = random.randint(0, len(list) - 1)
                    self.vokabel_three = list[self.g]
                    list.remove(list[self.g])

                    self.h = random.randint(0, len(list) - 1)
                    self.vokabel_four = list[self.h]
                    list.remove(list[self.h])

        elif mode == 0:
            # gesuchte Vokabel
            a_a = random.randint(0, len(self.Vokabeln) - 1)
            self.a = str(self.Vokabeln[a_a].latein)

            # richtige Vokabel
            self.b = str(self.Vokabeln[a_a].deutsch)

            # falsche Vokabeln
            j_a = random.randint(0, len(self.Vokabeln) - 1)
            self.j = str(self.Vokabeln[j_a].deutsch)

            k_a = random.randint(0, len(self.Vokabeln) - 1)
            self.k = str(self.Vokabeln[k_a].deutsch)

            l_a = random.randint(0, len(self.Vokabeln) - 1)
            self.l = str(self.Vokabeln[l_a].deutsch)

            if a_a == j_a or a_a == k_a or a_a == l_a or j_a == a_a or j_a == k_a or j_a == l_a or k_a == l_a or k_a == a_a or k_a == j_a or l_a == a_a or l_a == k_a or l_a == j_a:
                self.get_quiz_question(0)

            else:
                self.rep.append(a_a)
                if len(self.rep) > 4:
                    self.rep.remove(self.rep[0])

                if self.rep[0] == self.rep[1] or self.rep[0] == self.rep[2] or self.rep[0] == self.rep[3] or self.rep[
                    1] == self.rep[3] or self.rep[2] == self.rep[3] or self.rep[1] == self.rep[2] or self.rep[2] == \
                        self.rep[1] or self.rep[2] == self.rep[0]:
                    self.get_quiz_question(0)

                else:
                    # verteilung der Antworten
                    list = [self.b, self.j, self.k, self.l]

                    self.e = random.randint(0, len(list) - 1)
                    self.vokabel_one = list[self.e]
                    list.remove(list[self.e])

                    self.f = random.randint(0, len(list) - 1)
                    self.vokabel_two = list[self.f]
                    list.remove(list[self.f])

                    self.g = random.randint(0, len(list) - 1)
                    self.vokabel_three = list[self.g]
                    list.remove(list[self.g])

                    self.h = random.randint(0, len(list) - 1)
                    self.vokabel_four = list[self.h]
                    list.remove(list[self.h])

        else:
            print "Fehler bei der Vokabelauswahl in get_quiz_question, quiz.py"

    def get_next(self):
        m = random.randint(0, 1)
        self.get_quiz_question(m)

    def get_answer(self):
        """
        Korrekte Antwort wird ausgegeben.
        """
        return self.b

    def richtig(self):
        with open("data/statistiken.txt") as f:
            lines = f.readlines()
        current = lines[0]
        new = int(current) + 1
        lines[0] = (str(new) + "\n")
        with open("data/statistiken.txt", "w") as f:
            f.writelines(lines)
        self.result = "richtig"
        self.get_next()

    def falsch(self):
        with open("data/statistiken.txt") as f:
            lines = f.readlines()
        current = lines[1]
        new = int(current) + 1
        lines[1] = (str(new) + "\n")
        with open("data/statistiken.txt", "w") as f:
            f.writelines(lines)
        self.result = "falsch"

    def answercheck(self):
        if self.buttonclicked == 1 and self.e == 0:
            self.richtig()
        elif self.buttonclicked == 2 and self.f == 0 and self.e != 0:
            self.richtig()
        elif self.buttonclicked == 3 and self.g == 0 and self.f != 0 and self.e != 0:
            self.richtig()
        elif self.buttonclicked == 4 and self.h == 0 and self.g != 0 and self.f != 0 and self.e != 0:
            self.richtig()
        else:
            self.falsch()

    def Buttonclicked1(self):
        self.buttonclicked = 1

    def Buttonclicked2(self):
        self.buttonclicked = 2

    def Buttonclicked3(self):
        self.buttonclicked = 3

    def Buttonclicked4(self):
        self.buttonclicked = 4

    def ScrollLabels(self, v):
        """
        Weist den Labeln aus ScrollView die richtigen Wörter zu, je nach Länge der Lektionsliste.
        """
        mehrals19 = False
        mehrals35 = False
        mehrals36 = False
        mehrals37 = False
        mehrals38 = False
        mehrals40 = False
        mehrals41 = False
        mehrals42 = False
        mehrals43 = False
        mehrals50 = False

        if v == 1:
            self.l = self.Lektion_1
            self.lektionstatus = "Lektion 1"
        elif v == 2:
            self.l = self.Lektion_2
            mehrals36 = True
            self.lektionstatus = "Lektion 2"
        elif v == 3:
            self.l = self.Lektion_3
            mehrals37 = True
            self.lektionstatus = "Lektion 3"
        elif v == 4:
            self.l = self.Lektion_4
            mehrals40 = True
            self.lektionstatus = "Lektion 4"
        elif v == 5:
            self.l = self.Lektion_5
            mehrals19 = True
            self.lektionstatus = "Lektion 5"
        elif v == 6:
            self.l = self.Lektion_6
            mehrals42 = True
            self.lektionstatus = "Lektion 6"
        elif v == 7:
            self.l = self.Lektion_7
            mehrals19 = True
            self.lektionstatus = "Lektion 7"
        elif v == 8:
            self.l = self.Lektion_8
            mehrals41 = True
            self.lektionstatus = "Lektion 8"
        elif v == 9:
            self.l = self.Lektion_9
            mehrals37 = True
            self.lektionstatus = "Lektion 9"
        elif v == 10:
            self.l = self.Lektion_10
            mehrals42 = True
            self.lektionstatus = "Lektion 10"
        elif v == 11:
            self.l = self.Lektion_11
            mehrals38 = True
            self.lektionstatus = "Lektion 11"
        elif v == 12:
            self.l = self.Lektion_12
            mehrals38 = True
            self.lektionstatus = "Lektion 12"
        elif v == 13:
            self.l = self.Lektion_13
            mehrals35 = True
            self.lektionstatus = "Lektion 13"
        elif v == 14:
            self.l = self.Lektion_14
            mehrals36 = True
            self.lektionstatus = "Lektion 14"
        elif v == 15:
            self.l = self.Lektion_15
            mehrals38 = True
            self.lektionstatus = "Lektion 15"
        elif v == 16:
            self.l = self.Lektion_16
            mehrals36 = True
            self.lektionstatus = "Lektion 16"
        elif v == 17:
            self.l = self.Lektion_17
            mehrals36 = True
            self.lektionstatus = "Lektion 17"
        elif v == 18:
            self.l = self.Lektion_18
            mehrals36 = True
            self.lektionstatus = "Lektion 18"
        elif v == 19:
            self.l = self.Lektion_19
            mehrals38 = True
            self.lektionstatus = "Lektion 19"
        elif v == 20:
            self.l = self.Lektion_20
            mehrals19 = True
            self.lektionstatus = "Lektion 20"

        self.dv1 = self.l[0].deutsch
        self.lv1 = self.l[0].latein
        self.dv2 = self.l[1].deutsch
        self.lv2 = self.l[1].latein
        self.dv3 = self.l[2].deutsch
        self.lv3 = self.l[2].latein
        self.dv4 = self.l[3].deutsch
        self.lv4 = self.l[3].latein
        self.dv5 = self.l[4].deutsch
        self.lv5 = self.l[4].latein
        self.dv6 = self.l[5].deutsch
        self.lv6 = self.l[5].latein
        self.dv7 = self.l[6].deutsch
        self.lv7 = self.l[6].latein
        self.dv8 = self.l[7].deutsch
        self.lv8 = self.l[7].latein
        self.dv9 = self.l[8].deutsch
        self.lv9 = self.l[8].latein
        self.dv10 = self.l[9].deutsch
        self.lv10 = self.l[9].latein
        self.dv11 = self.l[10].deutsch
        self.lv11 = self.l[10].latein
        self.dv12 = self.l[11].deutsch
        self.lv12 = self.l[11].latein
        self.dv13 = self.l[12].deutsch
        self.lv13 = self.l[12].latein
        self.dv14 = self.l[13].deutsch
        self.lv14 = self.l[13].latein
        self.dv15 = self.l[14].deutsch
        self.lv15 = self.l[14].latein
        self.dv16 = self.l[15].deutsch
        self.lv16 = self.l[15].latein
        self.dv17 = self.l[16].deutsch
        self.lv17 = self.l[16].latein
        self.dv18 = self.l[17].deutsch
        self.lv18 = self.l[17].latein
        self.dv19 = self.l[18].deutsch
        self.lv19 = self.l[18].latein
        if mehrals19 or mehrals35 or mehrals36 or mehrals37 or mehrals38 or mehrals40 or mehrals41 or mehrals42 or mehrals43 or mehrals50:
            self.dv20 = self.l[19].deutsch
            self.lv20 = self.l[19].latein
            self.dv21 = self.l[20].deutsch
            self.lv21 = self.l[20].latein
            self.dv22 = self.l[21].deutsch
            self.lv22 = self.l[21].latein
            self.dv23 = self.l[22].deutsch
            self.lv23 = self.l[22].latein
            self.dv24 = self.l[23].deutsch
            self.lv24 = self.l[23].latein
            self.dv25 = self.l[24].deutsch
            self.lv25 = self.l[24].latein
            self.dv26 = self.l[25].deutsch
            self.lv26 = self.l[25].latein
            self.dv27 = self.l[26].deutsch
            self.lv27 = self.l[26].latein
            self.dv28 = self.l[27].deutsch
            self.lv28 = self.l[27].latein
            self.dv29 = self.l[28].deutsch
            self.lv29 = self.l[28].latein
            self.dv30 = self.l[29].deutsch
            self.lv30 = self.l[29].latein
            self.dv31 = self.l[30].deutsch
            self.lv31 = self.l[30].latein
            self.dv32 = self.l[31].deutsch
            self.lv32 = self.l[31].latein
            self.dv33 = self.l[32].deutsch
            self.lv33 = self.l[32].latein
            self.dv34 = self.l[33].deutsch
            self.lv34 = self.l[33].latein
            self.dv35 = self.l[34].deutsch
            self.lv35 = self.l[34].latein
            if mehrals35 or mehrals36 or mehrals37 or mehrals38 or mehrals40 or mehrals41 or mehrals42 or mehrals43 or mehrals50:
                self.dv36 = self.l[35].deutsch
                self.lv36 = self.l[35].latein
                if mehrals36 or mehrals37 or mehrals38 or mehrals40 or mehrals41 or mehrals42 or mehrals43 or mehrals50:
                    self.dv37 = self.l[36].deutsch
                    self.lv37 = self.l[36].latein
                    if mehrals37 or mehrals38 or mehrals40 or mehrals41 or mehrals42 or mehrals43 or mehrals50:
                        self.dv38 = self.l[37].deutsch
                        self.lv38 = self.l[37].latein
                        if mehrals38 or mehrals40 or mehrals41 or mehrals42 or mehrals43 or mehrals50:
                            self.dv39 = self.l[38].deutsch
                            self.lv39 = self.l[38].latein
                            self.dv40 = self.l[39].deutsch
                            self.lv40 = self.l[39].latein
                            if mehrals40 or mehrals41 or mehrals43 or mehrals50:
                                self.dv41 = self.l[40].deutsch
                                self.lv41 = self.l[40].latein
                                if mehrals41 or mehrals43 or mehrals50:
                                    self.dv42 = self.l[41].deutsch
                                    self.lv42 = self.l[41].latein
                                    if mehrals43 or mehrals50:
                                        self.dv43 = self.l[42].deutsch
                                        self.lv43 = self.l[42].latein
                                    else:
                                        self.dv43 = ""
                                        self.lv43 = ""
                                else:
                                    self.dv42 = ""
                                    self.lv42 = ""
                                    self.dv43 = ""
                                    self.lv43 = ""
                            else:
                                self.dv41 = ""
                                self.lv41 = ""
                                self.dv41 = ""
                                self.lv41 = ""
                                self.dv42 = ""
                                self.lv42 = ""
                                self.dv43 = ""
                                self.lv43 = ""

                        else:
                            self.dv39 = ""
                            self.lv39 = ""
                            self.dv40 = ""
                            self.lv40 = ""
                            self.dv41 = ""
                            self.lv41 = ""
                            self.dv41 = ""
                            self.lv41 = ""
                            self.dv42 = ""
                            self.lv42 = ""
                            self.dv43 = ""
                            self.lv43 = ""
                    else:
                        self.dv38 = ""
                        self.lv38 = ""
                        self.dv39 = ""
                        self.lv39 = ""
                        self.dv40 = ""
                        self.lv40 = ""
                        self.dv41 = ""
                        self.lv41 = ""
                        self.dv41 = ""
                        self.lv41 = ""
                        self.dv42 = ""
                        self.lv42 = ""
                        self.dv43 = ""
                        self.lv43 = ""
                else:
                    self.dv37 = ""
                    self.lv37 = ""
                    self.dv38 = ""
                    self.lv38 = ""
                    self.dv39 = ""
                    self.lv39 = ""
                    self.dv40 = ""
                    self.lv40 = ""
                    self.dv41 = ""
                    self.lv41 = ""
                    self.dv41 = ""
                    self.lv41 = ""
                    self.dv42 = ""
                    self.lv42 = ""
                    self.dv43 = ""
                    self.lv43 = ""

            else:
                self.dv36 = ""
                self.lv36 = ""
                self.dv37 = ""
                self.lv37 = ""
                self.dv38 = ""
                self.lv38 = ""
                self.dv39 = ""
                self.lv39 = ""
                self.dv40 = ""
                self.lv40 = ""
                self.dv41 = ""
                self.lv41 = ""
                self.dv41 = ""
                self.lv41 = ""
                self.dv42 = ""
                self.lv42 = ""
                self.dv43 = ""
                self.lv43 = ""
        else:
            self.dv20 = ""
            self.lv20 = ""
            self.dv21 = ""
            self.lv21 = ""
            self.dv22 = ""
            self.lv22 = ""
            self.dv23 = ""
            self.lv23 = ""
            self.dv24 = ""
            self.lv24 = ""
            self.dv25 = ""
            self.lv25 = ""
            self.dv26 = ""
            self.lv26 = ""
            self.dv27 = ""
            self.lv27 = ""
            self.dv28 = ""
            self.lv28 = ""
            self.dv29 = ""
            self.lv29 = ""
            self.dv30 = ""
            self.lv30 = ""
            self.dv31 = ""
            self.lv31 = ""
            self.dv32 = ""
            self.lv32 = ""
            self.dv33 = ""
            self.lv33 = ""
            self.dv34 = ""
            self.lv34 = ""
            self.dv35 = ""
            self.lv35 = ""
            self.dv36 = ""
            self.lv36 = ""
            self.dv37 = ""
            self.lv37 = ""
            self.dv38 = ""
            self.lv38 = ""
            self.dv39 = ""
            self.lv39 = ""
            self.dv40 = ""
            self.lv40 = ""
            self.dv41 = ""
            self.lv41 = ""
            self.dv41 = ""
            self.lv41 = ""
            self.dv42 = ""
            self.lv42 = ""
            self.dv43 = ""
            self.lv43 = ""

    # properties werden benötigt, um eventgebundene Änderungen auf das UI zu übertragen
    Vokabeln = ObjectProperty(None)
    vokabel_one = ObjectProperty(None)
    vokabel_two = ObjectProperty(None)
    vokabel_three = ObjectProperty(None)
    vokabel_four = ObjectProperty(None)
    a = ObjectProperty(None)
    b = ObjectProperty(None)
    message = ObjectProperty(None)
    lektionstatus = ObjectProperty(None)
    lektionsstatusc = ObjectProperty(None)
    dv1 = ObjectProperty(None)
    lv1 = ObjectProperty(None)
    dv2 = ObjectProperty(None)
    lv2 = ObjectProperty(None)
    dv3 = ObjectProperty(None)
    lv3 = ObjectProperty(None)
    dv4 = ObjectProperty(None)
    lv4 = ObjectProperty(None)
    dv5 = ObjectProperty(None)
    lv5 = ObjectProperty(None)
    dv6 = ObjectProperty(None)
    lv6 = ObjectProperty(None)
    dv7 = ObjectProperty(None)
    lv7 = ObjectProperty(None)
    dv8 = ObjectProperty(None)
    lv8 = ObjectProperty(None)
    dv9 = ObjectProperty(None)
    lv9 = ObjectProperty(None)
    dv10 = ObjectProperty(None)
    lv10 = ObjectProperty(None)
    dv11 = ObjectProperty(None)
    lv11 = ObjectProperty(None)
    dv12 = ObjectProperty(None)
    lv12 = ObjectProperty(None)
    dv13 = ObjectProperty(None)
    lv13 = ObjectProperty(None)
    dv14 = ObjectProperty(None)
    lv14 = ObjectProperty(None)
    dv15 = ObjectProperty(None)
    lv15 = ObjectProperty(None)
    dv16 = ObjectProperty(None)
    lv16 = ObjectProperty(None)
    dv17 = ObjectProperty(None)
    lv17 = ObjectProperty(None)
    dv18 = ObjectProperty(None)
    lv18 = ObjectProperty(None)
    dv19 = ObjectProperty(None)
    lv19 = ObjectProperty(None)
    dv20 = ObjectProperty(None)
    lv20 = ObjectProperty(None)
    dv21 = ObjectProperty(None)
    lv21 = ObjectProperty(None)
    dv22 = ObjectProperty(None)
    lv22 = ObjectProperty(None)
    dv23 = ObjectProperty(None)
    lv23 = ObjectProperty(None)
    dv24 = ObjectProperty(None)
    lv24 = ObjectProperty(None)
    dv25 = ObjectProperty(None)
    lv25 = ObjectProperty(None)
    dv26 = ObjectProperty(None)
    lv26 = ObjectProperty(None)
    dv27 = ObjectProperty(None)
    lv27 = ObjectProperty(None)
    dv28 = ObjectProperty(None)
    lv28 = ObjectProperty(None)
    dv29 = ObjectProperty(None)
    lv29 = ObjectProperty(None)
    dv30 = ObjectProperty(None)
    lv30 = ObjectProperty(None)
    dv31 = ObjectProperty(None)
    lv31 = ObjectProperty(None)
    dv32 = ObjectProperty(None)
    lv32 = ObjectProperty(None)
    dv33 = ObjectProperty(None)
    lv33 = ObjectProperty(None)
    dv34 = ObjectProperty(None)
    lv34 = ObjectProperty(None)
    dv35 = ObjectProperty(None)
    lv35 = ObjectProperty(None)
    dv36 = ObjectProperty(None)
    lv36 = ObjectProperty(None)
    dv37 = ObjectProperty(None)
    lv37 = ObjectProperty(None)
    dv38 = ObjectProperty(None)
    lv38 = ObjectProperty(None)
    dv39 = ObjectProperty(None)
    lv39 = ObjectProperty(None)
    dv40 = ObjectProperty(None)
    lv40 = ObjectProperty(None)
    dv41 = ObjectProperty(None)
    lv41 = ObjectProperty(None)
    dv42 = ObjectProperty(None)
    lv42 = ObjectProperty(None)
    dv43 = ObjectProperty(None)
    lv43 = ObjectProperty(None)

    ##################################################################################################################


    Lektion_1 = [Entry("ave", "sei gegrüßt"), Entry("populus", "Volk, Publikum"),
                 Entry("clamare", "rufen, schreien"), Entry("et", "und, auch"),
                 Entry("nam", "denn, nämlich"), Entry("imperator", "Feldherr, Herrscher"),
                 Entry("apparere", "erscheinen, sich zeigen"), Entry("nunc", "jetzt, nun"),
                 Entry("appellare", "anreden, nennen"), Entry("turba", "Menschenmenge"),
                 Entry("non", "nicht"), Entry("sed", "aber, sondern"),
                 Entry("audire", "hören, zuhören"), Entry("autem", "aber, jedoch"),
                 Entry("magnus/-a/-um", "groß, bedeutend"), Entry("spectaculum", "Schau, Schauspiel"),
                 Entry("promittere", "versprechen"), Entry("tum", "da, dann"),
                 Entry("clarus/-a/-um", "hell, berühmt")]

    Lektion_2 = [Entry("videre", "sehen"), Entry("quo", "wohin"), Entry("vadere", "gehen"),
                 Entry("in", "in, nach"), Entry("forum, n", "Forum, Marktplatz"),
                 Entry("basilica, f", "Basilika, Kirche"), Entry("orator, m", "Redner"),
                 Entry("causa, f", "Ursache; Prozess"), Entry("agere", "treiben, verhandeln"),
                 Entry("causam agere", "einen Prozess führen"), Entry("pro", "vor; für"),
                 Entry("ego", "ich"), Entry("studere", "sich bemühen, wollen"), Entry("quid", "was"),
                 Entry("cum", "(zusammen) mit"), Entry("sedere", "sitzen"), Entry("ludere", "spielen, sich vergnügen"),
                 Entry("amicus, m", "Freund"), Entry("amica, f", "Freundin"), Entry("ut", "wie"),
                 Entry("nondum", "noch nicht"), Entry("e, ex", "aus, von aus"), Entry("nonne?", "(etwa) nicht?"),
                 Entry("unus/-a/-um", "ein, eine(r/s)"), Entry("num?", "etwa?"),
                 Entry("errare", "irren, sich täuschen"), Entry("-ne (angehängt)", "(Fragesignal)"),
                 Entry("fortasse", "vielleicht"), Entry("sine", "ohne"), Entry("neque, nec", "(und/auch/aber) nicht"),
                 Entry("pecunia, f", "Geld"), Entry("a, ab", "von; seit"), Entry("ubi", "wo"),
                 Entry("mos (pl. mores), m", "Sitte, Brauch, Art"), Entry("ad", "zu, an, bei"),
                 Entry("eiusmodi", "derartig, solch"), Entry("intellegere", "erkennen, verstehen")]

    Lektion_3 = [Entry("multus/-a/-um", "viel, zahlreich"), Entry("dum", "während"),
                 Entry("gladiator, m", "Gladiator"), Entry("arena, f", "Sand, Arena"),
                 Entry("alius/-a/-ud", "ein anderer"), Entry("alii - alii", "die einen - die anderen"),
                 Entry("petere", "aufsuchen; angreifen"), Entry("gladius, m", "Schwert"),
                 Entry("vacare", "frei sein (von), nicht haben"), Entry("timor, m", "Furcht"),
                 Entry("bonus/-a/-um", "gut, tüchtig"), Entry("animus, m", "Geist, Verstand"),
                 Entry("bono animo esse", "guten Mutes sein"), Entry("occidere", "niederschlagen, töten"),
                 Entry("pugnare", "kämpfen"), Entry("tamen", "dennoch, trotzdem"),
                 Entry("dubitare", "zögern, zweifeln"), Entry("observare", "beobachten, einhalten"),
                 Entry("tandem", "endlich, schließlich"), Entry("timere", "(sich) fürchten"),
                 Entry("cunctus/ -a/ -um", "all(es), gesamt"), Entry("malus/-a/-um", "schlecht, schlimm, böse"),
                 Entry("solum", "allein, nur"), Entry("hic", "hier"),
                 Entry("locus, m (pl loca, n)", "Ort, Platz, Rang"), Entry("cavere", "sich hüten"),
                 Entry("neque enim", "denn nicht"), Entry("pugna, f", "Kampf"),
                 Entry("gaudere", "sich freuen"), Entry("vulnerare", "verwunden"),
                 Entry("de", "von, über"), Entry("deliberare", "erwägen, überlegen"),
                 Entry("ludus, m", "Spiel, Schule"), Entry("misericordia, f", "Mitleid, Barmherzigkeit"),
                 Entry("subito", "plötzlich"), Entry("iacere", "liegen, daliegen"),
                 Entry("victoria, f", "Sieg"), Entry("victor, m", "Sieger"),
                 Entry("laudare", "loben, rühmen"), Entry("cedere", "weggehen; nachgeben")]

    Lektion_4 = [Entry("unde", "woher"), Entry("ira, irae, f", "Zorn"),
                 Entry("dominus, domini, m", "Herr"), Entry("domina, dominae, f", "Herrin"),
                 Entry("libertus, liberti, m", "Freigelassener"), Entry("mercator, mercatoris, m", "Kaufmann"),
                 Entry("inter", "zwischen; während", ), Entry("vivere", "leben"),
                 Entry("quis", "wer", ), Entry("filius, filii, m", "Sohn"),
                 Entry("filia, filiae, f", "Tochter"), Entry("pater, patris, m", "Vater"),
                 Entry("patres, patrum, m", "Senatoren, Patrizier"), Entry("honestus/-a/-um", "angesehen, ehrenhaft"),
                 Entry("nihil", "nichts"), Entry("nisi", "wenn nicht; außer"),
                 Entry("servus, servi, m", "Sklave"), Entry("serva, servae, f", "Sklavin"),
                 Entry("itaque", "deshalb, daher"), Entry("tacere", "schweigen"),
                 Entry("parere", "gehorchen"), Entry("debere", "müssen; schulden"),
                 Entry("non debere", "nicht dürfen"), Entry("vix", "kaum"),
                 Entry("tenere", "halten, festhalten"), Entry("familia, familae, f", "Familie"),
                 Entry("reprehendere", "tadeln"), Entry("sermo, sermonis, m", "Gespräch, Sprache"),
                 Entry("neque - neque", "weder - noch"), Entry("curare", "besorgen, sorgen"),
                 Entry("quidem", "zwar, wenigstens"), Entry("neque tamen", "aber nicht"),
                 Entry("descendere", "herabsteigen"), Entry("quoque", "auch"),
                 Entry("igitur", "also, folglich"), Entry("apud", "bei, in der Nähe von"),
                 Entry("iam", "schon, bereits; gleich"), Entry("hospes, hospitis, m", "Gast; Fremder"),
                 Entry("molestus/-a/-um", "lästig, peinlich"), Entry("profecto", "in der Tat"),
                 Entry("desinere", "ablassen, aufhören")]

    Lektion_5 = [Entry("per", "(hin)durch, über"), Entry("thermae, thermarum, f", "Thermen"),
                 Entry("ambulare", "spazieren gehen"), Entry("ubique", "überall"),
                 Entry("quaerere, quaero, quaesivi", "suchen"), Entry("quaerere ex", "fragen"),
                 Entry("quot", "wie viele"), Entry("quantus/-a/-um", "wie groß/viel"),
                 Entry("tot", "so viele"), Entry("cum (Subjunktion)", "als (plötzlich)"),
                 Entry("bibliotheca, bibliothecae, f", "Bibliothek"), Entry("legere, lego, legi", "lesen"),
                 Entry("gaudium, gaudi, n", "Freude"), Entry("rogare", "fragen, bitten"),
                 Entry("inquam, inquit", "sag(t)e ich/er/sie"), Entry("satis", "genug"),
                 Entry("dare, do, dedi", "geben"), Entry("deponere, depono, deposui", "ablegen"),
                 Entry("diu", "lange, lange Zeit"), Entry("manere, maneo, mansi", "bleiben"),
                 Entry("quod", "weil"), Entry("aqua, aquae, f", "Wasser"),
                 Entry("postquam", "nachdem, als"), Entry("relinquere, relinquo, reliqui", "zurücklassen"),
                 Entry("spoliare", "berauben, entkleiden"), Entry("non iam", "nicht mehr"),
                 Entry("frustra", "vergeblich"), Entry("vocare", "rufen, nennen"),
                 Entry("parentes, parent(i)um, m", "Eltern"), Entry("mittere, mitto, misi", "schicken"),
                 Entry("currere, curro, cucurri", "laufen, rennen"), Entry("statim", "sofort"),
                 Entry("invenire, invenio, inveni", "finden, erfinden"), Entry("quamquam", "obwohl"),
                 Entry("novus/-a/-um", "neu, neuartig")]

    Lektionen1bis5 = Lektion_1 + Lektion_2 + Lektion_3 + Lektion_4 + Lektion_5

    Lektion_6 = [Entry("ara, arae, f", "Altar"), Entry("pax, pacis, f", "Friede"),
                 Entry("aedificare", "bauen, errichten"), Entry("ipse/ipsa/ipsum", "selbst"),
                 Entry("pulcher/pulchra/pulchrum", "schön, hübsch"), Entry("is/ea/id", "er/sie/es"),
                 Entry("frater, fratris, m", "Bruder"), Entry("honor, honoris, m", "Ehre"),
                 Entry("ornare", "ausstatten, schmücken"), Entry("habere", "haben, besitzen"),
                 Entry("nepos, nepotis, m", "Enkel, Neffe"), Entry("vita, vitae, f", "Leben"),
                 Entry("vita cedere", "sterben"), Entry("vitam agere", "ein Leben führen"),
                 Entry("adulescens, adulescentis, m", "junger Mann"), Entry("post", "nach, hinter"),
                 Entry("mors, mortis, f", "Tod"), Entry("saepe", "oft"),
                 Entry("vir, viri, m", "Mann"), Entry("nonnulli/-ae/-a", "einige, manche"),
                 Entry("annus, anni, m", "Jahr"), Entry("dum", "solange (bis)"),
                 Entry("laedere, laedo, laesi", "verletzen"), Entry("liber/-a/-um", "frei, unabhängig"),
                 Entry("nex, necis, f", "Tod, Mord"), Entry("parare", "bereiten, vorbereiten"),
                 Entry("parvus/-a/-um", "klein, gering"), Entry("insula, insulae, f", "Insel"),
                 Entry("transportare", "hinüberbringen"), Entry("miser/-a/-um", "elend, armselig"),
                 Entry("pauci/-ae/-a", "wenige"), Entry("post", "später, darauf"),
                 Entry("venia, veniae, f", "Verzeihung"), Entry("immo (vero)", "ja sogar"),
                 Entry("vero", "aber"), Entry("negare", "leugnen, bestreiten"),
                 Entry("tam", "so"), Entry("severus/-a/-um", "ernst, streng"),
                 Entry("sui, suorum, m", "seine Leute"), Entry("aliter", "anders, sonst"),
                 Entry("liberi, liberorum, m", "Kinder"), Entry("solere", "gewohnt sein, pflegen"),
                 Entry("quam", "als, wie")]

    Lektion_7 = [Entry("nox, noctis, f", "Nacht"), Entry("somnus, somni, m", "Schlaf"),
                 Entry("se/sibi", "sich"), Entry("se somno dare", "sich schlafen legen"),
                 Entry("imago, imaginis, f", "Bild, Abbild"), Entry("fugere, fugio, fugi", "fliehen, meiden"),
                 Entry("hostis, hostis, m", "Feind"), Entry("murus, muri, m", "Mauer"),
                 Entry("capere, capio, cepi", "fassen"), Entry("sacrum, sacri, n", "Heiligtum"),
                 Entry("patria, patriae, f", "Vaterland"), Entry("servare", "retten, bewahren"),
                 Entry("cupere, cupio, cupivi", "begehren"), Entry("via, viae, f", "Weg, Straße"),
                 Entry("urbs, urbis, f", "Stadt"), Entry("iacere, iacio, ieci", "werfen"),
                 Entry("telum, teli, n", "(Wurf-)Geschoss"), Entry("virgo, virginis, f", "Mädchen"),
                 Entry("rapere, rapio, rapui", "rauben"), Entry("si", "wenn"),
                 Entry("mulier, mulieris, f", "Frau, Ehefrau"), Entry("senex, senis, m", "alt; Greis"),
                 Entry("ille/illa/illud", "jener/jene/jenes"), Entry("aspicere, aspicio, aspexi", "ansehen"),
                 Entry("qui/qua/quod", "der/die/das"), Entry("arx, arcis, f", "Burg"),
                 Entry("malum, mali, n", "Übel, Leid"), Entry("facere, facio, feci", "tun"),
                 Entry("hic/haec/hoc", "dieser/diese/dieses"), Entry("verbum, verbi, n", "Wort"),
                 Entry("movere, moveo, movi", "bewegen"), Entry("dicere, dico, dixi", "sagen"),
                 Entry("flamma, flammae, f", "Flamme, Feuer"), Entry("signum, signi, n", "Zeichen"),
                 Entry("monere", "mahnen, auffordern")]

    Lektion_8 = [Entry("sedes, sedis, f", "Sitz, Wohnsitz"), Entry("beatus/-a/-um", "glücklich"),
                 Entry("sedes beatae", "Gefilde der Seeligen"), Entry("sors, sortis, f", "Schicksal, Los"),
                 Entry("gens, gentis, f", "Geschlecht"), Entry("ducere, duco, duxi", "führen"),
                 Entry("anima, animae, f", "Atem, Seele"), Entry("monstrare", "zeigen"),
                 Entry("tempus, temporis, n", "Zeit, Zeitpunkt"), Entry("suo tempore", "zur rechten Zeit"),
                 Entry("lux, lucis, f", "Licht"), Entry("fatum, fati, n", "Schicksal"),
                 Entry("docere, doceo, docui", "lehren"), Entry("rex, regis, m", "König"),
                 Entry("regnare", "König sein, herrschen"), Entry("mons, montis, m", "Berg"),
                 Entry("ponere, pono, posui", "stellen"), Entry("nomen, nominis, n", "Name"),
                 Entry("omen, ominis, n", "Vorzeichen"), Entry("condere, condo, condidi", "gründen"),
                 Entry("moenia, moenium, n", "Stadtmauer"), Entry("turris, turris, f", "Turm"),
                 Entry("circumdare, circumdo", "umzingeln"), Entry("primus/-a/-um", "der/die/das erste"),
                 Entry("opus, operis, n", "Werk, Arbeit"), Entry("vis, vim, f", "Gewalt, Kraft"),
                 Entry("vincere, vinco, vici", "siegen"), Entry("finis, finis, m", "Grenze, Ende"),
                 Entry("imperium, imperi, n", "Befehl, Reich"), Entry("orbis, orbis, m", "Kreis(lauf)"),
                 Entry("terra, terrae, f", "Land, Erde"), Entry("orbis terrarum", "Erdkreis, Welt"),
                 Entry("superbus/-a/-um", "hochmütig, stolz"), Entry("pellere, pello, pepuli", "ver-) treiben"),
                 Entry("civitas, civitatis, f", "Bürgerrecht, Staat"), Entry("consul, consulis, m", "Konsul"),
                 Entry("triumphus, triumphi, m", "Triumph"), Entry("triumphum agere", "einen Triumph feiern"),
                 Entry("dux, ducis, m/f", "Führer/in"), Entry("auctor, auctoris, m", "Begründer, Verfasser"),
                 Entry("iustus/-a/-um", "gerecht"), Entry("parcere, parco, peperci", "schonen")]

    Lektion_9 = [Entry("acer/acris/acre", "spitz"), Entry("tribunus, tribuni, m", "Tribun"),
                 Entry("celer/celeris/celere", "schnell"), Entry("auxilium, auxili, n", "Hilfe"),
                 Entry("opus est", "es ist nötig"), Entry("discordia, discordiae, f", "Zwietracht"),
                 Entry("plebs, plebis, f", "Volk"), Entry("lex, legis, f", "Gesetz"),
                 Entry("scribere, scribo, scripsi", "schreiben"), Entry("crudelis/crudele", "grausam, brutal"),
                 Entry("iudicium, iudici, n", "Gericht"), Entry("ira motus", "aus Zorn"),
                 Entry("iterum", "wiederum"), Entry("fabula, fabulae, f", "Erzählung"),
                 Entry("brevis/breve", "kurz"), Entry("eques, equitis, m", "Reiter, Ritter"),
                 Entry("omnis/omne", "all(es), ganz"), Entry("mortalis/mortale", "sterblich"),
                 Entry("putare", "glauben, meinen"), Entry("periculum, periculi, n", "Gefahr"),
                 Entry("imminere", "drohen, bedrohen"), Entry("perdere, perdo, perdidi", "vernichten"),
                 Entry("necesse est", "es ist nötig"), Entry("concedere, concedo, concessi", "zugestehen"),
                 Entry("civis, civis, m", "Bürger"), Entry("utilis/utile", "nützlich"),
                 Entry("constat", "es ist bekannt"), Entry("salus, salutis, f", "Wohl"),
                 Entry("communis/commune", "allgemein, gemeinsam"), Entry("consulere, consulo", "beratschlagen"),
                 Entry("convenit", "es ziemt sich"), Entry("legatus, legati, m", "Abgesandter"),
                 Entry("ius, iuris, n", "Recht"), Entry("tradere, trado, tradidi", "übergeben"),
                 Entry("prudens, prudentis", "klug, umsichtig"), Entry("corrigere, corrigo, correxi", "berichtigen"),
                 Entry("tabula, tabulae, f", "Tafel, Gemälde"), Entry("apparet", "es ist offensichtlich, klar")]

    Lektion_10 = [Entry("totus/-a/-um", "ganz"), Entry("fere", "ungefähr, fast"),
                  Entry("exercitus, exercitus, m", "Heer"), Entry("caedere, caedo, cecidi", "fällen, schlagen"),
                  Entry("socius, soci, m", "Gefährte, Verbündeter"), Entry("pars, partis, f", "Teil"),
                  Entry("et - et", "sowohl - als auch"), Entry("quaestor, quaestoris, m", "Quästor"),
                  Entry("miles, militis, m", "Soldat"), Entry("tribunus militum", "Militärtribun"),
                  Entry("praetera", "außerdem"), Entry("senatus, senatus, m", "Senat"),
                  Entry("pedes, peditis, m", "Infanterist"), Entry("castra, castrorum, n", "Lager"),
                  Entry("evadere, evado, evasi", "herausgehen"), Entry("nuntiare", "melden, mitteilen"),
                  Entry("nemo", "niemand"), Entry("clades, cladis, f", "Niederlage"),
                  Entry("numquam", "niemals"), Entry("tantus/-a/-um", "so groß/ viel"),
                  Entry("tumultus, tumultus, m", "Aufruhr"), Entry("praetor, praetoris, m", "Prätor"),
                  Entry("curia, curiae, f", "Kurie"), Entry("magistratus, magistratus, m", "Amt"),
                  Entry("consilium, consili, n", "Rat"), Entry("pro certo habere", "für sicher halten"),
                  Entry("impetus, impetus, m", "Angriff"), Entry("impetu", "im Sturmangriff"),
                  Entry("prudentia, prudentiae, f", "Klugheit"), Entry("constantia, constantiae, f", "Festigkeit"),
                  Entry("certus/-a/-um", "sicher"), Entry("certe", "sicherlich, gewiss"),
                  Entry("scire", "wissen"), Entry("augere, augeo, auxi", "vergrößern"),
                  Entry("multitudo, multitudinis, f", "Vielzahl"), Entry("tollere, tollo, sustuli", "(auf-)heben"),
                  Entry("arcere", "abhalten, abwehren"), Entry("matrona, matronae, f", "Frau, Matrone"),
                  Entry("publicum, publici, n", "Öffentlichkeit"), Entry("custos, custodis, m", "Wächter"),
                  Entry("porta, portae, f", "Tor"), Entry("salvus/-a/-um", "wohlbehalten"),
                  Entry("expugnare", "erstürmen, erobern")]

    Lektionen6bis10 = Lektion_6 + Lektion_7 + Lektion_8 + Lektion_9 + Lektion_10

    Lektion_11 = [Entry("amor, amoris, m", "Liebe"), Entry("adducere, adduco, adduxi", "heranführen"),
                  Entry("ut", "dass, damit"), Entry("praecipere, praecipio, praecepi", "vorwegnehmen"),
                  Entry("aut", "oder"), Entry("memoria, memoriae, f", "Gedächtnis"),
                  Entry("memoria tenere", "im Gedächtnis behalten"), Entry("provincia, provinciae, f", "Provinz"),
                  Entry("humanitas, humanitatis, f", "Menschlichkeit"), Entry("littera, litterae, f", "Buchstabe"),
                  Entry("maxime", "am meisten"), Entry("natura, naturae, f", "Natur"),
                  Entry("virtus, virtutis, f", "Tapferkeit"), Entry("religio, religionis, f", "Bedenken"),
                  Entry("antiquitas, antiquitatis, f", "Altertum"), Entry("factum, facti, n", "Tat"),
                  Entry("antiquus/-a/-um", "alt"), Entry("despicere, despicio, despexi", "herabsehen"),
                  Entry("superbia, superbiae, f", "Hochmut"), Entry("ignorare", "nicht wissen"),
                  Entry("ne", "dass nicht"), Entry("clementia, clementiae, f", "Milde"),
                  Entry("conciliare", "gewinnen"), Entry("terror, terroris, m", "Schrecken"),
                  Entry("abstinere", "abhalten"), Entry("recedere, recedo, recessi", "zurückweichen"),
                  Entry("ante", "vor"), Entry("oculus, oculi, m", "Auge"),
                  Entry("servire", "Sklave sein, dienen"), Entry("minuere, minuo, minui", "verringern"),
                  Entry("servitus, servitutis, f", "Sklaverei"), Entry("turpis/turpe", "hässlich"),
                  Entry("libertas, libertatis, f", "Freiheit"), Entry("credere, credo, credidi", "glauben"),
                  Entry("initium, initi, n", "Anfang"), Entry("initio", "anfangs"),
                  Entry("equidem", "(ich) jedenfalls"), Entry("modus, modi, m", "Art, Weise"),
                  Entry("nimius/-a/-um", "zu groß/viel"), Entry("vale/valete", "leb/lebt wohl!")]

    Lektion_12 = [Entry("bellum, belli, n", "Krieg"), Entry("gerere, gero, gessi", "tragen ausführen"),
                  Entry("bellum gerere", "Krieg führen"), Entry("divitae, divitarum, f", "Reichtum"),
                  Entry("cupidus/-a/-um", "begierig"), Entry("cum", "als, nachdem"),
                  Entry("occidens, occidentis, m", "Westen, Abendland"),
                  Entry("oriens, orientis, m", "Osten, Morgenland"),
                  Entry("pergere, pergo, perrexi", "weitermachen"),
                  Entry("finem facere", "eine Grenze setzen"), Entry("arma, armorum, n", "Waffen"),
                  Entry("vertere, verto, verti", "wenden"),
                  Entry("pestis, pestis, f", "Seuche, Unglück"), Entry("nihil nisi", "nichts als"),
                  Entry("ne...quidem", "nicht einmal"), Entry("dissimulare", "sich verstellen"),
                  Entry("quomodo", "wie, auf welche Weise"), Entry("mirus/-a/-um", "wunderbar"),
                  Entry("regnum, regni, n", "Königreich"), Entry("fas, n", "(göttliches) Recht"),
                  Entry("foedus, foederis, n", "Bündnis, Vertrag"), Entry("frangere, frango, fregi", "brechen"),
                  Entry("prodere, prodo, prodidi", "preisgeben"), Entry("oppidum, oppidi, n", "Stadt"),
                  Entry("delere, deleo, delevi", "zerstören"), Entry("invidia, invidiae, f", "Neid, Abneigung"),
                  Entry("avaritia, avaritiae, f", "Habgier"), Entry("etiam", "auch, sogar"),
                  Entry("praeda, praedae, f", "Beute"), Entry("sperare", "hoffen"),
                  Entry("posse, possum, potui", "können"), Entry("praesidium, praesidi, n", "Schutz"),
                  Entry("intendere, intendo, intendi", "beabsichtigen, anspannen"),
                  Entry("damnum, damni, n", "Schaden"),
                  Entry("imprimis", "besonders, vor allem"), Entry("neve", "und dass/damit nicht"),
                  Entry("sinere, sino, sivi, situm", "lassen"), Entry("gloria, gloriae, f", "Ruhm"),
                  Entry("latro, latronis, m", "Räuber"), Entry("opprimere, opprimo, oppressi", "unterdrücken")]

    Lektion_13 = [Entry("oratio, orationis, f", "Rede"), Entry("valere", "gesund sein"),
                  Entry("vox, vocis, f", "Stimme, Wort"), Entry("perturbare", "(völlig) verwirren"),
                  Entry("statuere, statuo, statui", "aufstellen"), Entry("dissere, dissero, disserui", "erörtern"),
                  Entry("intrare", "eintreten"), Entry("nullus/-a/-um", "kein"),
                  Entry("cupiditas, cupiditatis, f", "Begierde"), Entry("maiores, maiorum, m", "Vorfahren, Ahnen"),
                  Entry("vehemens, vehementis", "heftig"), Entry("vexare", "quälen, beunruhigen"),
                  Entry("ideo", "deswegen, deshalb"), Entry("defendere, defendo, defendi", "verteidigen"),
                  Entry("invadere, invado, invasi", "eindringen"), Entry("longus/-a/-um", "lang, weit"),
                  Entry("latus/-a/-um", "breit"), Entry("longe lateque", "weit und breit"),
                  Entry("vastare", "verwüsten"), Entry("mutare", "ändern, verändern"),
                  Entry("ager, agri, m", "Acker, Feld"), Entry("atque, ac", "und, und auch"),
                  Entry("possidere, possideo, possedi", "besitzen"), Entry("semper", "immer"),
                  Entry("imponere, impono, imposui", "hineinsetzen"), Entry("tutus/-a/-um", "geschützt, sicher"),
                  Entry("quies, quietis, f", "Ruhe, Erholung"), Entry("stipendium, stipendi, n", "Steuer, Sold"),
                  Entry("tributum, tributi, n", "Abgabe, Steuer"), Entry("plerumque", "meistens"),
                  Entry("legio, legionis, f", "Legion"), Entry("praeesse, praesum, praefui", "an der Spitze"),
                  Entry("regere, rego, rexi, rectum", "leiten"), Entry("claudere, claudo, clausi", "schließen"),
                  Entry("quietus/-a/-um", "ruhig"), Entry("copia, copiae, f", "Vorrat, Menge")]

    Lektion_14 = [Entry("cohors, cohortis, f", "Kohorte"), Entry("flumen, fluminis, n", "Fluss"),
                  Entry("praefectus, praefecti, n", "Präfekt"), Entry("navis, navis, f", "Schiff"),
                  Entry("lacus, lacus, m", "See, Teich"), Entry("amittere, amitto, amisi", "aufgeben"),
                  Entry("agmen, agminis, n", "Heereszug"), Entry("ultimus/-a/-um", "der/die/das letzte"),
                  Entry("procul", "fern, weit weg"), Entry("dolus, doli, m", "List, Betrug"),
                  Entry("iniquus/-a/-um", "ungleich/ungerecht"), Entry("inquirere, inquiro, inquisivi", "untersuchen"),
                  Entry("reliquiae, reliquiarum, f", "Überreste"), Entry("causa", "wegen, um...willen"),
                  Entry("praemittere, praemitto", "vorausschicken"), Entry("brevi (tempore)", "bald darauf"),
                  Entry("aspectus, aspectus, m", "Anblick"), Entry("terribilis/terribile", "schrecklich"),
                  Entry("primo", "zuerst"), Entry("deinde", "von da an"),
                  Entry("campus, campi, m", "Ebene, Feld"), Entry("equus, equi, m", "Pferd"),
                  Entry("arbor, arboris, f", "Baum"), Entry("figere, figo, fixi", "befestigen"),
                  Entry("caput, capitis, n", "Kopf, Hauptstadt"), Entry("silva, silvae, f", "Wald"),
                  Entry("barbarus, barbari, m", "Nichtrömer"), Entry("centurio, centurionis, m", "Zenturio"),
                  Entry("cadere, cado, cecidi", "fallen"), Entry("secundus/-a/-um", "der/die/das zweite"),
                  Entry("vulnus, vulneris, n", "Wunde"), Entry("accipere, accipio, accepi", "annehmen"),
                  Entry("manus, manus, f", "Hand"), Entry("acerbus/-a/-um", "herb, bitter"),
                  Entry("sepelire, sepelio, sepelivi", "begraben"), Entry("colere, colo, colui", "bebauen"),
                  Entry("fortis/forte", "tapfer, mutig")]

    Lektion_15 = [Entry("maior/maius", "größer, bedeutender"), Entry("victus, victus, m", "Lebensunterhalt"),
                  Entry("caro, carnis, f", "Fleisch"), Entry("consistere, consisto", "bestehen"),
                  Entry("proprius/-a/-um", "eigen"), Entry("singuli/-ae/-a", "einzeln"),
                  Entry("tribuere, tribuo, tribui", "zuteilen"), Entry("cogere, cogo, coegi", "sammeln"),
                  Entry("potens, potentis", "mächtig"), Entry("pauper, pauperis", "arm"),
                  Entry("diligens, diligentis", "sorgfältig"), Entry("incipere, incipio, coepi", "anfangen"),
                  Entry("luxuria, luxuriae, f", "Überfluss"), Entry("maximus/-a/-um", "der/die/das größte"),
                  Entry("futurum esse (~fore)", "sein"), Entry("ops, opis, f", "Kraft, Stärke"),
                  Entry("aequare", "gleichmachen"), Entry("laus, laudis, f", "Lob, Ruhm"),
                  Entry("quam", "möglichst"), Entry("circa/circum", "um...herum"),
                  Entry("ignominia, ignominiae, f", "Beschimpfung"), Entry("extra", "außerhalb"),
                  Entry("excercere", "üben, betreiben"), Entry("cum", "(immer) wenn"),
                  Entry("princeps, principis, m", "erster Mann"), Entry("concilium, concili, n", "Versammlung"),
                  Entry("comprare", "vergleichen"), Entry("contendere, contendo", "eilen"),
                  Entry("domus, domus, f", "Haus"), Entry("domi", "zu Hause"),
                  Entry("plurimi/-ae/-a", "die meisten"), Entry("contumelia, contumeliae, f", "Kränkung"),
                  Entry("afficere, afficio, affeci", "versehen (mit)"), Entry("contumeliis afficere", "beschimpfen"),
                  Entry("iniuria, iniuriae, f", "Unrecht"), Entry("prohibere", "abhalten"),
                  Entry("sanctus/-a/-um", "heilig"), Entry("patere", "offen stehen"),
                  Entry("iuvare, iuvo, iuvi", "unterstützen"), Entry("plus, pluris", "mehr")]

    Lektionen11bis15 = Lektion_11 + Lektion_12 + Lektion_13 + Lektion_14 + Lektion_15

    Lektion_16 = [Entry("uxor, uxoris, f", "Ehefrau"), Entry("arbitrari, arbitror", "meinen"),
                  Entry("aliquando", "einst"), Entry("versari, versor", "sich aufhalten"),
                  Entry("indignari, indignor", "empört sein"), Entry("profisci, profiscor", "aufbrechen"),
                  Entry("oraculum, oraculi, n", "Orakel"), Entry("sic", "so, auf diese Weise"),
                  Entry("hortari, hortor", "ermahnen"), Entry("mater, matris, f", "Mutter"),
                  Entry("(uxorem) ducere", "heiraten"), Entry("regredi, regredior", "zurückgehen"),
                  Entry("vereri, vereor", "sich scheuen"), Entry("vehere, veho, vexi", "tragen"),
                  Entry("vehi, vehor", "reiten"), Entry("mori, morior", "sterben"),
                  Entry("obviam", "entgegen"), Entry("cunctari, cunctor", "zögern"),
                  Entry("alter/altera/alterum", "der/die/das eine"), Entry("irasci, irascor", "zornig werden"),
                  Entry("tueri, tueor", "betrachten"), Entry("mentior", "lügen"),
                  Entry("postea", "nachher, später"), Entry("morari, moror", "zögern"),
                  Entry("monstrum, monstri, n", "Ungeheuer"), Entry("conspicari, conspicor", "erblicken"),
                  Entry("corpus, corporis, n", "Körper"), Entry("leo, leonis, m", "Löwe"),
                  Entry("solvere, solvo, solvi, soltum", "lösen"), Entry("qui/quae/quod", "welcher/welche/welches"),
                  Entry("animal, animalis, n", "Lebewesen"), Entry("pes, pedis, m", "Fuß"),
                  Entry("vesperi", "abends"), Entry("respondere, respondeo", "antworten"),
                  Entry("praecipitare", "stürzen"), Entry("liberare", "befreien"),
                  Entry("finire", "begrenzen, beenden")]

    Lektion_17 = [Entry("vivus/-a/-um", "lebend"), Entry("dici, dicor", "heißen, man sagt"),
                  Entry("uterque/utraque/utrumque", "jeder"), Entry("repetere, repeto, repetivi", "wiederholen"),
                  Entry("contrahere, contraho", "zusammenziehen"), Entry("oppugnare", "bestürmen"),
                  Entry("proelium, proeli, n", "Gefecht"), Entry("videre, videor", "scheinen, gelten"),
                  Entry("canis, canis, m", "Hund"), Entry("proicere, proicio, proieci", "hinwerfen"),
                  Entry("iubere, iubeo, iussi", "beauftragen"), Entry("disponere, dispono", "verteilen"),
                  Entry("edicere, edico, edixi", "verkünden"), Entry("iste/ista/istud", "dieser/diese/dieses"),
                  Entry("edictum, edicti, n", "Anordnung"), Entry("mortuus/-a/-um", "tot"),
                  Entry("cognoscere, cognosco", "erkennen"), Entry("pietas, pietatis, f", "Frömmigkeit"),
                  Entry("humus, humi, f", "Erde"), Entry("tegere, tego, texi", "decken"),
                  Entry("custodire", "bewachen. behüten"), Entry("comprehendere, comprehendo", "ergreifen"),
                  Entry("praeceptum, praecepti, n", "Vorschrift"), Entry("immortalis/immortale", "unsterblich"),
                  Entry("magis", "mehr"), Entry("damnare", "verdammen"),
                  Entry("capitis damnare", "zum Tode verurteilen"), Entry("resistere, resisto", "Widerstand leisten"),
                  Entry("solus/-a/-um", "allein"), Entry("constituiere, constituo", "fortsetzen"),
                  Entry("sepulcrum, sepulcri, n", "Grab"), Entry("aperire, aperio", "öffnen"),
                  Entry("dolor, doloris, m", "Schmerz"),
                  Entry("propinquus, propinqui, m", "Verwandter"), Entry("culpa, culpae, f", "Schuld"),
                  Entry("sero", "(zu) spät"), Entry("dolere", "Schmerz empfinden, wehtun")]

    Lektion_18 = [Entry("numen, numinis, n", "Macht"), Entry("mundus, mundi, m", "Welt(all)"),
                  Entry("sub", "unter"), Entry("situs/-a/-um", "gelegen, befindlich"),
                  Entry("ire, eo, ii, itum", "gehen"), Entry("vincire, vincio", "fesseln"),
                  Entry("ferre, fero, tuli, latum", "tragen"), Entry("modo", "eben (erst)"),
                  Entry("calamitas, calamitatis, f", "Unheil"), Entry("velle, volo", "wollen"),
                  Entry("preces, precum, f", "Bitten, Gebet"), Entry("adire, adeo", "herangehen"),
                  Entry("reddere, reddo", "zurückgeben, machen"), Entry("peragare, perago", "durchführen"),
                  Entry("invitus/-a/-um", "ungern"), Entry("humanus/-a/-um", "menschlich"),
                  Entry("genus, generis, n", "Geschlecht"), Entry("sin (autem)", "wenn aber"),
                  Entry("nolle, nolo", "nicht wollen"), Entry("redire, redeo", "zurückgehen"),
                  Entry("dulcis/dulce", "süß, angenehm"), Entry("cantare", "singen"),
                  Entry("flere, fleo", "weinen"), Entry("stare, sto", "stehen"),
                  Entry("captare", "(zu) fangen"), Entry("saxum, saxi, n", "Fels"),
                  Entry("volvere, volvo", "wälzen, rollen"), Entry("primum", "zum ersten Mal"),
                  Entry("lacrima, lacrimae, f", "Träne"), Entry("fama, famae, f", "Gerücht"),
                  Entry("fama fert", "es wird erzählt"), Entry("condicio, condicionis, f", "Bedingung"),
                  Entry("flectere, flecto", "biegen"), Entry("priusquam", "bevor, ehe"),
                  Entry("exire, exeo", "hinausgehen"), Entry("propter", "wegen"),
                  Entry("appropinquare", "sich nähern")]

    Lektion_19 = [Entry("spes, spei, f", "Hoffnung"), Entry("me spes tenet", "ich habe die Hoffnung"),
                  Entry("iudex, iudicis, m", "Richter"), Entry("bene", "gut"),
                  Entry("evenire, evenit", "geschehen"), Entry("quod", "dass"),
                  Entry("aut - aut", "entweder - oder"), Entry("sensus, sensus, m", "Sinn"),
                  Entry("auferre, aufero", "wegtragen"), Entry("ob", "wegen"),
                  Entry("res, rei, f", "Sache"), Entry("quam ob rem", "deswegen"),
                  Entry("altus/-a/-um", "hoch, tief"), Entry("similis/simile", "ähnlich"),
                  Entry("dies, diei, m", "Tag"), Entry("reperire, reperio", "wieder finden"),
                  Entry("anteponere, antepono", "voranstellen"), Entry("futurus/-a/-um", "zukünftig"),
                  Entry("verus/-a/-um", "wahr"), Entry("vere", "in Wahrheit"),
                  Entry("incolere, incolo", "wohnen"), Entry("excedere, excedo", "hinausgehen"),
                  Entry("convenire, convenio", "zusammenkommen"), Entry("fides, fidei, f", "Treue"),
                  Entry("colloqui, colloquor", "sich unterhalten"), Entry("licet", "man darf"),
                  Entry("fieri, fio", "werden"), Entry("temptare", "angreifen, versuchen"),
                  Entry("exquirere, exquiro", "untersuchen"), Entry("sicut", "(so) wie"),
                  Entry("absolvere, absolvo", "loslösen"), Entry("umquam", "jemals"),
                  Entry("neglegere, neglego", "sich nicht kümmern"), Entry("non habeo quod", "ich habe keinen Grund"),
                  Entry("suscensere", "aufgebracht sein"), Entry("accusare", "anklagen, beschuldigen"),
                  Entry("nocere", "schaden"), Entry("abire, abeo", "weggehen"),
                  Entry("uter/utra/utrum", "welcher/welche/welches"), Entry("melior/melius", "besser")]

    Lektion_20 = [Entry("disputare", "erörtern, diskutieren"), Entry("adesse, adsum", "anwesend sein"),
                  Entry("quidam/quedam/quoddam", "ein"), Entry("philosophus, philosophi, n", "Philosoph"),
                  Entry("inferre, infero", "zufügen"), Entry("qua de causa", "weshalb"),
                  Entry("ita", "so"), Entry("doctrina, doctrinae, f", "Lehre"),
                  Entry("auris, auris, f", "Ohr"), Entry("ergo", "also, folglich"),
                  Entry("medius/-a/-um", "der/die/das mittlere"), Entry("ignotus/-a/-um", "unbekannt"),
                  Entry("nescire", "nicht wissen"), Entry("venerari, veneror", "verehren"),
                  Entry("demonstrare", "zeigen, beweisen"), Entry("quia", "weil"),
                  Entry("caelum, caeli, n", "Himmel"), Entry("habitare", "wohnen"),
                  Entry("templum, templi, n", "Tempel"), Entry("quasi", "wie, sozusagen"),
                  Entry("egere", "brauchen"), Entry("quamvis", "obwohl"),
                  Entry("unusquisque", "jeder einzelne"), Entry("poeta, poetae, m", "Dichter"),
                  Entry("aestimare", "schätzen"), Entry("simulacrum, simulacri, n", "Abbild"),
                  Entry("aurum, auri, n", "Gold"), Entry("argentum, argenti, n", "Silber"),
                  Entry("paenitentia, paenitentiae, f", "Reue"), Entry("scelus, sceleris, n", "Verbrechen"),
                  Entry("flagitium, flagiti, n", "Schande"), Entry("committere, committo", "zustande bringen"),
                  Entry("iudicare", "richten, beurteilen"), Entry("ut", "als, sobald"),
                  Entry("sunt qui", "manche")]

    Lektionen16bis20 = Lektion_16 + Lektion_17 + Lektion_18 + Lektion_19 + Lektion_20

    # weitere Lektion folgen... vielleicht ;)
