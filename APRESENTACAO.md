# Apresentação das Soluções - Desafio de Programação

## 📌 Visão Geral

Este documento apresenta as soluções implementadas para o desafio de programação, detalhando a abordagem técnica, raciocínio e decisões de design para cada uma das 4 perguntas.

---

## 🎯 Pergunta 1: Verificação de String

### Enunciado
Escrever uma função que determina se uma string termina com 'A' e começa com 'B'.

### Solução Implementada

```python
def verifica_string(texto: str) -> bool:
    if not texto:
        return False
    return texto.startswith('B') and texto.endswith('A')
```

### Raciocínio

1. **Abordagem**: Utilizei métodos nativos do Python (`startswith` e `endswith`) por serem:
   - **Eficientes**: Implementados em C, otimizados para performance
   - **Legíveis**: Código auto-explicativo
   - **Confiáveis**: Testados extensivamente pela comunidade Python

2. **Tratamento de Casos Especiais**:
   - String vazia retorna `False`
   - Validação simples e direta

3. **Funcionalidade Adicional**:
   - Implementei versão case-insensitive para maior flexibilidade
   - Demonstra compreensão de diferentes requisitos de negócio

### Complexidade
- **Tempo**: O(1) - Verifica apenas primeiro e último caractere
- **Espaço**: O(1) - Não usa estruturas auxiliares

### Casos de Teste
- ✓ "BananaA" → True
- ✓ "Casa" → False
- ✓ "BA" → True (caso mínimo válido)
- ✓ "" → False (string vazia)

---

## 🔢 Pergunta 2: Sequência Aritmética

### Enunciado
Sequência: 11, 18, 25, 32, 39...
Criar função que retorna o valor na posição x (começando de 1).

### Análise Matemática

A sequência é uma **Progressão Aritmética (PA)**:
- Primeiro termo: a₁ = 11
- Razão: r = 18 - 11 = 7
- Fórmula geral: **aₙ = a₁ + (n-1) × r**

### Solução Implementada

```python
def print_valor(x: int) -> int:
    if x < 1:
        raise ValueError("A posição deve ser maior ou igual a 1")
    
    primeiro_termo = 11
    razao = 7
    
    return primeiro_termo + (x - 1) * razao
```

### Raciocínio

1. **Fórmula Matemática Direta**:
   - Não usa loops ou recursão
   - Cálculo instantâneo independente do tamanho de x
   - Funciona até para valores gigantes (x = 3.542.158)

2. **Validações**:
   - Levanta exceção para posições inválidas (x < 1)
   - Type hints para documentação clara

3. **Funções Auxiliares Implementadas**:
   - `obter_posicao_valor()`: Função inversa (dado valor, retorna posição)
   - `gerar_sequencia()`: Gera primeiros n termos
   - Demonstra pensamento completo sobre o problema

### Complexidade
- **Tempo**: O(1) - Operações aritméticas constantes
- **Espaço**: O(1) - Sem estruturas auxiliares

### Validação dos Exemplos
- print_valor(1) = 11 ✓
- print_valor(200) = 1.404 ✓
- print_valor(3.542.158) = 24.795.110 ✓

### Decisões de Design
- **Por que não usar loop?** Loop seria O(n), desnecessário quando temos fórmula fechada
- **Por que validar entrada?** Previne comportamentos inesperados
- **Por que funções auxiliares?** Demonstra compreensão profunda do domínio

---

## 🎲 Pergunta 3: Jogo de Tabuleiro

### Enunciado
Jogo onde jogadores andam 1, 2 ou 3 casas (roleta). Se ultrapassar, faz looping.

Calcular:
1. Quantidade mínima de turnos (caminho ótimo)
2. Probabilidade de executar o caminho ótimo
3. Combinações de movimentos sem looping

### Análise do Problema

Este é um problema de **Programação Dinâmica** e **Teoria dos Grafos**:
- Cada posição do tabuleiro é um estado
- Cada movimento é uma transição
- Queremos encontrar o caminho mais curto

