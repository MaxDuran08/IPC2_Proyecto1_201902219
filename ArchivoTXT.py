import os
import webbrowser
class Instrucciones:
    def __init__(self,Instrucciones):
        self.Instrucciones=Instrucciones
        self.n=""
        self.Crear()
    
    def Crear(self):
        Ruta=self.Calcular()
        try:
            Reporte=open(Ruta,"w")
            Reporte.write(self.Instrucciones)
            Reporte.close
            print("[INSTRUCCIONES]: Se guardo el archivo con el nombre: "+str(Ruta))
            try:
                Archivo="file:///"+os.getcwd()+"/"+Ruta
                webbrowser.open_new_tab(Archivo)
            except:
                print("[ERROR-INSTRUCCIONES]: Problema al abrir el archivo")
        except:
            print("[ERROR-INSTRUCCIONES]: Problema al generar las instrucciones")

    def Calcular(self):
        n=None
        if self.n=="":
            n=0
            self.n=0
        else:
            n=self.n
        
        while True:
            ruta="Instrucciones"+str(n)+".txt"
            Existe=os.path.exists(ruta)
            if Existe==True:
                n+=1
            else:
                self.n=n
                return ruta