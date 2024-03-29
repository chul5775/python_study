from abc import *

class Employee(metaclass = ABCMeta):
    def __init__(self,irum,nai):      
        self.irum = irum
        self.nai = nai
    
    @abstractmethod
    def data_print(self):
        pass
    
    @abstractmethod
    def pay(self):
        pass
    
    def irumnai_print(self):
        print('이름:' + self.irum + ', 나이:' + str(self.nai), end = ' ')
   
class Temporary(Employee):
    def __init__(self,irum,nai,ilsu,ildang):      
        Employee.__init__(self, irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
    
    def pay(self):
        return self.ilsu * self.ildang
        
    def data_print(self):
        self.irumnai_print()
        print('월급:{}'.format(self.pay()))
    
class Regular(Employee):
    def __init__(self,irum,nai,salary):      
        super().__init__(irum, nai)
        self.salary = salary
    
    def pay(self):
        return self.salary
      
    def data_print(self):
        self.irumnai_print()
        print('급여:{}'.format(self.pay()))
    
class Salesman(Regular):
    def __init__(self,irum,nai,salary,sales,commission):      
        super().__init__(irum, nai, salary)
        self.sales = sales
        self.commission = commission
    
    def pay(self):
        return super().pay() + (self.sales * self.commission)
    
    def data_print(self):
        self.irumnai_print()
        print('수령액:{}'.format(self.pay()))

def main():          
    t = Temporary('홍길동',25,20,150000)
    r = Regular('한국인',27,3500000)
    s = Salesman('손오공',29,1200000,5000000,0.25)
    t.data_print()
    r.data_print()
    s.data_print()

if __name__ == '__main__':
    main()



