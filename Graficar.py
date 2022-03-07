import os
from os import system,startfile
import pathlib
import graphviz
class Graficar:
    def __init__(self,matriz,codigo,patron):
        self.matriz=matriz
        self.codigo=str(codigo)+" => "+str(patron)
        self.n=""
        self.Crear()
    
    def Crear(self):
        Ruta=self.Calcular()
        RutaPng="Grafica"+str(self.n)

        text="""digraph L{
    node[shape=plain fontname=\"Arial\"]
    
    subgraph cluster1{
        label = \""""+str(self.codigo)+"""\"
        fontname=\"Arial\"
        bgcolor = lightseagreen
        a0 [label=<
        <TABLE border=\"4\" cellspacing=\"10\" cellpadding=\"10\" style=\"rounded\" bgcolor=\"lightblue\">"""

        matriz=self.matriz

        for i in range(len(matriz)):
            text+="\n<TR>"
            for j in range(len(matriz[0])):
                color=""
                if str(matriz[i][j])=="W":
                    color="white"
                else:
                    color="black"
                text+="<TD border=\"3\"  bgcolor=\""+str(color)+"\"></TD>"
            text+="</TR>"
        text+="""
                </TABLE>>];
    }
}
        """

        try:
            Reporte=open(Ruta,"w")
            Reporte.write(text)
            Reporte.close
            print("[GRAFICAR]: Se guardo el archivo con el nombre: "+str(Ruta))
            try:
                src = graphviz.Source(text,format="png")
                src.render(RutaPng)
                if os.path.exists(RutaPng):
                    os.remove(RutaPng)
                startfile(str(RutaPng)+".png")
                print("[GRAFICAR]: Se guardo el archivo con el nombre: "+str(RutaPng)+".png")
            except:
                print("[ERROR-GRAFICA]: Problema al abrir el archivo")
        except:
            print("[ERROR-GRAFICA]: Problema al generar las instrucciones")

    def Calcular(self):
        n=None
        if self.n=="":
            n=0
            self.n=0
        else:
            n=self.n
        
        while True:
            ruta="Grafica"+str(n)+".dot"
            Existe=os.path.exists(ruta)
            if Existe==True:
                n+=1
            else:
                self.n=n
                return ruta