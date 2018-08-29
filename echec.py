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
    print('  ',0,1,2,3,4,5,6,7)
    print('   --------------->',' y')


#Permet de vérifier si les coordonnées sont bien dans l'échiquier. Demande aussi à l'utilisateur de les saisir.
def verifCoord(coordX,coordY):
    erreur=0
    while erreur == 0:
        print('les types des coordonnées valent :',type(coordX),' et ',type(coordY))
        if type(coordX) != int or type(coordY) != int:
            print(' Les coordonées ne sont pas des entiers, saissisez des nombres entre 0 et 7:')
            coordY=int(input('Coordonnée x: '))
            coordX=int(input('Coordonnée y: '))
        elif int(coordY) < 0 or int(coordY) >= 8 or int(coordX) < 0 or int(coordX) >= 8:
            print('Coordonées incorrecte, ressaisissez les coordonnées:')
            coordY=int(input('Coordonnée x: '))
            coordX=int(input('Coordonnée y: '))
        else:
            erreur=1
    return True
#Determine la couleur de la pièce dans des coordonnées précis. Renvoie la couleur 'vide' quand il n'y a pas de pièce.
def verifCouleur(y,x):
    if plateau[y][x].islower():
        return 'Noir'
    elif  plateau[y][x] == ".":
        return 'Vide'
    return 'Blanc'
    
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
    if y1<0 or x1<0 or y2<0 or x2<0:
        return 'Impossible'
    if y1==6 and y1==y2+2 and verifPiece(y2,x2)==0:#Avancer de 2 noir
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
    elif y1==1 and y1==y2-2 and verifPiece(y2,x2)==0:#Avancer de 2 blanc
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
    elif x1 == x2-1 and y2 == y1 and verifPiece(y2,x2) == 0:#Avancer de 1
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
    elif verifPiece(y2,x2)!= 0 and x1+1==x2 and y2==y1+1 or y2==y1-1 and y1-1>=0 and y1+1<8 and x1+1<8:#Manger piece
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
    else :
        return 'Impossible'
          
#Permet d'utiliser le fou.
def fou(x1,y1,x2,y2):
    verifX=y1
    verifY=x1
    if y1<0 or x1<0 or y2<0 or x2<0 or y1>8 or x1>8 or y2>8 or x2>8:
        return 'impossible'
    if y1>y2 and verifPiece(verifX-1,verifY-1)==0 or verifPiece(verifX+1,verifY-1)==0:#Monter
        while verifX != y2 and verifY != x2:
            if x1>x2 and verifPiece(verifX-1,verifY-1)==0:#monter gauche
                verifX-=1
                verifY-=1
                print('haut gauche')
            elif x1<x2 and verifPiece(verifX-1,verifY+1)==0 :#monter droite
                verifX-=1
                verifY+=1
                print('haut droite')
            elif verifPiece(verifX,verifY)!=0 :
                return 'Impossible'
    if y1<y2:#Descendre
        while verifX != y2 and verifY != x2:
            if y2>y1 and verifPiece(verifX+1,verifY+1)==0:#descendre droite
                verifX+=1
                verifY+=1
                print('descend droite')
            elif y2<y1 and verifPiece(verifX-1,verifY+1)==0:#descendre gauche
                verifX-=1
                verifY+=1
                print('descend gauche')
            elif verifPiece(verifX,verifY)!=0:          
                return 'Impossible'
    if verifPiece(y2,x2) == 0:
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
    else:
        return 'impossible'
    affichePlateau()

def reine():
    return "slt g des boobs"
def roi():
    return "slt c le roi"
def cavalier():
    return "slt c le cavalier"

