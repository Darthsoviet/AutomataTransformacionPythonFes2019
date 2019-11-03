

class Tupla:

    def __init__(self,tipo):
        self.__lista = []
        self.__tipo = tipo

    def es_determinista(self):
        return self.__tipo

    def insertarEstados(self, numero_estados):
        i = 0
        while i <= numero_estados-1:
            print(f"q{i}",end=",")
            aux=[]
            aux.append("q"+str(i))
            self.__lista.append(aux)
            i+=1
        print()

    def insertar_relacion(self,q,A,B):
        aux=A.split(" ")
        aux1=B.split(" ")
        if self.es_determinista() and len(aux) !=1:
            print("no se pueden insertar mas de un estado si es determinista")
            return False

        elif self.es_determinista() and len(aux1) !=1:
            print("no se pueden insertar mas de un estado si es determinista")
            return False
        elif not self.es_determinista() and  len(aux)<=3 and len(aux1)<=3:
            i = 0
            for j in self.__lista:
                if  j[0]==q:
                    j.append(A)
                    j.append(B)
            return True
        else:
            print("condicion no valida mas de 3 relaciones")
            return False

    def mostrar(self):
        print(["Estado","A","B"])
        for i in self.__lista:
            print(i)

    def relacionar(self):
        print("No se pemiten mas de 3 relaciones, el vacio se representa con v y los estados se separan por coma")
        for i in self.__lista:
           print("___________________________________")
           q=i[0]
           condicion=self.insertar_relacion(q,input(f"inserte estados de {i[0]} para A\n"),input(f"inserte estados de {i[0]} para B \n"))
           if not condicion:
               break

    def convertir(self,cadena):
        string=str(cadena)
        lista=string.split(',')
        return lista

    def comparar_cadenas(self,cadena1,cadena2):
        cadena1=self.convertir(cadena1)
        cadena2 = self.convertir(cadena2)
        elementos=len(cadena1)
        if len(cadena2)==len(cadena1):
            aux=0
            for i in cadena1:
                if i in cadena2:
                    aux+=1
            if aux==elementos:
                return True
            else:
                return False
        else:
            return False

    def transformar_a_determinista2(self):
        if self.es_determinista:
            cambios=1
            estado_transformar=""
            sub_indice=len(self.__lista)
            for i in self.__lista:   #se busca un estado que no sea determinista q
                for j in  i:         #j es un objeto de tipo string
                    if ','in j or 'v' in j:    #detecta si hay un vacio o una coma en la cadena
                        estado_transformar=j
                        break
            nuevo="q"+str(sub_indice) #se remplazan todos los valores que fueron no deterministas por un nuevo estad0
            sub_indice+=sub_indice
            for i in range(len(self.__lista)):
                for j in range(3):
                    #if self.__lista[i][j]==estado_transformar:
                    if self.comparar_cadenas(self.__lista[i][j],estado_transformar):
                        self.__lista[i][j]=nuevo#cambua el estado anterior por el nuevo #se remplazan las cadenas por una nueva cadena r



tupla=Tupla(False)

n=int(input("inserte un numero de estados < 8"))
tupla.insertarEstados(n)
tupla.relacionar()
tupla.mostrar()
i=0
while i<n*3:
    tupla.transformar_a_determinista2()
    tupla.mostrar()
    i+=1
tupla.mostrar()





