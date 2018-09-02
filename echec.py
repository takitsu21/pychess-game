# -*- coding: utf-8 -*-
#! /usr/bin/env python3

"""
Created on Wed Aug 22 00:31:34 2018
@author: Ralagane,Taki
Jeu d'échec
"""
#----------------Init plateau de jeu------------------#

global continuerPartie
plateau=[['t', 'c', 'f', 'k', 'q', 'f', 'c', 't'],
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
 ['.', '.', '.', '.', '.', '.', '.','.'] ,
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.','.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
 ['T', 'C', 'F', 'K', 'Q', 'F', 'C', 'T']]

#---------------------------------------------------------------------------------------------------#
#---------------------Fonctions utile au bon fonctionnement de l'échiquier--------------------------#

#Affiche le plateau dans le terminal.
def affichePlateau():
    print()
    acc=1
    print("y")
    print('^',0,end='  ')
    for i in range(8):
        for j in range(8):
            print(plateau[i][j],end=' ')
        print()
        if i != 7:
            print('|',acc,end='  ')
        if acc > 0:
            acc+=1
    print()
    print('    ',0,1,2,3,4,5,6,7)
    print('     --------------->',' x')


#Permet de vérifier si les coordonnées sont bien dans l'échiquier. Demande aussi à l'utilisateur de les saisir.
def verifCoord(coordX,coordY):
    if coordX <0 or coordX >8 or  coordY <0 or coordY >8:
        return False
    return True

#Determine la couleur de la pièce dans des coordonnées précis. Renvoie la couleur 'vide' quand il n'y a pas de pièce.
def verifCouleur(y,x):
    if plateau[y][x].islower():
        return 'Noir'
    elif  plateau[y][x] == ".":
        return 'Vide'
    return 'Blanc'

#Permet de déplacer une pièce dans l'échiquier en partant du principe que tout a été vérifié
def mouvementPiece(y1,x1,y2,x2):
    tmp=plateau[y1][x1]
    plateau[y1][x1]='.'
    plateau[y2][x2]=tmp
 
#Donne le type de la pièce à des coordonnées précis.
def verifPiece(y,x):
    if plateau[y][x].lower()=='p':#pion
        return 1
    if plateau[y][x].lower()=='f':#fou
        return 2
    if plateau[y][x].lower()=='q':#reine
        return 3    
    if plateau[y][x].lower()=='k':#roi
        return 4
    if plateau[y][x].lower()=='c':#cavalier
        return 5
    if plateau[y][x].lower()=='t':#tour
        return 6
    return False    #case vide

#Verifie si la position y2 et x2 sont bien sur la diagonale de la piece selectionner
def estDiagonale(y1,x1,y2,x2,coteAVerifier):
    Y2=y2
    X2=x2
    if coteAVerifier==0:#haut droite
        for i in range(y1-y2):
            X2-=1
            Y2+=1
        if X2==x1 and Y2==y1:
            return True
    if coteAVerifier==1:#bas gauche
        for i in range(y2-y1):
            X2+=1
            Y2-=1
        if X2==x1 and Y2==y1:
            return True
    if coteAVerifier==2:#bas droite
        for i in range(y2-y1):
            X2-=1
            Y2-=1
        if X2==x1 and Y2==y1:
            return True
    if coteAVerifier==3:#haut gauche
        for i in range(y1-y2):
            X2+=1
            Y2+=1
        if X2==x1 and Y2==y1:
            return True
    return False

def estHorizontale(x1,x2,coteAVerifier):
    X2=x2
    if coteAVerifier==1:#gauche
        for i in range(x1-x2):
            X2+=1
    else:#droite
        for i in range(x2-x1):
            X2-=1
    if X2==x1:
        return True
    return False

#Permet de voir si un déplacement est valide sur les diagonales
def verificationDeplacementValideDiagonale(y1,x1,y2,x2,coteAVerifier):#0 haut droit 1 bas gauche 2 bas droit 3 haut gauche
    if coteAVerifier == 0:  
        for i in range (1,y1-y2): #vérification en diagonale droit vers le haut
            if verifCouleur(y1-i,x1+i) !='Vide' and y1-i !=y1 and x1+i!=x1:
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False
        return True
    if coteAVerifier == 1:
        for i in range(1,y2-y1): #vérification en diagonale gauche vers le bas
            if verifCouleur(y1-i,x1-i) != 'Vide' and y1-i != y1 and x1-i !=x1: 
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False
        return True
    if coteAVerifier == 2:
        for i in range(1,y2-y1): #Vérification en diagonale droit  vers le bas
            if verifCouleur(y1+i,x1-i) != 'Vide' and y1+i != y1 and x1-i !=x1: 
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False
        return True
    if coteAVerifier == 3:
        for i in range (1,y1-y2): #Vérification en diagonale gauche vers le haut
            if verifCouleur(y1-i,x1-i)!= 'Vide' and y1-i != y1 and x1-i !=x1: 
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False
        return True
    
