class Car:
    sales = 0
    cc = 1000
    def __init__(self):
        Car.sales += 1
        self.item = dict()
    def desc(self):
        print(f'배기량: {Car.cc}')
        print(f'전체 판매대수: {Car.sales}')
    def customize(self, **kwargs):
        for k,v in kwargs.items():
            self.item[k] = v

class Sedan(Car):
    cc = 3500
    def desc(self):
        print(f'배기량: {Sedan.cc}')
        for k,v in self.item.items():
            print(f'{k}:{v}', end = ' ')
        if self.item:
            print()
        print(f'전체 판매대수: {Sedan.sales}')

if __name__=='__main__':
    c1 = Car()
    c1.desc()
    c1.customize(aircon=True)
    c1.desc()
    s1 = Sedan()
    s1.desc()
    s1.customize(cc=4000)
    s1.desc()
