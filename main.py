# -*- coding: utf-8 -*-
# APP VERSION 1.6


########################################################################################


# python's module
import random
import webbrowser

# kivy's module
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivy.app import runTouchApp
from kivy.uix.image import Image

# meine module
from quiz import Quiz
from deklinationen import Deklinationen
from konjugationen import Konjugationen

########################################################################################


# farben im hintergrund
Window.clearcolor = get_color_from_hex("#162038")

# schriftarten registrieren
LabelBase.register(
    name="Roboto",
    fn_regular="./fonts/Roboto-Thin.ttf",
    fn_bold="./fonts/Roboto-Medium.ttf"
)


########################################################################################


class KivyLateinRoot(BoxLayout, Quiz, Deklinationen, Konjugationen):
    """
    Root aller Widgets.
    """
    quiz_screen = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(KivyLateinRoot, self).__init__(**kwargs)
        # screenliste
        self.screen_list = []
        self.quiz_popup = QuizPopup()

    def changeScreen(self, next_screen):

        if self.ids.screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.screen_manager.current)

        if next_screen == "about":
            self.ids.screen_manager.current = "about_screen"

        elif next_screen == "quiz":
            self.ids.screen_manager.current = "quiz_screen"

        elif next_screen == "vokabeln":
            self.ids.screen_manager.current = "vokabeln_screen"

        elif next_screen == "grammatik":
            self.ids.screen_manager.current = "grammatikauswahl_screen"

        elif next_screen == "statistiken":
            self.ids.screen_manager.current = "statistics_screen"

        elif next_screen == "lektionen":
            self.ids.screen_manager.current = "custom_quiz_screen"

        elif next_screen == "deklinationen":
            self.ids.screen_manager.current = "grammatik_screen"

        elif next_screen == "ppa":
            self.ids.screen_manager.current = "ppa_screen"

        elif next_screen == "konjugationen":
            self.ids.screen_manager.current = "konjugations_screen"

        elif next_screen == "info":
            self.ids.screen_manager.current = "info_screen"

    def onBackBtn(self):
        # kontrolliert ob es screens zum zurückgehen gibt
        if self.screen_list:
            # wenn es screens zum zurückgehen gibt, zurückgehen
            self.ids.screen_manager.current = self.screen_list.pop()
            # app nicht beenden
            return True
        # keine weiteren screens, app beenden
        return False


########################################################################################


class InfoScreen(Screen, Quiz):
    """
    Screen zum navigieren zwischen den Info - Screens.
    """

    def __init__(self, *args, **kwargs):
        super(InfoScreen, self).__init__(*args, **kwargs)


########################################################################################


class StatisticsScreen(Screen, Quiz, Deklinationen, Konjugationen):
    """
    Screen im Infomenü, der die App - Statistiken anzeigt.
    """

    def __init__(self, *args, **kwargs):
        super(StatisticsScreen, self).__init__(*args, **kwargs)
        self.stats_richtig = ObjectProperty(None)
        self.stats_falsch = ObjectProperty(None)
        self.insg = ObjectProperty(None)
        self.stats_richtig_gr = ObjectProperty(None)
        self.stats_falsch_gr = ObjectProperty(None)
        self.insggr = ObjectProperty(None)
        self.get_stats_update()

    def get_stats_update(self):
        with open("data/statistiken.txt") as rfile:
            lines = rfile.readlines()[0:5]
            # x bezeichnet richtige, y falsche antworten im Quiz
            # xgr bezeichnet richtige, ygr falsche antworten in der Grammatik
            x = lines[0]
            y = lines[1]
            xgr = lines[2]
            ygr = lines[3]

        e = int(x)
        d = int(y)
        g = int(d) + int(e)
        p = g / float(100)
        r = e / float(p)
        try:
            r = round(r, 2)
        except:
            pass
        self.stats_falsch = str((100 - r))
        self.stats_richtig = str(r)
        self.insg = str(g)
        self.stats_richtig = (self.stats_richtig + " " + "%")
        self.stats_falsch = (self.stats_falsch + " " + "%")

        e = int(xgr)
        d = int(ygr)
        g = int(d) + int(e)
        p = g / float(100)
        r = e / float(p)
        try:
            r = round(r, 2)
        except:
            pass
        self.stats_falsch_gr = str((100 - r))
        self.stats_richtig_gr = str(r)
        self.insggr = str(g)
        self.stats_richtig_gr = (self.stats_richtig_gr + " " + "%")
        self.stats_falsch_gr = (self.stats_falsch_gr + " " + "%")

    stats_richtig = ObjectProperty(None)
    stats_falsch = ObjectProperty(None)
    stats_richtig_gr = ObjectProperty(None)
    stats_falsch_gr = ObjectProperty(None)
    insg = ObjectProperty(None)
    insggr = ObjectProperty(None)


