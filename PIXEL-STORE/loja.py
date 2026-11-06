# Pixel Pátio - Loja de jogos digitais (versão terminal)

import textwrap

# ================================
# CONFIGURAÇÕES
# ================================

NOME_DA_LOJA = "PIXEL STORE"
ARQUIVO_PEDIDOS = "pedidos.txt"
FORMAS_DE_PAGAMENTO = ["Pix", "Cartão de crédito", "Boleto"]


# ================================
# CATÁLOGO DE JOGOS
# ================================

# Lista de dicionários: cada dicionário é um jogo da loja
# Preço 0.0 significa que o jogo é gratuito
JOGOS = [
    {
        "id": 1,
        "titulo": "Phasmophobia",
        "genero": "Terror",
        "plataforma": "PC",
        "preco": 59.99,
        "ano": 2020,
        "descricao": (
            "Terror cooperativo para até 4 jogadores: use equipamentos de "
            "caça-fantasmas, colete evidências e descubra que tipo de "
            "espírito assombra a casa."
        )
    },
    {
        "id": 2,
        "titulo": "Counter-Strike 2",
        "genero": "Tiro",
        "plataforma": "PC",
        "preco": 0.0,
        "ano": 2023,
        "descricao": (
            "O clássico FPS tático competitivo: duas equipes, rodadas "
            "curtas, economia de armas e muita precisão. Gratuito para "
            "jogar."
        )
    },
    {
        "id": 3,
        "titulo": "Minecraft",
        "genero": "Sandbox",
        "plataforma": "PC",
        "preco": 129.99,
        "ano": 2011,
        "descricao": (
            "Construa, minere, explore e sobreviva em mundos infinitos "
            "feitos de blocos, sozinho ou com amigos. Inclui as edições "
            "Java e Bedrock."
        )
    },
    {
        "id": 4,
        "titulo": "Valorant",
        "genero": "Tiro",
        "plataforma": "PC",
        "preco": 0.0,
        "ano": 2020,
        "descricao": (
            "FPS tático 5 contra 5 com agentes de habilidades únicas. Mire "
            "bem, use as habilidades certas e domine o mapa. Gratuito para "
            "jogar."
        )
    },
    {
        "id": 5,
        "titulo": "Fortnite",
        "genero": "Battle Royale",
        "plataforma": "Multi",
        "preco": 0.0,
        "ano": 2017,
        "descricao": (
            "Cem jogadores, uma ilha e só um vencedor. Construa, lute e "
            "participe de eventos ao vivo. Gratuito e disponível em várias "
            "plataformas."
        )
    },
    {
        "id": 6,
        "titulo": "Forza Horizon 6",
        "genero": "Corrida",
        "plataforma": "PC/Xbox",
        "preco": 299.0,
        "ano": 2026,
        "descricao": (
            "Corrida em mundo aberto ambientada no Japão, com centenas de "
            "carros, festivais e corridas para correr com amigos."
        )
    },
    {
        "id": 7,
        "titulo": "GTA V",
        "genero": "Ação",
        "plataforma": "PC",
        "preco": 149.9,
        "ano": 2013,
        "descricao": (
            "Três protagonistas, uma cidade enorme e muito crime. Inclui a "
            "versão Enhanced para PC e acesso ao GTA Online."
        )
    },
    {
        "id": 8,
        "titulo": "R.E.P.O.",
        "genero": "Terror",
        "plataforma": "PC",
        "preco": 19.99,
        "ano": 2025,
        "descricao": (
            "Cooperativo de terror e comédia física: recupere objetos "
            "valiosos em locais assombrados sem deixar que eles (ou os "
            "monstros) se quebrem."
        )
    },
    {
        "id": 9,
        "titulo": "The Last of Us Part I",
        "genero": "Aventura",
        "plataforma": "PC/PS5",
        "preco": 199.9,
        "ano": 2022,
        "descricao": (
            "Joel e Ellie atravessam um mundo devastado em uma das "
            "histórias mais marcantes dos games, agora completa no PC."
        )
    },
    {
        "id": 10,
        "titulo": "The Last of Us Part II",
        "genero": "Aventura",
        "plataforma": "PC/PS5",
        "preco": 249.9,
        "ano": 2020,
        "descricao": (
            "Continuação emocionante e intensa, com combate brutal, "
            "furtividade e uma narrativa sobre perda e vingança."
        )
    },
    {
        "id": 11,
        "titulo": "Resident Evil 4",
        "genero": "Terror",
        "plataforma": "PC/PS5",
        "preco": 199.9,
        "ano": 2023,
        "descricao": (
            "Remake do clássico de terror e ação: Leon S. Kennedy precisa "
            "resgatar a filha do presidente em uma vila misteriosa."
        )
    },
    {
        "id": 12,
        "titulo": "EA SPORTS FC 27",
        "genero": "Esporte",
        "plataforma": "PC",
        "preco": 299.0,
        "ano": 2026,
        "descricao": (
            "O simulador de futebol da EA com Carreira, Ultimate Team, "
            "Clubes e as principais ligas e seleções."
        )
    },
    {
        "id": 13,
        "titulo": "Hogwarts Legacy",
        "genero": "RPG",
        "plataforma": "PC",
        "preco": 249.99,
        "ano": 2023,
        "descricao": (
            "RPG de mundo aberto no universo de Harry Potter: frequente "
            "aulas, aprenda feitiços e descubra os segredos de Hogwarts."
        )
    },
    {
        "id": 14,
        "titulo": "Cyberpunk 2077",
        "genero": "RPG",
        "plataforma": "PC",
        "preco": 199.9,
        "ano": 2020,
        "descricao": (
            "RPG de ação em Night City: personalize seu mercenário V, faça "
            "escolhas e enfrente uma conspiração em um futuro sombrio."
        )
    },
    {
        "id": 15,
        "titulo": "God of War Ragnarök",
        "genero": "Ação",
        "plataforma": "PC/PS5",
        "preco": 249.9,
        "ano": 2022,
        "descricao": (
            "Kratos e Atreus enfrentam o Fimbulwinter e os deuses nórdicos "
            "em uma aventura épica de combate visceral."
        )
    },
    {
        "id": 16,
        "titulo": "Dead by Daylight",
        "genero": "Terror",
        "plataforma": "PC",
        "preco": 59.99,
        "ano": 2016,
        "descricao": (
            "Terror multiplayer assimétrico: um assassino contra quatro "
            "sobreviventes. Escape ou cace, em partidas cheias de tensão."
        )
    },
    {
        "id": 17,
        "titulo": "Crimson Desert Enhanced",
        "genero": "Aventura",
        "plataforma": "PC/PS5",
        "preco": 279.99,
        "ano": 2026,
        "descricao": (
            "RPG de ação em mundo aberto com combate espetacular. A versão "
            "Enhanced traz cenas novas e dublagem em português do Brasil."
        )
    },
    {
        "id": 18,
        "titulo": "DayZ",
        "genero": "Sobrevivência",
        "plataforma": "PC",
        "preco": 129.99,
        "ano": 2018,
        "descricao": (
            "Sobrevivência em mundo aberto cheio de zumbis e outros "
            "jogadores. Encontre recursos, forme grupos e tente chegar vivo "
            "ao amanhã."
        )
    },
    {
        "id": 19,
        "titulo": "Battlefield 6",
        "genero": "Tiro",
        "plataforma": "PC",
        "preco": 299.0,
        "ano": 2025,
        "descricao": (
            "FPS de guerra total com grandes mapas, veículos, destruição e "
            "partidas multiplayer para dezenas de jogadores."
        )
    },
    {
        "id": 20,
        "titulo": "Nomad Drive",
        "genero": "Simulação",
        "plataforma": "PC",
        "preco": 39.99,
        "ano": 2026,
        "descricao": (
            "Conserte um trailer abandonado e viaje por um mundo pós- "
            "apocalíptico, cozinhando, plantando e sobrevivendo sozinho ou "
            "com até 3 amigos."
        )
    }
]


