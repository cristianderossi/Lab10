import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_collegamenti(self, e):
        """
        Funzione che controlla prima se il valore dell'importo inserito sia valido (es. non deve essere una stringa) e
        poi popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Filiali presenti
        * Numero di Collegamenti
        * Lista di Collegamenti che superano l'importo indicato come soglia
        """
        # TODO

        testo = self._view.importo_medio_minimo.value
        if testo is None or testo.strip() == "":
            self._view.show_alert("Inserire un importo medio minimo.")
            return

        # 2. Converto in numero (accetto anche la virgola come separatore decimale)
        try:
            soglia = float(testo.replace(",", "."))
        except ValueError:
            self._view.show_alert("L'importo deve essere un numero (es. 300).")
            return

        if soglia < 0:
            self._view.show_alert("L'importo non può essere negativo.")
            return

        # 3. Faccio costruire il grafo al model
        self._model.costruisci_grafo(soglia)

        # 4. Mostro i risultati nella view
        self._view.lista_visualizzazione.controls.clear()

        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Filiali: {self._model.get_num_nodes()}"))
        self._view.lista_visualizzazione.controls.append(
            ft.Text(f"Numero di Collegamenti: {self._model.get_num_edges()}"))

        for i, (f1, f2, attr) in enumerate(self._model.get_all_edges(), start=1):
            self._view.lista_visualizzazione.controls.append(
                ft.Text(f"{i}) [{f1} -> {f2}] -- Importo medio per bonifico: € {attr['weight']:.2f}"))

        self._view.update()