########################################################################################


class GrammatikauswahlScreen(Screen):
    """
    Screen für die Auswahl zwischen Konjugationen und Deklinationen.
    """
    pass


class KonjugationsauswahlScreen(Screen, Konjugationen):
    """
    Screen für die Auswahl zwischen verschiedenen Konjugationen und der PPA - Deklination.
    """
    pass


########################################################################################


class KonjugationsScreen(Screen, Konjugationen):
    """
    Screen für alle Konjugationen
    """

    def __init__(self, *args, **kwargs):
        super(KonjugationsScreen, self).__init__(*args, **kwargs)
        self.colorESG = ListProperty()
        self.colorZSG = ListProperty()
        self.colorDSG = ListProperty()
        self.colorEPL = ListProperty()
        self.colorZPL = ListProperty()
        self.colorDPL = ListProperty()
        self.colorESG = [1, 1, 1, 1]
        self.colorZSG = [1, 1, 1, 1]
        self.colorDSG = [1, 1, 1, 1]
        self.colorEPL = [1, 1, 1, 1]
        self.colorZPL = [1, 1, 1, 1]
        self.colorDPL = [1, 1, 1, 1]

    def check_kon(self, klasse, kon, akpa, esg, zsg, dsg, epl, zpl, dpl):
        false_color = [.8, 0, 0, 1]
        right_color = [0, .8, 0, 1]
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

        if esg == v[0]:
            self.colorESG = right_color
            self.richtig_kon()
        else:
            self.colorESG = false_color
            self.falsch_kon()
        if zsg == v[1]:
            self.colorZSG = right_color
            self.richtig_kon()
        else:
            self.colorZSG = false_color
            self.falsch_kon()
        if dsg == v[2]:
            self.colorDSG = right_color
            self.richtig_kon()
        else:
            self.colorDSG = false_color
            self.falsch_kon()
        if epl == v[3]:
            self.colorEPL = right_color
            self.richtig_kon()
        else:
            self.colorEPL = false_color
            self.falsch_kon()
        if zpl == v[4]:
            self.colorZPL = right_color
            self.richtig_kon()
        else:
            self.colorZPL = false_color
            self.falsch_kon()
        if dpl == v[5]:
            self.colorDPL = right_color
            self.richtig_kon()
        else:
            self.colorDPL = false_color
            self.falsch_kon()


########################################################################################


