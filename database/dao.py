from unittest import result

from database.DB_connect import DBConnect
from model.filiale import Filiale


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """

    @staticmethod
    def get_filiali(self):

        cnx=DBConnect.get_connection()
        result=[]

        if cnx is  None:
            print('database non trovato')

            return None

        cursor = cnx.cursor(dictionary=True)

        try:

             query = "select * from filiale"

             cursor.execute(query)

             for row in cursor:
                 result.append(Filiale(**row))

             return result

        finally:
         cursor.close()
         cnx.close()


    def get_filiale_edges(self):
        #'importo medio dei bonifici effettuati in un collegamento:
        # ciò significa sommare l'importo (campo importo della tabella bonifico)
        # di tutti i bonifici tra due filiali, considerando sia la direzione A→B
        # sia la direzione B→A, e dividere questo totale per il
        # numero complessivo dei bonifici per quella coppia di filiali.

        cnx=DBConnect.get_connection()

        result=[]

        if cnx is None:
            print('database non trovato')
            return None

        cursor=cnx.cursor(dictionary=True)

        try:
            query =  """SELECT AVG(importo) as media ,b.id_filiale_origine ,b.id_filiale_destinazione
                     from bonifico b
                     where b.id_filiale_origine != b.id_filiale_destinazione
                     Group By b.id_filiale_destinazione ,b.id_filiale_origine"""


            cursor.execute(query)

            for row in cursor:

                result.append(Filiale(**row))

            return result

        finally:
            cursor.close()
            cnx.close()





















