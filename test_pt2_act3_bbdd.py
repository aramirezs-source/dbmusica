import unittest
import os
import shutil
import sqlite3

from pt2_act3_bbdd import crear_taula, afegir_grup, mostrar_grups,actualitzar_grup, eliminar_grup

# Rutes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_ORIGINAL = os.path.join(BASE_DIR, "grups_musica.db")
DB_TEST = os.path.join(BASE_DIR, "grups_test.db")

class TestGestorGrups(unittest.TestCase):

    def setUp(self):
        """Guarda una còpia de la base de dades original i configura el test amb la còpia."""
        if os.path.exists(DB_ORIGINAL):
            shutil.copy(DB_ORIGINAL, DB_TEST)
        else:
            raise FileNotFoundError(f"La base de dades original {DB_ORIGINAL} no existeix.")

        # Forcem el mòdul pt2_act3_bbdd a treballar amb la base de dades de test
        import pt2_act3_bbdd
        pt2_act3_bbdd.DB = DB_TEST

        # Obrim connexió per consultar dades
        self.conn = sqlite3.connect(DB_TEST)
        self.cursor = self.conn.cursor()

    def tearDown(self):
        """Restaura la base de dades original i elimina la de test."""
        self.conn.close()
        os.remove(DB_TEST)
    
    def test_mostrar_grups(self):
        """Comprova que després de l'execució de l'aplicació, la taula 'grups' conté dades, com el grup Txarango."""
        crear_taula()
        self.cursor.execute("SELECT * FROM grups WHERE nom_grup='Txarango'")
        resultat = self.cursor.fetchone()
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat[1], "Txarango")   

    def test_crear_taula(self):
        """Comprova que la taula 'grups' es crea correctament si no existeix."""
        self.cursor.execute("DROP TABLE IF EXISTS grups")
        self.conn.commit()

        crear_taula()

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='grups'")
        self.assertIsNotNone(self.cursor.fetchone())

    def test_afegir_grup(self):
        """Comprova que afegir un grup l'insereix a la base de dades."""
        crear_taula()
        afegir_grup("Test Grup", 2023, "Pop", 4)
        afegir_grup("Test Bis", 2025, "Folk", 5)

        self.cursor.execute("SELECT * FROM grups WHERE nom_grup='Test Grup'")
        resultat = self.cursor.fetchone()
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat[1], "Test Grup")

    def test_actualitzar_grup(self):
        """Comprova que actualitzar un grup modifica correctament les dades."""
        crear_taula()
        afegir_grup("Test Grup", 2023, "Pop", 4)
        actualitzar_grup("Test Grup", nou_nom_grup="Grup Actualitzat", any_inici=2024)

        self.cursor.execute("SELECT * FROM grups WHERE nom_grup='Grup Actualitzat'")
        resultat = self.cursor.fetchone()
        self.assertIsNotNone(resultat)
        self.assertEqual(resultat[1], "Grup Actualitzat")
        self.assertEqual(resultat[2], 2024)
        self.assertEqual(resultat[3], "Pop")
        self.assertEqual(resultat[4], 4)

    def test_eliminar_grup(self):
        """Comprova que eliminar un grup elimina correctament les dades de la base de dades."""
        crear_taula()
        afegir_grup("Test Grup", 2023, "Pop", 4)
        eliminar_grup("Test Grup")

        self.cursor.execute("SELECT * FROM grups WHERE nom_grup='Test Grup'")
        resultat = self.cursor.fetchone()
        self.assertIsNone(resultat)
        self.assertEqual(resultat, None)
        
if __name__ == "__main__":
    unittest.main()