#Permet de faire bouger la tour en respectant les contraintes. Ne fait pas le roc.
def tour(y1,x1,y2,x2):    
    if y1==y2 or x1==x2: #On regarde d'abord si le déplacement correspond à celle d'une tour   
        if verifCouleur(y1,x1) ==verifCouleur(y2,x2)  :#On regarde ensuite si la pièce dans les coord d'arrivées est une alliée
            print ("Vous tentez de capturer une pièce alliée, ce qui est impossible évidemment.")
            return
        if y1 == y2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and x2>x1:#Déplacement de gauche à droite avec prise de pièce enemie
           for i in range(x2-x1):
               if verifCoord((y1+i),(x1+i)) !=0 and y1+i != y1 and x1+i !=x1:
                   print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                   return 
               tmp=plateau[y1][x1]
               plateau[y1][x1]='.'
               plateau[y2][x2]=tmp
        if y1==y2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and x2 <x1:#Déplacement de droite à gauche avec prise de pièce enemie
            for i in range (x1-x2):
                if verifCoord((y1+i),(x1+i)) !=0 and y1+i != y1 and x1+i !=x1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return 
            tmp=plateau[y1][x1]
            plateau[y1][x1]='.'
            plateau[y2][x2]=tmp
        if x1==x2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and y2>y1:#Déplacement du haut vers le bas avec prise de pièce enemie
            for i in range (y2-y1):
                if verifCoord((y1+i),(x1+i)) !=0 and y1+i != y1 and x1+i !=x1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return 
            tmp=plateau[y1][x1]
            plateau[y1][x1]='.'
            plateau[y2][x2]=tmp
        if x1==x2 and verifCouleur(y1,x1) !=verifCouleur(y2,x2) and y1>y2:#Déplacement du bas vers le haut avec prise de pièce enemie
            for i in range (y1-y2):
                if verifCoord((y1+i),(x1+i)) !=0 and y1+i != y1 and x1+i !=x1:
                    print ("La tour ne peut pas se déplacer car il y\'a une pièce sur son chemin.")
                    return 
            tmp=plateau[y1][x1]
            plateau[y1][x1]='.'
            plateau[y2][x2]=tmp
    else:
        print("Le coordonées données ne respectent pas les caractéristiques de la tour : la tour se déplace soit horizontalement ou verticalement.")
        return

#Permet de faire appel aux bonnes fonctions quand le joueur souhaite bouger une pièce.
def executerFonctionPiece(y,x,y1,x1):
    if verifPiece(y,x) == 1:
        print ("le Pion a été selectionné.")
        pion(y,x,y1,x1)
    elif verifPiece(y,x) == 2:
        print ("le Fou a été selectionné.")
        fou(y,x,y1,x1)
    elif verifPiece(y,x) == 3:
        print ("la Reine a été selectionnée.")
        reine(y,x,y1,x1)
    elif verifPiece(y,x) == 4:
        print ("le Roi a été selectionné.")
        roi(y,x,y1,x1)
    elif verifPiece(y,x) == 5:
        print ("le Cavalier a été selectionné.")
        cavalier(y,x,y1,x1)
    elif verifPiece(y,x) == 6:
        print ("la Tour a été selectionnée.")
        tour(y,x,y1,x1)
    else:
        print("Il n'y a pas de pièce à cet emplacement")

#Permet de faire bouger les pièces.
def executionDeLaPartie(coordY,coordX):
    if int(coordY) == (-1) and int(coordX) ==(-1):
        print ("fin de partie")
        return 1
    if verifCoord(int(coordY),int(coordX)) == True:
        print("Saissisez les coordonnées d'arrivées (ou saissisez les coordonnées -1 -1 pour vous arrêter) :")
        coordY1=int(input('Coordonnée x: '))
        coordX1=int(input('Coordonnée y: '))
        return 0
    if int(coordY) == (-1) and int(coordX) ==(-1):
        print ("fin de partie")
        return 1
    if verifCoord(int(coordY1),int(coordX1)) == True:
        executerFonctionPiece(int(coordY),int(coordX),int(coordY1),int(coordX1))
        return 0
    

#La fonction principale : elle gère la partie.
def partie():
    tour = 'Blanc'
    continuerPartie= 'Oui'
    print ("Bienvenue dans ce petit jeu d\'échec") 
    print ("Les blancs commencent.")
    affichePlateau()
    while continuerPartie == 'Oui':
        print ('Saissisez les coordonnées de départ (ou saissisez les coordonnées -1 -1 pour vous arrêter)')
        coordY=input('Coordonnée x: ')
        coordX=input('Coordonnée y: ')
        if verifCouleur(int(coordY),int(coordX)) == 'Blanc' and tour =='Blanc':
            if executionDeLaPartie(int(coordY),int(coordX)) !=1:
                print('------------------------------------------------------')
                print ("c\'est au tour des noirs.")
                tour ='Noir'
            else:
                return
        elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Blanc' :
            print('------------------------------------------------------')
            print ("C\'est impossible, les blancs doivent jouer se tour.")
        elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Noir':
            if executionDeLaPartie(int(coordY),int(coordX)) !=1:
                print('------------------------------------------------------')
                print ("c\'est au tour des Blancs.")
                tour = 'Blanc'
            else:
                return
        elif verifCouleur(int(coordY),int(coordX)) == 'Noir' and tour =='Blanc':
            print('------------------------------------------------------')
            print ("C\'est impossible, les noirs doivent jouer se tour.")
        elif verifCouleur(int(coordY),int(coordX)) == 'Vide':
            print('------------------------------------------------------')
            print ("La case est vide, choissisez une pièce.")
        affichePlateau()

            
        
partie()         
        