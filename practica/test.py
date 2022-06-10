import unittest
from practicatdd import Contador

class Test_contador(unittest.TestCase):
        #Primer test
    def test1(self):
        # condicion inicial
        contador1 = Contador(0, 2, 5)
        # verificar
        self.assertEqual(contador1.inicio, 0)
        self.assertEqual(contador1.incremento, 2)
        self.assertEqual(contador1.limite, 5)
    def test2(self):
        #Segundo test
        variable = 3
        contador2 = Contador()
        self.assertEqual(contador2.inicio, 0)
        self.assertEqual(contador2.incremento, 1)
        self.assertEqual(contador2.limite, variable)
    def test3(self):
        #Tercer test
        contador3 = Contador(inicial=0, incremento=2, limite=4)

        self.assertEqual(contador3.inicio)
        self.assertEqual(contador3.incremento)
        self.assertEqual(contador3.limite)

if __name__=="__main__":
    unittest.main()