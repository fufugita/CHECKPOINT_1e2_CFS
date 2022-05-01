# Importa a função random do py
from random import *
secret = randrange(10)

check = False
i = 0

# Loop que define as 3 tentativas e acaba quando o usuário ganha
while i < 3 and not check:

    # Input da tentativa do usuário
    num = int(input("Adivinhe o número secreto entre 0 e 10: "))

    # Condição que verifica se o Input é diferente do número
    if num != secret:
      print("\nERRO – Tente novamente, o numero secreto não é: {0}.".format(num))
      
      if num < secret:
        print("O número secreto é maior que: {0}.".format(num))
      else :
        print("O número secreto é menor que: {0}.".format(num))

      print("Você tem {0} tentativas.".format(2-i))
      i+=1
        
    else:
        print("\nParabéns você acertou o número secreto que é: {0}.".format(secret))
        check = True
