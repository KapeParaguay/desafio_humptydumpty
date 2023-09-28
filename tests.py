import unittest
from desafio import humpty_dumpty

class TestHumptyDumpty(unittest.TestCase):
    
    def test_humpty_dumpty(self):
        # Prueba casos normales
        self.assertEqual(humpty_dumpty(15), [
            "1", "2", "Humpty", "4", "Humpty", "Humpty", "7", "8", "Humpty", "Humpty",
            "11", "Humpty", "13", "14", "Humpty Dumpty"])
        
        # Prueba con un numero pequeno
        self.assertEqual(humpty_dumpty(2), ["1", "2"])
        
        # Prueba con un numero negativo
        self.assertEqual(humpty_dumpty(-5), [])
        
        # Agrega mas casos de prueba segun sea necesar
        
if __name__=="main":
    unittest.main()