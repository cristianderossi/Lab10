from database.DB_connect import DBConnect



class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """


     def get_filiali(self):

         cnx=DBConnect.get_connection()
         result=[]

         if cnx is  None:
            print('database non trovato')

            return None
         cursor = cnx.cursor()

         try:

             query = "select * from filiali"

             cursor.execute(query)

             result=cursor.fetchall()
             return result

         finally:
             cursor.close()
             cnx.close()












