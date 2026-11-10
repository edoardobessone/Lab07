from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_biblioteche(self) -> list[Biblioteca] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM biblioteca"""
        cursor.execute(query)

        risultato = []
        for riga in cursor:
            biblioteca = Biblioteca(
                riga["id"],
                riga["nome"],
                riga["indirizzo"]
            )
            risultato.append(biblioteca)

        cursor.close()
        cnx.close()
        return risultato