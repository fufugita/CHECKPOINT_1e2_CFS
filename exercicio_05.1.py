from random import randrange

def palavra_secreta():
    palavras = ["Bigode", "Cadeira", "Doce", "Mola", "Assobio", "Sobrancelhas", "Lamente", "Pimenta", "Capacete", "Limpo", "Estanho", "Mala", "Soldado", "Torneira", "Dinheiro", "Peixe", "Garrafa", "Joelho", "Melancia", "Ovos"]

    # Escolha aleatória de um número entre 0 e comprimento da lista
    num = randrange(0, len(palavras))
    ps = palavras[num].upper()
  
    return ps


def censura(palavra_secreta):
  cens = ["_" for letra in palavra_secreta]
  
  return cens

def marca_acerto(letra, letras_acertadas, palavra_secreta):
  i = 0
  # Loop que passa em cada letra da palavra secreta
  for l in palavra_secreta:
      # Condição que verifica o chute com as letras da palavra secreta
      if (letra == l):
          # Substituição do chute certo com as letras da palavra secreta
          letras_acertadas[i] = l
      i += 1


def jogo(palavra_secreta):
  
  resposta = censura(palavra_secreta)
  print(palavra_secreta)
  
  acertou = False
  enforcou = False

  erros = 0
  tentativas = 5
  lista_erros = []
  faltando = len(resposta)

  print("Tente acertar a palavra de {0} letras".format(len(resposta)))
  print(resposta)

  while not acertou and not enforcou:
    
    chute = input("\nDigita uma letra: ").upper()
    if chute in palavra_secreta:
      
      marca_acerto(chute, resposta, palavra_secreta)
      faltando = resposta.count('_')
      print(resposta)
      print("Letras erradas: ", lista_erros)

    else:
      print("A letra '{0}' não está na palavra.\n".format(chute))
      if chute not in lista_erros:
        lista_erros.append(chute)
  
        erros += 1
        print(resposta)
        print("\nLetras erradas: ", lista_erros)
        print("\nAinda faltam {0} letras.".format(faltando))
        print("Você tem {0} tentativas.".format(tentativas-erros))

    if erros == 5:
      enforcou = True
    elif "_" not in resposta:
      acertou = True
      
  if acertou:
    print("\nVocê ganhou parabéns!")
  else:
    print("\nVocê perdeu a palavra era: {0}!".format(palavra_secreta))
    print("Fim do jogo...")

# Inicialização do jogo 
jogo(palavra_secreta())
