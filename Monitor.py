#!/bin/python
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk
import threading
import requests
import time
from Active import Active
from Card import Card

########################################################
actives = []
actives.append(Active("CIEL3.SA", 8.16, 1))
actives.append(Active("ABCB4.SA", 18.30, 10))
actives.append(Active("FIIB11.SA", 525.01, 1))
actives.append(Active("MGLU3.SA", 33.48, 10))
actives.append(Active("TIET11.SA", 12.06, 10))
#actives.append(Active("TIET11.SA", 12.03, 10))
actives.append(Active("UNIP6.SA", 31.68, 10))
actives.append(Active("WIZS3.SA", 11.49, 10))
actives.append(Active("TUPY3.SA", 17.76, 10))
actives.append(Active("OIBR4.SA", 1.6  ,81))

class MainWindow:
    def __init__(self):
         # Inicia o Gtk e seta layout
        self.builder = Gtk.Builder()
        self.builder.add_from_file('MainWindow.glade')
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("mainWindow")
        self.flow = self.builder.get_object("mainFlow")

        column = 0
        line = 0
        self.cards = []
        for ative in actives:
            card = Card(ative)
            self.cards.append(card)
            self.flow.add(card.get_grid())

        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)

    def __del__(self):
        for card in self.cards:
            card.stop()


if __name__ == '__main__':
    mv = MainWindow()
    Gtk.main()

