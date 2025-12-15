# 🔧 Configuração do Git

## Inicializar Repositório

### 1. Inicializar Git no projeto

```bash
cd /home/vitorhugo/personal-projects/challenge_3s
git init
```

### 2. Configurar informações do usuário (se necessário)

```bash
git config user.name "Seu Nome"
git config user.email "seu.email@exemplo.com"
```

### 3. Adicionar todos os arquivos

```bash
git add .
```

### 4. Fazer o primeiro commit

```bash
git commit -m "feat: implementação completa do desafio de programação

- Pergunta 1: Verificação de string (começa com B, termina com A)
- Pergunta 2: Sequência aritmética com fórmula matemática
- Pergunta 3: Jogo de tabuleiro com programação dinâmica
- Pergunta 4: Cálculo de benefícios trabalhistas

Inclui:
- Código Python com type hints e documentação
- Testes abrangentes para todas as soluções
- Documentação completa (README, APRESENTACAO, RESUMO_EXECUTIVO)
- Script consolidado de testes
- Guia de apresentação"
```

---

## Conectar com GitHub

### 1. Criar repositório no GitHub

Acesse [GitHub](https://github.com/new) e crie um novo repositório vazio.

**Recomendações:**
- Nome: `challenge-3s` ou `desafio-programacao-python`
- Descrição: "Soluções para desafio de programação - 4 perguntas em Python"
- ✅ **Não** marque "Initialize with README" (já temos um)
- Escolha licença se quiser (sugestão: MIT)

### 2. Conectar repositório local ao GitHub

```bash
# Adicionar remote
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git

# Ou com SSH (recomendado)
git remote add origin git@github.com:SEU_USUARIO/NOME_DO_REPO.git

# Verificar remote
git remote -v
```

### 3. Enviar código para o GitHub

```bash
# Renomear branch para main (padrão moderno)
git branch -M main

# Push para o GitHub
git push -u origin main
```

---

## Estrutura do Repositório

Após o commit, seu repositório terá:

```
challenge_3s/
├── .gitignore                    # Arquivos ignorados pelo Git
├── .gitattributes                # Configurações de atributos Git
├── pergunta_1.py                 # Solução 1: Verificação de String
├── pergunta_2.py                 # Solução 2: Sequência Aritmética
├── pergunta_3.py                 # Solução 3: Jogo de Tabuleiro
├── pergunta_4.py                 # Solução 4: Benefícios Trabalhistas
├── run_all_tests.py              # Executor consolidado de testes
├── README.md                     # Documentação técnica principal
├── APRESENTACAO.md               # Explicação detalhada das soluções
├── RESUMO_EXECUTIVO.md           # Resumo executivo
├── GUIA_APRESENTACAO.md          # Guia para apresentação
└── GIT_SETUP.md                  # Este arquivo
```

**Nota:** A pasta `__pycache__/` está no `.gitignore` e não será commitada.

---

## Commits Subsequentes

### Padrão de Mensagens de Commit

Use [Conventional Commits](https://www.conventionalcommits.org/):

```bash
# Nova funcionalidade
git commit -m "feat: adicionar validação de entrada na pergunta 1"

# Correção de bug
git commit -m "fix: corrigir cálculo de meses proporcionais na pergunta 4"

# Documentação
git commit -m "docs: atualizar README com exemplos de uso"

# Refatoração
git commit -m "refactor: separar lógica de cálculo em funções menores"

# Testes
git commit -m "test: adicionar testes unitários com pytest"

# Melhoria de performance
git commit -m "perf: otimizar cálculo de combinações na pergunta 3"
```

### Workflow Recomendado

```bash
# 1. Verificar status
git status

# 2. Ver mudanças
git diff

# 3. Adicionar arquivos específicos
git add pergunta_1.py

# Ou adicionar tudo
git add .

# 4. Fazer commit
git commit -m "tipo: descrição breve"

# 5. Enviar para GitHub
git push
```

---

## Branches (Opcional)

Para desenvolvimento organizado:

```bash
# Criar e mudar para branch de feature
git checkout -b feature/adicionar-testes

# Fazer alterações e commits
git add .
git commit -m "test: adicionar testes unitários"

# Voltar para main
git checkout main

# Fazer merge da feature
git merge feature/adicionar-testes

# Deletar branch após merge
git branch -d feature/adicionar-testes
```

---

## Tags (Versões)

Marcar versões do projeto:

```bash
# Criar tag anotada
git tag -a v1.0.0 -m "Versão 1.0.0 - Implementação completa do desafio"

# Ver tags
git tag

# Push de tags para GitHub
git push origin v1.0.0

# Ou push de todas as tags
git push --tags
```

---

## Arquivo .gitignore Explicado

O `.gitignore` criado ignora:

### Python
- `__pycache__/` - Cache de bytecode Python
- `*.pyc`, `*.pyo` - Arquivos compilados
- `.pytest_cache/` - Cache do pytest
- `venv/`, `.venv/` - Ambientes virtuais

### IDEs
- `.vscode/` - Configurações VS Code
- `.idea/` - Configurações PyCharm
- `*.swp` - Arquivos temporários do Vim

### Sistema Operacional
- `.DS_Store` - Arquivos do macOS
- `Thumbs.db` - Miniaturas do Windows
- `*~` - Backups do Linux

### Outros
- `.env` - Variáveis de ambiente sensíveis
- `*.log` - Arquivos de log
- `*.bak` - Arquivos de backup

---

## Comandos Úteis

```bash
# Ver histórico de commits
git log
git log --oneline
git log --graph --oneline --all

# Desfazer último commit (mantendo alterações)
git reset --soft HEAD~1

# Desfazer alterações em arquivo
git checkout -- pergunta_1.py

# Ver diferenças
git diff
git diff pergunta_1.py

# Ver branches
git branch
git branch -a  # incluindo remotas

# Atualizar do GitHub
git pull

# Clonar repositório
git clone https://github.com/USUARIO/REPO.git
```

---

## Ignorar Arquivos Já Commitados

Se você já commitou arquivos que deveriam ser ignorados:

```bash
# Remover arquivo do Git (mas manter local)
git rm --cached arquivo.txt

# Remover pasta do Git
git rm --cached -r pasta/

# Commit da remoção
git commit -m "chore: remover arquivos que devem ser ignorados"

# Push
git push
```

---

## Boas Práticas

✅ **Commits pequenos e frequentes** - Mais fácil de revisar e reverter

✅ **Mensagens claras** - Explique o "porquê", não apenas o "quê"

✅ **Testar antes de commitar** - Execute `python run_all_tests.py`

✅ **Não commitar dados sensíveis** - Senhas, tokens, chaves API

✅ **Usar .gitignore** - Evita commitar arquivos desnecessários

✅ **README atualizado** - Documentação sempre sincronizada com código

---

## Compartilhar com Recrutadores

Após fazer push para GitHub:

### Link do Repositório
```
https://github.com/SEU_USUARIO/challenge-3s
```

### Destacar no README do GitHub

Certifique-se que o README.md mostra:
- ✅ Descrição clara do projeto
- ✅ Como executar (`python run_all_tests.py`)
- ✅ Tecnologias utilizadas
- ✅ Status dos testes (todos passando)
- ✅ Link para documentação adicional

### Adicionar Badge de Status (opcional)

No README.md, você pode adicionar badges:

```markdown
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Status](https://img.shields.io/badge/status-completed-success.svg)
![Tests](https://img.shields.io/badge/tests-passing-success.svg)
```

---

## Checklist Final

Antes de compartilhar o repositório:

- [ ] Git inicializado e commitado
- [ ] Repositório criado no GitHub
- [ ] Código enviado com `git push`
- [ ] README.md está visível e bem formatado
- [ ] Todos os testes passam (`python run_all_tests.py`)
- [ ] Não há dados sensíveis commitados
- [ ] `.gitignore` está funcionando corretamente
- [ ] Link do repositório está disponível

---

## 🎯 Pronto!

Seu código agora está versionado e disponível no GitHub. Você pode:
- Compartilhar o link com recrutadores
- Mostrar em portfolios
- Continuar desenvolvendo com controle de versão

**Boa sorte no processo seletivo! 🚀**

