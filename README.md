# ⚡ Análise de Grafos: Rede Elétrica

Programa em Python, executado no terminal, que modela uma rede de distribuição de energia como um **grafo direcionado** e permite visualizar a estrutura, listar vértices e arestas e encontrar caminhos entre dois pontos, com análise de **capacidade limitante** e **perdas acumuladas**.

Projeto desenvolvido com fins acadêmicos para praticar **Teoria dos Grafos**, **busca em largura (BFS)** e manipulação de estruturas de dados em Python.

---

## 📌 Sumário

- [Funcionalidades](#-funcionalidades)
- [Modelagem da rede](#-modelagem-da-rede)
- [Como executar](#-como-executar)
- [Exemplo de uso](#-exemplo-de-uso)
- [Como funciona](#-como-funciona)
- [Limitações conhecidas](#-limitações-conhecidas)
- [Possíveis melhorias](#-possíveis-melhorias)
- [Tecnologias](#-tecnologias)

---

## ✨ Funcionalidades

| Opção | Descrição |
|-------|-----------|
| **1 - Visualizar rede elétrica** | Mostra cada ponto da rede com suas conexões, capacidade (kW) e perda (kW). |
| **2 - Listar vértices e arestas** | Exibe a estrutura do grafo e os totais de vértices e arestas. |
| **3 - Encontrar e analisar caminho** | Busca o caminho entre dois pontos e calcula capacidade limitante e soma das perdas. |
| **4 - Sair** | Encerra o programa. |

Extras:

- Entrada de nomes **tolerante**: ignora maiúsculas/minúsculas, acentos e espaços extras (`subestacao 1`, `SUBESTAÇÃO 1` e `Subestação 1` funcionam).
- Atalho para consumidores: digitar apenas `A` equivale a `Consumidor A`.

---

## 🗺️ Modelagem da rede

A rede é um grafo direcionado com **13 vértices** e **12 arestas**, no sentido do fluxo de energia:

```
                         Usina
              ┌────────────┼────────────┐
        Subestação 1  Subestação 2  Subestação 3
         ┌───┼───┐     ┌───┼───┐     ┌───┼───┐
         A   B   C     D   E   F     G   H   I
```

- **Vértices:** a usina, 3 subestações e 9 consumidores.
- **Arestas:** conexões entre eles, cada uma com `capacidade` e `perda` (ambas em kW).
- **Representação:** lista de adjacência (`rede_eletrica`) + dicionário de atributos por aresta (`detalhes_conexoes`).

### Dados das conexões

| Conexão | Capacidade (kW) | Perda (kW) |
|---------|:---:|:---:|
| Usina → Subestação 1 | 100 | 5 |
| Usina → Subestação 2 | 80 | 3 |
| Usina → Subestação 3 | 90 | 4 |
| Subestação 1 → Consumidor A / B / C | 35 / 40 / 25 | 2 / 1 / 2 |
| Subestação 2 → Consumidor D / E / F | 30 / 25 / 25 | 2 / 1 / 0 |
| Subestação 3 → Consumidor G / H / I | 35 / 35 / 20 | 3 / 0 / 1 |

---

## 🚀 Como executar

**Pré-requisito:** Python 3.8 ou superior. Não há dependências externas, só a biblioteca padrão (`collections` e `unicodedata`).

```bash
# 1. Clone o repositório
git clone https://github.com/hugocodez7/RedeEletrica.git

# 2. Entre na pasta
cd RedeEletrica

# 3. Execute
python SistemaEletrico.py
```


---

## 💻 Exemplo de uso

Opção `3`, com origem `Usina` e destino `consumidor b`:

```
Caminho encontrado:
Usina -> Subestação 1 -> Consumidor B

========== ANALISE DO CAMINHO ==========

Usina -> Subestação 1
Capacidade da conexao: 100 kW
Perda cadastrada: 5 kW

Subestação 1 -> Consumidor B
Capacidade da conexao: 40 kW
Perda cadastrada: 1 kW

Resumo do caminho:
Capacidade limitante: 40 kW
Soma das perdas cadastradas: 6 kW
```

---

## 🧠 Como funciona

### Busca de caminho (BFS)

`encontrar_caminho` usa **busca em largura** com uma fila (`deque`). Cada item da fila é o caminho completo percorrido até ali; um conjunto `visitados` evita revisitar vértices. O primeiro caminho que chega ao destino é retornado, e em um grafo não ponderado, o BFS garante o caminho com **menor número de arestas**.

- Complexidade de tempo: **O(V + E)**
- Complexidade de espaço: **O(V)** para a fila e o conjunto de visitados (mais o tamanho dos caminhos armazenados)

### Análise do caminho

Para cada aresta percorrida:

- **Capacidade limitante** = menor capacidade entre as conexões do caminho (o "gargalo", como na lógica de fluxo máximo para um único caminho).
- **Perda total** = soma aritmética das perdas cadastradas em cada aresta.

---

## 🛠️ Tecnologias

- **Python 3**
- `collections.deque` (fila do BFS)
- `unicodedata` (normalização de texto)
