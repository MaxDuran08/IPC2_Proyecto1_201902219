import easygui
import xml.etree.ElementTree as ET
from ListaEnlazada import ListaEnlazada as MiLista
from Transformacion import Transformacion as TF
from ArchivoTXT import Instrucciones as MostrarInstrucciones
from Graficar import Graficar as G

Menu=True
Data=MiLista()
PisoSeleccionado=None
PatronSeleccionado=None
NuevoPatronSeleccionado=None

def esMayor(primero,segundo):
    Lista1=MiLista()
    Lista2=MiLista()
    
    tamaño1=len(primero)
    tamaño2=len(segundo)
    
    for i in primero:
        Lista1.Append(i)
    for i in segundo:
        Lista2.Append(i)

    if tamaño1==1 and tamaño2>1:
        if ord(Lista1[0])>ord(Lista2[0]):
            return True
        elif ord(Lista1[0])==ord(Lista2[0]):
            return False
        else:
            return False
    elif tamaño1>1 and tamaño2==1:
        if ord(Lista1[0])>ord(Lista2[0]):
            return True
        elif ord(Lista1[0])==ord(Lista2[0]):
            return True
        else:
            return False
    elif tamaño1==tamaño2:
        for i in range(tamaño1):
            if ord(Lista1[i])>ord(Lista2[i]):
                return True
        return False
    elif tamaño1>tamaño2:
        for i in range(tamaño2):
            if ord(Lista1[i])>ord(Lista2[i]):
                return True
        return True
    
def Ordenamiento(Lista):
    for i in range(len(Lista)):
        for j in range(0, len(Lista)-i-1):
            primero=str(Lista[j][0])
            segundo=str(Lista[j+1][0])
            #print(str(Lista))
            #print("Probando con => ["+primero+"], ["+segundo+"]")
            if esMayor(primero,segundo):
                temp = Lista[j]
                Lista[j] = Lista[j+1]
                Lista[j+1] = temp
                #print("Se realizo un cambio, queda: ["+segundo+"], ["+primero+"]")
            #else:
                #print("No se hace cambio, queda: ["+primero+"], ["+segundo+"]")
def CargarDatos():
    #tree = ET.parse(easygui.fileopenbox(title="Abre el archivo .XML"))
    #tree = ET.parse("C:\\Users\\Usuario\\Documents\\USAC\\Class\\IPC 2\\Lab\\pruebas\\prueba.xml")
    tree = ET.parse("prueba.xml")
    root = tree.getroot()
    for i in range(len(root)):
        CurrentLista1=MiLista()
        CurrentLista1.Append(root[i].attrib["nombre"])
        CurrentLista1.Append(root[i][0].text.replace(" ","").replace("\n",""))
        CurrentLista1.Append(root[i][1].text.replace(" ","").replace("\n",""))
        CurrentLista1.Append(root[i][2].text.replace(" ","").replace("\n",""))
        CurrentLista1.Append(root[i][3].text.replace(" ","").replace("\n",""))
        CurrentLista2=MiLista()
        for j in range(len(root[i][4])):
            if len(root[i][4][j].text.replace(" ","").replace("\n",""))==(int(root[i][0].text.replace(" ","").replace("\n",""))*int(root[i][1].text.replace(" ","").replace("\n",""))):
                #print("aceptable")
                CurrentLista3=MiLista()
                CurrentLista3.Append(root[i][4][j].attrib["codigo"])
                CurrentLista3.Append(root[i][4][j].text.replace(" ","").replace("\n",""))
                CurrentLista3.Append(CrearMatrices(int(root[i][0].text.replace(" ","").replace("\n","")),int(root[i][1].text.replace(" ","").replace("\n","")),root[i][4][j].text.replace(" ","").replace("\n","")))
                CurrentLista2.Append(CurrentLista3)
        Ordenamiento(CurrentLista2)
        CurrentLista1.Append(CurrentLista2)
        Data.Append(CurrentLista1)
    
def CrearMatrices(filas,columnas,patron):
    #print("Filas: "+str(filas)+", Columnass: "+str(columnas)+" ,Patron: "+str(patron))
    PatronLista=MiLista()
    for x in patron:
        PatronLista.Append(x)
    cont=0
    MatrizPatron=MiLista()
    for i in range(filas):
        filaLista=MiLista()
        for j in range(columnas):
            filaLista.Append(PatronLista[cont])
            cont+=1
        MatrizPatron.Append(filaLista)
    return MatrizPatron

