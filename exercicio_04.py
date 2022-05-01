from exercicio_03 import *

def calculadora():
  
  print("1 – soma\n2 – subtração\n3 – divisão\n4 – multiplicação\n5 – velocidade media\n")

  num = int(input("Digite qual ação deseja realizar: "))

  if num == 1:
    soma = soma_dois()
    print("Resultado: ", soma)
 
    
  elif num == 2:
    sub = sub_dois()
    print("Resultado: ", sub)

  elif num == 3:
    div = div_dois()
    print("Resultado: ", div)

  elif num == 4:
    mult = mult_dois()
    print("Resultado: ", mult)

  elif num == 5:
    x = int(input("Digite a distância: "))
    y = int(input("Digite o tempo: "))
    vm = vel_media(x, y)
    print("Distância: {0}m, Tempo: {1}s, Velocidade Média {2}m/s.".format(vm[0], vm[1], vm[2]))


calculadora()
