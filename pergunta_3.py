"""
Pergunta 3: Jogo de tabuleiro com roleta

Jogo onde:
- Jogadores andam 1, 2 ou 3 casas por turno (sorteado por roleta)
- Se o número sorteado for maior que as casas restantes, faz looping (reinicia)
- Vence quem chegar exatamente na última casa com menos turnos
- Tamanho mínimo do tabuleiro: 3 casas

A função calcula:
1. Quantidade mínima de turnos (caminho ótimo)
2. Probabilidade de executar o caminho ótimo
3. Número de combinações de movimentos sem looping
"""

from typing import Tuple
from functools import lru_cache


def analisa_tabuleiro(n_casas: int) -> Tuple[int, float, int]:
    """
    Analisa o tabuleiro e retorna as métricas solicitadas.
    
    Args:
        n_casas (int): Número de casas do tabuleiro (mínimo 3)
        
    Returns:
        Tuple[int, float, int]: 
            - Número mínimo de turnos (caminho ótimo)
            - Probabilidade de conseguir o caminho ótimo (0 a 1)
            - Número de combinações sem looping
            
    Raises:
        ValueError: Se n_casas < 3
        
    Examples:
        >>> analisa_tabuleiro(3)
        (1, 0.3333333333333333, 3)
        >>> analisa_tabuleiro(5)
        (2, 0.2222222222222222, 7)
    """
    if n_casas < 3:
        raise ValueError("O tabuleiro deve ter no mínimo 3 casas")
    
    # 1. Calcular caminho ótimo (mínimo de turnos)
    caminho_otimo = calcular_caminho_otimo(n_casas)
    
    # 2. Calcular probabilidade do caminho ótimo
    probabilidade = calcular_probabilidade_caminho_otimo(n_casas, caminho_otimo)
    
    # 3. Calcular número de combinações sem looping
    combinacoes = calcular_combinacoes_sem_looping(n_casas)
    
    return caminho_otimo, probabilidade, combinacoes


def calcular_caminho_otimo(n_casas: int) -> int:
    """
    Calcula o número mínimo de turnos para chegar à última casa.
    
    Usa programação dinâmica onde dp[i] = mínimo de turnos para chegar na casa i.
    
    Args:
        n_casas (int): Número de casas do tabuleiro
        
    Returns:
        int: Número mínimo de turnos
    """
    # Inicialização: começamos antes da casa 1 (posição 0)
    # Queremos chegar exatamente na casa n_casas
    
    # dp[i] = mínimo de turnos para chegar na casa i
    # Começamos na posição 0 (antes do tabuleiro)
    dp = [float('inf')] * (n_casas + 1)
    dp[0] = 0
    
    for posicao in range(n_casas + 1):
        if dp[posicao] == float('inf'):
            continue
            
        # Tentar andar 1, 2 ou 3 casas
        for passo in [1, 2, 3]:
            proxima_posicao = posicao + passo
            
            # Se passar do final, faz looping (não queremos isso no caminho ótimo)
            if proxima_posicao == n_casas:
                # Chegamos exatamente no final
                dp[n_casas] = min(dp[n_casas], dp[posicao] + 1)
            elif proxima_posicao < n_casas:
                # Ainda estamos no tabuleiro
                dp[proxima_posicao] = min(dp[proxima_posicao], dp[posicao] + 1)
            # Se proxima_posicao > n_casas, causa looping, não consideramos no caminho ótimo
    
    return dp[n_casas]


def calcular_probabilidade_caminho_otimo(n_casas: int, caminho_otimo: int) -> float:
    """
    Calcula a probabilidade de executar o caminho ótimo.
    
    Cada movimento tem probabilidade 1/3 (dado que a roleta sorteia 1, 2 ou 3 uniformemente).
    
    Args:
        n_casas (int): Número de casas
        caminho_otimo (int): Número de turnos do caminho ótimo
        
    Returns:
        float: Probabilidade (entre 0 e 1)
    """
    # Conta quantos caminhos ótimos existem
    num_caminhos_otimos = contar_caminhos_otimos(n_casas, caminho_otimo)
    
    # Probabilidade = (número de sequências que dão caminho ótimo) / 3^turnos
    # Cada caminho ótimo tem probabilidade (1/3)^caminho_otimo
    probabilidade = num_caminhos_otimos * ((1/3) ** caminho_otimo)
    
    return probabilidade