#Permet de voir si un déplacement est valide sur les côtés
def verificationDeplacementValideHonrizontal(y1,x1,y2,x2,coteAVerifier):
    if coteAVerifier == 0:
        for i in range(1,x2-x1): #vérification à droite
            if verifCouleur(y1,x1+i) !='Vide' and y1==y2 and x1+i!=x1:
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False
    else:    
        for i in range (1,x1-x2): #vérification à gauche
             if verifCouleur(y1,x1-i) !='Vide' and y1==y2 and x1-i!=x1:
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False 
    return True

#Permet de voir si un déplacement est valide sur les en hat et en bas
def  verificationDeplacementValideVertical(y1,x1,y2,x2,coteAVerifier):
    if coteAVerifier == 0:
        for i in range ((y1-y2) +1) : #Vérification haut 
            if verifCouleur(y1+i,x1) !='Vide' and y1+i !=y1 :
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False
    else :
        for i in range ((y2-y1) +1): #Vérification bas
            if verifCouleur(y1+i,x1) !='Vide' and y1+i !=y1:
                print("Une pièce est sur le chemin, le déplacement ne peut se faire.")
                return False
    return True    

#permet de voir si le roi à le champ libre pour se déplacer
def verificationDeplacementValideDuRoi(y1,x1,y2,x2):
    couleurDuRoi = verifCouleur(y1,x1)
    for i in range((7-y2)+2): #vérification à droite du roi
        if verifCouleur(y1+i,x1) == couleurDuRoi and y1+i !=y1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1) =="q" and verifCouleur(y1+i,x1) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return False
        if verifPiece(y1+i,x1) =="t" and verifCouleur(y1+i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False  
    for i in range (y1+1): #vérification à gauche du roi
         if verifCouleur(y1-i,x1) == couleurDuRoi and y1-i !=y1: #Une pièce protège le roi
            break
         if verifPiece(y1-i,x1) =="q" and verifCouleur(y1-i,x1) != couleurDuRoi: 
             print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
             return False
         if verifPiece(y1-i,x1) =="t" and verifCouleur(y1-i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False
    for i in range ((7-y1)+1): #vérification en diagonale droit vers le haut
        if verifCouleur(y1+i,x1+i) == couleurDuRoi and y1+i !=y1 and x1+i!=x1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1+i) =="q" and verifCouleur(y1+i,x1+i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return False
        if verifPiece(y1+i,x1+i) =="t" and verifCouleur(y1+i,x1+i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False
    for i in range(y1+1): #vérification en diagonale gauche vers le bas
        if verifCouleur(y1-i,x1-i) == couleurDuRoi and y1-i != y1 and x1-i !=x1: #Une pièce protège le roi
            break
        if verifPiece(y1-i,x1-i) =="q" and verifCouleur(y1-i,x1-i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return False
        if verifPiece(y1-i,x1-i) =="t" and verifCouleur(y1-i,x1-i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False
    for i in range (y1+1): #Vérification en diagonale gauche vers le haut
        if verifCouleur(y1-i,x1+i) == couleurDuRoi and y1-i != y1 and x1+i !=x1: #Une pièce protège le roi
            break
        if verifPiece(y1-i,x1+i) =="q" and verifCouleur(y1-i,x1+i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return False
        if verifPiece(y1-i,x1+i) =="t" and verifCouleur(y1-i,x1+i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False
    for i in range((7-y1)+1): #Vérification en diagonale droit  vers le bas
        if verifCouleur(y1+i,x1-i) == couleurDuRoi and y1+i != y1 and x1-i !=x1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1-i) =="q" and verifCouleur(y1+i,x1-i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return False
        if verifPiece(y1+i,x1-i) =="t" and verifCouleur(y1+i,x1-i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False
    for i in range (y1 +1) : #Vérification haut du roi
        if verifCouleur(y1-i,x1) == couleurDuRoi and y1-i !=y1: #Une pièce protège le roi
            break
        if verifPiece(y1-i,x1) =="q" and verifCouleur(y1-i,x1) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return False
        if verifPiece(y1-i,x1) =="t" and verifCouleur(y1-i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False
    for i in range ((7-y1)+1): #Vérification bas du roi
        if verifCouleur(y1+i,x1) == couleurDuRoi and y1+i !=y1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1) =="q" and verifCouleur(y1+i,x1) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return False
        if verifPiece(y1+i,x1) =="t" and verifCouleur(y1+i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return False
    return True  

#---------------------------------------------------------------#
#---------------------Fonctions des pièces----------------------#
    
#Permet de faire bouger le pion. N'exécute pas pour le moment la prise en passant.
def pion(y1,x1,y2,x2):
    if verifCoord(y2,x2):
        if x2==x1 and verifPiece(y2,x2)==0 and verifCouleur(y1,x1)=='Blanc':#Avancer tout droit blanc
            if y1==6 and y2+2==y1:#Avance de 2 blanc
                mouvementPiece(y1,x1,y2,x2)
                return True
            elif y2+1==y1 :#Avance de 1 blanc
                mouvementPiece(y1,x1,y2,x2)
                return True
        elif x2==x1 and verifPiece(y2,x2)==0 and verifCouleur(y1,x1)=='Noir':#Avancer tout droit noir
            if y1==1 and y2-2==y1:#Avance de 2 noir
                mouvementPiece(y1,x1,y2,x2)
                return True
            elif y2-1==y1:#Avance de 1 noir
                mouvementPiece(y1,x1,y2,x2)
                return True
        elif verifPiece(y2,x2)!= 0 and verifCouleur(y1,x1)!=verifCouleur(y2,x2) and y2==y1-1  and x2==x1+1 :#Manger piece noir droite
            mouvementPiece(y1,x1,y2,x2)
            return True
        elif verifPiece(y2,x2)!= 0 and verifCouleur(y1,x1)!=verifCouleur(y2,x2) and y2==y1+1  and x2==x1+1 :#Manger piece blanche droite
            mouvementPiece(y1,x1,y2,x2)
            return True
        elif verifPiece(y2,x2)!= 0 and verifCouleur(y1,x1)!=verifCouleur(y2,x2) and y2==y1-1  and x2==x1-1 :#Manger piece noir gauche
            mouvementPiece(y1,x1,y2,x2)
            return True
        elif verifPiece(y2,x2)!= 0 and verifCouleur(y1,x1)!=verifCouleur(y2,x2) and y2==y1+1  and x2==x1-1 :#Manger piece blanche gauche
            mouvementPiece(y1,x1,y2,x2)
    return False

#Permet d'utiliser le fou.
def fou(y1,x1,y2,x2):
    coteAVerifier=-1
    if y2<y1 and x2<x1:
        coteAVerifier=3
    if y2<y1 and x2>x1:
        coteAVerifier=0
    if y2>y1 and x2<x1:
        coteAVerifier=1
    if y2>y1 and x2>x1:
        coteAVerifier=2
    if verifCouleur(y2,x2)!=verifCouleur(y1,x1) and verificationDeplacementValideDiagonale(y1,x1,y2,x2,coteAVerifier)==1 and estDiagonale(y1,x1,y2,x2,coteAVerifier):
        mouvementPiece(y1,x1,y2,x2)
        return True
    return False

#permet d'utiliser la reine
def reine(y1,x1,y2,x2):
    coteAVerifier=-1
    if y2<y1 and x2<x1:
        coteAVerifier=3
    if y2<y1 and x2>x1:
        coteAVerifier=0
    if y2>y1 and x2<x1:
        coteAVerifier=1
    if y2>y1 and x2>x1:
        coteAVerifier=2
    if verifCouleur(y2,x2)!=verifCouleur(y1,x1) and verificationDeplacementValideDiagonale(y1,x1,y2,x2,coteAVerifier)==1 and estDiagonale(y1,x1,y2,x2,coteAVerifier):
        mouvementPiece(y1,x1,y2,x2)
        return True
    if y2==y1 and x2<x1:#gauche
        coteAVerifier=1
    if y2==y1 and x2>x1:#droite
        coteAVerifier=0
    if verifCouleur(y2,x2)!=verifCouleur(y1,x1) and verificationDeplacementValideHonrizontal(y1,x1,y2,x2,coteAVerifier)==1 and estHorizontale(x1,x2,coteAVerifier):
        mouvementPiece(y1,x1,y2,x2)
        return True    
    return False  

# Permet de faire bouger le roi tout en regardant s'il peut bouger sans prolbème.
def roi(y1,x1,y2,x2):
    if verifCouleur(y1,x1) ==verifCouleur(y2,x2)  :#On regarde ensuite si la pièce dans les coord d'arrivées est une alliée
        print ("Vous tentez de capturer une pièce alliée, ce qui est impossible évidemment.")
        return False
        
    if x1==x2 and y2-1 ==y1 or y2+1 ==y1 : #déplacement honrizontal
        if verificationDeplacementValideDuRoi(y1,x1,y2,x2) == 1:
            mouvementPiece(y1,x1,y2,x2)
            return True
        else:
            return False
    if y1==y2 and x2-1 == x1 or x2+1 == x1: #déplacement vertical
        if verificationDeplacementValideDuRoi(y1,x1,y2,x2) == 1:
            mouvementPiece(y1,x1,y2,x2)
            return True
        else:
            return False 

#Permet de faire bouger le cavalier. Vérifie si le déplacement est valide.
def cavalier(y1,x1,y2,x2):
    if verifCouleur(y1,x1) == verifCouleur(y2,x2):
        print ("Vous tentez de capturer une pièce qui est dans votre camp, ce qui est impossible.")
        return False
    if y1 >y2 and x1== x2 +1 or x1==x2-1 and y1 ==y2-3: #déplacement honrizontal sur la gauche
        mouvementPiece(y1,x1,y2,x2)
        return True
    if y2>y1 and x1==x2+1 or x1==x2-1 and y2 == y1-3: #déplacement honrizontal sur la droite
        mouvementPiece(y1,x1,y2,x2)
        return True
    if x1>x2 and x2+3==x1 and y1==y2+1 or y1==y2-1: #Déplacement vertical vers le bas
        mouvementPiece(y1,x1,y2,x2)
        return True
    if x2>x1 and x1+3==x2 and y1==y2+1 or y1==y2-1: #Déplacement vertical vers le haut
         mouvementPiece(y1,x1,y2,x2)
         return True
    else:
         print("Le déplacement n'est pas valide, le cavalier se déplace en L : deux cases devant lui et un case sur la gauche ou la droite.")
         return False
        
#Permet de faire bouger la tour en respectant les contraintes. Ne fait pas le roc.
def tour(y1,x1,y2,x2):    
    if y1==y2 or x1==x2: #On regarde d'abord si le déplacement correspond à celle d'une tour 
        couleurDeLaTour =verifCouleur(y1,x1)
        couleurDeLaPiece =verifCouleur(y2,x2) 
        if couleurDeLaTour ==couleurDeLaPiece  :#On regarde ensuite si la pièce dans les coord d'arrivées est une alliée
            print ("Vous tentez de capturer une pièce alliée, ce qui est impossible évidemment.")
            return False
        if y1 == y2 and couleurDeLaTour !=couleurDeLaPiece and x2>x1:#Déplacement de gauche à droite avec prise de pièce enemie
           for i in range((x2-x1)+1):
               if verifCouleur((y1),(x1+i)) !='Vide' and x1+i !=x1:
                   print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                   return False
               mouvementPiece(y1,x1,y2,x2)
               return True
        if y1==y2 and couleurDeLaTour !=couleurDeLaPiece and x2 <x1:#Déplacement de droite à gauche avec prise de pièce enemie
            for i in range ((x1-x2)+1):
                if verifCouleur((y1),(x1-i)) !='Vide' and x1-i !=x1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return False
            mouvementPiece(y1,x1,y2,x2)
            return True
        if x1==x2 and couleurDeLaTour !=couleurDeLaPiece and y2>y1:#Déplacement du haut vers le bas avec prise de pièce enemie
            for i in range ((y2-y1)+1):
                if verifCouleur(y1+i,x1)!='Vide' and y1+i !=y1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return False
            mouvementPiece(y1,x1,y2,x2)
            return True
        if x1==x2 and couleurDeLaTour !=couleurDeLaPiece and y1>y2:#Déplacement du bas vers le haut avec prise de pièce enemie
            for (i) in range ((y1-y2)+1):
                if verifCouleur(y1-i,x1)!='Vide' and y1-i !=y1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return False
            mouvementPiece(y1,x1,y2,x2)
            return True
    else:
        print("Le coordonées données ne respectent pas les caractéristiques de la tour : la tour se déplace soit horizontalement ou verticalement.")
        return False

#-----------------------------------------------------------#
#---------------Fonctions qui gère la partie----------------#

#Permet de faire appel aux bonnes fonctions quand le joueur souhaite bouger une pièce.
def executerFonctionPiece(y,x,y1,x1):
    if verifPiece(y,x) == 1:
        print ("le Pion a été selectionné.")
        if pion(y,x,y1,x1) == 0:
            return False
        else :
            return True
    elif verifPiece(y,x) == 2:
        print ("le Fou a été selectionné.")
        if fou(y,x,y1,x1) == 0:
            return False
        else :
            return True
    elif verifPiece(y,x) == 3:
        print ("la Reine a été selectionnée.")
        if reine(y,x,y1,x1) == 0:
            return False
        else :
            return True
    elif verifPiece(y,x) == 4:
        print ("le Roi a été selectionné.")
        if roi(y,x,y1,x1) == 0:
            return False
        else :
            return True
    elif verifPiece(y,x) == 5:
        print ("le Cavalier a été selectionné.")
        if cavalier(y,x,y1,x1) == 0:
            return False
        else :
            return True
    elif verifPiece(y,x) == 6:
        print ("la Tour a été selectionnée.")
        if tour(y,x,y1,x1) == 0:
            return False
        else :
            return True
    else:
        print("Il n'y a pas de pièce à cet emplacement.")
        return False

#Permet de faire bouger les pièces.
def executionDeLaPartie(coordY,coordX):
    if int(coordY) == (-1) and int(coordX) ==(-1):
        print("fin de partie, merci d'avoir joué.")
        return 2
    print("Saissisez les coordonnées d'arrivées (ou saissisez les coordonnées -1 -1 pour vous arrêter) :")
    coordY1=int(input('Coordonnée y: '))
    coordX1=int(input('Coordonnée x: '))
    while verifCoord(int(coordY1),int(coordX1)) == False:
        print("les coordonnées saisi sont incorrectes, veuillez recommencer...")
        coordY1=int(input('Coordonnée y: '))
        coordX1=int(input('Coordonnée x: '))
    if int(coordY1) == (-1) and int(coordX1) ==(-1):
        print ("fin de partie")
        return True
    if executerFonctionPiece(int(coordY),int(coordX),int(coordY1),int(coordX1)) == 0:
        return False
    else:
        return True
    

#La fonction principale : elle gère la partie.
def partie():
    tour = 'Blanc'
    continuerPartie= 'Oui'
    print ("Bienvenue dans ce petit jeu d'échec :)") 
    print ("Les blancs commencent.")
    affichePlateau()
    while continuerPartie == 'Oui':
        print ('Saissisez les coordonnées de départ (ou saissisez les coordonnées -1 -1 pour vous arrêter)')
        coordY=int(input('Coordonnée y: '))
        coordX=int(input('Coordonnée x: '))
        if coordX >=0 and coordX <8 and coordY >=0 and coordY <8 or coordX==-1 and coordY ==-1 :
            if verifCouleur(int(coordY),int(coordX)) == 'Blanc' and tour =='Blanc':
                if executionDeLaPartie(int(coordY),int(coordX)) ==1:
                    print('------------------------------------------------------')
                    print ("c\'est au tour des noirs.")
                    tour ='Noir'
                elif  executionDeLaPartie(int(coordY),int(coordX)) ==0:
                    print('------------------------------------------------------')
                    print ("le déplacement n\'est pas valide, il va falloir recommencer.")
                else:
                    break
            elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Blanc' :
                print('------------------------------------------------------')
                print ("C\'est impossible, les blancs doivent jouer se tour.")
            elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Noir':
                if executionDeLaPartie(int(coordY),int(coordX)) ==1:
                    print('------------------------------------------------------')
                    print ("c\'est au tour des Blancs.")
                    tour = 'Blanc'
                elif executionDeLaPartie(int(coordY),int(coordX)) ==0:
                    print('------------------------------------------------------')
                    print ("le déplacement n\'est pas valide, il va falloir recommencer.")
                else :
                    break
            elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Blanc':
                print('------------------------------------------------------')
                print ("C\'est impossible, les noirs doivent jouer se tour.")
            elif verifCouleur(int(coordY),int(coordX)) == 'Vide':
                print('------------------------------------------------------')
                print ("La case est vide, choissisez une pièce.")
        else:
            print('------------------------------------------------------')
            print("Les coordonnées ne sont pas comprises dans l\'échiquier.")
        affichePlateau()

#----------------------------------------------#
#----------------Lance la partie---------------#          
        
if __name__ =='__main__':
    partie()      

#----------------------------------------------#