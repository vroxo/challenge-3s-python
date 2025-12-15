"""
Pergunta 1: Determinar se uma string termina com 'A' e começa com 'B'

Esta função verifica se uma string atende a dois critérios:
- Começa com a letra 'B'
- Termina com a letra 'A'
"""


def verifica_string(texto: str) -> bool:
    """
    Verifica se a string começa com 'B' e termina com 'A'.
    
    Args:
        texto (str): String a ser verificada
        
    Returns:
        bool: True se começa com 'B' e termina com 'A', False caso contrário
        
    Examples:
        >>> verifica_string("BananaA")
        True
        >>> verifica_string("BolaA")
        True
        >>> verifica_string("Casa")
        False
        >>> verifica_string("BA")
        True
        >>> verifica_string("B")
        False
    """
    if not texto:
        return False
    
    # Verifica se começa com 'B' (case-sensitive) e termina com 'A'
    return texto.startswith('B') and texto.endswith('A')


def verifica_string_case_insensitive(texto: str) -> bool:
    """
    Versão case-insensitive da verificação.
    
    Args:
        texto (str): String a ser verificada
        
    Returns:
        bool: True se começa com 'B' ou 'b' e termina com 'A' ou 'a'
        
    Examples:
        >>> verifica_string_case_insensitive("banana")
        True
        >>> verifica_string_case_insensitive("BOLA")
        True
    """
    if not texto:
        return False
    
    return texto.upper().startswith('B') and texto.upper().endswith('A')


if __name__ == "__main__":
    # Testes
    print("=== Testes da Pergunta 1 ===\n")
    
    test_cases = [
        ("BananaA", True),
        ("BolaA", True),
        ("Casa", False),
        ("BA", True),
        ("B", False),
        ("A", False),
        ("", False),
        ("BrasilA", True),
        ("Brasil", False),
        ("AbrasilB", False),
    ]
    
    print("Testes com case-sensitive:")
    for texto, esperado in test_cases:
        resultado = verifica_string(texto)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} verifica_string('{texto}') = {resultado} (esperado: {esperado})")
    
    print("\nTestes com case-insensitive:")
    case_insensitive_tests = [
        ("banana", True),
        ("BOLA", True),
        ("brasil", False),
        ("bRaSiLa", True),
    ]
    
    for texto, esperado in case_insensitive_tests:
        resultado = verifica_string_case_insensitive(texto)
        status = "✓" if resultado == esperado else "✗"
        print(f"{status} verifica_string_case_insensitive('{texto}') = {resultado} (esperado: {esperado})")

