from __future__ import annotations
from dataclasses import dataclass
from pessoa import Pessoa

@dataclass
class No:
    elemento: Pessoa
    altura: int = 0
    filhoEsq: No | None = None
    filhoDir: No | None = None

class AVL:
    " Representa uma árvore AVL"
    def __init__(self):
        self.raiz: No | None = None

    def vazia(self):
        return self.raiz == None
    
    # calcula o FB do nó
    def _fb(self, no: No) -> int:
        if no == None:
            return 0
        altSAE = -1
        altSAD = -1
        if no.filhoEsq != None:
            altSAE = no.filhoEsq.altura
        if no.filhoDir != None:
            altSAD = no.filhoDir.altura
        return altSAD - altSAE

    # atualiza a altura do nó
    def _atualizaAltura(self, no: No) -> None:
        if no != None:
            altSAE = -1
            altSAD = -1
            if no.filhoEsq != None:
                altSAE = no.filhoEsq.altura
            if no.filhoDir != None:
                altSAD = no.filhoDir.altura
            no.altura = max(altSAE, altSAD) + 1

    # faz rotação simples para a esquerda
    def _rotacionaEsq(self, pai: No) -> No:
        if pai == None:
            raise ValueError('Referência inválida')
        filho = pai.filhoDir
        pai.filhoDir = filho.filhoEsq
        filho.filhoEsq = pai
        self._atualizaAltura(pai)
        self._atualizaAltura(filho)
        return filho
    
    # faz rotação simples para a direita
    def _rotacionaDir(self, pai: No) -> No:
        if pai == None:
            raise ValueError('Referência inválida')
        filho = pai.filhoEsq
        pai.filhoEsq = filho.filhoDir
        filho.filhoDir = pai
        self._atualizaAltura(pai)
        self._atualizaAltura(filho)
        return filho
    
    # faz o balanceamento do nó
    def _balanceia(self, no: No) -> No | None:
        if no != None:
            # desbalanceado para a direita
            if self._fb(no) == 2:
                if self._fb(no.filhoDir) == -1:
                    no.filhoDir = self._rotacionaDir(no.filhoDir) 
                # rotaciona para a esquerda
                no = self._rotacionaEsq(no)
            # desbalanceado para a esquerda
            elif self._fb(no) == -2:
                if self._fb(no.filhoEsq) == 1:
                    no.filhoEsq = self._rotacionaEsq(no.filhoEsq)
                # rotaciona para a direita
                no = self._rotacionaDir(no)
        return no

    def insere(self, elem: Pessoa) -> None:
        self.raiz = self._insereNo(elem, self.raiz)

    def _insereNo(self, elem: Pessoa, raiz: No) -> No:
        if raiz == None:
            raiz = No(elem)
        else:
            if elem.nome < raiz.elemento.nome:
                raiz.filhoEsq = self._insereNo(elem, raiz.filhoEsq)            
            elif elem.nome > raiz.elemento.nome:
                raiz.filhoDir = self._insereNo(elem, raiz.filhoDir)
            # rebalanceando
            self._atualizaAltura(raiz)
            raiz = self._balanceia(raiz)
        return raiz
    
    def remove(self, elem: Pessoa) -> None:
          self.raiz = self._removeNo(elem, self.raiz)
     
    def _removeNo(self, elem: Pessoa, raiz: No) -> No | None:
        if raiz != None:
            if elem.nome < raiz.elemento.nome:
                raiz.filhoEsq = self._removeNo(elem, raiz.filhoEsq)
            elif elem.nome > raiz.elemento.nome:
                raiz.filhoDir = self._removeNo(elem, raiz.filhoDir)
            # elem está na raiz
            else:
                # raiz tem dois filhos
                if raiz.filhoEsq != None and raiz.filhoDir != None:
                    self._trocaSucessor(raiz)
                    raiz.filhoDir = self._removeNo(elem, raiz.filhoDir)
                # raiz tem um filho ou é folha
                elif raiz.filhoEsq != None:
                    raiz = raiz.filhoEsq
                else:
                    raiz = raiz.filhoDir
            # rebalanceando
            self._atualizaAltura(raiz)
            raiz = self._balanceia(raiz)
        return raiz
    
    # função auxiliar da remoção: troca o item do nó pelo do sucessor
    def _trocaSucessor(self, no: No) -> None:
        sucessor = no.filhoDir
        while (sucessor.filhoEsq != None):
            sucessor = sucessor.filhoEsq   
        no.elemento, sucessor.elemento = sucessor.elemento, no.elemento

    def exibe(self) -> None:
        self._exibeNo(self.raiz)
        print()
    
    def _exibeNo(self, raiz: No) -> None:
        if raiz != None:
            print('(', end='')
            self._exibeNo(raiz.filhoEsq)
            print(' ', raiz.elemento.nome, ' ', end='')
            self._exibeNo(raiz.filhoDir)
            print(')', end='')

    def busca(self, elem: Pessoa) -> No | None:
        return self._buscaNo(elem, self.raiz)
    
    # Método de busca binária modificado para pesquisar pelo nome, e não pelo objeto Nó
    def _buscaNo(self, elem: Pessoa, raiz: No) -> No | None:
        if raiz != None:
            if elem.nome == raiz.elemento.nome:
                return raiz
            elif elem.nome < raiz.elemento.nome:
                return self._buscaNo(elem, raiz.filhoEsq)
            else:
                return self._buscaNo(elem, raiz.filhoDir)
        else:
            return None
        
    def _visitaNo (self, no: No) -> Pessoa:
        print(no.elemento.nome)
        return no.elemento
        
    def _percorreInOrdem(self, raiz: No) -> list:
        if raiz != None:
            if raiz.filhoEsq != None:
                self._percorreInOrdem(raiz.filhoEsq)
            pessoas = []
            pessoas.append(raiz)
            if raiz.filhoDir!= None:
                self._percorreInOrdem(raiz.filhoDir)
            return pessoas

    def percorreArvoreInOrdem(self) -> list:
        pessoas = self._percorreInOrdem(self.raiz)
        return pessoas