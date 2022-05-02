from random import randrange

def palavra_secreta():
    palavras = ["Bigode", "Cadeira", "Doce", "Mola", "Assobio", "Sobrancelhas", "Lamente", "Pimenta", "Capacete", "Limpo", "Estanho", "Mala", "Soldado", "Torneira", "Dinheiro", "Peixe", "Garrafa", "Joelho", "Melancia", "Ovos"]

    # Escolha aleatória de um número entre 0 e comprimento da lista de palavras
    num = randrange(0, len(palavras))
    ps = palavras[num].upper()
  
    return ps

# Função que preenche uma lista com "_" as letras de acordo com a quantidade de letras da palavra secreta
def censura(palavra_secreta):
  
  cens = ["_" for letra in palavra_secreta]
  
  return cens

# Função que marca acertos do usuário substituindo os "_" pelas letras corretas
def marca_acerto(chute, letras_acertadas, palavra_secreta):

  # Contador do comprimento da palavra secreta
  for i in range(len(palavra_secreta)):
    # Loop que passa em cada letra da palavra secreta
    for l in palavra_secreta:
        # Condição que verifica o chute com as letras da palavra secreta
        if chute == l:
            # Substituição do chute certo com as letras da palavra secreta
            letras_acertadas[i] = l



def jogo(palavra_secreta):

  # Seleção e Censura da palavra secreta aleatória
  resposta = censura(palavra_secreta)

  # Condições para acabar o jogo
  ganhou = False
  perdeu = False

  erros = 0
  tentativas = 5
  lista_erros = []
  faltando = len(resposta)

  print("Tente acertar a palavra de {0} letras".format(len(resposta)))

  # Loop que verifica se o jogo não acabou ainda
  while not ganhou or not perdeu:

    # Input do chute do usuário
    chute = input("\nDigita uma letra: ").upper()

    # Condição que verifica se o chute está correto
    if chute in palavra_secreta:

      # Chama a função que substitui os "_" pelo chute correto
      marca_acerto(chute, resposta, palavra_secreta)
      # Conta quantos "_" restam ainda
      faltando = resposta.count('_')
      
      print(resposta)
      print("Letras erradas: ", lista_erros)

    else:
      # Condição que adiciona as letras erradas em uma lista
      print("A letra '{0}' não está na palavra.\n".format(chute))
      if chute not in lista_erros:
        lista_erros.append(chute)
  
        erros += 1
        
        print(resposta)
        print("\nLetras erradas: ", lista_erros)
        print("\nAinda faltam {0} letras.".format(faltando))
        print("Você tem {0} tentativas.".format(tentativas-erros))

    # Verifica as condições para acabar o jogo sendo 6 o número de tentativas caso erre
    if erros == 5:
      perdeu = True
    elif "_" not in resposta:
      ganhou = True
      
  if ganhou:
    print("\nVocê ganhou parabéns!")
  else:
    print("\nVocê perdeu a palavra era: {0}!".format(palavra_secreta))
    print("Fim do jogo...")

# Inicialização do jogo 
jogo(palavra_secreta())
