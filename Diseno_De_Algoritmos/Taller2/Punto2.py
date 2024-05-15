import numpy as np
def suma_matrices(n, lista): 
  matriz= np.array(lista).reshape(n,n)
  l= len(lista)
  if n == 0 or l == 0: 
    return 0 
  else: 
    if n == 1: 
      return sum(lista)
    else: 
      if n == 2: 
        fila1=matriz[0]
        suma1 = sum(fila1)
        fila2=matriz[1]
        suma2 = sum(fila2)
        if suma1 < suma2 : 
          return suma2 
        else: 
          return suma1 

suma_matrices(2, [2,20,6,8])
