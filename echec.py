# -*- coding: utf-8 -*-
#! /usr/bin/env python3

"""
Created on Wed Aug 22 00:31:34 2018

@author: Ralagane,Taki
"""
global continuerPartie

plateau=[['t', 'c', 'f', 'k', 'q', 'f', 'c', 't'],
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
 ['.', '.', '.', '.', '.', '.', '.','.'] ,
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.','.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
 ['T', 'C', 'F', 'K', 'Q', 'F', 'C', 'T']]

#Affiche le plateau dans le terminal.
def affichePlateau():
    print()
    acc=1
    print("x")
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
    print('     --------------->',' y')


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
    return 0    #case vide

#Permet de faire bouger le pion. N'exécute pas pour le moment la prise en passant.
def pion(y1,x1,y2,x2):
    if verifCoord(y2,x2):
        if x2==x1:#Avancer tout droit
            if y1==6 and y2+2==y1 or y1==1 and y2-2==y1:#Avance de 2
                mouvementPiece(y1,x1,y2,x2)
                return 1
            elif y2+1==y1 or y2-1==y1 :#Avance de 1
                mouvementPiece(y1,x1,y2,x2)
                return 1
        elif verifPiece(y2,x2)!= 0 and verifCouleur(y1,x1)!=verifCouleur(y2,x2) and y2==y1-1 or y2==y1+1 and x2==x1+1 or x2==x1-1:#Manger piece
            mouvementPiece(y1,x1,y2,x2)
            return 1
    return 0
          
#Permet d'utiliser le fou.
def fou(y1,x1,y2,x2):
    verifX=y1
    verifY=x1
    if verifCoord(y2,x2):
        if verifPiece(y2,x2)!= 0 and verifCouleur(y1,x1)!=verifCouleur(y2,x2):#Manger
            if y1>y2:
                while True:
                    if x1>x2 and verifPiece(verifX-1,verifY-1)==0:#monter gauche
                        verifX-=1
                        verifY-=1
                        if verifPiece(verifX-1,verifY-1)==0 :
                            if verifPiece(verifX-2,verifY-2)!=0:
                                mouvementPiece(y1,x1,y2,x2)
                                return 1
                            mouvementPiece(y1,x1,y2,x2)
                            return 1   
                    elif x1<x2 and verifPiece(verifX-1,verifY+1)==0 :#monter droite
                        verifX-=1
                        verifY+=1
                        if verifPiece(verifX-1,verifY+1)==0:
                            if verifPiece(verifX-2,verifY+2)!=0:
                                mouvementPiece(y1,x1,y2,x2)
                                return 1
                            mouvementPiece(y1,x1,y2,x2)
                            return 1                      
            if y1<y2:#Descendre
                while True:
                    if y2>y1 and verifPiece(verifX+1,verifY+1)==0:#descendre droite
                        verifX+=1
                        verifY+=1
                        if verifPiece(verifX+1,verifY+1)==0:
                            if verifPiece(verifX+2,verifY+2)!=0:
                                mouvementPiece(y1,x1,y2,x2)
                                return 1
                            mouvementPiece(y1,x1,y2,x2)
                            return 1                       
                    elif y2<y1 and verifPiece(verifX-1,verifY+1)==0:#descendre gauche
                        verifX-=1
                        verifY+=1
                        if verifPiece(verifX-1,verifY+1)==0:
                            if verifPiece(verifX-2,verifY+2)!=0:
                                mouvementPiece(y1,x1,y2,x2)
                                return 1
                            mouvementPiece(y1,x1,y2,x2)
                            return 1                    
        else:
            if y1>y2 and verifPiece(verifX-1,verifY-1)==0 or verifPiece(verifX+1,verifY-1)==0:#Monter
                while verifX != y2 and verifY != x2:
                    if x1>x2 and verifPiece(verifX-1,verifY-1)==0:#monter gauche
                        verifX-=1
                        verifY-=1
                    elif x1<x2 and verifPiece(verifX-1,verifY+1)==0 :#monter droite
                        verifX-=1
                        verifY+=1
                    elif verifPiece(verifX,verifY)!=0 :
                        return 0
                mouvementPiece(y1,x1,y2,x2)
                return 1
            if y1<y2:#Descendre
                while verifX != y2 and verifY != x2:
                    if y2>y1 and verifPiece(verifX+1,verifY+1)==0:#descendre droite
                        verifX+=1
                        verifY+=1
                    elif y2<y1 and verifPiece(verifX-1,verifY+1)==0:#descendre gauche
                        verifX-=1
                        verifY+=1
                    elif verifPiece(verifX,verifY)!=0:          
                        return 0
                mouvementPiece(y1,x1,y2,x2)
                return 1
    return 0


def reine():
    return "slt g des boobs"

