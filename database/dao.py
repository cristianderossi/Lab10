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
