def MenuOpcion():
    print("<*>===================================<*>")
    print(" | 1. CARGAR DATOS                     |")
    print(" | 2. PISOS                            |")
    print(" | 0. SALIR                            |")
    print("<*>===================================<*>")

def MenuOpcionVerPisos():
    print("<*>===================================<*>")
    print(" | SELECCIONE UN PISO                  |")
    n=1
    for x in range(len(Data)):
        print(" | "+str(n)+". "+str(Data[x][0]))
        n+=1
    print(" | 0. REGRESAR                         |")
    print("<*>===================================<*>")

def MenuPatrones():
    print("<*>===================================<*>")
    print(" | PISO SELECCIONADO: \""+str(PisoSeleccionado[0])+"\"")
    print(" | SELECCIONE UN PATRON                |")
    n=1
    for x in range(len(PisoSeleccionado[5])):
        print(" | "+str(n)+". "+str(PisoSeleccionado[5][x][0]))
        n+=1
    print(" | 0. REGRESAR                         |")
    print("<*>===================================<*>")

def MenuPatronesNuevo():
    print("<*>===================================<*>")
    print(" | PISO SELECCIONADO: \""+str(PisoSeleccionado[0])+"\"")
    print(" | SELECCIONE UN PATRON                |")
    n=1
    for x in range(len(PisoSeleccionado[5])):
        print(" | "+str(n)+". "+str(PisoSeleccionado[5][x][0]))
        n+=1
    print(" | 0. REGRESAR                         |")
    print("<*>===================================<*>")

def MenuPatronesPlus():
    print("<*>===================================<*>")
    print(" | PATRON SELECCIONADO: \""+str(PatronSeleccionado[0])+"\"")
    print(" | 1. GRAFICAR PATRON                  |")
    print(" | 2. TRANSFORMAR PATRON ACTUAL        |")
    print(" | 0. REGRESAR                         |")
    print("<*>===================================<*>")

def MenuFinal():
    print("<*>===================================<*>")
    print(" | 1. MOSTRAR COSTO MINIMO DEL CAMBIO  |")
    print(" | 2. MOSTRAR INSTRUCCIONES PASO A PASO|")
    print(" | 3. GRAFICAR NUEVO PATRON            |")
    print(" | 0. REGRESAR                         |")
    print("<*>===================================<*>")

def MenuInstrucciones():
    print("<*>===================================<*>")
    print(" | 1. MOSTRAR INSTRUCCIONES EN CONSOLA |")
    print(" | 2. MOSTRAR INSTRUCCIONES UN ARCHIVO |")
    print(" | 0. REGRESAR                         |")
    print("<*>===================================<*>")

def ObtenerOpcion(tipoMenu):
    while True:
        try:
            opcion=int(input())
            return opcion      
        except:
            print("[ERROR]: El dato ingresado no es un entero")
            if tipoMenu==1:
               MenuOpcion()
            elif tipoMenu==2:
                MenuOpcionVerPisos()
            elif tipoMenu==3:
                MenuPatrones()
            elif tipoMenu==4:
                MenuPatronesPlus()
            elif tipoMenu==5:
                MenuPatronesNuevo()
            elif tipoMenu==6:
                MenuFinal()
            elif tipoMenu==7:
                MenuInstrucciones()

