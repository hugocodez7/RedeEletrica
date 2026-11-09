from collections import deque
import unicodedata


rede_eletrica = {
    "Usina": ["Subestação 1", "Subestação 2", "Subestação 3"],
    "Subestação 1": ["Consumidor A", "Consumidor B", "Consumidor C"],
    "Subestação 2": ["Consumidor D", "Consumidor E", "Consumidor F"],
    "Subestação 3": ["Consumidor G", "Consumidor H", "Consumidor I"]
}


detalhes_conexoes = {
    ("Usina", "Subestação 1"): {"capacidade": 100, "perda": 5},
    ("Usina", "Subestação 2"): {"capacidade": 80, "perda": 3},
    ("Usina", "Subestação 3"): {"capacidade": 90, "perda": 4},

    ("Subestação 1", "Consumidor A"): {"capacidade": 35, "perda": 2},
    ("Subestação 1", "Consumidor B"): {"capacidade": 40, "perda": 1},
    ("Subestação 1", "Consumidor C"): {"capacidade": 25, "perda": 2},

    ("Subestação 2", "Consumidor D"): {"capacidade": 30, "perda": 2},
    ("Subestação 2", "Consumidor E"): {"capacidade": 25, "perda": 1},
    ("Subestação 2", "Consumidor F"): {"capacidade": 25, "perda": 0},

    ("Subestação 3", "Consumidor G"): {"capacidade": 35, "perda": 3},
    ("Subestação 3", "Consumidor H"): {"capacidade": 35, "perda": 0},
    ("Subestação 3", "Consumidor I"): {"capacidade": 20, "perda": 1}
}


def normalizar_texto(texto):
    texto = texto.strip().casefold()

    texto = unicodedata.normalize("NFD", texto)

    texto = "".join(
        caractere for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def identificar_ponto(nome, vertices):
    nome_normalizado = normalizar_texto(nome)

    if len(nome_normalizado) == 1 and nome_normalizado in "abcdefghi":
        nome_normalizado = "consumidor " + nome_normalizado

    for vertice in vertices:
        if normalizar_texto(vertice) == nome_normalizado:
            return vertice

    return None


def pegar_todos_os_pontos(rede):
    vertices = []

    for origem, destinos in rede.items():
        if origem not in vertices:
            vertices.append(origem)

        for destino in destinos:
            if destino not in vertices:
                vertices.append(destino)

    return vertices


def mostrar_rede_completa():
    print("\n========== REDE ELETRICA ==========")

    for origem, destinos in rede_eletrica.items():
        print(f"\n{origem}:")

        for destino in destinos:
            dados = detalhes_conexoes[(origem, destino)]

            print(
                f"  -> {destino} "
                f"[Capacidade: {dados['capacidade']} kW"
                f" | Perda: {dados['perda']} kW]"
            )


def mostrar_estrutura_grafo():
    vertices = pegar_todos_os_pontos(rede_eletrica)
    quantidade_arestas = 0

    print("\n========== ESTRUTURA DO GRAFO ==========")

    print("\nVertices:")

    for vertice in vertices:
        print(f"- {vertice}")

    print("\nArestas:")

    for origem, destinos in rede_eletrica.items():
        for destino in destinos:
            print(f"{origem} -> {destino}")
            quantidade_arestas += 1

    print(f"\nTotal de vertices: {len(vertices)}")
    print(f"Total de arestas: {quantidade_arestas}")


def encontrar_caminho(origem, destino):
    fila = deque([[origem]])
    visitados = {origem}

    while fila:
        caminho = fila.popleft()
        atual = caminho[-1]

        if atual == destino:
            return caminho

        for vizinho in rede_eletrica.get(atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)

                novo_caminho = caminho + [vizinho]

                fila.append(novo_caminho)

    return None


def analisar_caminho(caminho):
    if len(caminho) == 1:
        print("\nOrigem e destino sao o mesmo vertice.")
        print("Nenhuma conexao precisa ser percorrida.")
        return

    capacidade_minima = float("inf")
    perda_total = 0

    print("\n========== ANALISE DO CAMINHO ==========")

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]

        dados = detalhes_conexoes[(origem, destino)]

        capacidade = dados["capacidade"]
        perda = dados["perda"]

        capacidade_minima = min(capacidade_minima, capacidade)
        perda_total += perda

        print(f"\n{origem} -> {destino}")
        print(f"Capacidade da conexao: {capacidade} kW")
        print(f"Perda cadastrada: {perda} kW")

    print("\nResumo do caminho:")
    print(f"Capacidade limitante: {capacidade_minima} kW")
    print(f"Soma das perdas cadastradas: {perda_total} kW")


def consultar_caminho():
    vertices = pegar_todos_os_pontos(rede_eletrica)

    print("\n========== ENCONTRAR CAMINHO ==========")
    print("Pontos disponiveis:")

    for vertice in vertices:
        print(f"- {vertice}")

    origem_digitada = input("\nPonto de origem: ")
    destino_digitado = input("Ponto de destino: ")

    origem = identificar_ponto(origem_digitada, vertices)
    destino = identificar_ponto(destino_digitado, vertices)

    if origem is None or destino is None:
        print("\nErro: um dos pontos nao existe na rede.")
        return

    caminho = encontrar_caminho(origem, destino)

    if caminho is None:
        print("\nNao existe caminho entre esses pontos.")
        return

    print("\nCaminho encontrado:")
    print(" -> ".join(caminho))

    analisar_caminho(caminho)


def menu():
    opcao = ""

    while opcao != "4":
        print("\n========================================")
        print("     ANALISE DE GRAFOS - REDE ELETRICA")
        print("========================================")
        print("1 - Visualizar rede eletrica")
        print("2 - Listar vertices e arestas")
        print("3 - Encontrar e analisar caminho")
        print("4 - Sair")
        print("========================================")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            mostrar_rede_completa()

        elif opcao == "2":
            mostrar_estrutura_grafo()

        elif opcao == "3":
            consultar_caminho()

        elif opcao == "4":
            print("Encerrando o programa...")

        else:
            print("Opcao invalida. Tente novamente.")


menu()