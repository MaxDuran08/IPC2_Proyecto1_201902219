import easygui
import xml.etree.ElementTree as ET
Menu=True

def CargarDatos():
    print("")
    #tree = ET.parse(easygui.fileopenbox(title="Abre el archivo .XML"))
    tree = ET.parse("C:\\Users\\Usuario\\Documents\\USAC\\Class\\IPC 2\\Lab\\pruebas\\prueba.xml")
    root = tree.getroot()
    print("======================================")
    for i in range(len(root)):
        print("Nombre:"+root[i].attrib["nombre"])
        print("R:"+root[i][0].text)
        print("C:"+root[i][1].text)
        print("F:"+root[i][2].text)
        print("S:"+root[i][3].text)
        for j in range(len(root[i][4])):
            print("Piso #"+str(j+1))
            print("Codigo:"+root[i][4][j].attrib["codigo"])
            print("Patron:"+root[i][4][j].text.replace(" ","").replace("\n",""))
        print("======================================")




def MenuOpcion():
    print("<*>==================================<*>")
    print(" | 1. CARGAR DATOS                    |")
    print(" | 2.                                 |")
    print(" | 5. SALIR                           |")
    print("<*>==================================<*>")
while Menu:
    MenuOpcion()
    try:
        Opcion=int(input())
        if Opcion==1:
            print("op 1")
            CargarDatos()
        elif Opcion==2:
            print("op 2")
        elif Opcion==3:
            print("op 3")
        elif Opcion==4:
            print("op 4")
        elif Opcion==5:
            print("[OPCION-SALIR]: Saliendo del programa")
            Menu=False
        else:
            print("[ERROR-MENU]: Debe de ingresar un valor numerico aceptable")
    except:
        print("[ERROR-MENU]: Debe de ingresar un valor numerico")