class PPAScreen(Screen, Konjugationen):
    """
    Screen für die PPA - Deklination.
    """

    def __init__(self, *args, **kwargs):
        super(PPAScreen, self).__init__(*args, **kwargs)
        self.colorN = ListProperty()
        self.colorG = ListProperty()
        self.colorD = ListProperty()
        self.colorA = ListProperty()
        self.colorAB = ListProperty()
        self.colorN = [1, 1, 1, 1]
        self.colorG = [1, 1, 1, 1]
        self.colorD = [1, 1, 1, 1]
        self.colorA = [1, 1, 1, 1]
        self.colorAB = [1, 1, 1, 1]

    def check_kon(self, kon, N, G, D, AKK, ABL):
        false_color = [.8, 0, 0, 1]
        right_color = [0, .8, 0, 1]
        if kon == "PPA, m/f":
            if self.NOM == "ns":
                # Singular
                self.colorN = right_color
                self.richtig_kon()
                if G == self.PPAListSg[1]:
                    self.richtig_kon()
                    self.colorG = right_color
                else:
                    self.falsch_kon()
                    self.colorG = false_color
                if D == self.PPAListSg[2]:
                    self.richtig_kon()
                    self.colorD = right_color
                else:
                    self.falsch_kon()
                    self.colorD = false_color
                if AKK == self.PPAListSg[3]:
                    self.richtig_kon()
                    self.colorA = right_color
                else:
                    self.falsch_kon()
                    self.colorA = false_color
                if ABL == self.PPAListSg[4]:
                    self.richtig_kon()
                    self.colorAB = right_color
                else:
                    self.falsch_kon()
                    self.colorAB = false_color
            else:
                # Plural
                if N == self.PPAListPl[0]:
                    self.richtig_kon()
                    self.colorN = right_color
                else:
                    self.falsch_kon()
                    self.colorN = false_color
                if G == self.PPAListPl[1]:
                    self.richtig_kon()
                    self.colorG = right_color
                else:
                    self.falsch_kon()
                    self.colorG = false_color
                if D == self.PPAListPl[2]:
                    self.richtig_kon()
                    self.colorD = right_color
                else:
                    self.falsch_kon()
                    self.colorD = false_color
                if AKK == self.PPAListPl[3]:
                    self.richtig_kon()
                    self.colorA = right_color
                else:
                    self.falsch_kon()
                    self.colorA = false_color
                if ABL == self.PPAListPl[4]:
                    self.richtig_kon()
                    self.colorAB = right_color
                else:
                    self.falsch_kon()
                    self.colorAB = false_color


########################################################################################


class GrammatikScreen(Screen, Deklinationen):
    """
    Screen für die Deklinationen.
    """

    def __init__(self, *args, **kwargs):
        super(GrammatikScreen, self).__init__(*args, **kwargs)
        # farben der textfelder
        self.colorNS = ListProperty()
        self.colorNP = ListProperty()
        self.colorGS = ListProperty()
        self.colorGP = ListProperty()
        self.colorDS = ListProperty()
        self.colorDP = ListProperty()
        self.colorAKS = ListProperty()
        self.colorAKP = ListProperty()
        self.colorABS = ListProperty()
        self.colorABP = ListProperty()
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

    def printTxt(self, NS, NP, GS, GP, DS, DP, AKS, AKP, ABS, ABP):
        self.check_dek(NS, NP, GS, GP, DS, DP, AKS, AKP, ABS, ABP)


########################################################################################


class QuizPopup(Popup, Quiz):
    """
    Popup für Feedback im Quiz.
    """
    # feedback - text für das quiz
    GOOD = "{}"
    BAD = "{}, richtige Antwort: [b]{}[/b]"
    GOOD_LIST = "Ja! Super! Richtig! Korrekt! Perfekt! Genau! Bravo!".split()
    BAD_LIST = ["Nein", "Nicht ganz", "Fast", "Probier's nochmal", "Vielleicht klappt's nächstes mal", "Leider falsch"]

    message = ObjectProperty()
    wrapped_button = ObjectProperty()

    def __init__(self, *args, **kwargs):
        super(QuizPopup, self).__init__(*args, **kwargs)

    def open(self, correct):
        # wenn antwort = richtig, "schließen" button nicht sichtbar
        if correct:
            if self.wrapped_button in self.content.children:
                self.content.remove_widget(self.wrapped_button)
        # wenn antwort falsch, button on falls nicht sichtbar
        else:
            if self.wrapped_button not in self.content.children:
                self.content.add_widget(self.wrapped_button)

        self.message.text = self._prep_text(correct)

        # zeigt popup bei richtiger antwort für eine bestimmte zeit an
        super(QuizPopup, self).open()
        if correct:
            Clock.schedule_once(self.dismiss, 0.6)
            # wenn die antwort falsch ist, muss der benutzer das popup wegklicken

    def _prep_text(self, correct):
        # bereitet die feedback - nachricht vor ("bravo!", "sorry!" usw)
        if correct:
            index = random.randint(0, len(self.GOOD_LIST) - 1)
            return self.GOOD.format(self.GOOD_LIST[index])
        else:
            index = random.randint(0, len(self.BAD_LIST) - 1)
            quiz_screen = App.get_running_app().root.quiz_screen
            answer = quiz_screen.get_answer()
            return self.BAD.format(self.BAD_LIST[index], answer)


