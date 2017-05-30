#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import csv
import Tkinter as tk
from Tkinter import *
from tkFileDialog import askopenfilename, askdirectory,askopenfilenames  # chercher le path d'un fichier
import subprocess 
from os import listdir # pour afficher le contenu d'un repertoire
from tkMessageBox import * # dialogo message de confirmation
from Selection import *
from PIL import Image, ImageTk


import re
class Parameters(tk.Frame):  # Definition de notre class Parameters 

    def __init__(self, parent, controller): # constructeur de notre class
        tk.Frame.__init__(self, parent)
        
        
        
        frame=tk.Frame(self,borderwidth=2,width=1200,height=50, relief=GROOVE,bg="#FFFFCC") #Frame on haut dans la tête qui contient les frames pour les boutons et les images
        frame.pack(side="top", expand=True,padx=20,pady=(20,5))   
             
        
        frameBtn=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')                    #frame qui contient tous les 5 boutons de passage en haut                                                                                       
        frmleft=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')                     #Frame left et right sert comme un conteneur pour,
        frmRight=tk.Frame(frame,borderwidth=2, relief=GROOVE,bg='ivory')                         # le label qui continet l'image de logo ipmc
        
        img = Image.open("ipmc.png")                                                        #avec la librery PIL on utilise le module Image
        photoimg = ImageTk.PhotoImage(img)                                                      # et ImageTk.PhotoImage qui sert à ouvir et charge une image
             
        lblLeft =tk. Label(frmleft,image=photoimg)                                          # Label qui contient l'image de logo ipmc
        lblLeft.image = photoimg 
        lblLeft.pack()
           
        lblRight =tk. Label(frmRight,image=photoimg)
        lblRight.image = photoimg 
        lblRight.pack() 
          
        # les boutons qui permettent le passage entre pages
        
        button = tk.Button(frameBtn, text="Page Main",
                           command=lambda: controller.show_frame("PageMain"))
        button1 = tk.Button(frameBtn, text="Parameters",state="disabled",background="yellow", disabledforeground="#F50743",
                           command=lambda: controller.show_frame("Parameters"))    
        button2 = tk.Button(frameBtn, text="Select Cages",
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
       
        # variables de controle 
        
        self.filename = StringVar(value='Results')
        self.fps = StringVar()
        self.hh = StringVar()
        self.mm=StringVar()
        self.ss=StringVar()
        self.movie_files=StringVar()
        self.Contenu()
       
               
    def Contenu(self):  # fontion qui contient tous les wiget et fonctions 
        
        contenu=tk.Frame(self,borderwidth=3,width=1000,height=600, relief=GROOVE, bg="#FFFFCC" )  #Frame Conteneur du contenu qui contient 4 grandes frames
        contenu.pack(side="top", expand=True,padx=(50,50),pady=(30,10))
        contenu.pack_propagate(False)
     
        
    #////////////////////////////// CONTENU FRAME PATH et INFO VIDEO /////////////////////////////////////////////////////          
    
        contVideo=tk.Frame(contenu,width=900,height=200, borderwidth=2, relief=GROOVE,bg='ivory') #conteneur generale
        
        #***************************************frame pour les boutons a gauches correspondant à select videos***************************
        framebtn1=tk.Frame(contVideo,borderwidth=2, relief=GROOVE,bg="#FFFFCC") 
        button=tk.Button(framebtn1,text="Select MultiVideos",activebackground="yellow",command=self.selectMultiVideo)
        button.pack(side="top",padx=(10,10),pady=(10,10))
        
        btnInfo=tk.Button(framebtn1,text="Select a Video",activebackground="yellow",command=self.selectOneVideo)
        btnInfo.pack(side="top",padx=10,pady=(5,5))  
                       
        framebtn1.pack(side="left",padx=(10,10),pady=(10,10))
        
        #************************** la listBox où s'affichera les info demandé **************************
        self.info=tk.Listbox(contVideo,width=60, height=10,)
        self.info.pack(side="left",padx=(20,20),pady=(5,5))
        #fpsInfo=StringVar()
        
        #************************************frame pour les boutons à droit correspondant à effacer la listBox******************************
        framebtn2=tk.Frame(contVideo,borderwidth=2, relief=GROOVE,bg="#FFFFCC")       
        btnClear=tk.Button(framebtn2,text="Restart",activebackground="yellow",command=self.clear)
        btnClear.pack(side="bottom",padx=10,pady=(5,5)) 
               
        framebtn2.pack(side="right",padx=10,pady=(10,10))
        
        contVideo.pack(padx=50,pady=(30,10),side="top")
        contVideo.pack_propagate(False)
              
        
        
    #////////////////////////////// CONTENEUR FRAME POUR FPS /////////////////////////////////////////////////////    
        contFPS=tk.Frame(contenu,width=900,height=100, borderwidth=2, relief=GROOVE,bg='ivory')
        
        label=tk.Label(contFPS,text="Select FPS : ").pack(side="left",padx=(80,100),pady=(5,5))
        #fps = StringVar()
        sb = tk.Spinbox(contFPS,values=(25,30),textvariable=self.fps)
        sb.pack(side="left",padx=(93,93),pady=(5,5))            
        #button= tk.Button(contFPS, text="OK") 
        #button.pack(side="right",padx=(20,20),pady=(20,20))
                  
        contFPS.pack(padx=50,pady=5,side="top")
        contFPS.pack_propagate(False)      
        
        
    # ////////////////////////////// CONTENEUR FRAME POUR LA  DUREE /////////////////////////////////////////////////////              
        contDure=tk.Frame (contenu,width=900,height=100, borderwidth=2, relief=GROOVE,bg='ivory')
        
            
        label=tk.Label(contDure,text="Select Duration Video : ").pack(side="left",padx=(60,50),pady=(5,5))
        hh = StringVar()
        heures= tk.Entry(contDure,textvariable=self.hh,width=5)
        heures.pack(side="left",padx=(50,5),pady=(5,5))
        hhlabel=tk.Label(contDure,text="HH").pack(side="left",padx=(10,50),pady=(5,5))
                
        #mm=StringVar()
        minutes = tk.Entry(contDure,textvariable=self.mm,width=5)
        minutes.pack(side="left",padx=(30,5),pady=(5,5))
        mmlabel=tk.Label(contDure,text="MM").pack(side="left",padx=(5,60),pady=(5,5))
               
        #ss = StringVar()
        seconde= tk.Entry(contDure,textvariable=self.ss,width=5)
        seconde.pack(side="left",padx=(30,5),pady=(5,5))
        
        sslabel=tk.Label(contDure,text="SS").pack(side="left",padx=(10,50),pady=(5,5))    
        
        
        #button= tk.Button(contDure, text="OK") 
        #button.pack(side="right",padx=(30,20),pady=(20,20))
        
        contDure.pack(padx=5,pady=5,side="top")
        contDure.pack_propagate(False)
      
          
        
    #////////////////////////////// CONTENEUR FRAME POUR FILE NAME txt /////////////////////////////////////////////////////                     
        contFile=tk.Frame (contenu,width=900,height=100, borderwidth=2, relief=GROOVE,bg='ivory')
        
        
        label=tk.Label(contFile,text="Analysis file name : ").pack(side="left",padx=(60,40),pady=(5,5))
       
        self.entry = tk.Entry(contFile,textvariable=self.filename,width=40)   # boite pour ecrire le nom du fichier
        self.entry.pack(side="left",padx=(50,5),pady=(5,5))
        
        btnframe=tk.Frame(contFile,borderwidth=1, relief=GROOVE,bg="#FFFFCC")    #frame qui contient les boutons
        
        btnfile= tk.Button(btnframe, text="open",command=self.choose_file_name)
        btnfile.pack(side="top",padx=(20,20),pady=(5,5))
        #btnOk= tk.Button(btnframe, text="OK") 
        #btnOk.pack(side="bottom",padx=(20,20),pady=(5,5))
        
        btnframe.pack(side="right",padx=(30,30),pady=(5,5))
        
        contFile.pack(padx=5,pady=5,side="top")
        contFile.pack_propagate(False)
        
               
        
    #////////////////////////////// CONTENEUR FRAME POUR PIE de PAGE  /////////////////////////////////////////////////////       
        
        contPie=tk.Frame (self,width=1000, height=70, borderwidth=3, relief=GROOVE,bg="#FFFFCC")
        framePie=tk.Frame(contPie,borderwidth=2, relief=GROOVE,bg='ivory')
        btnSave=tk.Button(framePie,text="SAVE",activebackground="yellow",width=10, height=9,command=self.save)
        btnSave.pack(padx=5,pady=5)
        btnSave.pack_propagate(False)
        framePie.pack(side="bottom",padx=5,pady=5)
        
        contPie.pack(padx=5,pady=(10,20),side="bottom")
        contPie.pack_propagate(False)
        
        
        
    #**************************************** FONCTIONS ************************************************
      
    
    
       
    def save(self):          #On récupère la valeur de fps, duration, nom de fichier text, et  On l'enregistre dans les variables
            global file
            #nomFile=self.filename.get()
            choose_file_name = self.filename.get()
            nomFile = choose_file_name + '.txt'
            
            fps=self.fps.get()
            heure=self.hh.get()
            minute=self.mm.get() 
            seconde=self.ss.get()
            
            
             
            if  minute!="" and nomFile!="" and heure!="" and fps!="" and seconde!="":      #si tous les info ont été saisi , message de confirmation et on peut envoyer les parametres             
                showinfo('result','Your selection has been registered successfully!!! .\nNext step Select Cages!')
                
                source = csv.writer(open("fichierVar.csv", "w"))
                source.writerow([file,fps,heure,minute,seconde,nomFile]) 
                                
            else:
                showwarning('Résult','Attention empty spaces.\nwould you like to complete please  !')                            
                
            
       
    def selectMultiVideo(self):   # On selectionne un repertoire et on affiche le contenu
            
            
            pathDir=askdirectory(title="Choose a directory to save to",initialdir = '/home/fabrice/IPMC/VIDEOS').encode('utf-8')
            
            if pathDir != "" :    
                self.info.insert(END,"--------------------------------------------------------------------------------------------- ")
                self.info.insert(END,"****************  PATH DIRECTORY SELECTED  **************")
                self.info.insert(END,"--------------------------------------------------------------------------------------------- ")
                self.info.insert(END,pathDir)
                self.info.insert(END,"\n","--------------------------------------------------------------------------------------------- ")
                self.info.insert(END,"*********************** CONTENT : ************************")
                
                dirs = os.listdir(pathDir)

                for file in dirs:
                                    
                    command = ['ffmpeg', '-i', pathDir+'/'+file]
                            
                    p = subprocess.Popen(command, stderr=subprocess.PIPE)
                
                    text = p.stderr.read() 
                    
                    duration = re.search(r'Duration:(\s)*((\d+[:])*(\d+)[.](\d+))', text)               
                    if duration is not None:

                        duration = duration.group(2)      
                
                
                    fps = re.search(r'(\d+([\,\.]{1}\d+)?)(\s)fps', text)
                    if fps is not None:

                        fps = fps.group(1)
                     
                        
                    self.info.insert(END,"Name :   "+file )
                    self.info.insert(END,"fps :   "+fps )
                    self.info.insert(END,"duration :   "+duration )
                    self.info.insert(END,"--------------------------------------------------------------------------------------------- ")
                   
                    #fichier qui va contenir le file, fps et duration de tous les vidéos selectionnés
                    source = csv.writer(open("fichierMultiVideos.csv", "a")) # à revoir
                    source.writerow([pathDir+'/'+file,fps,duration])
                
                          
            else: 
                self.info.insert(END,"************************ You have not selected No folder!!! ... ********************")
            
    def selectOneVideo(self):      # On selectionne un filevideo et on affiche les info de fps et duration
            
            global file 
            path_movie_file = askopenfilename(filetypes = [("Video files", "*.avi *.flv *.mp4 *.mpeg *.asf *.dav")], title=("Choose a video file"),initialdir = '/home/fabrice/IPMC/VIDEOS')
            file=path_movie_file
            
            if file != "":
                '''vidFile = cv2.VideoCapture(path_movie_file)
                
                nFrames = int(vidFile.get(cv2.CAP_PROP_FRAME_COUNT))  # on obtient le numero total de frames
                fpsInfo = vidFile.get(cv2.CAP_PROP_FPS)               # on obtient le frame par seconde de la vidéo
                duration=nFrames/(fpsInfo*60)                     #on obtient la duration de la vidéo en minutes
                '''
                command = ['ffmpeg', '-i', file]
                
                
                
                p = subprocess.Popen(command, stderr=subprocess.PIPE)
                
                text = p.stderr.read()                
                  
                duration = re.search(r'Duration:(\s)*((\d+[:])*(\d+)[.](\d+))', text)
                if duration is not None:

                    duration = duration.group(2)              
                
                fps = re.search(r'(\d+([\,\.]{1}\d+)?)(\s)fps', text)
                if fps is not None:

                    fps = fps.group(1)
                



                self.info.insert(END," ***************************************************************")
                self.info.insert(END,"                         INFO (FPS and DURATION)                            ")
                self.info.insert(END," ------------------------------------------------------------------------------------------- -")
                self.info.insert(END,"from :   "+ file)
                self.info.insert(END,"fps :   "+fps)           
                self.info.insert(END,"duration : "+duration)
                self.info.insert(END," **************************** END *****************************")
                
                source = csv.writer(open("fichierOneVideo.csv", "w"))
                source.writerow([file,fps,duration])
            
            else:               
                self.info.insert(END,"************************ You have not selected No file!!! ... ********************")
            
    #correspondant à l'automatisation
    '''def choose_videos(self):  # On selectionne un ou plusieurs videos et on l'affiche        
    
            
            movie_files = askopenfilenames(filetypes = [("Video files", "*.avi *.flv *.mp4 *.mpeg *.asf *.dav")], title=("Choose a video(s) file"),initialdir = '/home/fabrice/IPMC/VIDEOS')
            path=movie_files
            
            if path!= "":
            
                self.info.insert(END," ------------------------------------------------------------------------------------------- ")
                self.info.insert(END,"                                             VIDEO(S) SELECTED                                        ")
                self.info.insert(END," ------------------------------------------------------------------------------------------  ")
                self.info.insert(END,path) 
            #return path   
            else:              
                self.info.insert(END,"************************ You have not selected No file(s)!!! ... ********************")  
    
            source=csv.writer(open("fichierPath.csv", "w"))
            source.writerow(path)   '''
                    
                    
   
    def choose_file_name(self):  # On on récupère le nom du fichier où sera stocké les infos de "seizure infos"
            
            choose_file_name= askopenfilename(filetypes = [("files", "*.txt ")], title=("Choose a  file"),initialdir = '/home/fabrice/IPMC/')
            file=choose_file_name
            
            self.entry.delete(0,"end") 
            self.entry.insert(END, file)
            
            
                         
    def clear(self):  # On effacer tout le contenu affiché dans le listBox
          
        self.info.delete(0,"end") 
        
            
    
                        
    
            
                 
         
            