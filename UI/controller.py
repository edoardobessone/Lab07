import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        biblioteche = self._model.get_biblioteche()
        if biblioteche is None:
            self._view.show_alert("❌ Errore di connessione al database.")
            return

        self._view.dd_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for biblioteca in biblioteche:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(biblioteca.nome))

        generi = self._model.get_generi()
        if generi is None:
            self._view.show_alert("❌ Errore di connessione al database.")
            return

        self._view.dd_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        for genere in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(genere))

    # CALLBACKS DROPDOWN
    def seleziona_biblioteca(self, e):
        valore = self._view.dd_biblioteca.value
        if valore == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = valore

    def seleziona_genere(self, e):
        valore = self._view.dd_genere.value
        if valore == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self, e):
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if libri is None:
            self._view.show_alert("❌ Errore di connessione al database.")
            return

        self._view.lista_libri.controls.clear()
        if len(libri) == 0:
            self._view.show_alert("Nessun libro soddisfa i criteri di filtraggio indicati.")
        else:
            for libro in libri:
                self._view.lista_libri.controls.append(ft.Text(f"{libro}"))

        self._view.update()