########################################################################################


class QuizScreen(Screen, Quiz):
    """
    Bildschirm mit Frage und Antwortmöglichkeiten (das Quiz).
    """
    result = ObjectProperty(None)

    def __init__(self, *args, **kwargs):
        super(QuizScreen, self).__init__(*args, **kwargs)
        self.lektionsstatusc = "Lektion 1"
        self.get_next()

    def Popitup(self):
        root = App.get_running_app().root
        self.answercheck()
        if self.result == "richtig":
            root.quiz_popup.open(True)
        elif self.result == "falsch":
            root.quiz_popup.open(False)
        else:
            print "Error Popup Antwortcheck"

    def beforec(self):
        if self.c == 2:
            self.c = 1
            self.statusc(1)
            self.get_next()
        elif self.c == 3:
            self.c = 2
            self.statusc(2)
            self.get_next()
        elif self.c == 4:
            self.statusc(3)
            self.c = 3
            self.get_next()
        elif self.c == 5:
            self.statusc(4)
            self.c = 4
            self.get_next()
        elif self.c == 51:
            self.c = 5
            self.statusc(5)
            self.get_next()
        elif self.c == 6:
            self.statusc(51)
            self.c = 51
            self.get_next()
        elif self.c == 7:
            self.statusc(6)
            self.c = 6
            self.get_next()
        elif self.c == 8:
            self.statusc(7)
            self.c = 7
            self.get_next()
        elif self.c == 9:
            self.statusc(8)
            self.c = 8
            self.get_next()
        elif self.c == 10:
            self.statusc(9)
            self.c = 9
            self.get_next()
        elif self.c == 61:
            self.statusc(10)
            self.c = 10
            self.get_next()
        elif self.c == 11:
            self.statusc(61)
            self.c = 61
            self.get_next()
        elif self.c == 12:
            self.statusc(11)
            self.c = 11
            self.get_next()
        elif self.c == 13:
            self.statusc(12)
            self.c = 12
            self.get_next()
        elif self.c == 14:
            self.statusc(13)
            self.c = 13
            self.get_next()
        elif self.c == 15:
            self.statusc(14)
            self.c = 14
            self.get_next()
        elif self.c == 71:
            self.statusc(15)
            self.c = 15
            self.get_next()
        elif self.c == 16:
            self.statusc(71)
            self.c = 71
            self.get_next()
        elif self.c == 16:
            self.statusc(71)
            self.c = 71
            self.get_next()
        elif self.c == 17:
            self.statusc(16)
            self.c = 16
            self.get_next()
        elif self.c == 18:
            self.statusc(17)
            self.c = 17
            self.get_next()
        elif self.c == 19:
            self.statusc(18)
            self.c = 18
            self.get_next()
        elif self.c == 20:
            self.statusc(19)
            self.c = 19
            self.get_next()
        elif self.c == 81:
            self.statusc(20)
            self.c = 20
            self.get_next()
        else:
            self.statusc(81)
            self.c = 81
            self.get_next()

    def afterc(self):
        if self.c == 1:
            self.statusc(2)
            self.c = 2
            self.get_next()
        elif self.c == 2:
            self.c = 3
            self.statusc(3)
            self.get_next()
        elif self.c == 3:
            self.c = 4
            self.statusc(4)
            self.get_next()
        elif self.c == 4:
            self.c = 5
            self.statusc(5)
            self.get_next()
        elif self.c == 5:
            self.c = 51
            self.statusc(51)
            self.get_next()
        elif self.c == 51:
            self.c = 6
            self.statusc(6)
            self.get_next()
        elif self.c == 6:
            self.c = 7
            self.statusc(7)
            self.get_next()
        elif self.c == 7:
            self.c = 8
            self.statusc(8)
            self.get_next()
        elif self.c == 8:
            self.c = 9
            self.statusc(9)
            self.get_next()
        elif self.c == 9:
            self.c = 10
            self.statusc(10)
            self.get_next()
        elif self.c == 10:
            self.c = 61
            self.statusc(61)
            self.get_next()
        elif self.c == 61:
            self.c = 11
            self.statusc(11)
            self.get_next()
        elif self.c == 11:
            self.c = 12
            self.statusc(12)
            self.get_next()
        elif self.c == 12:
            self.c = 13
            self.statusc(13)
            self.get_next()
        elif self.c == 13:
            self.c = 14
            self.statusc(14)
            self.get_next()
        elif self.c == 14:
            self.c = 15
            self.statusc(15)
            self.get_next()
        elif self.c == 15:
            self.c = 71
            self.statusc(71)
            self.get_next()
        elif self.c == 71:
            self.c = 16
            self.statusc(16)
            self.get_next()
        elif self.c == 16:
            self.c = 17
            self.statusc(17)
            self.get_next()
        elif self.c == 17:
            self.c = 18
            self.statusc(18)
            self.get_next()
        elif self.c == 18:
            self.c = 19
            self.statusc(19)
            self.get_next()
        elif self.c == 19:
            self.c = 20
            self.statusc(20)
            self.get_next()
        elif self.c == 20:
            self.c = 81
            self.statusc(81)
            self.get_next()
        else:
            self.statusc(1)
            self.c = 1
            self.get_next()