# ================================
# FUNÇÕES AUXILIARES
# ================================

# Função que transforma um número em texto de preço (ex: 59.9 vira "R$ 59,90")
def formatar_preco(valor):
    if valor == 0:
        return "Grátis"

    # O :.2f deixa sempre 2 casas decimais e o replace troca o ponto pela vírgula
    return f"R$ {valor:.2f}".replace(".", ",")


# Função que lê um número inteiro dentro de um intervalo
# Usa try/except para o programa não quebrar se o usuário digitar uma letra
def ler_numero(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem)

        try:
            numero = int(entrada)
        except ValueError:
            # O int() dá ValueError quando o texto não é um número
            print("\n  ⚠️  Digite apenas números!\n")
            continue

        if numero < minimo or numero > maximo:
            print(f"\n  ⚠️  Digite um número entre {minimo} e {maximo}!\n")
            continue

        return numero


# Função que lê S ou N e devolve True para sim e False para não
def ler_sim_nao(mensagem):
    while True:
        resposta = input(mensagem).upper()

        if resposta == "S":
            return True
        elif resposta == "N":
            return False
        else:
            print("\n  ⚠️  Digite S para sim ou N para não.\n")


# Função que soma o preço de todos os jogos do carrinho
def calcular_total(carrinho):
    total = 0

    for jogo in carrinho:
        total += jogo["preco"]

    return total


