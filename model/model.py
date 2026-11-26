from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutte le Filiali (i nodi) presenti e filtrando i Collegamenti con
        importo medio per bonifico >= threshold (euro)
        """
        # TODO

        if self.G is None:
            self.G= nx.Graph()

        self.G.clear()


        self._nodes=DAO.get_filiali()
        self.G.add_nodes_from(self._nodes)


        id_map={f.id:f  for f in self._nodes}

        self._edges=DAO.get_filiale_edges()

        for row in self._edges:

            media=float(row['media'])

            if media >= threshold:
                f1=id_map[row['id_f1']]
                f2=id_map[row['id_f2']]
                self.G.add_edge(f1,f2,weight=media)


    def get_num_edges(self):
        """
        Restituisce il numero di Collegamenti (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO

        return self.G.number_of_edges()

    def get_num_nodes(self):
        """
        Restituisce il numero di Filiali (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO

        return self.G.number_of_nodes()





    def get_all_edges(self):
        """
        Restituisce tutti i Collegamenti (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO

        return self.G.edges()




