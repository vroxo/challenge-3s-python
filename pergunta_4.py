"""
Pergunta 4: Cálculo de Férias e Décimo Terceiro Salário

Calcula os valores a receber de férias e décimo terceiro ao pedir demissão.

Regras:
- Férias: Zeram a cada aniversário de emprego (sempre tirou férias corretamente)
- Décimo Terceiro: Zera a cada virada de ano (sem resíduos de anos anteriores)

Férias: 
- Direito a 30 dias após 12 meses
- Proporcional: (meses trabalhados / 12) * salário
- Acréscimo de 1/3 constitucional sobre as férias

Décimo Terceiro:
- Proporcional aos meses trabalhados no ano
- (meses / 12) * salário
- Considera-se mês trabalhado se trabalhou 15 dias ou mais
"""

from datetime import datetime, date
from typing import Tuple


def calcular_beneficios(
    salario: float,
    data_admissao: date,
    data_demissao: date
) -> Tuple[float, float, dict]:
    """
    Calcula férias e décimo terceiro proporcionais.
    
    Args:
        salario (float): Salário bruto mensal do funcionário
        data_admissao (date): Data de admissão do funcionário
        data_demissao (date): Data de demissão do funcionário
        
    Returns:
        Tuple[float, float, dict]: 
            - Valor das férias (incluindo 1/3 constitucional)
            - Valor do décimo terceiro
            - Dicionário com detalhes do cálculo
            
    Raises:
        ValueError: Se data_demissao for anterior a data_admissao ou salário for negativo
        
    Examples:
        >>> calcular_beneficios(3000, date(2023, 1, 15), date(2024, 6, 20))
        (1750.0, 1500.0, {...})
    """
    # Validações
    if data_demissao < data_admissao:
        raise ValueError("Data de demissão não pode ser anterior à data de admissão")
    
    if salario < 0:
        raise ValueError("Salário não pode ser negativo")
    
    # Calcular férias
    valor_ferias, detalhes_ferias = calcular_ferias(salario, data_admissao, data_demissao)
    
    # Calcular décimo terceiro
    valor_decimo, detalhes_decimo = calcular_decimo_terceiro(salario, data_admissao, data_demissao)
    
    # Montar detalhes completos
    detalhes = {
        'salario': salario,
        'data_admissao': data_admissao.strftime('%d/%m/%Y'),
        'data_demissao': data_demissao.strftime('%d/%m/%Y'),
        'ferias': detalhes_ferias,
        'decimo_terceiro': detalhes_decimo,
        'total_a_receber': valor_ferias + valor_decimo
    }
    
    return valor_ferias, valor_decimo, detalhes


def calcular_ferias(
    salario: float,
    data_admissao: date,
    data_demissao: date
) -> Tuple[float, dict]:
    """
    Calcula o valor proporcional de férias.
    
    Férias zeram a cada aniversário de emprego.
    
    Args:
        salario (float): Salário mensal
        data_admissao (date): Data de admissão
        data_demissao (date): Data de demissão
        
    Returns:
        Tuple[float, dict]: Valor das férias e detalhes do cálculo
    """
    # Encontrar a data do último aniversário de emprego antes da demissão
    ultimo_aniversario = encontrar_ultimo_aniversario(data_admissao, data_demissao)
    
    # Calcular meses trabalhados desde o último aniversário
    meses_trabalhados = calcular_meses_proporcionais(ultimo_aniversario, data_demissao)
    
    # Férias proporcionais: (meses/12) * salário
    ferias_proporcionais = (meses_trabalhados / 12) * salario
    
    # Acréscimo de 1/3 constitucional
    adicional_um_terco = ferias_proporcionais / 3
    
    # Valor total
    valor_total = ferias_proporcionais + adicional_um_terco
    
    detalhes = {
        'ultimo_aniversario': ultimo_aniversario.strftime('%d/%m/%Y'),
        'meses_trabalhados': meses_trabalhados,
        'ferias_proporcionais': round(ferias_proporcionais, 2),
        'adicional_um_terco': round(adicional_um_terco, 2),
        'valor_total': round(valor_total, 2)
    }
    
    return round(valor_total, 2), detalhes