########################################################################################


class VokabelnScreen(Screen, Quiz):
    """
    Bildschirm im ScrollView mit Vokabeln und Übersetzungen.
    """

    def __init__(self, **kwargs):
        super(VokabelnScreen, self).__init__(**kwargs)
        self.lektionstatus = "Lektion 1"
        self.ScrollLabels(1)
        self.status = 1

    def before(self):
        if self.status == 1:
            self.status = 20
            self.ScrollLabels(20)
        elif self.status == 2:
            self.status = 1
            self.ScrollLabels(1)
        elif self.status == 3:
            self.status = 2
            self.ScrollLabels(2)
        elif self.status == 4:
            self.status = 3
            self.ScrollLabels(3)
        elif self.status == 5:
            self.status = 4
            self.ScrollLabels(4)
        elif self.status == 6:
            self.status = 5
            self.ScrollLabels(5)
        elif self.status == 7:
            self.status = 6
            self.ScrollLabels(6)
        elif self.status == 8:
            self.status = 7
            self.ScrollLabels(7)
        elif self.status == 9:
            self.status = 8
            self.ScrollLabels(8)
        elif self.status == 10:
            self.status = 9
            self.ScrollLabels(9)
        elif self.status == 11:
            self.status = 10
            self.ScrollLabels(10)
        elif self.status == 12:
            self.status = 11
            self.ScrollLabels(11)
        elif self.status == 13:
            self.status = 12
            self.ScrollLabels(12)
        elif self.status == 14:
            self.status = 13
            self.ScrollLabels(13)
        elif self.status == 15:
            self.status = 14
            self.ScrollLabels(14)
        elif self.status == 15:
            self.status = 14
            self.ScrollLabels(14)
        elif self.status == 16:
            self.status = 15
            self.ScrollLabels(15)
        elif self.status == 17:
            self.status = 16
            self.ScrollLabels(16)
        elif self.status == 18:
            self.status = 17
            self.ScrollLabels(17)
        elif self.status == 19:
            self.status = 18
            self.ScrollLabels(18)
        elif self.status == 20:
            self.status = 19
            self.ScrollLabels(19)

    def after(self):
        if self.status == 1:
            self.status = 2
            self.ScrollLabels(2)
        elif self.status == 2:
            self.status = 3
            self.ScrollLabels(3)
        elif self.status == 3:
            self.status = 4
            self.ScrollLabels(4)
        elif self.status == 4:
            self.status = 5
            self.ScrollLabels(5)
        elif self.status == 5:
            self.status = 6
            self.ScrollLabels(6)
        elif self.status == 6:
            self.status = 7
            self.ScrollLabels(7)
        elif self.status == 7:
            self.status = 8
            self.ScrollLabels(8)
        elif self.status == 8:
            self.status = 9
            self.ScrollLabels(9)
        elif self.status == 9:
            self.status = 10
            self.ScrollLabels(10)
        elif self.status == 10:
            self.status = 11
            self.ScrollLabels(11)
        elif self.status == 11:
            self.status = 12
            self.ScrollLabels(12)
        elif self.status == 12:
            self.status = 13
            self.ScrollLabels(13)
        elif self.status == 13:
            self.status = 14
            self.ScrollLabels(14)
        elif self.status == 14:
            self.status = 15
            self.ScrollLabels(15)
        elif self.status == 15:
            self.status = 16
            self.ScrollLabels(16)
        elif self.status == 16:
            self.status = 17
            self.ScrollLabels(17)
        elif self.status == 17:
            self.status = 18
            self.ScrollLabels(18)
        elif self.status == 18:
            self.status = 19
            self.ScrollLabels(19)
        elif self.status == 19:
            self.status = 20
            self.ScrollLabels(20)
        elif self.status == 20:
            self.status = 1
            self.ScrollLabels(1)


