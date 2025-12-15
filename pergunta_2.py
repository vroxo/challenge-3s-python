"""
Pergunta 2: Sequência numérica com progressão aritmética

Sequência: 11, 18, 25, 32, 39...
- Primeiro termo (a1) = 11
- Razão (r) = 7
- Fórmula: an = a1 + (n-1) * r

Esta função calcula o valor na posição x da sequência.
"""


def print_valor(x: int) -> int:
    """
    Calcula o valor na posição x da sequência aritmética.
    
    A sequência segue a progressão aritmética: 11, 18, 25, 32, 39...
    onde a1 = 11 e r = 7
    
    Args:
        x (int): Posição na sequência (começando de 1)
        
    Returns:
        int: Valor na posição x
        
    Raises:
        ValueError: Se x for menor que 1
        
    Examples:
        >>> print_valor(1)
        11
        >>> print_valor(2)
        18
        >>> print_valor(3)
        25
        >>> print_valor(200)
        1404
        >>> print_valor(254)
        1782
        >>> print_valor(3542158)
        24795110
    """
    if x < 1:
        raise ValueError("A posição deve ser maior ou igual a 1")
    
    # Fórmula da progressão aritmética: an = a1 + (n-1) * r
    primeiro_termo = 11
    razao = 7
    
    return primeiro_termo + (x - 1) * razao


def obter_posicao_valor(valor: int) -> int:
    """
    Função inversa: dado um valor, retorna sua posição na sequência.
    
    Args:
        valor (int): Valor a ser encontrado
        
    Returns:
        int: Posição do valor na sequência (ou -1 se não pertencer à sequência)
        
    Examples:
        >>> obter_posicao_valor(11)
        1
        >>> obter_posicao_valor(18)
        2
        >>> obter_posicao_valor(1404)
        200
    """
    primeiro_termo = 11
    razao = 7
    
    # Verifica se o valor pertence à sequência
    if (valor - primeiro_termo) % razao != 0:
        return -1
    
    # Calcula a posição: n = (an - a1) / r + 1
    posicao = (valor - primeiro_termo) // razao + 1
    
    return posicao if posicao >= 1 else -1


def gerar_sequencia(n_termos: int) -> list[int]:
    """
    Gera os primeiros n termos da sequência.
    
    Args:
        n_termos (int): Número de termos a gerar
        
    Returns:
        list[int]: Lista com os n primeiros termos
        
    Examples:
        >>> gerar_sequencia(5)
        [11, 18, 25, 32, 39]
    """
    return [print_valor(i) for i in range(1, n_termos + 1)]


if __name__ == "__main__":
    print("=== Testes da Pergunta 2 ===\n")
    
    # Testes conforme especificação
    test_cases = [
        (1, 11),
        (2, 18),
        (200, 1404),
        (254, 1782),
        (3542158, 24795110),
    ]
    
    print("Testes principais:")
    for posicao, esperado in test_cases:
        resultado = print_valor(posicao)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} print_valor(x={posicao:,}) = {resultado:,} (esperado: {esperado:,})")
    
    # Verificação da sequência inicial
    print("\nPrimeiros 10 termos da sequência:")
    primeiros_termos = gerar_sequencia(10)
    print(primeiros_termos)
    
    # Teste da função inversa
    print("\nTeste da função inversa (obter posição de um valor):")
    valores_teste = [11, 18, 25, 1404, 1782]
    for valor in valores_teste:
        posicao = obter_posicao_valor(valor)
        print(f"O valor {valor} está na posição {posicao}")
    
    # Teste com valor que não pertence à sequência
    print(f"\nO valor 20 pertence à sequência? Posição: {obter_posicao_valor(20)}")
    
    # Validação matemática
    print("\n=== Validação Matemática ===")
    print(f"Razão (diferença entre termos consecutivos): {print_valor(2) - print_valor(1)}")
    print(f"Verificação: {print_valor(3) - print_valor(2)} = {print_valor(4) - print_valor(3)}")

