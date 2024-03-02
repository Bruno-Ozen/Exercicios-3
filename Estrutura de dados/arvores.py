from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Item:
     valor: str | int | float

@dataclass
class No:
     elemento: Item
     filhoEsq: No | None = None
     filhoDir: No | None = None

class AB:
     " Representa uma árvore binária"
     def __init__(self):
          self.raiz: No | None = None

     def vazia(self):
          return self.raiz == None

     def insereRaiz(self, elem: Item) -> bool:
          if self.vazia():
               self.raiz = No(elem)
               return True
          return False
    
     def insereNaEsq(self, elem: Item, pai: No) -> bool:
          if pai.filhoEsq == None:
               pai.filhoEsq = No(elem)
               return True
          return False

     def insereNaDir(self, elem: Item, pai: No) -> bool:
          if pai.filhoDir == None:
               pai.filhoDir = No(elem)
               return True
          return False
    
     def exibe(self) -> None:
          self._exibeNo(self.raiz)
          print()
    
     def _exibeNo(self, raiz: No) -> None:
          if raiz != None:
               print('(', end='')
               self._exibeNo(raiz.filhoEsq)
               print(' ', raiz.elemento.valor, ' ', end='')
               self._exibeNo(raiz.filhoDir)
               print(')', end='')

     def busca(self, elem: Item) -> No | None:
          return self._buscaNo(elem, self.raiz)
    
     def _buscaNo(self, elem: Item, raiz: No) -> No | None:
          if raiz != None:
               if raiz.elemento.valor == elem.valor:
                    return raiz
               no = self.buscaNo(elem, raiz.filhoEsq)
               if no != None:
                    return no
               return self.buscaNo(elem, raiz.filhoDir)
          return None
       
     def insereNaEsquerda(self, elem: Item, elemPai: Item) -> bool:
          pai = self.busca(elemPai)
          if pai != None:
               return self.insereNaEsq(elem, pai)
          return False
    
     def insereNaDireita(self, elem: Item, elemPai: Item) -> bool:
          pai = self.busca(elemPai)
          if pai != None:
               return self.insereNaDir(elem, pai)
          return False
     
     def altura(self) -> int:
          if self.vazia():
               raise ValueError('Árvore vazia')
          return self._alturaNo(self.raiz)

     def _alturaNo(self, raiz: No) -> int:
          if raiz == None:
               return -1
          return 1 + max(self._alturaNo(raiz.filhoEsq), self._alturaNo(raiz.filhoDir))
     
     # Possíveis valores para ordem: 
     # 0 = pré-ordem, 1 = in-ordem e 2 = pos-ordem
     def percorreArvore(self, ordem: int = 0) -> None:
          if ordem == 0:
               self._percorrePreOrdem(self.raiz)
          elif ordem == 1:
               self._percorreInOrdem(self.raiz)
          elif ordem == 2:
               self._percorrePosOrdem(self.raiz)
          else: 
               raise ValueError('Valor inválido para o parâmetro de ordem')
          print()
     
     def _percorrePreOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._visitaNo(raiz)
               self._percorrePreOrdem(raiz.filhoEsq)
               self._percorrePreOrdem(raiz.filhoDir)

     def _percorreInOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._percorreInOrdem(raiz.filhoEsq)
               self._visitaNo(raiz)
               self._percorreInOrdem(raiz.filhoDir)

     def _percorrePosOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._percorrePosOrdem(raiz.filhoEsq)
               self._percorrePosOrdem(raiz.filhoDir)
               self._visitaNo(raiz)

     def _visitaNo (self, no: No) -> None:
          print(no.elemento.valor, ' ', end='')
          

