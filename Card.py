import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk
import threading
import time
import Active

class Card:
    def refresh_thread(self):
        while self.running:
            self.ative.refresh()
            self.set_values()
            self.get_grid()
            time.sleep(5)

###############################################################################
    def stop(self):
        self.running = False
###############################################################################
    def get_grid(self):
        return self.grid

###############################################################################
    def set_values(self):
        try:
            labels = []
            nome = self.builder.get_object("nome")
            nome.set_label(self.ative.name)

            valor_atual = self.builder.get_object("valorAtual")
            valor_atual.set_label(str(round(self.ative.actual_value,2)))
            labels.append(valor_atual)

            valor_compra = self.builder.get_object("valorCompra")
            valor_compra.set_label(str(round(self.ative.buy_val,2)))
            labels.append(valor_compra)

            quantidade = self.builder.get_object("quantidade")
            quantidade.set_label(str(round(self.ative.quantity,2)))
            labels.append(quantidade)

            total  = self.builder.get_object("valorTotal")
            total.set_label(str(round(self.ative.quantity * self.ative.actual_value,2)))
            labels.append(total)

            diferenca = self.builder.get_object("diferenca")
            diferenca.set_label(str(round(self.ative.stonk,2)))
            labels.append(diferenca)
            
            diferencaPorCento = self.builder.get_object("diferencaPorCento")
            diferencaPorCento.set_label(str(round(self.ative.percent_stonk*100,2)))
            labels.append(diferencaPorCento)

            for label in labels:
                if self.ative.stonk >= 0:
                    color = Gdk.color_parse("green")
                else:
                    color = Gdk.color_parse("red")

                rgba = Gdk.RGBA.from_color(color)
                label.override_background_color(0, rgba)
        except:
            print("Erro atualizando " + self.ative.name)

###############################################################################
    def __init__(self,ative):
        self.running = True
        self.ative = ative

        self.builder  = Gtk.Builder()
        self.builder.add_from_file("Card.glade")
        self.builder.connect_signals(self)
        self.grid = self.builder.get_object("mainGrid")
        self.set_values()
        self.refresh_thread = threading.Thread(target=self.refresh_thread, args=())
        self.refresh_thread.start()
###############################################################################
    def __del__(self):
        self.running = False