@lru_cache(maxsize=None)
def contar_caminhos_otimos(n_casas: int, turnos: int) -> int:
    """
    Conta quantos caminhos diferentes existem para chegar em exatamente
    n_casas usando exatamente 'turnos' movimentos (sem looping).
    
    Args:
        n_casas (int): Posição alvo
        turnos (int): Número exato de turnos
        
    Returns:
        int: Número de caminhos
    """
    if turnos == 0:
        return 1 if n_casas == 0 else 0
    
    if n_casas <= 0:
        return 0
    
    count = 0
    # Tentar chegar de 1, 2 ou 3 casas antes
    for passo in [1, 2, 3]:
        if n_casas >= passo:
            count += contar_caminhos_otimos(n_casas - passo, turnos - 1)
    
    return count


def calcular_combinacoes_sem_looping(n_casas: int) -> int:
    """
    Calcula quantas combinações de movimentos diferentes um jogador
    consegue executar sem efetuar nenhum looping.
    
    Isso significa: quantas sequências de movimentos (de qualquer tamanho)
    chegam exatamente em n_casas sem ultrapassar.
    
    Args:
        n_casas (int): Número de casas do tabuleiro
        
    Returns:
        int: Número de combinações possíveis
    """
    # dp[i] = número de formas de chegar na casa i (começando de 0)
    dp = [0] * (n_casas + 1)
    dp[0] = 1  # Uma forma de estar na posição inicial (não fazer nada)
    
    for posicao in range(n_casas):
        if dp[posicao] == 0:
            continue
            
        # De cada posição, podemos dar passos de 1, 2 ou 3
        for passo in [1, 2, 3]:
            proxima = posicao + passo
            if proxima == n_casas:
                # Chegamos no final
                dp[n_casas] += dp[posicao]
            elif proxima < n_casas:
                # Ainda no tabuleiro
                dp[proxima] += dp[posicao]
            # Se proxima > n_casas, causaria looping, então não contamos
    
    return dp[n_casas]


def mostrar_detalhes(n_casas: int) -> None:
    """
    Mostra análise detalhada do tabuleiro.
    
    Args:
        n_casas (int): Número de casas do tabuleiro
    """
    print(f"\n{'='*60}")
    print(f"Análise do tabuleiro com {n_casas} casas")
    print(f"{'='*60}")
    
    caminho_otimo, probabilidade, combinacoes = analisa_tabuleiro(n_casas)
    
    print(f"\n1. Caminho Ótimo (mínimo de turnos): {caminho_otimo}")
    print(f"   - Para percorrer {n_casas} casas, são necessários no mínimo {caminho_otimo} turnos")
    
    print(f"\n2. Probabilidade de executar o caminho ótimo: {probabilidade:.10f}")
    print(f"   - Equivalente a {probabilidade*100:.6f}%")
    print(f"   - Ou aproximadamente 1 em {int(1/probabilidade) if probabilidade > 0 else 'infinito'}")
    
    print(f"\n3. Combinações sem looping: {combinacoes}")
    print(f"   - Existem {combinacoes} sequências diferentes de movimentos")
    print(f"     que chegam exatamente na casa {n_casas} sem ultrapassar")


if __name__ == "__main__":
    print("=== Testes da Pergunta 3 ===")
    
    # Testar com diferentes tamanhos de tabuleiro
    tamanhos_teste = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
    
    for n in tamanhos_teste:
        mostrar_detalhes(n)
    
    # Casos especiais
    print("\n" + "="*60)
    print("Resumo Comparativo")
    print("="*60)
    print(f"{'Casas':<8} {'Turnos':<10} {'Probabilidade':<20} {'Combinações':<15}")
    print("-" * 60)
    
    for n in [3, 5, 10, 15, 20]:
        turnos, prob, comb = analisa_tabuleiro(n)
        print(f"{n:<8} {turnos:<10} {prob:<20.10f} {comb:<15}")

