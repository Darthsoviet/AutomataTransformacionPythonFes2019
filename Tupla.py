

class Tupla:

    def __init__(self,tipo):
        self.__lista = []
        self.__tipo = tipo
        self.__estados_agregados=[]
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

    def __insertar_relacion(self,q,A,B):
        aux=A.split(",")
        aux1=B.split(",")
        if self.es_determinista() and len(aux) !=1:
            print("no se pueden insertar mas de un estado si es determinista")
            return False

        elif self.es_determinista() and len(aux1) ==1:
            i = 0
            for j in self.__lista:
                if j[0] == q:
                    j.append(A)
                    j.append(B)
            return True
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
        print("No se pemiten mas de 3 relaciones, el vacio se representa con \"v,\"y los estados se separan por coma")
        for i in self.__lista:
           q=i[0]
           condicion=self.__insertar_relacion(q,input(f" {i[0]} , A\n"),input(f" {i[0]} , B \n"))
           print()
           if not condicion:
               break
    """
    convierte una cadena a una lista
    """
    def __convertir(self,cadena):
        string=str(cadena)
        lista=string.split(',')
        return lista
    """
    compara si los elementos de dos listas son iguales aunque no esten ordenados
    ejemplo q1,q2=q2,q1
    
    """

    def __convertir_a_string(self,lista):
        aux=""
        for i in lista:
            aux+=i+","
        return aux.strip(",")


    def __comparar_listas(self, cadena1, cadena2):
            cadena1=sorted(cadena1)
            cadena2=sorted(cadena2)

            cadena1=self.__convertir_a_string(cadena1)
            cadena2 =self.__convertir_a_string(cadena2)
            if cadena1==cadena2:
                return True
            else:
                return False

    """
    verifica si una cadena esta en una lista
    """
    def esta_en_lista(self,lista,cadena):
        lista=list(lista)
        cadena=str(cadena)
        cadena=self.__convertir(cadena)

        for i in lista:
            i=self.__convertir(i)
            if self.__comparar_listas(cadena,i):
                return True


    def transformar_a_determinista2(self,ultimo_indice):
        if self.es_determinista:
            fin=True
            estado_transformar=""
            sub_indice=ultimo_indice+1
            while fin:
                for i in self.__lista:
                    if "," in i[0]  or "v" in i[0]:
                        estado_transformar=i[0]
                        fin=True
                        break
                    else:
                        fin=False

                nuevo="q"+str(sub_indice)
                sub_indice+=1
                for i in range(len(self.__lista)):
                    aux=self.__lista[i]
                    for j in range(len(aux)):
                        if self.__comparar_listas(self.__convertir(self.__lista[i][j]),self.__convertir(estado_transformar)):
                            self.__lista[i][j]=nuevo

    def transformar_a_determinista(self):
        if self.es_determinista:
            fin = True
            estado_transformar = ""

            while fin:
                for i in self.__lista:
                    if "," in i[0] or "v" in i[0]:
                        estado_transformar = i[0]
                        fin = True
                        break
                    else:
                        fin = False
                for i in range(len(self.__lista)):
                    aux = self.__lista[i]
                    for j in range(len(aux)):
                        if self.__comparar_listas(self.__convertir(self.__lista[i][j]),
                                                  self.__convertir(estado_transformar)):
                            self.__lista[i][j] = str(self.__lista[i][j]).strip(",")

    def generar_estados(self):
        if self.es_determinista:
            vacio="v"
            estado=""
            listaEstadosNoDeterministas=[]
            nuevos=[]
            for i in self.__lista:   #se busca un estado que no sea determinista q
                for j in  range(1,len(i)):         #j es un objeto de tipo string
                    if ','in i[j] or vacio in i[j]:    #detecta si hay un vacio o una coma en la cadena
                        estado=i[j]
                        """proceso complejo pero no tanto"""
                        if estado !=vacio:
                            if not self.esta_en_lista(self.__estados_agregados,estado):
                                lista=self.__proceso_uno(estado)#proceso mega mamalon y POJO  :c
                                """termina"""
                                nuevos.append(lista)
                        else:
                            nuevos.append(["v","q0","v"])
            lista_auxiliar=[]
            for i in nuevos:
                if  not self.esta_en_lista(lista_auxiliar,i[0]):
                    lista_auxiliar.append(i[0])
            print(f"estados a convertir>>>>>{lista_auxiliar}<<<<\n")
            for i in lista_auxiliar:
                for j in nuevos:
                    if j[0]==i:
                        listaEstadosNoDeterministas.append(j)
                        break
            print(f"estados no deterministas nuevos \n")
            for i in listaEstadosNoDeterministas:
                print(i)
                self.__estados_agregados.append(i[0])

            for estado in listaEstadosNoDeterministas:
                self.__lista.append(estado)

            return  len(lista_auxiliar)
        else:
            print("su cochinada ya es determinista")

    def ciclo_transformaciones(self):
       fsin=True
       lista_registrados = []
       while fsin:

            for i in self.__lista:
                print(i[0])
                lista_registrados.append(i[0])
            for i in self.__lista:  # se busca un estado que no sea determinista q
                for j in i:  # j es un objeto de tipo string
                    if not self.esta_en_lista(lista_registrados,j):  # detecta si hay un vacio o una coma en la cadena
                        print("se generan estados")
                        print("lista estados registrados",lista_registrados)
                        self.generar_estados()
                        for i in self.__lista:
                            if not self.esta_en_lista(lista_registrados,i[0]):
                                lista_registrados.append(i[0])
                        self.mostrar()
                        fsin=True
                        break
                    else:
                        fsin=False


       self.transformar_a_determinista2(self.__retorna_ultimo_nodeterminista())
       self.transformar_a_determinista()
       self.mostrar()

    def __devolver_indice(self,q):
        if "v" not in q:
            ultimo_estado=str(q)
            ultimo_estado = ultimo_estado.split("q")
            print(ultimo_estado)
            ultimo_estado = int(ultimo_estado[1])
            print("ultimo estado",ultimo_estado)
            return ultimo_estado

    def __retorna_ultimo_nodeterminista(self):
        lista=[]
        for i in self.__lista:
            for j in i:
                if "," not in j and "v"not in j:
                    lista.append(j)
        ordenada=sorted(lista)
        ultimo_estado= ordenada[len(ordenada)-1]
        return self.__devolver_indice(ultimo_estado)

    def __proceso_uno(self,estado):
        estado =str(estado)
        aux = []
        aux.append(estado)
        e = self.__convertir(estado)
        # obtener estados A
        aux_A = ""
        for q in e:
            a = self.__buscar_relacion_A(q)
            a = str(a)
            aux_A += a
        aux_A = aux_A.strip(",")
        aux_l = []
        aux_A = aux_A.split(",")
        for i in aux_A:  # se busca meter caracteres no repetidos a aux_l
            if i + "," not in aux_l:
                aux_l.append(i + ",")
        aux_A = ""
        for c in aux_l:
            aux_A += c
        aux_A = aux_A.strip(",")
        aux.append(aux_A)
        # obtener estados B
        aux_A = ""
        for q in e:
            a = self.__buscar_relacion_B(q)
            a = str(a)
            aux_A += a
        aux_A = aux_A.strip(",")
        aux_l = []
        aux_A = aux_A.split(",")
        for i in aux_A:  # se busca meter caracteres no repetidos a aux_l
            if i + "," not in aux_l:
                aux_l.append(i + ",")
        aux_A = ""
        for c in aux_l:
            aux_A += c
        aux_A = aux_A.strip(",")
        aux.append(aux_A)
        return aux

    def __buscar_relacion_A(self,q):
        for i in self.__lista:
            if q==i[0] and i[1]!="v":
                return i[1]+","
            else:
                return ""


    def __buscar_relacion_B(self,q):
        for i in self.__lista:
            if q==i[0] and i[2]!="v":
                return i[2]+","
            else:
                return ""

def main():
    TIPO=True
    while True:
        print("bienvenido escoja su tipo de automata finito 1=determinista, 0=no determinista")
        tipo=int(input())
        if tipo==1:
            TIPO=True
            print("su automata es determinista y no puede insertar mas de una relacion, ni vacios")
            tupla=Tupla(TIPO)
            numero_estados=int(input("inserte numeros de estados menor a 8 se nombraran automaticamente como qn"))
            tupla.insertarEstados(numero_estados)
            print("inserte relaciones no pueden ser mas de 3")
            tupla.relacionar()
            print("la tupla es la siguiente")
            tupla.mostrar()

        elif tipo==0:
            TIPO=False
            print("su automata es NO determinista y puede insertar hasta 3 relaciones")
            tupla = Tupla(TIPO)
            numero_estados = int(input("inserte numeros de estados menor a 8 se nombraran automaticamente como qn"))
            tupla.insertarEstados(numero_estados)
            print("inserte relaciones")
            tupla.relacionar()
            print("la tupla es la siguiente")
            tupla.mostrar()
            print("la transformacion a determinista es la siguiente...")
            print("la transformacion a determinista es la siguiente...")
            tupla.ciclo_transformaciones()
            tupla.mostrar()



        else:
            print("error")
main()





