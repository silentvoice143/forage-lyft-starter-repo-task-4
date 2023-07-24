import unittest
from tyres.octoprime_tyres import OctoprimeTyres

class OctoprimeTest:
    def tyre_need_service(self):
        cartyres=[0.3,0.5,0.8,0.6]

        tyres=OctoprimeTyres(cartyres)
        self.assertFalse(tyres.needs_service())

if __name__ == '__main__':
    unittest.main()