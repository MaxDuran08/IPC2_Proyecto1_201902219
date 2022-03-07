from ListaEnlazada import ListaEnlazada as MiLista
class Transformacion:
    def __init__(self,Piso,PrimerPatron,SegundoPatron):
        self.Piso=Piso
        self.PrecioVolteo=None
        self.PrecioIntercambio=None
        self.PrimerPatron=PrimerPatron
        self.SegundoPatron=SegundoPatron
        self.filas=None
        self.columnas=None
        self.matriz1=None
        self.matriz2=None
        self.CostoMinimo=0
        self.Instrucciones="[INSTRUCCIONES]\n"
        self.Pasos=0
        self.ObtenerPrecios()
        self.Ejecutar()
    
    def ObtenerPrecios(self):
        #print(self.Piso)
        self.PrecioVolteo=self.Piso[3]
        self.PrecioIntercambio=self.Piso[4]
    
    def AzulejosDesiguales(self):
        cont=0
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.matriz2[i][j]!=self.matriz1[i][j]:
                    #print("En la posicion ["+str(i)+"]["+str(j)+"] no coincide ")
                    cont+=1
        return cont

    def VolteoCoincidencia(self):
        for i in range(self.filas):
                    for j in range(self.columnas):
                        if self.matriz2[i][j]!=self.matriz1[i][j]:
                            self.Pasos+=1
                            self.Instrucciones+="[VOLTEO-PASO #"+str(self.Pasos)+"]:\nEn la posicion ["+str(i)+"]["+str(j)+"] se volteara el azulejo \""+str(self.matriz1[i][j])+"\", \nquedando: \""+str(self.matriz2[i][j])+"\"\n"
                            self.CostoMinimo+=int(self.PrecioVolteo)
                            self.matriz1[i][j]=self.matriz2[i][j]

    def IntercambioLateralCoincidencia(self):
        for i in range(self.filas):
                    for j in range(self.columnas):
                        if (j+1)<self.columnas:
                            if self.matriz2[i][j]!=self.matriz1[i][j] and self.matriz2[i][j+1]!=self.matriz1[i][j+1]:
                                
                                tengo1=self.matriz1[i][j]                            
                                tengo2=self.matriz1[i][j+1]                                
                                quiero1=self.matriz2[i][j]                                
                                quiero2=self.matriz2[i][j+1]
                                
                                if tengo1=="B" and tengo2=="W" and quiero1=="W" and quiero2=="B":
                                    self.Pasos+=1
                                    self.Instrucciones+="[INTERCAMBIO-PASO #"+str(self.Pasos)+"]:\nEn la posicion ["+str(i)+"]["+str(j)+"] y ["+str(i)+"]["+str(j+1)+"] se intercambiara el azulejo \""+str(self.matriz1[i][j])+"\" con el azulejo \""+str(self.matriz1[i][j+1])+"\"\nquedando: \""+str(self.matriz1[i][j+1])+"\",\""+str(self.matriz1[i][j])+"\"\n"
                                    self.CostoMinimo+=int(self.PrecioIntercambio)
                                    temp=self.matriz1[i][j]
                                    self.matriz1[i][j]=self.matriz1[i][j+1]
                                    self.matriz1[i][j+1]=temp
                                elif tengo1=="W" and tengo2=="B" and quiero1=="B" and quiero2=="W":
                                    self.Pasos+=1
                                    self.Instrucciones+="[INTERCAMBIO-PASO #"+str(self.Pasos)+"]:\nEn la posicion ["+str(i)+"]["+str(j)+"] y ["+str(i)+"]["+str(j+1)+"] se intercambiara el azulejo \""+str(self.matriz1[i][j])+"\" con el azulejo \""+str(self.matriz1[i][j+1])+"\"\nquedando: \""+str(self.matriz1[i][j+1])+"\",\""+str(self.matriz1[i][j])+"\"\n"
                                    self.CostoMinimo+=int(self.PrecioIntercambio)
                                    temp=self.matriz1[i][j]
                                    self.matriz1[i][j]=self.matriz1[i][j+1]
                                    self.matriz1[i][j+1]=temp

    def IntercambioVerticalCoincidencia(self):
        for i in range(self.filas):
                    for j in range(self.columnas):
                        if (i+1)<self.filas:
                            if self.matriz2[i][j]!=self.matriz1[i][j] and self.matriz2[i+1][j]!=self.matriz1[i+1][j]:
                                
                                tengo1=self.matriz1[i][j]                                
                                tengo2=self.matriz1[i+1][j]                                
                                quiero1=self.matriz2[i][j]                                
                                quiero2=self.matriz2[i+1][j]
                                
                                if tengo1=="B" and tengo2=="W" and quiero1=="W" and quiero2=="B":
                                    self.Pasos+=1
                                    self.Instrucciones+="[INTERCAMBIO-PASO #"+str(self.Pasos)+"]:\nEn la posicion ["+str(i)+"]["+str(j)+"] y ["+str(i+1)+"]["+str(j)+"] se intercambiara el azulejo \""+str(self.matriz1[i][j])+"\" con el azulejo \""+str(self.matriz1[i+1][j])+"\"\nquedando: \""+str(self.matriz1[i+1][j])+"\",\""+str(self.matriz1[i][j])+"\"\n"
                                    self.CostoMinimo+=int(self.PrecioIntercambio)
                                    temp=self.matriz1[i][j]
                                    self.matriz1[i][j]=self.matriz1[i+1][j]
                                    self.matriz1[i+1][j]=temp
                                elif tengo1=="W" and tengo2=="B" and quiero1=="B" and quiero2=="W":
                                    self.Pasos+=1
                                    self.Instrucciones+="[INTERCAMBIO-PASO #"+str(self.Pasos)+"]:\nEn la posicion ["+str(i)+"]["+str(j)+"] y ["+str(i+1)+"]["+str(j)+"] se intercambiara el azulejo \""+str(self.matriz1[i][j])+"\" con el azulejo \""+str(self.matriz1[i+1][j])+"\"\nquedando: \""+str(self.matriz1[i+1][j])+"\",\""+str(self.matriz1[i][j])+"\"\n"
                                    self.CostoMinimo+=int(self.PrecioIntercambio)
                                    temp=self.matriz1[i][j]
                                    self.matriz1[i][j]=self.matriz1[i+1][j]
                                    self.matriz1[i+1][j]=temp

    def Ejecutar(self):
        
        if str(self.PrimerPatron[0])==str(self.SegundoPatron[0]):
            self.Instrucciones="[NINGUN CAMBIO REALIZADO]: Se intenta transformar en el mismo patron"
        else:
            cBtengo=0
            cWtengo=0
            cBnecesito=0
            cWnecesito=0
            for x in str(self.PrimerPatron[1]):
                if x=="B":
                    cBtengo+=1
                else:
                    cWtengo+=1
            for x in str(self.SegundoPatron[1]):
                if x=="B":
                    cBnecesito+=1
                else:
                    cWnecesito+=1
            self.matriz1=self.PrimerPatron[2]
            self.matriz2=self.SegundoPatron[2]
            """print("=>")
            print(self.matriz1)
            print("Primer patron => B:"+str(cBtengo)+", W:"+str(cWtengo))
            print("=>")
            print(self.matriz2)
            print("Segundo patron => B:"+str(cBnecesito)+", W:"+str(cWnecesito))"""
            self.filas=int(self.Piso[1])
            self.columnas=int(self.Piso[2])
            """print("Filas: "+str(self.filas))
            print("Columnas: "+str(self.columnas))"""
            
            #print("No coincide en \""+str(self.AzulejosDesiguales())+"\" azulejos")
            if self.filas==1 and self.columnas>1:
                #print("matriz de 1*m")
                #Cambio lateral
                self.IntercambioLateralCoincidencia()
                self.VolteoCoincidencia()
                """print(self.matriz1)
                print(self.matriz2)
                print(str(self.Instrucciones))
                print("Costo: "+str(self.CostoMinimo))"""
            elif self.columnas==1 and self.filas>1:
                #print("matriz de n*1")
                #cambio vertical
                self.IntercambioVerticalCoincidencia()
                self.VolteoCoincidencia()
                """print(self.matriz1)
                print(self.matriz2)
                print(str(self.Instrucciones))
                print("Costo: "+str(self.CostoMinimo))"""
            else:
                #print("matriz de n*m")
                self.IntercambioLateralCoincidencia
                self.IntercambioVerticalCoincidencia()
                self.VolteoCoincidencia()
                """print(self.matriz1)
                print(self.matriz2)
                print(str(self.Instrucciones))
                print("Costo: "+str(self.CostoMinimo))"""