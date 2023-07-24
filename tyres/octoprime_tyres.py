from tyres.tyre import Tyres

class OctoprimeTyres(Tyres):
    def __intit__(self,cartyres):
        self._cart_tyres = cartyres
    

    def needs_service(self):
        sum:float
        for i in range (len(self.cartyres)):
            sum+=i
        
        if(sum>=3):
            return True
        else:
            return False
        