### Solução 1: Caminho Ótimo

```python
def calcular_caminho_otimo(n_casas: int) -> int:
    dp = [float('inf')] * (n_casas + 1)
    dp[0] = 0
    
    for posicao in range(n_casas + 1):
        if dp[posicao] == float('inf'):
            continue
        
        for passo in [1, 2, 3]:
            proxima_posicao = posicao + passo
            if proxima_posicao == n_casas:
                dp[n_casas] = min(dp[n_casas], dp[posicao] + 1)
            elif proxima_posicao < n_casas:
                dp[proxima_posicao] = min(dp[proxima_posicao], dp[posicao] + 1)
    
    return dp[n_casas]
```

**Raciocínio**:
- `dp[i]` = número mínimo de turnos para chegar na casa i
- Para cada posição, tentamos os 3 possíveis movimentos
- Ignoramos movimentos que causariam looping
- Complexidade: **O(n)** tempo, **O(n)** espaço

### Solução 2: Probabilidade do Caminho Ótimo

```python
def calcular_probabilidade_caminho_otimo(n_casas: int, caminho_otimo: int) -> float:
    num_caminhos_otimos = contar_caminhos_otimos(n_casas, caminho_otimo)
    probabilidade = num_caminhos_otimos * ((1/3) ** caminho_otimo)
    return probabilidade
```

**Raciocínio**:
- Cada movimento tem probabilidade 1/3 (roleta uniforme)
- Para k turnos, há 3^k sequências possíveis
- Contamos quantas sequências resultam no caminho ótimo
- Probabilidade = (sequências ótimas) / (total de sequências)

**Exemplo (3 casas)**:
- Caminho ótimo: 1 turno
- Sequências ótimas: [3]
- Total de sequências: [1], [2], [3] = 3
- Probabilidade: 1/3 = 33.33%

### Solução 3: Combinações sem Looping

```python
def calcular_combinacoes_sem_looping(n_casas: int) -> int:
    dp = [0] * (n_casas + 1)
    dp[0] = 1
    
    for posicao in range(n_casas):
        if dp[posicao] == 0:
            continue
        
        for passo in [1, 2, 3]:
            proxima = posicao + passo
            if proxima == n_casas:
                dp[n_casas] += dp[posicao]
            elif proxima < n_casas:
                dp[proxima] += dp[posicao]
    
    return dp[n_casas]
```

**Raciocínio**:
- `dp[i]` = número de formas de chegar na posição i
- Somamos todas as formas possíveis sem considerar looping
- Relação de recorrência: `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`
- Similar à sequência de Fibonacci, mas com 3 termos

### Resultados Interessantes

| Casas | Turnos Ótimos | Probabilidade | Combinações |
|-------|---------------|---------------|-------------|
| 3     | 1             | 33.33%        | 4           |
| 5     | 2             | 22.22%        | 13          |
| 10    | 4             | 12.35%        | 274         |
| 20    | 7             | 0.32%         | 121.415     |

**Observações**:
- Probabilidade do caminho ótimo **decresce rapidamente**
- Número de combinações cresce **exponencialmente**
- Para 20 casas: mais de 120 mil combinações diferentes!

### Otimizações Implementadas

1. **Memoização com @lru_cache**:
   - Cache automático de resultados
   - Evita recálculos desnecessários

2. **Programação Dinâmica Bottom-up**:
   - Mais eficiente que recursão
   - Evita stack overflow

### Complexidade
- Caminho ótimo: **O(n)** tempo, **O(n)** espaço
- Probabilidade: **O(n × k)** onde k é o número de turnos
- Combinações: **O(n)** tempo, **O(n)** espaço

---

## 💼 Pergunta 4: Cálculo de Benefícios Trabalhistas

### Enunciado
Calcular férias e décimo terceiro proporcionais na demissão.

**Regras**:
- Férias zeram a cada aniversário de emprego
- Décimo terceiro zera a cada virada de ano

