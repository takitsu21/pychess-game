# -*- coding: utf-8 -*-
#! /usr/bin/env python3

"""
Created on Wed Aug 22 00:31:34 2018

@author: Ralagane,Taki
"""


plateau=[['t', 'c', 'f', 'k', 'q', 'f', 'c', 't'],
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
 ['.', '.', '.', '.', '.', '.', '.','.'] ,
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.','.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
 ['T', 'C', 'F', 'K', 'Q', 'F', 'C', 'T']]

def affichePlateau():
    print()
    acc=1
    print(0,end='  ')
    for i in range(8):
        for j in range(8):
            print(plateau[i][j],end=' ')
        print()
        if i != 7:
            print(acc,end='  ')
        if acc > 0:
            acc+=1
    print()
    print('  ',0,1,2,3,4,5,6,7)

def verifCoord(coordX,coordY):
    erreur=0
    while erreur == 0:
        if type(coordX) != int or type(coordY) != int:
            print('Les coordonnées doivent être des entiers, ressaisissez les coordonnées:')
            coordY=input('Coordonnée x: ')
            coordX=input('Coordonnée y: ')
            print(type(coordX))
        elif int(coordY) < 0 or int(coordY) > 8 or int(coordX) < 0 or int(coordX) > 8:
            print('Coordonées incorrecte, ressaisissez les coordonnées:')
            coordY=input('Coordonnée x: ')
            coordX=input('Coordonnée y: ')
        else:
            erreur=1

def verifCouleur(y,x):
    if plateau[y][x].islower():
        return 'noir'
    return 'blanc'
    
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

#y1 = x1
#y2 = x2
def pion(x1,y1,x2,y2):
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
def tour():
    return "slt c la tour"

def executerFonctionPiece(x1,y1,x2,y2):
    if verifPiece(y1,x1) == 1:
        pion(x1,y1,x2,y2)
        return
    elif verifPiece(y1,x1) == 2:
        fou(x1,y1,x2,y2)
        affichePlateau()
    elif verifPiece(y1,x1) == 3:
        reine(y1,x1,y2,x2)
        affichePlateau()
    elif verifPiece(y1,x1) == 4:
        roi(y1,x1,y2,x2)
        affichePlateau()
    elif verifPiece(y1,x1) == 5:
        cavalier(y1,x1,y2,x2)
        affichePlateau()
    elif verifPiece(y1,x1) == 6:
        tour(y1,x1,y2,x2)
        affichePlateau()
    else:
        print("Il n'y a pas de pièce à cet emplacement")

def partie():
    global x1
    global x2
    global x2
    global y2
    affichePlateau()
    while True:
        print("Saissisez les coordonnées :")
        try:
            print('Coordonnée x de départ: ',end=' ');x1=int(input())
            print('Coordonnée y de départ: ',end=' ');y1=int(input())
            print('Coordonnée x2 d\'arrivé: ',end=' ');x2=int(input())
            print('Coordonnée y2 d\'arrivé: ',end=' ');y2=int(input())
            executerFonctionPiece(x1,y1,x2,y2)
            affichePlateau()
        except:
            continue     
partie()   
