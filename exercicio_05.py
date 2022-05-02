from random import *

# Função que usa a lista de palavras secretas para escolher uma aleatóriamente
def palavra_secreta():
    palavras = ["Bigode", "Cadeira", "Doce", "Mola", "Assobio", "Sobrancelhas", "Lamente", "Pimenta", "Capacete", "Limpo", "Estanho", "Mala", "Soldado", "Torneira", "Dinheiro", "Peixe", "Garrafa", "Joelho", "Melancia", "Ovos"]

    # Escolha aleatória de um número entre 0 e comprimento da lista
    num = randrange(0, len(palavras))
    ps = palavras[num].upper()
  
    return ps

# Função que preenche uma lista com "_" as letras de acordo com a quantidade de letras da palavra secreta
def letras_certas(p):
    return ["_" for letra in p]

# Função para chutes do usuário
def chute():
    c = input("\nDigite uma letra: ")
    c = c.strip().upper()
    return c

# Função que marca acertos do usuário e substitui os "_" pelas letras
def marca_acerto(letra, letras_acertadas, palavra_secreta):
    i = 0
    # Loop que passa em cada letra da palavra secreta
    for l in palavra_secreta:
        # Condição que verifica o chute com as letras da palavra secreta
        if letra == l:
            # Substituição do chute certo com as letras da palavra secreta
            letras_acertadas[i] = l
        i += 1

# Função que roda o jogo
def jogo():

    # Pega a palavra secreta
    ps = palavra_secreta()

    # Lista da palavra secreta com "_" no lugar das letras
    acertos = letras_certas(ps)

    # Condições para acabar o jogo
    morreu = False
    ganhou = False
  
    erros = 0
    l_erros = []
    faltando = len(acertos)

    # Imprime a palavra com "_" ou letras caso acertou
    print(letras_certas)

    # Loop que verifica se o jogo não acabou ainda
    while not ganhou and not morreu:

        # Chute do usuário
        c = chute()

        # Condição que verifica se o chute está correto
        if c in ps:
            # Chama a função que substitui os "_" pelo chute correto
            marca_acerto(c, acertos, ps)
            # Conta quantos "_" restam ainda
            faltando = acertos.count('_')
            print("Letras erradas: ", l_erros)
            if faltando == 0:
                print("\nVocê acertou! A palavra era {0}.".format(ps.upper()))
        else:
          # Condição que adiciona as letras erradas em uma lista
          if c not in l_erros:
            l_erros.append(c)
  
          erros += 1
          print(acertos)
          print("Letras erradas: ", l_erros)
          print('\nAinda faltam {0} letras.'.format(faltando))
          print('\nVocê tem {0} tentativas.'.format(6-erros))

        # Verifica as condições para acabar o jogo sendo 6 o número de tentativas caso erre
        if erros == 6:
          morreu = True
        elif "_" not in acertos:
          ganhou = True

        print(acertos)

    if ganhou:
        print("\nVocê ganhou parabéns!")
    else:
        print("\nVocê perdeu a palavra era: {0}!".format(ps))

    print("Fim do jogo...")

# Inicialização do jogo 
jogo()
