from typing_extensions import self
import unittest

from practicatdd import Contador

class Test_contador(unittest.TestCase):
        #Primer test
    def test1(self):
        # condicion inicial
        contador1 = Contador(0, 2, 5)
        # verificar
        self.assertEqual(contador1.inicial, 0)
        self.assertEqual(contador1.incremento, 2)
        self.assertEqual(contador1.limite, 5)

if __name__=="__main__":
    unittest.main()