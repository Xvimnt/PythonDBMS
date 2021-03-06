
import tkinter 
import tkinter as ttk
import tkinter as tk
from tkinter import scrolledtext as st
from tkinter import messagebox
from tkinter import Button
from tkinter import LabelFrame
from tkinter import  Label 
from tkinter import Menu
from tkinter import tix

from PIL import ImageTk, Image
# Librerias para la conexion
import socket
import sys
import http.client
import binascii
import json
class Aplicacion:

    def __init__(self):
        
        self.ventana1=tk.Tk()
        self.ventana1.title('TytusDB')
        self.ventana1.geometry("850x850+100+100")
        self.ventana1.configure(background='white')
        #PANEL PARA LAS PESTAÑAS
        #self.load = tk.Image.open("icondb.png")
        #self.ventana1.iconphoto(False, ImageTk.PhotoImage(self.load))
        #TEXTO DE ENTRADA
        self.scrolledtext1=st.ScrolledText(self.ventana1, wrap = tk.WORD, width = 50, height = 7, font = ("Times New Roman", 15))
        self.scrolledtext1.place(x=290, y=40)
        self.framecopia()        

        #TEXTO DE SALIDA
        self.scrolledtext2=st.ScrolledText(self.ventana1, wrap = tk.WORD, width = 50, height = 7, font = ("Times New Roman", 15))
        self.scrolledtext2.place(x=290, y=250) 

        #MENU
        self.menubar = Menu(self.ventana1,  background="gray")
        self.ventana1.config(menu=self.menubar)
        self.fileMenu = Menu(self.menubar)
        self.fileMenu.add_command(label="Exit", command=self.Exit)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.menubar.add_cascade(label="Object")
        self.menubar.add_cascade(label="Tools")        
        self.FileA = Menu(self.menubar)
        self.FileA.add_command(label="Acerca de", command=self.MensajeAcercaDe)
        self.FileA.add_command(label="Conectar",command=self.Conexion)
        self.menubar.add_cascade(label="Help", menu=self.FileA)

        #BARRA DE HERRAMIENTAS DEL CENTRO
        self.BarraHerramientas = LabelFrame(self.ventana1, text= '', background="white")
        self.BarraHerramientas.grid(row=0, column=0, columnspan=3, pady=95)
        self.BarraHerramientas.place(x=450, y=210)
            #IMAGEN DEL CENTRO
        self.load1 = Image.open("tytus.gif")
        self.render1 = ImageTk.PhotoImage(self.load1)
        self.img1 = Label(self.ventana1, image=self.render1)
        self.img1.image = self.render1
        self.img1.place(x=290, y=210)
        tk.Label(self.ventana1, text = "Salida", font = ("Arial", 20), background = '#B5F5E0', foreground = "black").place(x=370, y=210)
            #BOTON CORRER
        self.boton1=ttk.Button(self.BarraHerramientas, text="RUN", command=self.copiar)
        self.boton1.pack()
        #BOTON CONEXION

        #IMAGEN
        self.load = Image.open("icondb.png")
        self.render = ImageTk.PhotoImage(self.load)
        self.img = Label(self.ventana1, image=self.render)
        self.img.image = self.render
        self.img.place(x=0, y=0)

        self.ventana1.iconphoto(False, ImageTk.PhotoImage(self.load))
        self.ventana1.mainloop()
        
#CONFIGURANDO PARA LA BASE DE DATOS.
    def framecopia(self):
        self.Bases = LabelFrame(self.ventana1, text= 'BASES DE DATOS EXISTENTES', background="white")
        self.Bases.grid(row=0, column=0, columnspan=3, pady=95)
        Label(self.Bases, text='BASES DE DATOS 1').grid(row=1, column=0)
        Label(self.Bases, text='BASES DE DATOS 2').grid(row=2, column=0)
        Label(self.Bases, text='BASES DE DATOS 3').grid(row=3, column=0)
        Label(self.Bases, text='BASES DE DATOS 3.1').grid(row=4, column=1)
        Label(self.Bases, text='BASES DE DATOS 3.2').grid(row=5, column=1)
        Label(self.Bases, text='BASES DE DATOS 4').grid(row=6, column=0)   
    
    def copiar(self):
        #iniciofila=self.dato1.get()
        #iniciocolumna=self.dato2.get()
        #finfila=self.dato3.get()
        #fincolumna=self.dato4.get()        
        datos=self.scrolledtext1.get(1.0, tk.END)
        self.scrolledtext2.delete("1.0", tk.END)        
        self.scrolledtext2.insert("1.0", datos)
        self.Conexion()
        return datos
 
        
    def MensajeAcercaDe(self):          
                  self.messagebox.showinfo(message="ESTE PROGRAMA ES REALIZADO \n POR EL GRUPO 8:\n "
                +"Cinthya Andrea Palomo Galvez 201700670 \n Karla Julissa Ajtún Velásquez 201700565 \n"
                +"Javier Alejandro Monterroso Lopez 201700831 \n Byron Antonio Orellana Alburez 201700733 \n"
                +" Version 1.0.0", title="TytusDB")
               
    def Exit(self):
            messagebox.showinfo(message="Gracias por utilizar este programa! :v", title="TytusDB")
            quit();
    def Conexion(self):
        try:
                conexion= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("Conexion exitosamente creada")
        except socket.error as err:
                messagebox.showinfo(message="La creacion de la conexion fue un fracaso por: " + str(err) + ")", title="Conexion")
        port= 4040
        try:
                host_ip= socket.gethostbyname('localhost')#conectandome con el servidor
                 #para enviar informacrootion se necesita la libreria sendall
        except socket.gaierror:
                print("Hubo un error en la conexion")
                sys.exit()
        conexion.connect((host_ip,port))
        print("Servidor conectado exitosamente " +str(port))
        messagebox.showinfo(message="Conexion exitosamente creada", title="Conexion")
        # en vez de parameters va el texto del textarea
        parametros= self.scrolledtext1.get(1.0,tk.END)
        self.scrolledtext2.delete("1.0",tk.END)
        self.scrolledtext2.insert("1.0",parametros)                              
        
        jsonData = { "msg": parametros }
        myJson = json.dumps(jsonData)
        myConnection = http.client.HTTPConnection('localhost', 8000, timeout=10)
        headers = {
            "Content-type": "application/json"
        }
        myConnection.request("POST", "/", "", headers)
        response = myConnection.getresponse()
        print(response)
aplicacion1=Aplicacion()