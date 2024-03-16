def numero_de_digitos(n: int):

  if isinstance(n, str):
        return "Debe ser un entero"
  
  elif isinstance(n,float):
     return "No puede ser un flotante"
  
  elif n <= 9 and n>=-10:

    return 1
  
  else:

    return 1 + numero_de_digitos(n // 10)

numero_de_digitos(999)
