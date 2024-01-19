from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    valor: str

@dataclass
class No:
    elemento: Item | None
    proximo: No | None = None 


class ListaLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None
    

    def vazia(self):
        return self.inicio == None
    
    
    def tamanho(self) -> int:
        p = self.inicio
        tam = 0
        while p != None:
            tam += 1
            p = p.proximo
        return tam
    

    def primeiro(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.inicio
    

    def ultimo(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.fim
    
    
    def exibe(self) -> None:
        print('Lista: inicio --> [', end='')
        p = self.inicio
        while p != None:
            print(p.elemento.valor, end='')
            p = p.proximo
            if p != None: 
                print(', ', end='')
        print('] <-- fim')
    
    
    def busca(self, elem: Item) -> No | None:
        p = self.inicio
        while p != None and p.elemento.valor != elem.valor:
            p = p.proximo
        return p


    def buscaPos(self, pos: int) -> No:
        if pos < 0 or pos >= self.tamanho():
            raise ValueError('Posição inválida')
        i = 0
        p = self.inicio
        while p != None and i < pos:
            i += 1
            p = p.proximo
        return p
    

    def insereFim(self, elem: Item) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        novo = No(elem)
        if self.vazia():
            self.inicio = novo
        else:
            self.fim.proximo = novo
        self.fim = novo
    

    def insereInicio(self, elem: Item) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        novo = No(elem)
        if self.vazia():
            self.fim = novo
        novo.proximo = self.inicio
        self.inicio = novo
    

    def inserePos(self, elem: Item, pos: int) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        tam = self.tamanho()
        if pos < 0 or pos > tam:
            raise ValueError('Posição inválida')
        # inserção no início da lista
        if pos == 0:
            self.insereInicio(elem)
        # inserção no fim da lista
        elif pos == tam:
            self.insereFim(elem)
        # inserção no meio da lista
        else:
            i = 1
            p = self.inicio.proximo
            while p != None and i < pos-1:
                p = p.proximo
                i += 1
            novo = No(elem)
            novo.proximo = p.proximo
            p.proximo = novo       


    def removeInicio(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.inicio
        self.inicio = self.inicio.proximo
        if self.vazia():
            self.fim = None
        removido.proximo = None


    def removeFim(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        if self.tamanho() == 1:
            self.inicio = None
            self.fim = None
        else:
            p = self.inicio
            anterior = None        
            while p != self.fim:
                anterior = p
                p = p.proximo
            anterior.proximo = None
            self.fim = anterior
        

    def removePos(self, pos: int) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        tam = self.tamanho()
        if pos < 0 or pos >= tam:
            raise ValueError('Posição inválida')
        # remoção no início da lista
        if pos == 0:
            self.removeInicio()
        # remoção no fim da lista
        elif pos == tam - 1:
            self.removeFim()
        # remoção no meio da lista
        else:
            i = 1
            anterior = self.inicio
            p = self.inicio.proximo
            while p != None and i < pos:
                anterior = p
                p = p.proximo
                i += 1
            anterior.proximo = p.proximo
            p.proximo = None


    def removeElemento(self, elem: Item) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.busca(elem)
        if removido == self.inicio:
            self.removeInicio()
        elif removido == self.fim:
            self.removeFim()
        else:
            anterior = self.inicio
            p = self.inicio.proximo
            while p != removido:
                anterior = p
                p = p.proximo
            anterior.proximo = p.proximo
            p.proximo = None


    def esvazia(self) -> None:
        self.inicio = None
        self.fim = None


class ListaLigadaSentinela:
    def __init__(self):
        self.inicio = No(None)
        self.fim = self.inicio

    def vazia(self) -> bool:
    	return self.inicio.proximo == None   

    def tamanho(self) -> int:
        p = self.inicio.proximo
        tam = 0
        while p != None:
            tam += 1
            p = p.proximo
        return tam

    def primeiro(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.inicio.proximo

    def ultimo(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.fim
     
    def exibe(self) -> None:
        print('Lista: inicio --> [', end='')
        p = self.inicio.proximo
        while p != None:
            print(p.elemento.valor, end='')
            if p != self.fim: 
                print(', ', end='')
            p = p.proximo
        print('] <-- fim')
    
    def busca(self, elem: Item) -> No | None:
        p = self.inicio.proximo
        while p != None and p.elemento.valor != elem.valor:
            p = p.proximo
        return p

    def buscaPos(self, pos: int) -> No:
        if pos < 0 or pos >= self.tamanho():
            raise ValueError('Posição inválida')
        i = 0
        p = self.inicio.proximo
        while p != None and i < pos:
            i += 1
            p = p.proximo
        return p
    
    def insereFim(self, elem: Item) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        novo = No(elem)
        self.fim.proximo = novo
        self.fim = novo
    
    def insereInicio(self, elem: Item) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        novo = No(elem)
        if self.vazia():
            self.fim = novo
        novo.proximo = self.inicio.proximo
        self.inicio.proximo = novo
    
    def inserePos(self, elem: Item, pos: int) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        tam = self.tamanho()
        if pos < 0 or pos > tam:
            raise ValueError('Posição inválida')
        # # inserção no fim da lista
        if pos == tam:
            self.insereFim(elem)
        # inserção no meio da lista
        else:
            i = 0
            p = self.inicio
            while p != None and i < pos:
                i += 1
                p = p.proximo
            novo = No(elem)
            novo.proximo = p.proximo
            p.proximo = novo

    def removeInicio(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.inicio.proximo
        self.inicio.proximo = removido.proximo
        if self.vazia():
            self.fim = self.inicio
        removido.proximo = None

    def removeFim(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        anterior = self.inicio
        p = self.inicio.proximo
        while p != self.fim:
            anterior = p
            p = p.proximo
        anterior.proximo = p.proximo
        self.fim = anterior
        
    def removePos(self, pos: int) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        tam = self.tamanho()
        if pos < 0 or pos >= tam:
            raise ValueError('Posição inválida')
        # remoção no fim da lista
        elif pos == tam - 1:
            self.removeFim()
        # remoção no meio da lista
        else:
            i = 0
            anterior = self.inicio
            p = self.inicio.proximo
            while p != None and i < pos:
                anterior = p
                p = p.proximo
                i += 1
            anterior.proximo = p.proximo
            p.proximo = None

    def removeElemento(self, elem: Item) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.busca(elem)
        
        if removido == self.fim:
            self.removeFim()
        else:
            anterior = self.inicio
            p = self.inicio.proximo
            while p != removido:
                anterior = p
                p = p.proximo
            anterior.proximo = p.proximo
            p.proximo = None

    def esvazia(self) -> None:
        self.inicio.proximo = None
        self.fim = self.inicio


class ListaLigadaCircular:
    def __init__(self):
        self.fim: No | None = None
  
    def vazia(self) -> bool:
        return self.fim == None
    
    def tamanho(self) -> int:
        tam = 0
        if self.vazia():
            return tam
        p = self.fim.proximo
        while p != self.fim:
            tam += 1
            p = p.proximo
        tam += 1
        return tam

    def primeiro(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.fim.proximo

    def ultimo(self) -> No:
        if self.vazia():
            raise ValueError('Lista vazia')
        return self.fim
     
    def exibe(self) -> None:
        print('Lista: inicio --> [', end='')
        if not self.vazia():
            p = self.fim.proximo
            while p != self.fim:
                print(p.elemento.valor, end='')
                print(', ', end='')
                p = p.proximo
            print(p.elemento.valor, end='')
        print('] <-- fim')

    def busca(self, elem: Item) ->  No | None:
        if self.vazia():
            return None
        p = self.fim.proximo
        while p != self.fim and p.elemento.valor != elem.valor:
            p = p.proximo
        if p.elemento.valor == elem.valor:
            return p
        return None
        
    def insereInicio(self, elem: Item) -> None:
        if self.busca(elem) != None:
            raise ValueError('Elemento repetido')
        novo = No(elem)
        if self.vazia():
            novo.proximo = novo
            self.fim = novo
        else:
            novo.proximo = self.fim.proximo
            self.fim.proximo = novo


    def insereFim(self, elem: Item) -> None:
        self.insereInicio(elem)
        self.fim = self.fim.proximo


    def removeInicio(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        removido = self.fim.proximo
        self.fim.proximo = removido.proximo
        if removido == self.fim:
            self.fim = None
        removido.proximo = None

    def removeFim(self) -> None:
        if self.vazia():
            raise ValueError('Lista vazia')
        if self.tamanho() == 1:
            self.fim = None
        else:
            anterior = self.fim
            p = self.fim.proximo
            while p != self.fim:
                anterior = p
                p = p.proximo
            anterior.proximo = self.fim.proximo
            self.fim.proximo = None
            self.fim = anterior