def calcular_decimo_terceiro(
    salario: float,
    data_admissao: date,
    data_demissao: date
) -> Tuple[float, dict]:
    """
    Calcula o valor proporcional do décimo terceiro.
    
    Décimo terceiro zera a cada virada de ano.
    
    Args:
        salario (float): Salário mensal
        data_admissao (date): Data de admissão
        data_demissao (date): Data de demissão
        
    Returns:
        Tuple[float, dict]: Valor do décimo terceiro e detalhes do cálculo
    """
    # Início do ano da demissão
    inicio_ano = date(data_demissao.year, 1, 1)
    
    # Se foi admitido no mesmo ano, usar data de admissão
    data_inicial = max(data_admissao, inicio_ano)
    
    # Calcular meses trabalhados no ano
    meses_trabalhados = calcular_meses_proporcionais(data_inicial, data_demissao)
    
    # Décimo terceiro proporcional: (meses/12) * salário
    valor_decimo = (meses_trabalhados / 12) * salario
    
    detalhes = {
        'ano_referencia': data_demissao.year,
        'data_inicial': data_inicial.strftime('%d/%m/%Y'),
        'meses_trabalhados': meses_trabalhados,
        'valor_proporcional': round(valor_decimo, 2)
    }
    
    return round(valor_decimo, 2), detalhes


def encontrar_ultimo_aniversario(data_admissao: date, data_demissao: date) -> date:
    """
    Encontra a data do último aniversário de emprego antes da demissão.
    
    Args:
        data_admissao (date): Data de admissão
        data_demissao (date): Data de demissão
        
    Returns:
        date: Data do último aniversário
    """
    # Tenta o aniversário no ano da demissão
    ano_demissao = data_demissao.year
    try:
        aniversario = date(ano_demissao, data_admissao.month, data_admissao.day)
    except ValueError:
        # Caso 29 de fevereiro em ano não bissexto
        aniversario = date(ano_demissao, data_admissao.month, 28)
    
    # Se o aniversário ainda não aconteceu no ano da demissão, pega do ano anterior
    if aniversario > data_demissao:
        ano_anterior = ano_demissao - 1
        try:
            aniversario = date(ano_anterior, data_admissao.month, data_admissao.day)
        except ValueError:
            aniversario = date(ano_anterior, data_admissao.month, 28)
    
    # Se o resultado for antes da admissão, retorna a própria data de admissão
    if aniversario < data_admissao:
        return data_admissao
    
    return aniversario


def calcular_meses_proporcionais(data_inicial: date, data_final: date) -> int:
    """
    Calcula o número de meses proporcionais entre duas datas.
    
    Regra: considera-se mês completo se trabalhou 15 dias ou mais.
    
    Args:
        data_inicial (date): Data inicial
        data_final (date): Data final
        
    Returns:
        int: Número de meses proporcionais
    """
    # Calcula meses completos
    meses = (data_final.year - data_inicial.year) * 12
    meses += data_final.month - data_inicial.month
    
    # Ajusta baseado nos dias
    # Se o dia final for menor que o inicial, não completou o mês
    if data_final.day < data_inicial.day:
        meses -= 1
        # Mas se trabalhou 15 dias ou mais no último mês, conta
        dias_trabalhados = data_final.day
        if dias_trabalhados >= 15:
            meses += 1
    else:
        # Mês completo ou parcial
        dias_trabalhados = data_final.day - data_inicial.day + 1
        if dias_trabalhados >= 15:
            meses += 1
    
    return max(0, meses)