class ABB:
     " Representa uma árvore binária de busca"
     def __init__(self):
          self.raiz: No | None = None

     def vazia(self):
          return self.raiz == None
     
     def insere(self, elem: Item) -> None:
          self.raiz = self._insereNo(elem, self.raiz)

     def _insereNo(self, elem: Item, raiz: No) -> No | None:
          if raiz == None:
               raiz = No(elem)
          else:
               if elem.valor < raiz.elemento.valor:
                    raiz.filhoEsq = self._insereNo(elem, raiz.filhoEsq)            
               elif elem.valor > raiz.elemento.valor:
                    raiz.filhoDir = self._insereNo(elem, raiz.filhoDir)
          return raiz
     
     def busca(self, elem: Item) -> No | None:
          return self._buscaNo(elem, self.raiz)
    
     def _buscaNo(self, elem: Item, raiz: No) -> No | None:
          if raiz != None:
               if elem.valor == raiz.elemento.valor:
                    return raiz
               elif elem.valor < raiz.elemento.valor:
                    return self._buscaNo(elem, raiz.filhoEsq)
               else:
                    return self._buscaNo(elem, raiz.filhoDir)
          else:
               return None
    
     def remove(self, elem: Item) -> None:
          self.raiz = self._removeNo(elem, self.raiz)
     
     def _removeNo(self, elem: Item, raiz: No) -> No | None:
          if raiz != None:
               if elem.valor < raiz.elemento.valor:
                    raiz.filhoEsq = self._removeNo(elem, raiz.filhoEsq)
               elif elem.valor > raiz.elemento.valor:
                    raiz.filhoDir = self._removeNo(elem, raiz.filhoDir)
               # elem está na raiz
               else:
                    # raiz tem dois filhos
                    if raiz.filhoEsq != None and raiz.filhoDir != None:
                         sucessor = raiz.filhoDir
                         while (sucessor.filhoEsq != None):
                              sucessor = sucessor.filhoEsq
                         raiz.elemento, sucessor.elemento = sucessor.elemento, raiz.elemento
                         raiz.filhoDir = self._removeNo(elem, raiz.filhoDir)
                    # raiz tem um filho ou é folha
                    else:
                         if raiz.filhoEsq != None:
                              raiz = raiz.filhoEsq
                         else:
                              raiz = raiz.filhoDir
          return raiz          

     def exibe(self) -> None:
          self._exibeNo(self.raiz)
          print()
    
     def _exibeNo(self, no: No) -> None:
          if no != None:
               print('(', end='')
               self._exibeNo(no.filhoEsq)
               print(' ', no.elemento.valor, ' ', end='')
               self._exibeNo(no.filhoDir)
               print(')', end='')
     
     def altura(self) -> int:
          if self.vazia():
               raise ValueError('Árvore vazia')
          return self._alturaNo(self.raiz)

     def _alturaNo(self, raiz: No) -> int:
          if raiz == None:
               return -1
          return 1 + max(self._alturaNo(raiz.filhoEsq), self._alturaNo(raiz.filhoDir))
     
     # Possíveis valores para ordem: 
     # 0 = pré-ordem, 1 = in-ordem e 2 = pos-ordem
     def percorreArvore(self, ordem: int = 0) -> None:
          if ordem == 0:
               self._percorrePreOrdem(self.raiz)
          elif ordem == 1:
               self._percorreInOrdem(self.raiz)
          elif ordem == 2:
               self._percorrePosOrdem(self.raiz)
          else: 
               raise ValueError('Valor inválido para o parâmetro de ordem')
          print()
     
     def _percorrePreOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._visitaNo(raiz)
               self._percorrePreOrdem(raiz.filhoEsq)
               self._percorrePreOrdem(raiz.filhoDir)

     def _percorreInOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._percorreInOrdem(raiz.filhoEsq)
               self._visitaNo(raiz)
               self._percorreInOrdem(raiz.filhoDir)

     def _percorrePosOrdem(self, raiz: No) -> None:
          if raiz != None:
               self._percorrePosOrdem(raiz.filhoEsq)
               self._percorrePosOrdem(raiz.filhoDir)
               self._visitaNo(raiz)

     def _visitaNo (self, no: No) -> None:
          print(no.elemento.valor, ' ', end='')

     def string_ramo(self, n: No, nivel: int):
          s = ''
          s += '  '*nivel
          s += '|____'
          if n != None:
               s += str(n.elemento.valor) + '\n'
          else:
               s += '\n'
          if n != None:
               str_esq = self.string_ramo(n.filhoEsq,nivel+1)
               str_dir = self.string_ramo(n.filhoDir,nivel+1)
               s += str_esq + str_dir
          return s

     def string(self):
          return self.string_ramo(self.raiz, 0)
