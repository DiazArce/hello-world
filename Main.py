#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter as tk

#modules à import correspondant aux 5 pages
from PageMain import *
from Parameters import * 
from Selection import *
from Detection import *
from Results import *
import click_mouse
class Main(tk.Tk):# Définition de notre classe principale

    def __init__(self):  #  constructeur de notre classe  
        
        tk.Tk.__init__(self) #création de notre fenêtre principale
    
        self.title("IPMC")  # nom de notre fenêtre
        
        #Le conteneur sera l'endroit où on va empiler un tas de cadres ou frames
        #l'un sur l'autre, alors celui que on veut que soit visible
        #Sera élevé au dessus des autres
        
        
        container = tk.Frame(self,borderwidth=2,width=1800,height=1200, relief=GROOVE,bg='ivory')
        container.pack(side="left",expand=True,padx=20,pady=20)
        container.pack_propagate(False)         # evite que le conteneur soit distorsionné
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
 
        self.frames = {}                        

        for f in (PageMain, Parameters, Selection, Detection, Results):
            page_name=f.__name__
            frame = f(container, self)              # On Place toutes les pages au même endroit
                                                    # Celui sur le dessus de l'ordre d'empilement
                                                    # Sera celui qui est visible.
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageMain")                 # On montre la première page
        
    def show_frame(self, page_name):                #fonction qui permet afficher une page pour le nom de page donné
        frame = self.frames[page_name]
        frame.tkraise()
       
if __name__ == "__main__":
        app = Main()
        app.mainloop()

        
        
        
        
        
        
        
        
    