########################################################################################


class AboutScreen(Screen, Quiz):
    """
    Info Screen der App, inklusive How-to-Bilder.
    """
    def __init__(self, **kwargs):
        super(AboutScreen, self).__init__(**kwargs)

    def display_help_screen(self):
        # zeigt die how to bilder an
        image = Image(source="images/help4.png")
        help_screen1 = Popup(title="How to",
                             attach_to=self,
                             size_hint=(0.98, 0.98),
                             content=image)
        image.bind(on_touch_down=help_screen1.dismiss)
        help_screen1.open()
        image = Image(source="images/help3.png")
        help_screen2 = Popup(title="How to",
                             attach_to=self,
                             size_hint=(0.98, 0.98),
                             content=image)
        image.bind(on_touch_down=help_screen2.dismiss)
        help_screen2.open()
        image = Image(source="images/help2.png")
        help_screen3 = Popup(title="How to",
                             attach_to=self,
                             size_hint=(0.98, 0.98),
                             content=image)
        image.bind(on_touch_down=help_screen3.dismiss)
        help_screen3.open()
        image = Image(source="images/help1.png")
        help_screen4 = Popup(title="How to",
                             attach_to=self,
                             size_hint=(0.98, 0.98),
                             content=image)
        image.bind(on_touch_down=help_screen4.dismiss)
        help_screen4.open()


########################################################################################


class KivyLateinApp(App):
    """
    App Objekt.
    """

    def __init__(self, **kwargs):
        super(KivyLateinApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackBtn)

    def on_pause(self):
        return True

    def on_resume(self):
        pass

    def onBackBtn(self, window, key, *args):
        # wenn benutzer back button drückt
        if key == 27:
            return self.root.onBackBtn()
            # führt root.onBackBtn aus

    def build(self):
        self.icon = "icon.jpg"
        return KivyLateinRoot()

    def getPlaystorelink(self):
        return ("Wenn dir diese App gefällt, [b][ref=playstore]bewerte sie![/ref][/b]")

    def getText(self):
        return ("Hey!\n"
                "Diese App wurde mit "
                "[b][ref=kivy]Kivy[/ref][/b]"
                " geschrieben.\n"
                "Hier geht's zum [b][ref=github]Quellcode.\n[/ref][/b]"
                "Die Vokabeln basieren auf den Lektionen von Cursus Brevis.\n"
                "Bitte hilf mit, diese App zu verbessern, und melde Fehler oder "
                "sonstige Probleme an [b][ref=email]snowball27.info@gmail.com[/b].\n"
                "\n"
                "Version: 1.6")

    def on_ref_press(self, instance, ref):
        _dict = {
            "kivy": "http://www.kivy.org/#home",
            "github": "https://github.com/snowball27/Lateintrainer",
            "email": "https://snowball27.info@gmail.com",
            "playstore": "https://play.google.com/store/apps/details?id=org.lateintrnr.lateintrainer2"
        }

        webbrowser.open(_dict[ref])


########################################################################################

if __name__ == "__main__":
    runTouchApp(KivyLateinApp().run())