# Função que procura um jogo pelo id dentro de uma lista
# Retorna o jogo encontrado ou None se o id não estiver na lista
def buscar_jogo_por_id(lista, id_jogo):
    for jogo in lista:
        if jogo["id"] == id_jogo:
            return jogo

    return None


# Função que desenha uma caixa com título e linhas de texto
# O ljust completa o texto com espaços para a moldura ficar alinhada
def exibir_caixa(titulo, linhas):
    largura = 46

    print("\n╔" + "═" * largura + "╗")
    print("║" + titulo.center(largura) + "║")
    print("╠" + "═" * largura + "╣")
    for linha in linhas:
        print("║" + linha.ljust(largura) + "║")
    print("╚" + "═" * largura + "╝\n")


# ================================
# FUNÇÕES DE MENU
# ================================

# Função que exibe a tela de boas vindas da loja
def exibir_bemvindo():
    exibir_caixa(NOME_DA_LOJA, [
        "",
        "   Jogos digitais com a chave no seu e-mail!",
        "",
        "   Aqui você pode:",
        "    - ver o catálogo e buscar jogos",
        "    - montar o seu carrinho",
        "    - finalizar a compra",
        "",
        "   Projeto de estudo: os jogos e preços são",
        "   de exemplo e nenhum pagamento é real.",
        ""
    ])


# Função que exibe as opções do menu principal
def exibir_menu(carrinho):
    exibir_caixa("O QUE VOCÊ DESEJA FAZER?", [
        "",
        "   1) Ver catálogo completo",
        "   2) Buscar jogo pelo nome",
        "   3) Filtrar por gênero",
        "   4) Ver detalhes de um jogo",
        "   5) Ver carrinho",
        "   6) Finalizar compra",
        "   7) Sair",
        ""
    ])
    print(f"  🛒 Itens no carrinho: {len(carrinho)}\n")


# ================================
# FUNÇÕES DO CATÁLOGO
# ================================

