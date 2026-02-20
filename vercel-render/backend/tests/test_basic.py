import unittest
import sys
import os

# Ajustamos el path para poder importar main.py que está en la carpeta superior
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app # Importamos la aplicación Flask desde main.py

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status(self):
        """Prueba que la ruta base devuelve 200"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_not_found(self):
        """Prueba de error 404 para rutas inexistentes (Test adicional)"""
        result = self.app.get('/ruta-falsa')
        self.assertEqual(result.status_code, 404)

if __name__ == "__main__":
    unittest.main()