while Menu:
    MenuOpcion()
    #try:
    Opcion=ObtenerOpcion(1)
    if Opcion==1:
        print("[OPCION-CARGAR DATOS]")
        Data=MiLista()
        CargarDatos()
        Ordenamiento(Data)
        #for x in range(len(Data)):
        #    print(Data[x])
        print("[CARGAR DATOS]: CARGA SATISFACTORIA")
        #transformacion=TF(Data[0],Data[0][5][0],Data[0][5][1])
    elif Opcion==2:
        if len(Data)>0:
            print("[OPCION-PISOS]: Entrando a nuevo menu")
            VerPisos=True
            while VerPisos:
                MenuOpcionVerPisos()
                Opcion=ObtenerOpcion(2)
                if Opcion==0:
                    print("[OPCION-REGRESAR]: Regresando al menu principal")
                    VerPisos=False
                else:
                    try:
                        print("[SELECCION]: Selecciono el piso: "+str(Opcion))
                        PisoSeleccionado=None
                        PisoSeleccionado=Data[Opcion-1]
                        #print(PisoSeleccionado)
                        Patrones=True
                        while Patrones:
                            MenuPatrones()
                            Opcion=ObtenerOpcion(3)
                            if Opcion==0:
                                Patrones=False
                                print("[OPCION-REGRESAR]: Regresando al menu pisos")
                            else:
                                try:
                                    print("[SELECCION]: Selecciono el patron: "+str(Opcion))
                                    PatronSeleccionado=None
                                    PatronSeleccionado=PisoSeleccionado[5][Opcion-1]
                                    #print(PatronSeleccionado)
                                    MPatrones=True
                                    while MPatrones:
                                        MenuPatronesPlus()
                                        Opcion=ObtenerOpcion(4)    
                                        if Opcion==0:
                                            print("[OPCION-REGRESAR]: Regresando al menu patrones")
                                            MPatrones=False
                                        elif Opcion==1:
                                            print("Graficando el patron actual...")
                                            G(PatronSeleccionado[2],PatronSeleccionado[0],PatronSeleccionado[1])
                                        elif Opcion==2:
                                            print("[SELECCION]: Selecciono transformar el patron actual")
                                            try:
                                                nuevoPatron=True
                                                while nuevoPatron:
                                                    MenuPatronesNuevo()
                                                    Opcion=ObtenerOpcion(5)
                                                    if Opcion==0:
                                                        print("[OPCION-REGRESAR]: Regresando")
                                                        nuevoPatron=False
                                                    else:
                                                        try:
                                                            NuevoPatronSeleccionado=None
                                                            NuevoPatronSeleccionado=PisoSeleccionado[5][Opcion-1]
                                                            #print("Nuevo patron: "+str(NuevoPatronSeleccionado))
                                                            transformacion=TF(PisoSeleccionado,PatronSeleccionado,NuevoPatronSeleccionado)
                                                            mFinal=True
                                                            while mFinal:
                                                                MenuFinal()
                                                                Opcion=ObtenerOpcion(6)
                                                                if Opcion==0:
                                                                    mFinal=False
                                                                elif Opcion==1:
                                                                    print("El costo es de: "+str(transformacion.CostoMinimo))
                                                                elif Opcion==2:
                                                                    try:
                                                                        mInstrucciones=True
                                                                        while mInstrucciones:
                                                                            MenuInstrucciones()
                                                                            Opcion=ObtenerOpcion(7)
                                                                            if Opcion==1:
                                                                                print(str(transformacion.Instrucciones))
                                                                            elif Opcion==2:
                                                                                MostrarInstrucciones(str(transformacion.Instrucciones))
                                                                            elif Opcion==0:
                                                                                print("[OPCION-REGRESAR]: Regresando")
                                                                                mInstrucciones=False
                                                                            else:
                                                                                print("[ERROR]: Debe de ingresar un valor numerico aceptable") 
                                                                    except:
                                                                        print("[ERROR]: Debe de ingresar un valor numerico aceptable") 

                                                                elif Opcion==3:
                                                                    print("Graficar nuevo patron")
                                                                    G(transformacion.matriz1,PatronSeleccionado[0],NuevoPatronSeleccionado[1])
                                                                else:
                                                                    print("[ERROR]: Debe de ingresar un valor numerico aceptable") 
                                                        except:
                                                            print("[ERROR]: El patron seleccionado no existe")
                                            except:
                                                print("[ERROR]: El patron seleccionado no existe")
                                        else:
                                            print("[ERROR]: Debe de ingresar un valor numerico aceptable")  
                                    
                                except:
                                    print("[ERROR]: El patron seleccionado no existe")
                    except:
                        print("[ERROR]: El piso seleccionado no existe")
        else:
            print("[ERROR-MENU]: Debe de cargar informacion primero")
    elif Opcion==0:
        print("[OPCION-SALIR]: Saliendo del programa")
        Menu=False
    else:
        print("[ERROR-MENU]: Debe de ingresar un valor numerico aceptable")
    #except:
        #print("[ERROR]")