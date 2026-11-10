from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_libri_filtrati(self, biblioteca: str, genere: str) -> list[Libro] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT l.id, l.titolo, l.autore, l.genere, l.anno_pubblicazione, l.id_biblioteca
                   FROM libro l, biblioteca b
                   WHERE l.id_biblioteca = b.id
                   AND b.nome = COALESCE(%s, b.nome)
                   AND l.genere = COALESCE(%s, l.genere)"""
        cursor.execute(query, (biblioteca, genere))

        risultato = []
        for riga in cursor:
            libro = Libro(
                riga["id"],
                riga["titolo"],
                riga["autore"],
                riga["genere"],
                riga["anno_pubblicazione"],
                riga["id_biblioteca"]
            )
            risultato.append(libro)

        cursor.close()
        cnx.close()
        return risultato

    def get_generi(self) -> list[str] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT DISTINCT genere FROM libro"""
        cursor.execute(query)

        risultato = []
        for riga in cursor:
            risultato.append(riga["genere"])

        cursor.close()
        cnx.close()
        return risultato