### Análise das Regras Trabalhistas

#### Férias
- **Direito**: 30 dias após 12 meses trabalhados
- **Proporcional**: (meses/12) × salário
- **Adicional Constitucional**: +1/3 sobre as férias
- **Fórmula**: `férias_total = (meses/12) × salário × (1 + 1/3)`

#### Décimo Terceiro
- **Direito**: 1 salário ao final do ano
- **Proporcional**: (meses/12) × salário
- **Regra dos 15 dias**: Considera mês completo se trabalhou 15+ dias

### Solução Implementada

#### 1. Cálculo de Férias

```python
def calcular_ferias(salario: float, data_admissao: date, data_demissao: date) -> Tuple[float, dict]:
    # Encontrar último aniversário
    ultimo_aniversario = encontrar_ultimo_aniversario(data_admissao, data_demissao)
    
    # Meses desde último aniversário
    meses_trabalhados = calcular_meses_proporcionais(ultimo_aniversario, data_demissao)
    
    # Cálculo
    ferias_proporcionais = (meses_trabalhados / 12) * salario
    adicional_um_terco = ferias_proporcionais / 3
    valor_total = ferias_proporcionais + adicional_um_terco
    
    return round(valor_total, 2)
```

**Raciocínio**:
- Encontra o último aniversário de emprego antes da demissão
- Calcula meses trabalhados desde então
- Aplica fórmula proporcional + 1/3 constitucional

#### 2. Cálculo de Décimo Terceiro

```python
def calcular_decimo_terceiro(salario: float, data_admissao: date, data_demissao: date) -> Tuple[float, dict]:
    # Início do ano da demissão
    inicio_ano = date(data_demissao.year, 1, 1)
    
    # Se admitido no mesmo ano, usar data de admissão
    data_inicial = max(data_admissao, inicio_ano)
    
    # Meses no ano
    meses_trabalhados = calcular_meses_proporcionais(data_inicial, data_demissao)
    
    # Cálculo proporcional
    valor_decimo = (meses_trabalhados / 12) * salario
    
    return round(valor_decimo, 2)
```

**Raciocínio**:
- Considera apenas o ano corrente
- Se foi admitido no mesmo ano, conta desde a admissão
- Aplica regra dos 15 dias

#### 3. Cálculo de Meses Proporcionais

```python
def calcular_meses_proporcionais(data_inicial: date, data_final: date) -> int:
    # Meses completos
    meses = (data_final.year - data_inicial.year) * 12
    meses += data_final.month - data_inicial.month
    
    # Ajuste baseado em dias (regra dos 15 dias)
    if data_final.day < data_inicial.day:
        meses -= 1
        dias_trabalhados = data_final.day
        if dias_trabalhados >= 15:
            meses += 1
    else:
        dias_trabalhados = data_final.day - data_inicial.day + 1
        if dias_trabalhados >= 15:
            meses += 1
    
    return max(0, meses)
```

**Raciocínio**:
- Calcula diferença de meses considerando anos
- Aplica regra dos 15 dias (trabalhou 15+ dias = mês completo)
- Garante resultado não negativo

### Casos Especiais Tratados

1. **Anos Bissextos**:
   - Admissão em 29/02 em ano bissexto
   - Usa 28/02 para anos não bissextos

2. **Funcionário com Menos de 1 Ano**:
   - Último aniversário = data de admissão
   - Cálculo proporcional normal

3. **Demissão no Início do Ano**:
   - Décimo terceiro zerado do ano anterior
   - Calcula apenas meses do ano corrente

4. **Demissão no Final do Ano**:
   - Pode ter décimo terceiro integral (12 meses)

### Exemplo de Cálculo

**Cenário**: 
- Salário: R$ 3.000,00
- Admissão: 15/01/2023
- Demissão: 20/06/2024

**Férias**:
- Último aniversário: 15/01/2024
- Meses trabalhados: 5 meses
- Férias proporcionais: (5/12) × 3.000 = R$ 1.250,00
- Adicional 1/3: R$ 416,67
- **Total: R$ 1.666,67**

