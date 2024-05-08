def encontrar_min_lista(lista): 
  for i in lista: 
    if isinstance(i, str):  
      return "solo numeros"
  longitud = len(lista) 
  if longitud == 0: 
    return "la lista no tiene elementos" 
  else: 
    if longitud == 1: 
      return lista[0] 
    else: 
      mitad = longitud // 2 
      mitad_izquierda = lista[:mitad]
      mitad_derecha =lista[mitad:] 
      
      min_izquierda = min(mitad_izquierda)
      min_derecha = min(mitad_derecha)

      if min_izquierda < min_derecha: 
        return min_izquierda
      else: 
        return min_derecha

encontrar_min_lista([3, 0])