# Função que exibe uma lista de jogos em forma de tabela
def exibir_lista(lista, titulo):
    print("\n  " + "═" * 62)
    print(f"  🎮 {titulo}")
    print("  " + "═" * 62)

    if len(lista) == 0:
        print("\n  Nenhum jogo encontrado.\n")
        return

    print(f"  {'Nº':>2} │ {'JOGO':<24} │ {'GÊNERO':<14} │ {'PLAT.':<8} │ PREÇO")
    print("  " + "─" * 62)

    for jogo in lista:
        preco = formatar_preco(jogo["preco"])
        print(
            f"  {jogo['id']:>2} │ {jogo['titulo']:<24} │ {jogo['genero']:<14}"
            f" │ {jogo['plataforma']:<8} │ {preco}"
        )

    print("  " + "─" * 62 + "\n")


# Função que adiciona um jogo ao carrinho
def adicionar_ao_carrinho(carrinho, jogo):
    # Jogo digital: só pode ter uma cópia de cada jogo no carrinho
    if jogo in carrinho:
        print(f"\n  ℹ️  {jogo['titulo']} já está no seu carrinho.\n")
    else:
        carrinho.append(jogo)
        print(f"\n  ✅ {jogo['titulo']} foi adicionado ao carrinho!\n")


# Função que exibe a lista de jogos e deixa o usuário adicionar ao carrinho
# Recebe a lista que será mostrada (catálogo inteiro, resultado de busca, etc.)
def mostrar_e_comprar(lista, titulo, carrinho):
    exibir_lista(lista, titulo)

    if len(lista) == 0:
        input("  Pressione ENTER para continuar...")
        return

    while True:
        id_jogo = ler_numero(
            "  Número do jogo para adicionar ao carrinho (0 = voltar): ",
            0, len(JOGOS)
        )

        if id_jogo == 0:
            break

        # Só deixa adicionar jogos que aparecem na lista mostrada
        jogo = buscar_jogo_por_id(lista, id_jogo)

        if jogo is None:
            print("\n  ⚠️  Esse jogo não está na lista exibida!\n")
        else:
            adicionar_ao_carrinho(carrinho, jogo)


# Função que procura jogos pelo nome e mostra os resultados
def buscar_por_nome(carrinho):
    termo = input("\n  Digite parte do nome do jogo: ").strip().lower()
    resultados = []

    for jogo in JOGOS:
        # lower() deixa tudo minúsculo para a busca ignorar maiúsculas
        if termo in jogo["titulo"].lower():
            resultados.append(jogo)

    mostrar_e_comprar(resultados, f"RESULTADO DA BUSCA: {termo}", carrinho)


# Função que mostra os gêneros e filtra o catálogo pelo gênero escolhido
def filtrar_por_genero(carrinho):
    generos = []

    # Monta a lista de gêneros sem repetir nenhum
    for jogo in JOGOS:
        if jogo["genero"] not in generos:
            generos.append(jogo["genero"])

    # Coloca os gêneros em ordem alfabética
    generos.sort()

    print("\n  GÊNEROS DISPONÍVEIS:\n")
    for posicao in range(len(generos)):
        print(f"  {posicao + 1}) {generos[posicao]}")
    print("  0) Voltar\n")

    escolha = ler_numero("  Escolha um gênero: ", 0, len(generos))

    if escolha == 0:
        return

    genero_escolhido = generos[escolha - 1]
    filtrados = []

    for jogo in JOGOS:
        if jogo["genero"] == genero_escolhido:
            filtrados.append(jogo)

    mostrar_e_comprar(filtrados, f"GÊNERO: {genero_escolhido}", carrinho)


# Função que mostra todos os detalhes de um jogo
def ver_detalhes(carrinho):
    id_jogo = ler_numero("\n  Número do jogo (0 = voltar): ", 0, len(JOGOS))

    if id_jogo == 0:
        return

    jogo = buscar_jogo_por_id(JOGOS, id_jogo)

    print("\n  " + "═" * 50)
    print(f"  🎮 {jogo['titulo']}")
    print(f"  {jogo['genero']} · {jogo['plataforma']} · {jogo['ano']}")
    print(f"  Preço: {formatar_preco(jogo['preco'])}")
    print("  " + "─" * 50)
    # O textwrap.fill quebra o texto longo em linhas de até 50 caracteres
    print(textwrap.fill(jogo["descricao"], width=50,
                        initial_indent="  ", subsequent_indent="  "))
    print("  " + "═" * 50 + "\n")

    if ler_sim_nao("  Adicionar ao carrinho? (S/N): "):
        adicionar_ao_carrinho(carrinho, jogo)


