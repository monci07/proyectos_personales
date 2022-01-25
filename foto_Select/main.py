import tkinter as tk
import os
from PIL import ImageTk, Image
import sys

#variables globales
meses = ["1 Ene","2 Feb","3 Mar","4 Abr","5 May","6 Jun","7 Jul","8 Ago","9 Sep","10 Oct","11 Nov","12 Dic"]
años = ["Año 2002","Año 2003","Año 2004","Año 2005","Año 2006","Año 2007","Año 2008","Año 2009","Año 2010","Año 2011","Año 2012","Año 2013","Año 2014","Año 2015","Año 2016","Año 2017","Año 2018","Año 2019","Año 2020"]
ruta_original = '//moncivaisms/Media/Fotos/Año 2002/1 Ene 2002'
ruta_destino = '//moncivaisms/Media/Fotos/fotos x'
i=0

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Photo select")
        self.geometry("1000x650")
        self.attributes('-fullscreen', True)
        self.grid_rowconfigure(100, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.filenames = []
###########################creacion de widgets###########################    
    ###################seleccion_album###################
        self.control_mounth = tk.StringVar(self)
        self.control_year = tk.StringVar(self)
        self.mounthselector_widget = tk.OptionMenu(self,self.control_mounth, *meses)
        self.yearselector_widget = tk.OptionMenu(self,self.control_year, *años)

    ###################menu_de_fotos###################
        self.panel = tk.Label(self)
        self.instrucciones = tk.Text(self, height=22, width=23)
        self.instrucciones.insert(tk.END, "Instrucciones de uso:\n 1. Selecciona mes y año.\n 2. Precionar \'Buscar\'.\n 3. Utilizar \'Siguiente\' y \'Anterior\' para cambiar la imagen.\n 4. Para guardar una imagen precionar \'Guardar\'\n 5. Repetir el proceso por cada album y año que se quiera visitar.\n NOTAS:\n -Al acabar la sesion solo preciona \'Salir\'\n -Si la imagen no cambia al cambiar de album (osea al cambiar fecha y año y precionar \'Buscar\'), es por que el album esta vacio.")
        
        self.button_Buscar = tk.Button(self,text="Buscar", command = self.select_files, height=8, width=25)
        self.button_Guardar = tk.Button(self,text="Guardar", command = self.copy_picture, height=8, width=25)
        self.next_button = tk.Button(self, text = "Siguiente", command = self.show_next, height=8, width=25)
        self.last_button = tk.Button(self, text = "Anterior", command = self.show_last, height=8, width=25)
        self.exit = tk.Button(self,text="Salir", command = sys.exit, height=8, width=25)

        self.mes_label = tk.Label(self, text="Selecciona Mes: ")
        self.anio_label = tk.Label(self, text="Selecciona Año: ")

        self.instrucciones.place(x=0,y=0)
        
        self.mes_label.place(x=0, y=360)
        self.anio_label.place(x=0, y=390)
        self.mounthselector_widget.place(x=90, y=360)
        self.yearselector_widget.place(x=90, y=390)

        self.button_Buscar.place(x=0, y=420)
        self.last_button.place(x=0,y=555)
        self.next_button.place(x=0,y=690)
        self.button_Guardar.place(x=0, y=825)
        self.exit.place(x=0, y=960)

        self.panel.place(x=186, y=0)

    def show_next(self):
        global i
        if i<len(self.filenames)-1:
            i+=1
        else:
            i=0
        self.show_picture()


    def show_last(self):
        global i
        if i>0:
            i-=1
        else:
            i = len(self.filenames)-1
        self.show_picture()

    def select_files(self):
        global ruta_original, i
        self.filenames = []
        i = 0
        if len(self.control_mounth.get()) == 0 and len(self.control_year.get()) == 0:
            ruta_original='//moncivaisms/Media/Fotos/Año 2002/1 Ene 2002'
        elif len(self.control_mounth.get()) == 0:
            ruta_original="//moncivaisms/Media/Fotos/"+self.control_year.get()+"/1 Ene"+self.control_year.get()[3:8]
        elif len(self.control_year.get()) == 0:
            ruta_original="//moncivaisms/Media/Fotos/Año 2002/"+self.control_mounth.get()+" 2002"
        else:
            ruta_original="//moncivaisms/Media/Fotos/"+self.control_year.get()+"/"+self.control_mounth.get()+self.control_year.get()[3:8]
        #self.filenames = next(walk(ruta_original), (None, None, []))[2]
        [self.filenames.append(name) for name in os.listdir(ruta_original) if (name.lower().endswith(".jpg") or name.lower().endswith(".png")) and not name.startswith('._')]
        self.show_picture()
    

    def show_picture(self):
        img = ImageTk.PhotoImage(Image.open(ruta_original+'/'+self.filenames[i]).resize((1920,1080)))
        self.panel.image=img
        self.panel.config(image=img)

    def copy_picture(self):
        original = ruta_original+'/'+self.lista.get(self.lista.curselection())
        #    target = ruta_destino+'/'+self.lista.get(self.lista.curselection())
        #    shutil.copyfile(original, target)



if __name__ == '__main__':
    #creacion de ventana principal
    app=App()
    app.mainloop()