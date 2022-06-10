import unittest
from practicatdd import Contador

class Test_contador(unittest.TestCase):
        #Primer test
    def test1(self):
        # condicion inicial
        contador1 = Contador(0, 2, 5, 0)
        # verificar
        self.assertEqual(contador1.__inicio__(), 0)
        self.assertEqual(contador1.__incremento__(), 2)
        self.assertEqual(contador1.__limite__(), 5)
    def test2(self):
        #Segundo test
        variable = 3
        contador2 = Contador(0, 1, variable, 0)
        self.assertEqual(contador2.__inicio__(), 0)
        self.assertEqual(contador2.__incremento__(), 1)
        self.assertEqual(contador2.__limite__(), variable)
    def test3(self):
        #Tercer test
        contador3 = Contador(inicial=0, incremento=2, limite=4)
        self.assertEqual(contador3.__inicio__(), 0)
        self.assertEqual(contador3.__incremento__(), 2)
        self.assertEqual(contador3.__limite__(), 4)
    def test4(self):
        #Cuarto test
        contador4 = Contador(inicial=0, incremento=1, limite=4)
        
        contador4.__incrementar__()
        contador4.__incrementar__()
        contador4.__incrementar__()
        contador4.__incrementar__()
    def test5(self):
        #Cuarto test
        contador5 = Contador(inicial=0, incremento=1, limite=4)
        
        contador5.__incrementar__()
        contador5.__incrementar__()
        contador5.__incrementar__()
        contador5.__incrementar__()
        contador5.__incrementar__()

if __name__=="__main__":
    unittest.main()