#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk
from Tkinter import *
import cv2
import os
import csv
from tkMessageBox import *
from PIL import Image, ImageTk

import click_mouse
#pathV='/home/fabrice/workspace/DossierIPMC/4Mai/bb.avi'   # path de la vidéo 

class Selection(tk.Frame):
   
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
    
        button2 = tk.Button(frameBtn, text="Select Cages",state="disabled", disabledforeground="#F50743",background="yellow",
                            command=lambda: controller.show_frame("Selection"))
        button3 = tk.Button(frameBtn, text="Detect",
                            command=lambda: controller.show_frame("Detection"))
        button4 = tk.Button(frameBtn, text="Results",
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
        
    def Container(self):         # fontion qui contient tous les wiget et fonctions 
                
        
        contenu=tk.Frame(self,borderwidth=2,width=1000,height=600, relief=GROOVE, bg="#FFFFCC")
        
        contenu.pack(side="top", expand=True,padx=(50,50),pady=(30,10))
        contenu.pack_propagate(False)
          
        
         # ************************** frame qui contient la première image de la vidéo ********************
        frameImage=tk.Frame(contenu,borderwidth=2,width=450,height=400, relief=GROOVE, bg='ivory')
        
        labelTitle=tk.Label(frameImage,borderwidth=2,text="First Video Capture Image",bg= "#f3af38" )
        labelTitle.pack(side="top",padx=10,pady=5)
        
        btn=tk.Button(frameImage,text="captureImg1",activebackground="yellow",          #bouton qui permet l'affchage de la première image
                       command=lambda : self.getPathVideo())                   #appel à la fonction video_to_frame avec les paramètres
        btn.pack(side="top",pady=5)                                                            # le path est pour le moment en haut de la page entrée manuellement
        self.btnclear=tk.Button(frameImage,text="clearImage",state="disabled", disabledforeground="#F50743",          #bouton qui permet l'affchage de la première image
                       command=lambda : self.clearImg())                   #appel à la fonction video_to_frame avec les paramètres
        self.btnclear.pack(side="top",pady=5) 
        
        #*****************************canvas qui contiendra l'image *********************************
        self.canvas=tk.Canvas(frameImage,borderwidth=2,width=300, height=400,relief=GROOVE)
        self.canvas.pack(side="bottom",padx=20,pady=5)
        self.canvas.pack_propagate(False)
        frameImage.pack(side="left",expand=True,padx=(10,10),pady=5)
        frameImage.pack_propagate(False)
        
        
        #btnMulti=tk.Button(frameImage,text="captureImgMulti",activebackground="yellow",          #bouton qui permet l'affchage de la première image
         #              command=lambda : self.getPathVideoMulti())                   #appel à la fonction video_to_frame avec les paramètres
        #btnMulti.pack(side="top")  
        #****************************frame qui contiendra la liste de ROI selectionnés ****************     
        frameList=tk.Frame(contenu,borderwidth=2,width=450,height=400, relief=GROOVE, bg='ivory')
        labelInfo=tk.Label(frameList,borderwidth=2,text="Please draw one ROI for each cage",bg="#f3af38")
        labelInfo.pack(side="top",padx=10, pady=10)
        self.btnAdd=tk.Button(frameList,text="Add Cage",state="disabled",disabledforeground="#F50743",command=lambda:self.getPathImage(pathimg))
        self.btnAdd.pack(padx=10,pady=10)
        self.listRoi=tk.Listbox(frameList,width=40, height=30,)
        self.listRoi.pack(side="bottom",padx=(10,10),pady=(10,20))
        frameList.pack(side="top",expand=True,padx=(10,30),pady=(10,10))
        frameList.pack_propagate(False)
        
        
        #***************************** frame de pie de page ****************************************
        contPie=tk.Frame (self,width=1000, height=70, borderwidth=2, relief=GROOVE,bg="#FFFFCC")
        framePie=tk.Frame(contPie,borderwidth=2, relief=GROOVE,bg='ivory')
        btnSave=tk.Button(framePie,text="SAVE",activebackground="yellow").pack(padx=10,pady=10)
        framePie.pack(side="bottom",padx=10,pady=10)
        
        contPie.pack(padx=5,pady=(10,20),side="bottom")
        contPie.pack_propagate(False)
        


        # ////////////////////////////////////// FONTIONS  /////////////////////////////////////////////////
    def getPathVideo(self):
        global pathV
        #source = csv.reader(open("fichier.csv", "r"))
        source = csv.reader(open("fichierOneVideo.csv", "r"))
        for row in source:
            pathV = row[0]                                           # lire le contenu du fichier "csv" ligne par ligne 
                         
        return self.video_to_frame(pathV,'img')           
    
    '''def getPathVideoMulti(self):# à revoir pour la automatisation
        global pathV
        #source = csv.reader(open("fichier.csv", "r"))
        source = csv.reader(open("fichierMultiVideos.csv", "r"))
        for row in source[0]:
            pathV = row[0]                                           # lire le contenu du fichier "csv" ligne par ligne 
        print pathV               
        return self.video_to_frame(pathV,'img')'''
    
        
    def video_to_frame(self, video, path_output_dir):  # fontion qui récupère le path de la vidéo et donne la première image
            
            global pathimg,photoimg,labelClear,image
            vidcap = cv2.VideoCapture(video)
            vidcap.set(1, 100)
           
            success, image = vidcap.read()
            if success:
                cv2.imwrite(os.path.join(path_output_dir, 'img1.png'),  image)
                img = Image.open("img/img1.png")
                img = img.resize((250,250), Image.ANTIALIAS)
                photoimg = ImageTk.PhotoImage(img)
                #img.show()
                #canvas.create_image(0, 0, image = photoimg, anchor = NW)
                labelClear =tk. Label(self.canvas,image=photoimg)
                labelClear.image = photoimg # keep a reference!
                labelClear.pack()
                labelClear.pack_propagate(False)
            
            self.btnclear.configure(state="active")
            self.btnAdd.configure(state="active")
            pathimg="img/img1.png"
            return pathimg 
         
    def clearImg(self):
        global photoimg
        
        
        #global photoimg
        labelClear.config(image ="")
        labelClear.pack_propagate(False)
        self.btnclear.configure(state="disabled")
        #labelClear.setIcon(Null);
        #labelClear.image.blank()
        #labelClear.image = None
        
        '''root = tk.Tk()
        
        img = ImageTk.PhotoImage(Image.open(path))
        panel = tk.Label(root, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        def callback(e):
            img2 = ImageTk.PhotoImage(Image.open(path2))
            panel.configure(image = img2)
            panel.image = img2
        
        root.bind("<Return>", callback)
        root.mainloop()
                
        #self.canvas.delete(0,"end")  à revoir '''
        
                
    def getPathImage(self, nom):
            global pathImg
            
            pathImg = os.path.dirname(os.path.realpath(__file__))
            pathImg = os.path.join(pathImg, nom)
            
            return self.SelectROI(pathImg)
                
        
        
    def SelectROI(self,chemin):
        
        click_mouse.click(pathImg)  # fonction qui se trouve dans le module click_mouse qui sera appellé pour faire la selection de ROIS , on doit le passer un parametre de chemin de l'image
        
        list=[] #liste qui va contenir les coordonnées 
        source = csv.reader(open("fichierROI.csv", "r"))# fichier qui contient les coordonnées des ROIS selectionnées dans click_mouse
        
        for row in source:
            list=row
            
        #on affiche les coordonnées de ROI selectionné dans un ListBox 
        self.listRoi.insert(END,"from :"+":"+pathV)
        self.listRoi.insert(END,"--------------------------------------------------------------------------------------------- ")
        self.listRoi.insert(END,"you have selected "+" "+str(len(list))+" "+"Roi(s)") 
        self.listRoi.insert(END,"--------------------------------------------------------------------------------------------- ")
        for i in range(len(list)):
                      
            self.listRoi.insert(END,"ROI["+str(i)+']>>>'+list[i])
        
        
           
        #cv2.destroyAllWindows()
            
        