from typing import overload
from typing import Any, Optional

class result:
    def __init__(self) -> None:
        #(valor que o motoboy cobra, loja de exclusividade)
        self.motoboys = [(2,5), (2,5), (2,5), (2,0), (3,5)]
        ###############1111111111111111111111111###222222222222222222222222222222222222##3333333333333333333333333333333##
        self.lojas = [[(50, 5), (50, 5), (50, 5)], [(50, 5), (50, 5), (50, 5), (50, 5)], [(50, 15), (50, 15), (100, 15)]]
        self.table = {0: [], 1: [], 2: [], 3: [], 4: []}
        self.no =[]

    def search_exclusive(self, loja):
        for x in range(len(self.motoboys)):
            if self.motoboys[x][1] == loja:
                return x
        return 0

    @overload
    def calc(self) -> None:    
        pass

    @overload
    def calc(self, i: Any) -> None:
        pass

    def calc(self, i: Optional[Any] = None) -> None:
        for x in range(len(self.lojas)):
            count = 0
            for y in self.lojas[x]:
                search = self.search_exclusive(x)
                if search != 0 and search not in self.no:
                    sum = ((y[0] * y[1]) / 100) + self.motoboys[search][0]
                    self.table[search].append((sum, x))
                    self.no.append(search)
                    #print('A: ', sum, '    moto: ', search, '  loja: ', x)
                else:
                    sum = ((y[0] * y[1]) / 100) + self.motoboys[count][0]
                    self.table[count].append((sum, x))
                    self.no.append(count)
                    #print('B: ', sum, '    moto: ', count, '  loja: ', x)
                    count+=1
                        
            self.no.clear()    
        if not i: 
            for x in range(1, 6):
                print('MOTOBOY ', x)
                print('Quantidade de pedidos: ', len(self.table[x-1]))
                print('Lojas atendidas: ', end=' ')
                for y in self.table[x-1]:
                    print(y[1]+1, end=' ')
                print()
                print('Lucros R$: ', end=' ')
                for y in self.table[x-1]:
                    print(y[0], end=' ')
                print()
                sum = 0
                for y in self.table[x-1]:
                    sum+= y[0]
                print('Lucro total R$: ', sum)
                print()
        else:
            print('MOTOBOY ', i)
            print('Quantidade de pedidos: ', len(self.table[i-1]))
            print('Lojas atendidas: ', end=' ')
            for y in self.table[i-1]:
                print(y[1]+1, end=' ')
            print()
            print('Lucros R$: ', end=' ')
            for y in self.table[x-1]:
                print(y[0], end=' ')
            print()
            sum = 0
            for y in self.table[i-1]:
                sum+= y[0]
            print('Lucro total: ', sum)
            print()
    

if __name__ == '__main__':
    
    x = result()

    x.calc(4) #calc(informar ou não o motoboy)