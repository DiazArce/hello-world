#!/usr/bin/env python
# -*- coding: utf-8 -*
import Tkinter as tk
import ttk
from matplotlib import pyplot as plt #sudo apt-get install python-matplotlib
import random
#import matplotlib.pyplot as plt
import cv2
from Tkinter import *
from PIL import Image, ImageTk

class Results(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        
        frame=tk.Frame(self,borderwidth=2,width=1200,height=50, relief=GROOVE,bg="#FFFFCC")   #Frame on haut dans la tête qui contient les frames 1 ,2 et 3
        frame.pack(side="top", expand=True,padx=20,pady=(20,5))   
             
        
        frameBtn=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')                      #frame qui contient tous les 5 boutons de passage en haut                                                                                       
        frmleft=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')  #Frame 2 et 3 sert comme un conteneur pour
        frmRight=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')                      # le label qui continet l'image de logo ipmc
        
        img = Image.open("ipmc.png")                                                        #avec la librery PIL on utilise le module Image
        photoimg = ImageTk.PhotoImage(img)                                                  # et ImageTk.PhotoImage qui sert à ouvir et charge une image
            
        lblLeft =tk. Label(frmleft,image=photoimg)                                             # Label qui contient l'image de logo ipmc
        lblLeft.image = photoimg 
        lblLeft.pack()
           
        lblRight =tk. Label(frmRight,image=photoimg)
        lblRight.image = photoimg 
        lblRight.pack() 
        
        button = tk.Button(frameBtn, text="Page Main",
                           command=lambda: controller.show_frame("PageMain"))
        button1 = tk.Button(frameBtn, text="Parameters",
                           command=lambda: controller.show_frame("Parameters"))
    
        button2 = tk.Button(frameBtn, text="Select Cages",
                            command=lambda: controller.show_frame("Selection"))
        button3 = tk.Button(frameBtn, text="Detect",
                            command=lambda: controller.show_frame("Detection"))
        button4 = tk.Button(frameBtn, text="Results",state="disabled", disabledforeground="#F50743",background="yellow",
                            command=lambda: controller.show_frame("Results"))
           
        button.pack(side="left",padx= 10, pady=10)
        button1.pack(side="left",padx= 10, pady=10)
        button2.pack(side="left",padx= 10, pady=10)
        button3.pack(side="left",padx= 10, pady=10)
        button4.pack(side="left",padx= 10, pady=10)
        
        frmleft.pack(side="left", expand=True,padx=10,pady=10)  
        frameBtn.pack(side="left", expand=True,padx=10,pady=10) #on charge et on fixe le frame qui contient les 5 boutons
        frmRight.pack(side="left",expand=True,padx=10,pady=10)
        
        self.Container()
        
        
    def Container(self):   
                
        #obj.choose_files.movie_files
        contenu=tk.Frame(self,borderwidth=2,width=1000,height=600, relief=GROOVE,bg="#FFFFCC")
        
        
    
        #exitButton = tk.Button(contenu, text="EXIT",activebackground="yellow", command=exit)
        #exitButton.pack(side="bottom")
        contenu.pack(side="top", expand=True,padx=(50,50),pady=(30,10))
        contenu.pack_propagate(False)
        
        
        
         
        self.frameImage=tk.Frame(contenu,borderwidth=2,width=450,height=400, relief=GROOVE, bg='ivory')
        label=tk.Label(self.frameImage,borderwidth=2,text="Seizure Image",bg= "#f3af38" )
        label.pack(side="top",padx=10,pady=5)
        btnVideo=tk.Button(self.frameImage,text="Open Video",activebackground="yellow")                       
        btnVideo.pack(side="bottom",pady=5)
        self.frameImage.pack(side="left",expand=True,padx=(10,10),pady=(10,10))
        self.frameImage.pack_propagate(False)
        
        frameVideo=tk.Frame(contenu,borderwidth=2,width=450,height=400, relief=GROOVE, bg='ivory')
        
        
        frameVideo.pack(side="left",expand=True,padx=(10,10),pady=(10,10))
        frameVideo.pack_propagate(False)
        
       
        
        contPie=tk.Frame (self,width=1000, height=70, borderwidth=2, relief=GROOVE,bg="#FFFFCC")
        framePie=tk.Frame(contPie,borderwidth=2, relief=GROOVE,bg='ivory')
        btnSave=tk.Button(framePie,text="SAVE",activebackground="yellow").pack(padx=10,pady=10)
        framePie.pack(side="bottom",padx=10,pady=10)
        
        contPie.pack(padx=5,pady=(10,20),side="bottom")
        contPie.pack_propagate(False)
        btnstart=tk.Button(self.frameImage,text="Start",command=self.init)
        btnstart.pack(side="top")    
        
    #GESTION IMAGES ///////////////////  
    def init(self): 
        self.Btnimg = tk.Button(self.frameImage,text="Next",command=self.images)
        self.Btnimg.pack(side="bottom",pady=5)
        
        
        #img=['img0.png','img1.png','img2.png','ipmc.png']
        #img1=random.choice(img)
        img0='img0.png'
        image = Image.open(img0)#PIL
        image = image.resize((350,250), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)
        self.btnClick = tk.Button(self.frameImage, image=self.photo,command= lambda: self.ZoomImage(img0))
        self.btnClick.pack(side="top",padx=10,pady=5)
    
    def images(self):        
         
        img=['img0.png','img1.png','img2.png','img3.png']
        img1=random.choice(img)
        image = Image.open(img1)#PIL
        image = image.resize((350,250), Image.ANTIALIAS) #PIL
        
        self.photo = ImageTk.PhotoImage(image) #PIL
        self.btnClick.configure(image=self.photo)
        self.btnClick.configure(command= lambda: self.ZoomImage(img1))
            
    def ZoomImage(self,image):
        
        img=cv2.imread(image)

        plt.imshow(img,cmap='gray',interpolation='bicubic')
        plt.show()  
        
    
        
        
        
    
        
        
             
    #///////////////////////////////////////////////////////////////////////////////////   
    '''
        self.Btnimg = tk.Button(self.frameImage,text=">>",command=self.images)
        self.Btnimg.pack(side="bottom")    
        img=['img0.png','img1.png','img2.png','ipmc.png']
        img1=random.choice(img)
        image = Image.open(img )#PIL
        image = image.resize((333,222), Image.ANTIALIAS) #PIL
        
        self.photo = ImageTk.PhotoImage(image) #PIL
        
        
        self.btnClick = tk.Button(self.frameImage, image=self.photo,command= lambda: self.pointeur(img1))
        self.btnClick.pack(side="bottom",padx=10,pady=10)
        
    def images(self):
         
        img=['img0.png','img1.png','img2.png','ipmc.png']
        img1=random.choice(img)
        image = Image.open(img1) #PIL
        image = image.resize((333,222), Image.ANTIALIAS) #PIL
        
        self.photo = ImageTk.PhotoImage(image) #PIL
        self.btnClick.configure(image=self.photo)
        
        #canvas=tk.Canvas(frameImage,borderwidth=2,width=100, height=100,relief=GROOVE)
        #canvas.pack(side="bottom",padx=20,pady=20)
        
        
        
        
    def pointeur(self,image):
        
        #images = 'img2.png'
        
        print "qqqqq"   
        #image = 'img1.png'
            
            
        img=cv2.imread(image)

        plt.imshow(img)
        plt.show()'''
        
    #//////////////////////////////////////////////////////////////////////////////////
    '''self.Btnimg = tk.Button(self.frameImage,text=">>",command=self.images)
        self.Btnimg.pack(side="bottom")    
        img='img1.png'
        image = Image.open(img )#PIL
        image = image.resize((333,222), Image.ANTIALIAS) #PIL
        
        self.photo = ImageTk.PhotoImage(image) #PIL
        
        
        self.btnClick = tk.Button(self.frameImage, image=self.photo,command= lambda: self.pointeur(img))
        self.btnClick.pack(side="bottom",padx=10,pady=10)
        
    def images(self):
         
        img=['img0.png','img1.png','img2.png','ipmc.png']
        
        image = Image.open(random.choice(img) )#PIL
        image = image.resize((333,222), Image.ANTIALIAS) #PIL
        
        self.photo = ImageTk.PhotoImage(image) #PIL
        self.btnClick.configure(image=self.photo)
        
        #canvas=tk.Canvas(frameImage,borderwidth=2,width=100, height=100,relief=GROOVE)
        #canvas.pack(side="bottom",padx=20,pady=20)
        
        
        
        
    def pointeur(self,image):
        
        #images = 'img2.png'
        
        print "qqqqq"   
        #image = 'img1.png'
            
            
        img=cv2.imread(image)

        plt.imshow(img)
        plt.show()'''
     #//////////////////////////////////////////////////////////////////////////////////////////   
    
    