# ================================
# FUNÇÕES DO CARRINHO
# ================================

# Função que exibe os jogos do carrinho e o total
def exibir_carrinho(carrinho):
    print("\n  " + "═" * 50)
    print("  🛒 SEU CARRINHO")
    print("  " + "═" * 50)

    if len(carrinho) == 0:
        print("\n  Seu carrinho está vazio.\n")
        return

    for posicao in range(len(carrinho)):
        jogo = carrinho[posicao]
        print(f"  {posicao + 1}) {jogo['titulo']:<26} {formatar_preco(jogo['preco']):>10}")

    print("  " + "─" * 50)
    print(f"  TOTAL: {formatar_preco(calcular_total(carrinho))}")
    print("  " + "═" * 50 + "\n")


# Função que controla o menu do carrinho
def menu_do_carrinho(carrinho):
    while True:
        exibir_carrinho(carrinho)

        if len(carrinho) == 0:
            input("  Pressione ENTER para continuar...")
            break

        print("  1) Remover um jogo")
        print("  2) Esvaziar o carrinho")
        print("  3) Finalizar compra")
        print("  4) Voltar\n")

        opcao = ler_numero("  Escolha uma opção: ", 1, 4)

        if opcao == 1:
            posicao = ler_numero("  Número do jogo para remover: ", 1, len(carrinho))
            removido = carrinho.pop(posicao - 1)
            print(f"\n  🗑️  {removido['titulo']} foi removido.\n")
        elif opcao == 2:
            carrinho.clear()
            print("\n  🗑️  Carrinho esvaziado.\n")
        elif opcao == 3:
            if finalizar_compra(carrinho):
                break
        elif opcao == 4:
            break


# ================================
# FUNÇÕES DO PEDIDO
# ================================

# Função que lê o nome do cliente e só aceita nomes com 3 letras ou mais
def ler_nome():
    while True:
        nome = input("\n  Nome completo: ").strip()

        if len(nome) < 3:
            print("\n  ⚠️  Informe seu nome completo.\n")
        else:
            return nome


# Função que confere se o e-mail tem um formato válido
def email_valido(email):
    if " " in email:
        return False

    # Precisa ter exatamente um @
    if email.count("@") != 1:
        return False

    partes = email.split("@")
    usuario = partes[0]
    dominio = partes[1]

    # Precisa ter algo antes do @ e um ponto depois dele
    return len(usuario) > 0 and "." in dominio


# Função que lê o e-mail do cliente até ele digitar um e-mail válido
def ler_email():
    while True:
        email = input("  E-mail (as chaves chegam aqui): ").strip()

        if email_valido(email):
            return email
        else:
            print("\n  ⚠️  Informe um e-mail válido!\n")


# Função que mostra as formas de pagamento e devolve a escolhida
def escolher_pagamento():
    print("\n  FORMA DE PAGAMENTO:\n")

    for posicao in range(len(FORMAS_DE_PAGAMENTO)):
        print(f"  {posicao + 1}) {FORMAS_DE_PAGAMENTO[posicao]}")

    escolha = ler_numero("\n  Escolha uma forma de pagamento: ", 1, len(FORMAS_DE_PAGAMENTO))

    return FORMAS_DE_PAGAMENTO[escolha - 1]


