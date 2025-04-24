import unittest
from unittest.mock import patch
from io import StringIO
import sqlite3
import os

# Importar les funcions a provar
from gestor_grups import intro_dades, crear_taula, afegir_grup, mostrar_grups, DB

class TestGestorGrups(unittest.TestCase):

    def setUp(self):
        # Configura una base de dades temporal abans de cada test
        self.test_db = DB
        if os.path.exists(self.test_db):
            os.remove(self.test_db)
        crear_taula()

    @patch('builtins.input', side_effect=["Txarango", "2010", "Pop", "5"])
    def test_intro_dades_valida(self, mock_inputs):
        resultat = intro_dades()
        self.assertEqual(resultat, ("Txarango", 2010, "Pop", 5))

    @patch('builtins.input', side_effect=["", "abcd", "", "-1", "3"])
    def test_intro_dades_buida_o_invalida(self, mock_inputs):
        # Nom, any_inici, tipus, integrants amb errors que es repregunten
        with patch('builtins.input', side_effect=["Txarango", "2010", "Pop", "4"]):
            resultat = intro_dades()
            self.assertEqual(resultat, ("Txarango", 2010, "Pop", 4))

    def test_afegir_i_mostrar_grup(self):
        afegir_grup("Mishima", 1999, "Indie", 4)
        with patch('sys.stdout', new=StringIO()) as output:
            mostrar_grups()
            self.assertIn("Mishima", output.getvalue())
            self.assertIn("1999", output.getvalue())
            self.assertIn("Indie", output.getvalue())

if __name__ == '__main__':
    unittest.main()
