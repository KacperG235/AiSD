from typing import Callable


class ListaWpis:
    wart: float
    nast: 'ListaWpis'
    lista: 'Lista_1k_k'

    def __init__(self, wart, nast: 'ListaWpis' = None, lista: 'Lista_1k_k' = None):
        self.wart = wart
        self.nast = nast
        self.lista = Lista_1k_k(self)

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
        while i < idx:
            i += 1
            temp = temp.nast
        return temp

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

    def obrob_wartosci(self, funkcja: Callable[[float], None]) -> None:
        temp = self.element
        funkcja(temp.wart)
        while temp.nast != self.element:
            funkcja(temp.wart)
            temp = temp.nast

    def przekrec(self) -> None:
        temp1 = self.element
        temp2 = temp1.nast
        self.element = temp2

    def czy_posortowane(self) -> bool:
        if self.element is None:
            return True
        temp = self.element
        if temp.wart >= temp.nast.wart:
            return False
        while temp.nast != self.element:
            if temp.wart >= temp.nast.wart:
                return False
            temp = temp.nast
            return True

    def print(self) -> None:
        temp = self.element
        print('')
        print(temp.wart, end='->')
        while temp.nast != self.element:
            temp = temp.nast
            print(temp.wart, end='->')


def test(cos: float) -> None:
    cos *= 2


def main():



if __name__ == '__main__':
    main()
