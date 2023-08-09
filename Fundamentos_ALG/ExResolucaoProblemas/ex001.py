''' EXERCÍCIO 1
1. Análise
	- Verificar a senha a partir da entrada do usuário, e retornar
	se a senha está correta, que é ser igual a "Giva123".

2. Definição dos tipos de dados
	- As informações serão definidas no tipo caractere para a senha
	e mensagem de sua validação.   
'''

# 3. Especificação:
def validaSenha(senha: str) -> str:
    '''Verifica a validade da senha comparando se o valor de entrada
        é igual a "Giva123".

        Exemplos:
        >>> validaSenha('dinossauro')
        'Senha incorreta. Acesso não autorizado.'
        >>> validaSenha('Giva123')
        'Senha correta. Acesso autorizado.'
        >>> validaSenha('123456')
        'Senha incorreta. Acesso não autorizado.'
    '''
    # 4. Implementação
    if senha == 'Giva123':
        return 'Senha correta. Acesso autorizado.'
    else:
        return 'Senha incorreta. Acesso não autorizado.'

# 5. Verificação
if __name__ == "__main__":
    import doctest
    doctest.testmod()

''' 6. Revisão:
    Nenhuma modificação foi necessária. '''