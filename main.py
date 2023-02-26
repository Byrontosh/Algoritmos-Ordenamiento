

'''
    Función para imprmir arreglos
'''
def imprimir_Arreglo(arreglo):
  tamanio = len(arreglo)
  for i in range(tamanio-1):
    print(f' [ {arreglo[i]} ] ',end="")



'''
    Función para el ordenamiento por burbuja
'''
def algoritmo_Burbuja(arreglo):

  for i in range(len(arreglo)-1):
        
        for j in range(len(arreglo)-1-i):
          if arreglo[j]>arreglo[j+1]:
            aux= arreglo[j]
            arreglo[j] = arreglo[j+1]
            arreglo[j+1] = aux





'''
    Sección para realizar prueba
'''
listaSueldos = [20.8,150.5,170.5,180.8,190,30,75.6,200]
print("\n Suelo de empleados sin ordenar \n")
imprimir_Arreglo(listaSueldos)
algoritmo_Burbuja(listaSueldos)
print("\n\n Suelo de empleados ordenado \n")
imprimir_Arreglo(listaSueldos)


# programa de finalización