# Importa a função random do py
from random import *
secret = randrange(10)

# Input da dificuldade
nivel = int(input("Qual dificuldade de 1 à 3? "))

pontos = 1000

# Condição que verifica a dificuldade e cria variáveis de acordo
# l é o número de tentativas
if nivel == 1:
  l = 10
  sub = 100
elif nivel == 2:
  l = 5
  sub = 200
elif nivel == 3:
  l = 3
  sub = 333

# Loop que define as l tentativas e acaba quando o usuário ganha
for i in range(l):

     # Input da tentativa do usuário
    num = int(input("\nAdivinhe o número secreto entre 0 e 10: "))

    # Condição que verifica se o Input é diferente do número
    if num != secret:
      print("\nERRO – Tente novamente, o numero secreto não é: {0}.".format(num))

      # Condição que verifica se é a terceira dificuldade e última tentativa
      if nivel == 3 and i == 2:
        pontos -= (sub + 1)
        print("Seus pontos: {0}.".format(pontos))
      elif num < secret:
        print("O número secreto é maior que: {0}.".format(num))
        pontos -= sub
        print("Seus pontos: {0}.".format(pontos))
      elif num > secret:
        print("O número secreto é menor que: {0}.".format(num))
        pontos -= sub
        print("Seus pontos: {0}.".format(pontos))

      print("Você tem {0} tentativas.".format(l - (i + 1)))
        
    else:
        print("\nParabéns você acertou o número secreto que é: {0}.".format(secret))
        print("Seus pontos: {0}.".format(pontos))
        break
