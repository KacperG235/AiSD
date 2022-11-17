from typing import Callable


class ListaWpis:
    wart: float
    nast: 'ListaWpis'

    def __init__(self, wart, nast=None):
        self.wart = wart
        self.nast = nast

    def dodaj_po_nim(self, wart: float) -> None:
        temp = ListaWpis(wart)
        if self.nast is None:
            self.nast = temp
            temp.nast = self
        else:
            temp.nast = self.nast
            self.nast = temp


class Lista_1k_k:
    element: 'ListaWpis'
    dlugosc: int

    def __init__(self, element: 'ListaWpis' = None, dlugosc=0):
        self.element = element
        self.dlugosc = dlugosc

    def pobierz_el(self, idx: int) -> 'ListaWpis':
        i = 0
        temp = self.element
        if idx == 0:
            return temp
        else:
            while i < idx-1:
                i += 1
                temp = temp.nast
            return temp

    #def odwroc(self) -> 'Lista_1k_k':
        #nowa = Lista_1k_k()

    def zlicz_mniejsze(self, prog: float) -> int:
        temp = self.element
        i = 0
        if self.element.wart < prog:
            i += 1
        while temp.nast != self.element:
            temp = temp.nast
            if temp.wart < prog:
                i += 1
        return i

    '''def obrob_wartosci(self, funkcja: Callable[[float], None]) -> None:
        temp = self.element
        funkcja(temp.wart)
        while temp.nast != self.element:
            temp = temp.nast
            funkcja(temp.wart)'''

    def przekrec(self) -> None:
        temp1 = self.element
        temp2 = temp1.nast
        self.element = temp2

    def czy_posortowane(self) -> bool:
        if self.element is None:
            return True
        temp = self.element
        if self.element.wart <= temp.nast.wart:
            return False
        while temp.nast != self.element:
            temp = temp.nast
            if temp.wart <= temp.nast.wart:
                return False
        return True

    def print(self) -> None:
        temp = self.element
        print('')
        print(temp.wart, end='->')
        while temp.nast != self.element:
            temp = temp.nast
            print(temp.wart, end='->')

def razy_2(cos):
    print(2 * cos)

def main():
    elem = ListaWpis(1)
    lista = Lista_1k_k(elem)
    lista.element.dodaj_po_nim(2)
    lista.element.nast.dodaj_po_nim(1)
    print(lista.zlicz_mniejsze(4))
    lista.print()
    lista.przekrec()
    lista.print()
    print(lista.czy_posortowane())


if __name__ == '__main__':
    main()
