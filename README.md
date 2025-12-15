# Challenge 3S - Desafio de Programação Python

Este repositório contém as soluções para um desafio de processo seletivo composto por 4 perguntas de programação em Python.


## 🚀 Como Executar

Cada arquivo pode ser executado independentemente:

```bash
# Pergunta 1 - Verificação de String
python pergunta_1.py

# Pergunta 2 - Sequência Aritmética
python pergunta_2.py

# Pergunta 3 - Análise de Tabuleiro
python pergunta_3.py

# Pergunta 4 - Cálculo de Benefícios
python pergunta_4.py
```

## 📝 Descrição das Perguntas

### Pergunta 1: Verificação de String
**Objetivo:** Determinar se uma string começa com 'B' e termina com 'A'.

**Solução:** Utiliza os métodos nativos `startswith()` e `endswith()` do Python.

**Funcionalidades:**
- Verificação case-sensitive
- Verificação case-insensitive (função adicional)
- Tratamento de strings vazias

**Complexidade:** O(1)

---

### Pergunta 2: Sequência Aritmética
**Objetivo:** Calcular o valor em uma posição específica da sequência: 11, 18, 25, 32, 39...

**Solução:** Progressão aritmética com:
- Primeiro termo (a₁) = 11
- Razão (r) = 7
- Fórmula: aₙ = a₁ + (n-1) × r

**Funcionalidades:**
- Cálculo direto da posição
- Função inversa (dado valor, retorna posição)
- Gerador de sequência

**Complexidade:** O(1)

**Exemplos de uso:**
```python
print_valor(1)        # Retorna: 11
print_valor(200)      # Retorna: 1404
print_valor(3542158)  # Retorna: 24795110
```

---

### Pergunta 3: Jogo de Tabuleiro
**Objetivo:** Analisar um jogo de tabuleiro unidirecional com roleta.

**Regras do Jogo:**
- Roleta sorteia: 1, 2 ou 3 casas
- Se ultrapassar o final, faz looping (reinicia)
- Vence quem chegar exatamente na última casa

**Solução:** Implementa três análises:

1. **Caminho Ótimo (Programação Dinâmica)**
   - Calcula o número mínimo de turnos
   - Complexidade: O(n)

2. **Probabilidade do Caminho Ótimo**
   - Calcula a chance de executar o caminho perfeito
   - Considera distribuição uniforme (1/3 para cada resultado)

3. **Combinações sem Looping**
   - Conta todas as sequências válidas de movimentos
   - Usa programação dinâmica com memoização

**Exemplos de resultados:**
```
3 casas  → 1 turno,  33.33% prob, 3 combinações
5 casas  → 2 turnos, 22.22% prob, 7 combinações
10 casas → 4 turnos, 4.12% prob,  86 combinações
```

---

### Pergunta 4: Cálculo de Benefícios Trabalhistas
**Objetivo:** Calcular férias e décimo terceiro proporcionais na rescisão.

**Regras:**
- **Férias:** Zeram a cada aniversário de emprego
  - Proporcionais aos meses desde o último aniversário
  - Adicional de 1/3 constitucional
  
- **Décimo Terceiro:** Zera a cada virada de ano
  - Proporcional aos meses trabalhados no ano
  - Considera mês completo se trabalhou 15+ dias

**Solução:**
- Cálculo preciso de meses proporcionais
- Tratamento de anos bissextos
- Relatório detalhado formatado

**Funcionalidades:**
- Validação de datas e valores
- Cálculos separados para cada benefício
- Geração de relatório completo

---

## 🧠 Análise Técnica

### Pergunta 1 - Escalabilidade e Manutenibilidade
**Pontos Fortes:**
- Solução simples e direta usando métodos nativos
- Fácil de entender e manter
- Duas versões (case-sensitive e case-insensitive) para flexibilidade

---

### Pergunta 2 - Escalabilidade e Manutenibilidade
**Pontos Fortes:**
- Complexidade O(1) - extremamente eficiente mesmo para valores grandes
- Fórmula matemática direta sem loops
- Função inversa adicional agrega valor

---

### Pergunta 3 - Escalabilidade e Manutenibilidade
**Pontos Fortes:**
- Uso de programação dinâmica garante eficiência
- Memoização com `lru_cache` otimiza cálculos repetidos
- Solução elegante para problema complexo

**Considerações:**
- Para tabuleiros muito grandes (n > 10000), pode consumir mais memória
- A contagem de combinações cresce exponencialmente

---

### Pergunta 4 - Escalabilidade e Manutenibilidade
**Pontos Fortes:**
- Separação clara de responsabilidades (cada cálculo em função própria)
- Tratamento robusto de casos especiais (anos bissextos, diferentes datas)
- Documentação clara das regras trabalhistas


## 📊 Requisitos

- Python 3.8+
- Nenhuma dependência externa (usa apenas biblioteca padrão)

## 🧪 Testes

Cada arquivo possui uma seção `if __name__ == "__main__"` com testes demonstrativos.

---

## 👨‍💻 Autor

Desenvolvido como parte de um desafio de processo seletivo.

## 📄 Licença

Este projeto é de uso educacional.

