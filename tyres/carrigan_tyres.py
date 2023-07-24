from tyres.tyre import Tyres

class CarriganTyres(Tyres):
    def __init__(self,cartyres):
        self.cartyres=cartyres

    def needs_service(self):
        for it in self.cartyres:
            if(it>=0.9):
                return False
            else:
                return True