#permet de voir si le roi à le champ libre pour se déplacer
def verificationDeplacementValideDuRoi(y1,x1,y2,x2):
    couleurDuRoi = verifCouleur(y1,x1)
    for i in range((7-y2)+2): #vérification à droite du roi
        if verifCouleur(y1+i,x1) == couleurDuRoi and y1+i !=y1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1) =="q" and verifCouleur(y1+i,x1) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return 0
        if verifPiece(y1+i,x1) =="t" and verifCouleur(y1+i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
        
    for i in range (y1+1): #vérification à gauche du roi
         if verifCouleur(y1-i,x1) == couleurDuRoi and y1-i !=y1: #Une pièce protège le roi
            break
         if verifPiece(y1-i,x1) =="q" and verifCouleur(y1-i,x1) != couleurDuRoi: 
             print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
             return 0
         if verifPiece(y1-i,x1) =="t" and verifCouleur(y1-i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
        
    for i in range ((7-y1)+1): #vérification en diagonale droit vers le haut
        if verifCouleur(y1+i,x1+i) == couleurDuRoi and y1+i !=y1 and x1+i!=x1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1+i) =="q" and verifCouleur(y1+i,x1+i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return 0
        if verifPiece(y1+i,x1+i) =="t" and verifCouleur(y1+i,x1+i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
        
    for i in range(y1+1): #vérification en diagonale gauche vers le bas
        if verifCouleur(y1-i,x1-i) == couleurDuRoi and y1-i != y1 and x1-i !=x1: #Une pièce protège le roi
            break
        if verifPiece(y1-i,x1-i) =="q" and verifCouleur(y1-i,x1-i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return 0
        if verifPiece(y1-i,x1-i) =="t" and verifCouleur(y1-i,x1-i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
    
    for i in range (y1+1): #Vérification en diagonale gauche vers le haut
        if verifCouleur(y1-i,x1+i) == couleurDuRoi and y1-i != y1 and x1+i !=x1: #Une pièce protège le roi
            break
        if verifPiece(y1-i,x1+i) =="q" and verifCouleur(y1-i,x1+i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return 0
        if verifPiece(y1-i,x1+i) =="t" and verifCouleur(y1-i,x1+i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
    
    for i in range((7-y1)+1): #Vérification en diagonale droit  vers le bas
        if verifCouleur(y1+i,x1-i) == couleurDuRoi and y1+i != y1 and x1-i !=x1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1-i) =="q" and verifCouleur(y1+i,x1-i) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return 0
        if verifPiece(y1+i,x1-i) =="t" and verifCouleur(y1+i,x1-i) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
    
    for i in range (y1 +1) : #Vérification haut du roi
        if verifCouleur(y1-i,x1) == couleurDuRoi and y1-i !=y1: #Une pièce protège le roi
            break
        if verifPiece(y1-i,x1) =="q" and verifCouleur(y1-i,x1) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return 0
        if verifPiece(y1-i,x1) =="t" and verifCouleur(y1-i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
    for i in range ((7-y1)+1): #Vérification bas du roi
        if verifCouleur(y1+i,x1) == couleurDuRoi and y1+i !=y1: #Une pièce protège le roi
            break
        if verifPiece(y1+i,x1) =="q" and verifCouleur(y1+i,x1) != couleurDuRoi : 
            print("Le roi ne peut pas se déplacer, car la reine restraint ses déplacements.")
            return 0
        if verifPiece(y1+i,x1) =="t" and verifCouleur(y1+i,x1) != couleurDuRoi:
            print("Le roi ne peut pas se déplacer, car la tour restraint ses déplacements.")
            return 0
    return 1    

# Permet de faire bouger le roi tout en regardant s'il peut bouger sans prolbème.
def roi(y1,x1,y2,x2):
    if verifCouleur(y1,x1) ==verifCouleur(y2,x2)  :#On regarde ensuite si la pièce dans les coord d'arrivées est une alliée
        print ("Vous tentez de capturer une pièce alliée, ce qui est impossible évidemment.")
        return 0
        
    if x1==x2 and y2-1 ==y1 or y2+1 ==y1 : #déplacement honrizontal
        if verificationDeplacementValideDuRoi(y1,x1,y2,x2) == 1:
            mouvementPiece(y1,x1,y2,x2)
            return 1
        else:
            return 0
    if y1==y2 and x2-1 == x1 or x2+1 == x1: #déplacement vertical
        if verificationDeplacementValideDuRoi(y1,x1,y2,x2) == 1:
            mouvementPiece(y1,x1,y2,x2)
            return 1
        else:
            return 0 

def cavalier():
    return "slt c le cavalier"

#Permet de faire bouger la tour en respectant les contraintes. Ne fait pas le roc.
def tour(y1,x1,y2,x2):    
    if y1==y2 or x1==x2: #On regarde d'abord si le déplacement correspond à celle d'une tour   
        if verifCouleur(y1,x1) ==verifCouleur(y2,x2)  :#On regarde ensuite si la pièce dans les coord d'arrivées est une alliée
            print ("Vous tentez de capturer une pièce alliée, ce qui est impossible évidemment.")
            return 0
        if y1 == y2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and x2>x1:#Déplacement de gauche à droite avec prise de pièce enemie
           for i in range((x2-x1)+1):
               if verifCouleur((y1),(x1+i)) !='Vide' and x1+i !=x1:
                   print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                   return 0
               mouvementPiece(y1,x1,y2,x2)
               return 1
        if y1==y2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and x2 <x1:#Déplacement de droite à gauche avec prise de pièce enemie
            for i in range ((x1-x2)+1):
                if verifCouleur((y1),(x1-i)) !='Vide' and x1-i !=x1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return 0
            mouvementPiece(y1,x1,y2,x2)
            return 1
        if x1==x2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and y2>y1:#Déplacement du haut vers le bas avec prise de pièce enemie
            for i in range ((y2-y1)+1):
                if verifCouleur(y1+i,x1)!='Vide' and y1+i !=y1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return 0
            mouvementPiece(y1,x1,y2,x2)
            return 1
        if x1==x2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and y1>y2:#Déplacement du bas vers le haut avec prise de pièce enemie
            for (i) in range ((y1-y2)+1):
                if verifCouleur(y1-i,x1)!='Vide' and y1-i !=y1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return 0
            mouvementPiece(y1,x1,y2,x2)
            return 1
    else:
        print("Le coordonées données ne respectent pas les caractéristiques de la tour : la tour se déplace soit horizontalement ou verticalement.")
        return 0

#Permet de faire appel aux bonnes fonctions quand le joueur souhaite bouger une pièce.
def executerFonctionPiece(y,x,y1,x1):
    if verifPiece(y,x) == 1:
        print ("le Pion a été selectionné.")
        if pion(y,x,y1,x1) == 0:
            return 0
        else :
            return 1
    elif verifPiece(y,x) == 2:
        print ("le Fou a été selectionné.")
        if fou(y,x,y1,x1) == 0:
            return 0
        else :
            return 1
    elif verifPiece(y,x) == 3:
        print ("la Reine a été selectionnée.")
        if reine(y,x,y1,x1) == 0:
            return 0
        else :
            return 1
    elif verifPiece(y,x) == 4:
        print ("le Roi a été selectionné.")
        if roi(y,x,y1,x1) == 0:
            return 0
        else :
            return 1
    elif verifPiece(y,x) == 5:
        print ("le Cavalier a été selectionné.")
        if cavalier(y,x,y1,x1) == 0:
            return 0
        else :
            return 1
    elif verifPiece(y,x) == 6:
        print ("la Tour a été selectionnée.")
        if tour(y,x,y1,x1) == 0:
            return 0
        else :
            return 1
    else:
        print("Il n'y a pas de pièce à cet emplacement")
        return 0

#Permet de faire bouger les pièces.
def executionDeLaPartie(coordY,coordX):
    if int(coordY) == (-1) and int(coordX) ==(-1):
        print("fin de partie, merci d'avoir joué.")
        return 2
    print("Saissisez les coordonnées d'arrivées (ou saissisez les coordonnées -1 -1 pour vous arrêter) :")
    coordY1=int(input('Coordonnée x: '))
    coordX1=int(input('Coordonnée y: '))
    while verifCoord(int(coordY1),int(coordX1)) == False:
        print("les coordonnées saisi sont incorrectes, veuillez recommencer...")
        coordY1=int(input('Coordonnée x: '))
        coordX1=int(input('Coordonnée y: '))
    if int(coordY1) == (-1) and int(coordX1) ==(-1):
        print ("fin de partie")
        return 1
    if executerFonctionPiece(int(coordY),int(coordX),int(coordY1),int(coordX1)) == 0:
        return 0
    else:
        return 1
    

#La fonction principale : elle gère la partie.
def partie():
    tour = 'Blanc'
    continuerPartie= 'Oui'
    print ("Bienvenue dans ce petit jeu d'échec :)") 
    print ("Les blancs commencent.")
    affichePlateau()
    while continuerPartie == 'Oui':
        print ('Saissisez les coordonnées de départ (ou saissisez les coordonnées -1 -1 pour vous arrêter)')
        coordY=int(input('Coordonnée x: '))
        coordX=int(input('Coordonnée y: '))
        if coordX >=0 and coordX <8 and coordY >=0 and coordY <8 or coordX==-1 and coordY ==-1 :
            verification = executionDeLaPartie(int(coordY),int(coordX))
            if verifCouleur(int(coordY),int(coordX)) == 'Blanc' and tour =='Blanc':
                if verification ==1:
                    print('------------------------------------------------------')
                    print ("c\'est au tour des noirs.")
                    tour ='Noir'
                elif  verification ==0:
                    print('------------------------------------------------------')
                    print ("le déplacement n\'est pas valide, il va falloir recommencer.")
                else:
                    break
            elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Blanc' :
                print('------------------------------------------------------')
                print ("C\'est impossible, les blancs doivent jouer se tour.")
            elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Noir':
                if verification ==1:
                    print('------------------------------------------------------')
                    print ("c\'est au tour des Blancs.")
                    tour = 'Blanc'
                elif verification ==0:
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

            
        
if __name__ =='__main__':
    partie()      
        