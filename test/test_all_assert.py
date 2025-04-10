import unittest
import sys
import os

# Agregar la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
SERVER = "A"

class AllAssertsTest(unittest.TestCase):
    
    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("hola", "hola")
        
    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)
        
    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numro")
            
    def test_assert_in(self):
        self.assertIn(10, [12,11,10])
        self.assertNotIn(5, [12,11,10])
    
    def test_assert_dicts(self):
        user = {
                "first_name" : "David",
                "last_name" : "Lopez",
                "Age" : 33
            }
        self.assertDictEqual(
            {
                "first_name" : "David",
                "last_name" : "Lopez",
                "Age" : 33
            },user
        )
    
    @unittest.skip("Trabajo en progreso, sera habilidata despues de terminar los nuevos requerimientos")
    def test_skip(self):
        self.assertEqual("Hola", "Chao")
      
    @unittest.skipIf(SERVER == "B", "Saltada porque no esta en el servidor correcto")  
    def test_skip_if(self):
        self.assertEqual(2,2)     
    
    @unittest.expectedFailure
    def test_expected_error(self):
        self.assertEqual(11,12)