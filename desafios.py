# EXERCÍCIO 7
lista =  [10, -2, 4, 8, 100, 44, -19, 2, 3, 2, -90, 11, -33, 10, 67, 15]

# item a)
print(max(lista))

# item b)
print(min(lista))

# item c)
pares = []
for i in lista:

  if i % 2 == 0:
    pares.append(i)
    
for n in range(len(pares)):
    if n == len(pares)-1:
        print(pares[n], end="\n")
    else:
        print(pares[n], end=", ")

# item d)
vzs_primeiro = 0
for i in lista:
  if i == lista[0]:
    vzs_primeiro += 1

print(vzs_primeiro)

#item e)
soma = sum(lista)
tam = len(lista)
print(soma/tam)

#item f)
soma_n = 0
for i in lista:
  if i < 0:
    soma_n += i

print(soma_n)

#item g)
soma_p = 0
for i in lista:
  if i > 0:
    soma_p += i

print(soma_p)

#item h)
reps = []
for i in range(len(lista)):    
    for j in range(i+1, len(lista)):    
        if(lista[i] == lista[j]):    
            reps.append(lista[j]);   

for n in range(len(reps)):
    if n == len(reps)-1:
        print(reps[n], end="\n")
    else:
        print(reps[n], end=", ")
