#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import csv
if __name__ == '__main__' :



    # déclaration des variables concernant les régions d'intérêt
    '''std::vector<Rect> vecRect ;
    int numberOfRois = 0 ;'''
    vecRect =[]
    numberOfRois = 0 

    # variable de réduction de la taille de l'image
    '''float scale = .25 ;'''
    scale = .25 


    #déclaration des matrices OPENCV -- conteneurs pour images (Mat correspond à cv::Mat)
    '''Mat frame, previous_gray, next_gray, flow ;'''
    #frame        
    #previous_gray
    #next_gray
    #flow
    # déclaration et initialisation des conteneurs vidéos, à partir du fichier donné en argument #1
    '''VideoCapture cap(argv[1]) ;
	vidcap = cv2.VideoCapture(video)
    if(!cap.isOpened())
        return -1 ;'''
        #recuperation du path fichier csv : source = csv.reader(open("fichier.csv", "r")) 
    source = csv.reader(open("fichierVar.csv", "r"))
    for row in source:
            videoPath = row[0]
    
    vidcap=cv2.VideoCapture(videoPath)  
    #if not vidcap.isOpened():
     #       return -1 


    # initialisation des zones d'intéret à partir du fichier donné en paramètre #2
    '''std::ifstream file_rects(argv[2]) ;
    if(!file_rects)
    {
        std::cerr << "Erreur à l'ouverture du fichier de zones d'intérets!" << std::endl;
        return -1 ;
    }
    file_rects >> numberOfRois ;
    for (int i = 0 ; i < numberOfRois ; i++)
    {
        int x, y, w, h ;
        file_rects >> x >> y >> w >> h ;'''
     
    vecRect=[]
    file_rects = csv.reader(open("fichierROI.csv", "r")) #"à revoir pour la recuperation des coordonnées de la selection"
    for row in file_rects:
        vecRect.append(row)       
            
       # dans la variable de type std::vecteur, on place les coordonées du point haut/gauche, la longueur etla largeur de chaque zone d'intérêt
        # on met ces zones à l'échelle qui sera celle de l'image traitée
    '''vecRect.push_back(Rect(x*scale, y*scale, w*scale, h*scale)) ;
		}    
	file_rects.close() ;'''
    #vectRect.append((x*scale, y*scale,w*scale,h*scale))#à revoir 
        
    

    # délaration du fichier sur lequel on enregistrera les données brutes
    '''std::ofstream file(argv[3], std::ios::out | std::ios::trunc) ;
    if(!file)
    {
        std::cerr << "Erreur à l'ouverture !" << std::endl;
        return -1 ;
    }'''
    file_rects_out = csv.reader(open("fichier.csv", "w"))  #"à revoir pour l'enregistrement de données brutes"
    
    
    # initialisation de la présence d'affichage (boolean -> déclaration de la fenêtre si affichage)
    '''bool disp = atoi(argv[4]) ;
    if (disp)
    {
            namedWindow("frames", 1) ;
    }'''
    
    # initialisation de la variable FPS et mise à jour des paramètres du conteneur de capture des frames vidéos
    '''int fps = atoi(argv[5]) ;
    cap.set(CV_CAP_PROP_FPS, fps) ;'''
    
    source = csv.reader(open("fichierVar.csv", "r"))  # à revoir pour la recuperation de fps //////////////////////////////////////////////
    for row in source:
            fps = row[1]
            
            
    vidcap.set(cv2.CAP_PROP_FPS, fps)
    

   # variables de début de traitement de la vidéo -> arg[6] est l'index de l'heure, multiplié par 3600 secondes, multiplié par 1000 millisecondes
    '''long double tbegin = atoi(argv[6]) * 3600 * 1000 ;'''
    
    
    source = csv.reader(open("fichierVar.csv", "r")) #à revoir pour la récuperation de l'index de l'heure ///////////////////////////////////////////////////
    for row in source:
            Index_duration = row[2]
     
    
    tbegin = int(Index_duration) * 3600 * 1000
    #print tbegin
    # variables de fin de traitement de la vidéo -> tbegin + 1heure en millisecondes.
    # Attention, si le fps est différent de 30 (valeur par défaut), on appliquera un coeeficient multiplicateur fps/30 (soit deux fois plus d'images si fps == 60, 2 fois moins d'images si fps == 15, etc)
    '''long double tend = tbegin + 3600*1000 ;'''
   
    tend = int(tbegin) + 3600*1000
    #print tend

   #si on est en fin du fichier vidéo, et qu'il ne s'agit pas d'une heure complète, alors on met à jour tend en fonction
    '''if (cap.get(CV_CAP_PROP_FRAME_COUNT)/cap.get(CV_CAP_PROP_FPS)*1000 < tend)
        tend = cap.get(CV_CAP_PROP_FRAME_COUNT)/cap.get(CV_CAP_PROP_FPS)*1000 ;'''
    nFrames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))  # on obtient le numero total de frames
    Fps = vidcap.get(cv2.CAP_PROP_FPS)
   
    if (nFrames / Fps) * 1000 < tend:
        tend = vidcap.get(nFrames) / vidcap.get(Fps)*1000 
        

    # on initialise le fichier conteneur de frames à l'heure de démarrage du traitement
    '''cap.set(CV_CAP_PROP_POS_MSEC, tbegin) ;'''
    vidcap.set(cv2.CAP_PROP_POS_MSEC, tbegin) 

    # on récupère une première image dans la variable frame
    '''cap >> frame ;'''
    frame = vidcap.read() 
    
    # conversion en niveau de gris
    '''cvtColor(frame, previous_gray, COLOR_BGR2GRAY) ;'''
    cv2.cvtColor(frame,previous_gray, cv2.COLOR_BGR2GRAY)
    
    # on diminue la taille de l'image (peut être paramétré ?)  
    '''resize(previous_gray, previous_gray, Size(), scale, scale, INTER_CUBIC) ;'''
    cv2.resize(previous_gray, previous_gray, Size(), scale, scale, cv2.INTER_CUBIC)# Size?
    
    # on convertit le type de l'image (UINT plutôt que double)
    '''previous_gray.convertTo(previous_gray, CV_8U) ;'''
    previous_gray.cv2.convertScaleAbs(previous_gray,cv2.CV_8U) # 
     
   # un peu de lissage ; flou gaussien
    '''blur(previous_gray, previous_gray, Size(5, 5)) '''
    cv2.blur(previous_gray, previous_gray,(5,5))
    
    # on revient au type "double"
    '''previous_gray.convertTo(previous_gray, CV_32FC3) ;'''
    previous_gray.convertTo(previous_gray, cv2.CV_32FC3) 

    '''********************* on garde pour plus tard ; sert à initialiser une vidéo qui montre les résultats de la détection
    char videoOutput[128] ;
    sprintf(videoOutput, "%s/output%02d.avi", argv[7], atoi(argv[6])) ;
    *********************'''


    # boucle frame by frame jusqu'à fin de l'heure considérée
    '''while (cap.get(CV_CAP_PROP_POS_MSEC) < tend)'''
    while (vidcap.get(cv2.CAP_PROP_POS_MSEC) < tend):
    
    
            
        # on extraie une nouvelle image de la vidéo
        '''cap.read(frame) '''
        vidcap.read(frame) ;
        try:
        

            # initilisation des variables d'enregistrement des données brutes -> ici horodotage
           
            '''char str[8] = "-" ;
				sprintf(str, "%d%%", int((cap.get(CV_CAP_PROP_POS_MSEC) - tbegin)/(tend-tbegin)*100)) ;'''
            sprintf(str, "%d%%", int((vidcap.get(cv2.CAP_PROP_POS_MSEC) - tbegin)/(tend-tbegin)*100)) 

            # si on a décidé d'afficher, et bien ça affiche des valeurs ;)
            '''if (disp)
            {               
                Point p(10, 30) ;
                putText(frame, str, p, FONT_HERSHEY_PLAIN, 2, Scalar(255, 255, 255), 3, 8, false) ;
            }
            else
            {
                std::cout << "\b\b\b\b\b\b\b\b\b\b" << str ;
            }'''

            # conversion niveau de gris
            '''cvtColor(frame, next_gray, COLOR_BGR2GRAY) ;'''
            cv2.cvtColor(frame,next_gray, cv2.COLOR_BGR2GRAY) 

            # réduction de la taille de l'image
            '''resize(next_gray, next_gray, Size(), scale, scale, INTER_CUBIC) ;'''
            cv2.resize(next_gray, next_gray, Size(), scale, scale, cv2.INTER_CUBIC) 

            # conversion en UINT
            '''next_gray.convertTo(next_gray, CV_8U) ;'''
            next_gray.convertTo(next_gray, cv2.CV_8U) 

            # lissage par filtre gaussien
            '''blur(next_gray, next_gray, Size(5, 5)) ;'''
            cv2.blur(next_gray, next_gray,(5, 5)) 

            # conversion en type double
            '''next_gray.convertTo(next_gray, CV_32FC3) ;'''
            next_gray.convertTo(next_gray, cv2.CV_32FC3) 


            # cette partie est à revoir, mais en gros elle complète l'ffichage
            '''file << (cap.get(CV_CAP_PROP_POS_MSEC)/60000-tbegin/60000)  << ";" ;'''

	    file << (vidcap.get(cv2.CAP_PROP_POS_MSEC)/60000-tbegin/60000)  << ";"  #?

            
            # c'est ici que ça démarre pour de vrai !
            # sauf que la variable s ne sert plus à rien, tu peux la virer ;)
             #s = 0

            # on va comparer deux images pour estimer la quantité de mouvements entre les deux
            # pour cela, on aura une "image au temps précédent", et une image "au temps courant"

            # on met celle qui a été récupérée au temps précédent dans le conteneur cv::Mat dst ; ça n'est pas utilisé ici, mais le sera si on décide de créer ce fichier vidéo de résultat
            '''Mat dst ;
            previous_gray.copyTo(dst) ;'''
            dst=previous_gray.copy() 

            # on la convertit en couleur
            '''cvtColor(dst, dst, CV_GRAY2BGR) ;'''
            cv2.cvtColor(dst, dst, cv2.CV_GRAY2BGR) 


            # on va maintenant itérer pour chaque zone d'intérêt
            '''for (int k = 0 ; k < vecRect.size() ; k++) # c++'''
              
            for k in vecRect.size():#python
            
                # on récupère les coordonnées de la zone d'intérêt
                '''Rect roi = vecRect.at(k) ;'''
                
                roi.append(k)  # à revoir////////////////////////////////////////////////////////
                

                # on prend le petit bout d'image qui correspond à la zone d'intérêt dans l'image précédente
                '''Mat previous_cage = previous_gray(roi) ;'''
                previous_cage = previous_gray(roi) 
                
                # on prend le petit bout d'image qui correspond à la zone d'intérêt dans l'image courante
                '''Mat next_cage = next_gray(roi) ;'''
                next_cage = next_gray(roi)                
                
                # on calcule le flot optique avec la fonction dédiée de openCV ; le résultat va dans la variable/conteneur "flow"
                '''calcOpticalFlowFarneback(previous_cage, next_cage, flow, 0.5, 5, 3, 3, 5, 1.2, 0) ;'''
                cv2.calcOpticalFlowFarneback(previous_cage, next_cage,flow, 0.5, 5, 3, 3, 5, 1.2, 0)
                
                # on applique un seuil sur le flot -> si trop bas, on considère que c'est du bruit, on met à zéro
                '''threshold(flow, flow, scale, 5, 3) ;'''
                cv2.threshold(flow, flow, scale, 5, 3) 

                # ce qu'on a récupéré ici, c'est une estimation du mouvement en chaque pixel de l'image.
                # maintenant, de manière un peu grossière, on va en calculer la "somme", en utilisant une norme 2 -> sqrt(dx^2 + dy^2)

                # chaque mouvement est un vecteur dont les coordonnées sont en x et en y
                # gx est la matrice des coordonnées des vecteurs selon l'axe y, gy selon y
                '''Mat gx, gy ;
                cv::Sobel(flow, gx, flow.depth(), 1, 0, 3) ;      
                cv::Sobel(flow, gy, flow.depth(), 0, 1, 3) ;'''
                Sobel(flow, gx, flow.depth(), 1, 0, 3)     
                Sobel(flow, gy, flow.depth(), 0, 1, 3) 

                
                # mag est la magnitude du mouvement selon la formulé indiquée : sqrt(dx^2 + dy^2), norme 2 sur l'espace des fonctions
                ''' Mat mag(gx.size(), gx.type());
                magnitude(gx, gy, mag)'''
                mag(gx.size(), gx.type())
                magnitude(gx, gy, mag)           # à revoir

                # on enregistre les données dans fichier des données brutes
                '''file << sum(mag)[0] << ";" '''       #dans le fichier csv

               

                '''tout ce qui suit, on reviendra plus tard dessus, toujours cette histoire de "vidéo de résultats"
                /*for (int y = 0; y < previous_cage.rows; y += 2)
                {
                    for (int x = 0; x < next_cage.cols; x += 2)
                    {
                        // get the flow from y, x position * 10 for better visibility
                        const Point2f flowatxy = flow.at<Point2f>(y, x) * 10;
                        // draw line at flow direction
                        if (flowatxy.x*flowatxy.y > 0)
                        {
                            //line(dst, Point(x + roi.x, y + roi.y), Point(cvRound(x + roi.x + flowatxy.x), cvRound(y + roi.y + flowatxy.y)), Scalar(255,0,0));
                            float n = sqrt(flowatxy.x*flowatxy.x + flowatxy.y*flowatxy.y) ;
                           // draw initial point
                            circle(frame, Point(x/scale + roi.x/scale, y/scale + roi.y/scale), n/2 Scalar(255, 255,0), -1) ;
                        }
                    }
                }*/

            }

 
            //outVid << frame ;
            //if (fps == 15)
            //    outVid << frame ;


            // on vire le dernier point virgule qui ne sert à rien'''
            #file << "\b" << std::endl #?
        
        except:
        
            # si on a atteint la dernière frame ou que la frame est corrompue, on sort du programme
            '''goto end '''

        # l'ancienne "nouvelle frame" devient la nouvelle "ancienne frame"
        previous_gray = next_gray 

        # si affichage, alors affichage
        '''if (disp):
                   
            imshow("frames", next_gray) 
            cv2.waitKey(1) ;
        '''

    

    # on ferme tout et on s'en va
    '''end:

    

    file.close() 
    return 0 '''

