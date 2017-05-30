#!/usr/bin/env python
# -*- coding: utf-8 -*
import Tkinter as tk
import ttk
from matplotlib import pyplot as plt
import cv2
from Tkinter import *
from PIL import Image, ImageTk
import csv
class Detection(tk.Frame):
    

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
        button3 = tk.Button(frameBtn, text="Detect",state="disabled", disabledforeground="#F50743",background="yellow",
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
        
    def Container(self):   
                
        #obj.choose_files.movie_files
        contenu=tk.Frame(self,borderwidth=2,width=1000,height=600, relief=GROOVE,bg="#FFFFCC")
    
        contenu.pack(side="top", expand=True,padx=(50,50),pady=(30,10))
        contenu.pack_propagate(False)
        
        
        #/////////////////////////////////  FRAME FICHIERS SEIZURE INFO ///////////////////////////
         
        self.frameImage=tk.Frame(contenu,borderwidth=2,width=450,height=400, relief=GROOVE, bg='ivory')
        label=tk.Label(self.frameImage,borderwidth=2,text="fichiers Seizure",bg= "#f3af38" )
        label.pack(side="top",padx=10,pady=10)
        btn=tk.Button(self.frameImage,text="supprimer fichier",activebackground="yellow",command=self.btnSupp)
        btn.pack(side="top")
        
        self.info=tk.Listbox(self.frameImage,width=40, height=10,)
        self.info.pack(side="top",padx=(20,20),pady=(5,5))   
        
        btnMontrer=tk.Button(self.frameImage,text="ListFichiers",command=self.ListFichiers)
        btnMontrer.pack(side="top")
        self.frameImage.pack(side="left",expand=True,padx=(10,10),pady=(10,10))
        self.frameImage.pack_propagate(False)
        
        
     #////////////////////////////////////// FRAME POUR BAR PROGRESS /////////////////////////////   
        frameProg=tk.Frame(contenu,borderwidth=2,width=450,height=400, relief=GROOVE, bg='ivory')
        label=tk.Label(frameProg,borderwidth=2,text="Progress",bg="#f3af38")
        label.pack(side="top",padx=10, pady=10)
        btnStop=tk.Button(frameProg,text="Stop",activebackground="yellow")
        btnStop.pack(side="top",padx=10,pady=10)
        btnRestart=tk.Button(frameProg,text="Restart",activebackground="yellow")
        btnRestart.pack(side="top",padx=10,pady=(10,30))
        self.button = ttk.Button(frameProg,text="start", command=self.start)
        self.button.pack(side="bottom",pady=20)
        self.progress = ttk.Progressbar(frameProg, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack(side="top",pady=50)

        self.bytes = 0
        self.maxbytes = 0
        frameProg.pack(side="top",expand=True,padx=(10,30),pady=(10,10))
        frameProg.pack_propagate(False)
        
        
     # ///////////////////////////////////// FRAME PIE DE PAGE ///////////////////////////////////////////   
        contPie=tk.Frame (self,width=1000, height=70, borderwidth=2, relief=GROOVE,bg="#FFFFCC")
        framePie=tk.Frame(contPie,borderwidth=2, relief=GROOVE,bg='ivory')
        btnSave=tk.Button(framePie,text="SAVE",activebackground="yellow").pack(padx=10,pady=10)
        framePie.pack(side="bottom",padx=10,pady=10)
        
        contPie.pack(padx=5,pady=(10,20),side="bottom")
        contPie.pack_propagate(False)
    
    
        self.label=tk.Label(self.frameImage,text="select analyse ")   
        self.label.pack(side="left",padx=5)
        self.choix = IntVar()
        self.entry= tk.Entry(self.frameImage,textvariable=self.choix,width=5)
        self.entry.pack(side="left",padx=10,pady=10) 
        
        self.btn=tk.Button(self.frameImage,text="montrer")
        self.btn.pack(side="left",padx=5)
        self.btnClear=tk.Button(self.frameImage,text="clear",command=self.clear)
        self.btnClear.pack(side="right",padx=10)
        
        #self.btnSupp=tk.Button(self.frameImage,text="supprimer",command=self.btnSupp)
        #self.btnSupp.pack(side="top",padx=5)
    def start(self):
        self.progress["value"] = 0
        self.maxbytes = 50000
        self.progress["maximum"] = 50000
        self.read_bytes()

    def read_bytes(self):
        '''simulate reading 500 bytes; update progress bar'''
        self.bytes += 500
        self.progress["value"] = self.bytes
        
        if self.bytes < self.maxbytes:
            # read more bytes after 100 ms
            self.after(100, self.read_bytes)   
    
        
        
    #////////////////////////////////// GESTION FICHIER SEIZURE //////////////////////////////////   
    
    
    
    def csv_to_var(self,dico):
       global nameVideo, fps, duration , Number_of_img_seizure
           
       nameVideo = dico[0]
       fps = dico[1]
       duration = dico[2]
       Number_of_img_seizure=dico[3]
      
    def var_to_csv(self,dico):
       dico[0] = nameVideo
       dico[1] = fps
       dico[2] = duration
       dico[3]= Number_of_img_seizure
        
    def ListFichiers(self):
        self.info.delete(0,"end")
        self.liste=[]
        cpt=1
        source = csv.reader(open("fichierMultiVideos.csv", "r"), delimiter=',')
        
        self.info.insert(END,"**********VIDEOS ANALYSÉS********* "  )
        for line in source:
            l=[]                #liste qui contiendra les informations d'un contact sans les balises VCard
            for x in line:
                
                l.append(x)
            self.liste.append(l)
            self.csv_to_var(l)
            
            self.info.insert(END,str(cpt)+". >>> " + nameVideo )
            cpt=cpt+1
            
        self.entry.configure(textvariable=self.choix)
        self.btn.configure(command=self.ok)
        
        '''self.label=tk.Label(self.frameImage,text="select analyse ")   
        self.label.pack()
        self.choix = IntVar()
        self.entry= tk.Entry(self.frameImage,textvariable=self.choix,width=5)
        self.entry.pack(side="left",padx=(50,5),pady=(5,5))  
        
        
        btn=tk.Button(self.frameImage,text="ok", command=self.ok)
        btn.pack()'''
        
    def ok(self):
            
            self.info.delete(0,"end") 
            choix=self.choix.get()
            if  choix!="":
                choix=int(choix)
                choix=choix-1
                liste=self.liste[choix]
                self.csv_to_var(liste)
             
             
                self.info.insert(END,"Name :   "+nameVideo )
                self.info.insert(END,"fps :   "+fps )
                self.info.insert(END,"duration :   "+duration )
                self.info.insert(END,"Numbers :   "+ Number_of_img_seizure ) 
            
            #return self.montrer_contacts()
        
        
       
        
      
         
     
    def rewrite(self,dico):                #Réecrit le fichier vCard après modification d'une liste "dico"
        global nameVideo, fps, duration ,Number_of_img_seizure
        source = csv.writer(open("fichierMultiVideos.csv", "w"))
        for i in dico:
            nameVideo = i[0]
            fps = i[1]
            duration = i[2]
            Number_of_img_seizure = i[3]
            source.writerow([nameVideo,fps,duration,Number_of_img_seizure])
        
    '''def supprimer(self):   
        self.liste=[]
        cpt=1
        source = csv.reader(open("fichierMultiVideos.csv", "r"), delimiter=',')
        self.info.insert(END,"tapez le numero de fichier à suprimer "  ) 
        for line in source:
            l=[]                #liste qui contiendra les informations d'un contact sans les balises VCard
            for x in line:       
                l.append(x)
            self.liste.append(l)
            self.csv_to_var(l)
            #print(cpt,". >>> " + nameVideo )
            #cpt=cpt+1
            self.info.insert(END,str(cpt)+". >>> " + nameVideo )
            
            cpt=cpt+1
          
            #print("\n")
            
        self.entry.configure(textvariable=self.choix)
        #label=tk.Label(self.frame,text="Entrez le numéro du fichier pour supprimer")   
        #label.pack()
        #self.btnSupp.configure(command=self.btnSupp)
        '''
    def btnSupp(self):    
        
        
        choix=self.choix.get()
        #entry= tk.Entry(self.frameImage,textvariable=choix,width=5)
        #entry.pack(side="left",padx=(50,5),pady=(5,5))
         
        choix=int(choix)
        choix=choix-1
        
        #liste=self.liste[choix]
        #self.csv_to_var(liste)
        
        self.liste.pop(choix)        #On retire l'élement choisi de la liste des contacts
        self.rewrite(self.liste) 
        
        return self.ListFichiers()
    
    def clear(self):  # On effacer tout le contenu affiché dans le listBox
          
        self.info.delete(0,"end")
           
        
           
         
        