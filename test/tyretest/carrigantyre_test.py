import unittest
from tyres.carrigan_tyres import CarriganTyres

class CarriganTest:
    def tyre_need_service(self):
        cartyres=[0.9,0.5,1,0.6]

        tyres=CarriganTyres(cartyres)
        self.assertTrue(tyres.needs_service())

if __name__ == '__main__':
    unittest.main()