def formatar_relatorio(salario: float, data_admissao: date, data_demissao: date) -> str:
    """
    Gera um relatório formatado dos cálculos.
    
    Args:
        salario (float): Salário mensal
        data_admissao (date): Data de admissão
        data_demissao (date): Data de demissão
        
    Returns:
        str: Relatório formatado
    """
    valor_ferias, valor_decimo, detalhes = calcular_beneficios(
        salario, data_admissao, data_demissao
    )
    
    relatorio = f"""
{'='*70}
RELATÓRIO DE RESCISÃO - CÁLCULO DE BENEFÍCIOS
{'='*70}

DADOS DO FUNCIONÁRIO:
  Salário Mensal: R$ {salario:,.2f}
  Data de Admissão: {detalhes['data_admissao']}
  Data de Demissão: {detalhes['data_demissao']}

{'='*70}
FÉRIAS PROPORCIONAIS:
{'='*70}
  Último Aniversário de Emprego: {detalhes['ferias']['ultimo_aniversario']}
  Meses Trabalhados: {detalhes['ferias']['meses_trabalhados']} meses
  
  Férias Proporcionais: R$ {detalhes['ferias']['ferias_proporcionais']:,.2f}
  Adicional 1/3 Constitucional: R$ {detalhes['ferias']['adicional_um_terco']:,.2f}
  ─────────────────────────────────────
  TOTAL FÉRIAS: R$ {detalhes['ferias']['valor_total']:,.2f}

{'='*70}
DÉCIMO TERCEIRO PROPORCIONAL:
{'='*70}
  Ano de Referência: {detalhes['decimo_terceiro']['ano_referencia']}
  Data Inicial (início do ano): {detalhes['decimo_terceiro']['data_inicial']}
  Meses Trabalhados no Ano: {detalhes['decimo_terceiro']['meses_trabalhados']} meses
  
  TOTAL DÉCIMO TERCEIRO: R$ {detalhes['decimo_terceiro']['valor_proporcional']:,.2f}

{'='*70}
RESUMO FINANCEIRO:
{'='*70}
  Férias + 1/3: R$ {valor_ferias:,.2f}
  Décimo Terceiro: R$ {valor_decimo:,.2f}
  ─────────────────────────────────────
  TOTAL A RECEBER: R$ {detalhes['total_a_receber']:,.2f}
{'='*70}
"""
    return relatorio


if __name__ == "__main__":
    print("=== Testes da Pergunta 4 ===\n")
    
    # Teste 1: Funcionário com 5 meses no ano e 7 meses desde último aniversário
    print("TESTE 1: Funcionário demitido em meio de período")
    print(formatar_relatorio(
        salario=3000.00,
        data_admissao=date(2023, 1, 15),
        data_demissao=date(2024, 6, 20)
    ))
    
    # Teste 2: Funcionário com quase um ano completo
    print("\nTESTE 2: Funcionário com quase um ano completo")
    print(formatar_relatorio(
        salario=5000.00,
        data_admissao=date(2023, 3, 1),
        data_demissao=date(2024, 2, 28)
    ))
    
    # Teste 3: Funcionário demitido no início do ano
    print("\nTESTE 3: Funcionário demitido no início do ano")
    print(formatar_relatorio(
        salario=4000.00,
        data_admissao=date(2020, 5, 10),
        data_demissao=date(2024, 2, 15)
    ))
    
    # Teste 4: Funcionário com menos de 1 ano de empresa
    print("\nTESTE 4: Funcionário com menos de 1 ano")
    print(formatar_relatorio(
        salario=2500.00,
        data_admissao=date(2024, 8, 1),
        data_demissao=date(2024, 12, 15)
    ))
    
    # Teste 5: Funcionário demitido no final do ano
    print("\nTESTE 5: Funcionário demitido no final do ano")
    print(formatar_relatorio(
        salario=6000.00,
        data_admissao=date(2022, 3, 15),
        data_demissao=date(2024, 12, 31)
    ))

