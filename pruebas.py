import xml.etree.ElementTree as ET
from ListaEnlazada import ListaEnlazada as MiLista
tree = ET.parse("prueba.xml")
root = tree.getroot()
""""
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
"""
Lista=MiLista()
for i in range(len(root)):
    CurrentLista1=MiLista()
    CurrentLista1.Append(root[i].attrib["nombre"])
    CurrentLista1.Append(root[i][0].text.replace(" ","").replace("\n",""))
    CurrentLista1.Append(root[i][1].text.replace(" ","").replace("\n",""))
    CurrentLista1.Append(root[i][2].text.replace(" ","").replace("\n",""))
    CurrentLista1.Append(root[i][3].text.replace(" ","").replace("\n",""))
    CurrentLista2=MiLista()
    for j in range(len(root[i][4])):
        CurrentLista3=MiLista()
        CurrentLista3.Append(root[i][4][j].attrib["codigo"])
        CurrentLista3.Append(root[i][4][j].text.replace(" ","").replace("\n",""))
        CurrentLista2.Append(CurrentLista3)
    CurrentLista1.Append(CurrentLista2)
    Lista.Append(CurrentLista1)
#print(str(Lista[0]))
for i in range(len(Lista)):
    print(str(Lista[i]))

print(len(Lista))
print(len(Lista[0]))
print(len(Lista[0][5]))

print("Matriz 1")
patron=str(Lista[0][5][0][1])
print(Lista[0][1])
print(Lista[0][2])
fila=int(Lista[0][1])
columna=int(Lista[0][2])

PatronLista=MiLista()
for x in patron:
    PatronLista.Append(x)
print(str(PatronLista))
cont=0
MatrizPatron=MiLista()
for i in range(fila):
    filaLista=MiLista()
    for j in range(columna):
        filaLista.Append(PatronLista[cont])
        cont+=1
    MatrizPatron.Append(filaLista)
print(str(MatrizPatron))
print(str(MatrizPatron[0][2]))
