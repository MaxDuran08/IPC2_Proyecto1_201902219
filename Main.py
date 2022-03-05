import easygui
import xml.etree.ElementTree as ET
from ListaEnlazada import ListaEnlazada as MiLista

Menu=True
Data=MiLista()

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
    print("<*>==================================<*>")
    print(" | 1. CARGAR DATOS                    |")
    print(" | 2. VER PISOS                       |")
    print(" | 3. SALIR                           |")
    print("<*>==================================<*>")
while Menu:
    MenuOpcion()
    try:
        Opcion=int(input())
        if Opcion==1:
            print("[OPCION-CARGAR DATOS]")
            Data=MiLista()
            CargarDatos()
            Ordenamiento(Data)
            for x in range(len(Data)):
                print(Data[x])
            
        elif Opcion==2:
            print("op 2")
        elif Opcion==3:
            print("[OPCION-SALIR]: Saliendo del programa")
            Menu=False
        else:
            print("[ERROR-MENU]: Debe de ingresar un valor numerico aceptable")
    except:
        print("[ERROR-MENU]: Debe de ingresar un valor numerico")