# Função que descobre o número do próximo pedido lendo o arquivo de pedidos
# Se o arquivo ainda não existe (primeiro pedido), o try/except trata o erro
def proximo_numero_pedido():
    try:
        with open(ARQUIVO_PEDIDOS, "r", encoding="utf-8") as arquivo:
            quantidade = 0
            for linha in arquivo:
                if linha.startswith("PEDIDO #"):
                    quantidade += 1
            return quantidade + 1
    except OSError:
        # Arquivo não existe ainda (ou não pôde ser lido), então é o pedido número 1
        return 1


# Função que grava o pedido no arquivo de texto
# Retorna True se salvou e False se deu erro (ex: sem permissão para gravar)
def salvar_pedido(numero, nome, email, pagamento, carrinho, total):
    try:
        # O modo "a" (append) adiciona no final sem apagar os pedidos antigos
        with open(ARQUIVO_PEDIDOS, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"PEDIDO #{numero}\n")
            arquivo.write(f"Cliente: {nome} ({email})\n")
            arquivo.write(f"Pagamento: {pagamento}\n")
            for jogo in carrinho:
                arquivo.write(f"  - {jogo['titulo']} ({jogo['plataforma']}): {formatar_preco(jogo['preco'])}\n")
            arquivo.write(f"Total: {formatar_preco(total)}\n")
            arquivo.write("-" * 40 + "\n")
        return True
    except OSError:
        print("\n  ⚠️  Não foi possível salvar o pedido no arquivo.\n")
        return False


# Função que controla a finalização da compra
# Retorna True se o pedido foi concluído e False se foi cancelado
def finalizar_compra(carrinho):
    if len(carrinho) == 0:
        print("\n  Seu carrinho está vazio. Escolha um jogo para continuar.\n")
        input("  Pressione ENTER para continuar...")
        return False

    exibir_carrinho(carrinho)

    nome = ler_nome()
    email = ler_email()
    pagamento = escolher_pagamento()
    total = calcular_total(carrinho)

    print("\n  " + "═" * 50)
    print("  📋 RESUMO DO PEDIDO")
    print(f"  Cliente:   {nome}")
    print(f"  E-mail:    {email}")
    print(f"  Pagamento: {pagamento}")
    print(f"  Total:     {formatar_preco(total)}")
    print("  " + "═" * 50 + "\n")

    if not ler_sim_nao("  Confirmar o pedido? (S/N): "):
        print("\n  Pedido cancelado. Seu carrinho foi mantido.\n")
        return False

    numero = proximo_numero_pedido()
    salvou = salvar_pedido(numero, nome, email, pagamento, carrinho, total)

    print("\n  " + "═" * 50)
    print(f"  🎉 PEDIDO #{numero} CONFIRMADO!")
    print(f"  Obrigado, {nome}! As chaves serão enviadas para {email}.")
    if salvou:
        print(f"  (Pedido gravado em {ARQUIVO_PEDIDOS})")
    print("  " + "═" * 50 + "\n")

    # Esvazia o carrinho depois da compra
    carrinho.clear()
    input("  Pressione ENTER para continuar...")
    return True


# ================================
# FUNÇÃO PRINCIPAL
# ================================

# Função principal que controla o loop do menu da loja
def iniciar_loja():
    # O carrinho é uma lista que guarda os jogos escolhidos
    carrinho = []

    exibir_bemvindo()

    while True:
        exibir_menu(carrinho)
        opcao = ler_numero("DIGITE O NUMERO DA OPÇÃO: ", 1, 7)

        if opcao == 1:
            mostrar_e_comprar(JOGOS, "CATÁLOGO COMPLETO", carrinho)
        elif opcao == 2:
            buscar_por_nome(carrinho)
        elif opcao == 3:
            filtrar_por_genero(carrinho)
        elif opcao == 4:
            ver_detalhes(carrinho)
        elif opcao == 5:
            menu_do_carrinho(carrinho)
        elif opcao == 6:
            finalizar_compra(carrinho)
        elif opcao == 7:
            print("\n  Obrigado pela visita, volte sempre!\n")
            break


iniciar_loja()