**Décimo Terceiro**:
- Ano: 2024
- Data inicial: 01/01/2024
- Meses trabalhados: 6 meses
- Proporcional: (6/12) × 3.000 = **R$ 1.500,00**

**Total a Receber: R$ 3.166,67**

### Funcionalidades Adicionais

1. **Relatório Detalhado**:
   - Formatação profissional
   - Todos os cálculos discriminados
   - Fácil auditoria

2. **Validações**:
   - Data de demissão não pode ser anterior à admissão
   - Salário não pode ser negativo
   - Type hints para segurança de tipos

3. **Dicionário de Detalhes**:
   - Retorna estrutura com todos os dados
   - Útil para integrações futuras

### Complexidade
- **Tempo**: O(1) - Operações constantes
- **Espaço**: O(1) - Apenas variáveis escalares

---

## 📊 Análise Geral das Soluções

### Princípios Aplicados

1. **SOLID**:
   - **Single Responsibility**: Cada função tem uma responsabilidade clara
   - **Open/Closed**: Fácil estender sem modificar código existente

2. **Clean Code**:
   - Nomes descritivos
   - Funções pequenas e focadas
   - Comentários quando necessário

3. **DRY (Don't Repeat Yourself)**:
   - Funções reutilizáveis
   - Lógica centralizada

4. **Type Hints**:
   - Documentação inline
   - Melhor suporte de IDEs
   - Detecção precoce de erros

### Técnicas Utilizadas

1. **Programação Dinâmica** (Pergunta 3):
   - Otimização de problemas complexos
   - Evita recálculos

2. **Memoização** (Pergunta 3):
   - Cache automático com `@lru_cache`
   - Melhora performance drasticamente

3. **Validação de Entrada** (Todas):
   - Previne erros
   - Mensagens claras

4. **Separação de Responsabilidades** (Pergunta 4):
   - Funções modulares
   - Fácil testar e manter

### Testes Implementados

Cada arquivo possui seção `if __name__ == "__main__"` com:
- Casos de teste principais
- Casos extremos
- Validações de requisitos
- Saída formatada e legível

### Estrutura do Código

```
challenge_3s/
├── pergunta_1.py          # Simples e direto
├── pergunta_2.py          # Matemático e eficiente
├── pergunta_3.py          # Complexo, usa DP
├── pergunta_4.py          # Detalhado, muitas regras
├── run_all_tests.py       # Executor consolidado
├── README.md              # Documentação técnica
└── APRESENTACAO.md        # Este arquivo
```

---

## 🎯 Conclusão

As soluções implementadas demonstram:

✅ **Conhecimento Técnico**:
- Estruturas de dados apropriadas
- Algoritmos eficientes
- Complexidade otimizada

✅ **Boas Práticas**:
- Código limpo e legível
- Documentação adequada
- Type hints e validações

✅ **Pensamento Analítico**:
- Compreensão profunda dos problemas
- Abordagens matemáticas quando possível
- Consideração de casos especiais

✅ **Profissionalismo**:
- Código production-ready
- Facilmente extensível
- Bem testado

### Diferenciais da Implementação

1. **Além do Requisitado**:
   - Funções auxiliares úteis
   - Versões alternativas
   - Relatórios detalhados

2. **Código Robusto**:
   - Tratamento de erros
   - Validações completas
   - Casos extremos considerados

3. **Documentação Completa**:
   - Docstrings detalhadas
   - README profissional
   - Exemplos de uso

4. **Escalabilidade**:
   - Soluções eficientes
   - Uso inteligente de memória
   - Pronto para grandes volumes

---

## 🚀 Como Executar

```bash
# Executar todos os testes
python run_all_tests.py

# Ou executar individualmente
python pergunta_1.py
python pergunta_2.py
python pergunta_3.py
python pergunta_4.py
```

---

**Desenvolvido com atenção aos detalhes e foco em qualidade** ✨

