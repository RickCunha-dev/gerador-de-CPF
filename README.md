# 🪪 Gerador e Validador de CPF

Projeto desenvolvido como exercício prático da Udemy sem IA, com foco em aplicar e consolidar conceitos fundamentais de Python — como **list comprehension**, iteráveis eficientes com `range()` e manipulação de strings com `.join()`.

---

## 📋 Sobre o projeto

O programa realiza duas operações principais relacionadas ao CPF (Cadastro de Pessoa Física):

**Opção 1 — Verificar ou completar um CPF:**
- Se o usuário digitar 9 dígitos (com pontos), o programa calcula e gera os dois dígitos verificadores, exibindo o CPF completo e formatado.
- Se o usuário digitar o CPF completo (11 dígitos, com pontos e hífen), o programa valida os dígitos verificadores. Caso estejam incorretos, corrige e exibe o CPF válido.

**Opção 2 — Gerar um CPF aleatório:**
- Gera 9 dígitos aleatórios e calcula os dois dígitos verificadores automaticamente, exibindo um CPF válido e formatado.

---

## 🔢 Como funciona o algoritmo de validação

O CPF segue uma regra matemática oficial para calcular seus dois últimos dígitos (dígitos verificadores):

**Primeiro dígito verificador:**
1. Multiplica cada um dos 9 primeiros dígitos por uma contagem regressiva de 10 a 2.
2. Soma todos os resultados.
3. Multiplica a soma por 10 e divide por 11 (resto da divisão).
4. Se o resto for maior que 9, o dígito é 0; caso contrário, o resto é o próprio dígito.

**Segundo dígito verificador:**
1. Repete o processo acima, agora com os 10 dígitos (incluindo o primeiro verificador).
2. A contagem regressiva vai de 11 a 2.

---

## 🧠 O que foi aprendido e praticado

Este projeto foi desenvolvido de forma iterativa — primeiro de maneira mais verbosa, e depois com a lógica progressivamente compactada. Os principais aprendizados foram:

**List Comprehension** — substituição de loops `for` com `.append()` por expressões mais concisas e legíveis:
```python
# Forma tradicional
digitosMultiplicados = []
for digito, contagem in zip(listaDigitos, contagemRegressiva):
    digitosMultiplicados.append(digito * contagem)

# Com list comprehension
digitosMultiplicados = [digito * contagem for digito, contagem in zip(listaDigitos, contagemRegressiva)]
```

**`range()` como iterável leve** — ao invés de criar uma lista com os multiplicadores (`[10, 9, 8, ..., 2]`), o uso de `range(10, 1, -1)` gera os valores sob demanda, sem ocupar espaço desnecessário na memória.

**`.join()` para reconstruir strings** — para converter uma lista de dígitos de volta a uma string de CPF:
```python
cpfGerado = ''.join(str(d) for d in cpfComDoisDigitos)
```

**`zip()` para percorrer duas listas simultaneamente** — emparelha os dígitos com seus respectivos multiplicadores em um único loop.

**Formatação de CPF com slicing** — exibição no formato `XXX.XXX.XXX-XX` diretamente a partir de uma string de 11 caracteres:
```python
f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
```

---

## ▶️ Como executar

Certifique-se de ter o Python 3 instalado. Em seguida, execute o arquivo pelo terminal:

```bash
python gerador_cpf.py
```

Siga as instruções exibidas no menu interativo.

**Formatos de entrada aceitos:**

| Intenção | Formato esperado | Exemplo |
|---|---|---|
| Gerar CPF a partir de 9 dígitos | `XXX.XXX.XXX` | `133.248.546` |
| Validar/corrigir CPF completo | `XXX.XXX.XXX-XX` | `133.248.546-44` |
| Gerar CPF aleatório | *(sem entrada)* | Selecionar opção 2 |

---

## 📁 Estrutura

```
cpf.py   # Arquivo principal com toda a lógica do programa
```

---

## 🗒️ Observações

- O programa não contempla a regra de CPFs com todos os dígitos iguais (ex: `111.111.111-11`), que são tecnicamente inválidos mesmo passando pelo cálculo matemático.
- Desenvolvido como exercício educacional — o foco está na clareza do algoritmo e na prática dos conceitos de Python, não em uso em produção.

---

*Exercício prático — curso Python na Udemy.*
