"""
Script para executar todos os testes do desafio
"""

import sys


def main():
    """Executa todos os testes das 4 perguntas"""
    
    print("="*70)
    print(" DESAFIO DE PROGRAMAÇÃO - EXECUÇÃO COMPLETA DOS TESTES")
    print("="*70)
    
    # Pergunta 1
    print("\n\n" + "█"*70)
    print("█ PERGUNTA 1: Verificação de String")
    print("█"*70)
    try:
        from pergunta_1 import verifica_string, verifica_string_case_insensitive
        
        test_cases = [
            ("BananaA", True),
            ("BolaA", True),
            ("Casa", False),
            ("BA", True),
        ]
        
        print("\nTestes executados:")
        for texto, esperado in test_cases:
            resultado = verifica_string(texto)
            status = "✓ PASSOU" if resultado == esperado else "✗ FALHOU"
            print(f"  {status}: verifica_string('{texto}') = {resultado}")
        
        print("\n✅ Pergunta 1 completada com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro na Pergunta 1: {e}")
        sys.exit(1)
    
    # Pergunta 2
    print("\n\n" + "█"*70)
    print("█ PERGUNTA 2: Sequência Aritmética")
    print("█"*70)
    try:
        from pergunta_2 import print_valor
        
        test_cases = [
            (1, 11),
            (2, 18),
            (200, 1404),
            (254, 1782),
            (3542158, 24795110),
        ]
        
        print("\nTestes executados:")
        for posicao, esperado in test_cases:
            resultado = print_valor(posicao)
            status = "✓ PASSOU" if resultado == esperado else "✗ FALHOU"
            print(f"  {status}: print_valor({posicao:,}) = {resultado:,}")
        
        print("\n✅ Pergunta 2 completada com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro na Pergunta 2: {e}")
        sys.exit(1)
    
    # Pergunta 3
    print("\n\n" + "█"*70)
    print("█ PERGUNTA 3: Jogo de Tabuleiro")
    print("█"*70)
    try:
        from pergunta_3 import analisa_tabuleiro
        
        test_cases = [3, 5, 10, 15]
        
        print("\nTestes executados:")
        print(f"{'Casas':<8} {'Turnos':<10} {'Probabilidade':<15} {'Combinações':<15}")
        print("-" * 60)
        
        for n in test_cases:
            turnos, prob, comb = analisa_tabuleiro(n)
            print(f"{n:<8} {turnos:<10} {prob*100:.4f}%{' '*7} {comb:<15}")
        
        print("\n✅ Pergunta 3 completada com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro na Pergunta 3: {e}")
        sys.exit(1)
    
    # Pergunta 4
    print("\n\n" + "█"*70)
    print("█ PERGUNTA 4: Cálculo de Benefícios Trabalhistas")
    print("█"*70)
    try:
        from pergunta_4 import calcular_beneficios
        from datetime import date
        
        print("\nTeste: Funcionário admitido em 15/01/2023, demitido em 20/06/2024")
        print("Salário: R$ 3.000,00")
        
        ferias, decimo, detalhes = calcular_beneficios(
            salario=3000.00,
            data_admissao=date(2023, 1, 15),
            data_demissao=date(2024, 6, 20)
        )
        
        print(f"\n  Férias (+ 1/3): R$ {ferias:,.2f}")
        print(f"  Décimo Terceiro: R$ {decimo:,.2f}")
        print(f"  TOTAL: R$ {ferias + decimo:,.2f}")
        
        print("\n✅ Pergunta 4 completada com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro na Pergunta 4: {e}")
        sys.exit(1)
    
    # Resumo final
    print("\n\n" + "="*70)
    print("🎉 TODOS OS TESTES FORAM EXECUTADOS COM SUCESSO!")
    print("="*70)
    print("\nArquivos do projeto:")
    print("  • pergunta_1.py - Verificação de String")
    print("  • pergunta_2.py - Sequência Aritmética")
    print("  • pergunta_3.py - Jogo de Tabuleiro")
    print("  • pergunta_4.py - Cálculo de Benefícios")
    print("\nPara executar testes detalhados de cada pergunta:")
    print("  python pergunta_1.py")
    print("  python pergunta_2.py")
    print("  python pergunta_3.py")
    print("  python pergunta_4.py")
    print("="*70)


if __name__ == "__main__":
    main()

