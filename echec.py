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
            print('Coordonées sont des entiers, ressaisissez les coordonnées:')
            coordY=input('Coordonnée x: ')
            coordX=input('Coordonnée y: ')
        elif int(coordY) < 0 or int(coordY) > 8 or int(coordX) < 0 or int(coordX) > 8:
            print('Coordonées incorrecte, ressaisissez les coordonnées:')
            coordY=input('Coordonnée x: ')
            coordX=input('Coordonnée y: ')
        else:
            erreur=1
    executerFonctionPiece(coordX,coordY)

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
def pion(y1,x1,y2,x2):
    if y1<0 or x1<0 or y2<0 or x2<0:
        affichePlateau()
        return 'Impossible'
    if y1==6 and y1==y2+2 and verifPiece(y2,x2)==0:#Avancer de 2 noir
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    elif y1==1 and y1==y2-2 and verifPiece(y2,x2)==0:#Avancer de 2 blanc
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    elif x1 == x2-1 and y2 == y1 and verifPiece(y2,x2) == 0:#Avancer de 1
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    elif verifPiece(y2,x2)!= 0 and x1+1==x2 and y2==y1+1 or y2==y1-1 and y1-1>=0 and y1+1<8 and x1+1<8:#Manger piece
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    else :
        return 'Impossible'
          
def fou(y1,x1,y2,x2):
    verifY=y1
    verifX=x1
    if x2<x1 and verifPiece(verifY-1,verifX-1)==0 or verifPiece(verifY-1,verifX+1)==0:#Monter
        while verifY != y2 and verifX != x2:
            if y1>y2 and verifPiece(verifY-1,verifX-1)==0:#monter gauche
                verifY-=1
                verifX-=1
            elif y1<y2 and verifPiece(verifY-1,verifX+1)==0:#monter droite
                verifY-=1
                verifX+=1
            elif verifPiece(verifY,verifX)!=0 :
                return 'Impossible'
    else:#Descendre
        while verifY != y2 and verifX != x2:
            if y2>y1 and verifPiece(verifY+1,verifX+1)==0:#descendre droite
                verifY+=1
                verifX+=1
            elif y2<y1 and verifPiece(verifY-1,verifX+1)==0:#descendre gauche
                verifY-=1
                verifX+=1
            elif verifPiece(verifY,verifX)!=0:          
                return 'Impossible'
    print(verifY,verifX)
    if verifPiece(y2,x2) == 0 and verifY==y2 and verifX==x2:
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



def executerFonctionPiece(y,x):
    if verifPiece(y,x) == 1:
        pion(y,x)
    elif verifPiece(y,x) == 2:
        fou(y,x)
    elif verifPiece(y,x) == 3:
        reine(y,x)
    elif verifPiece(y,x) == 4:
        roi(y,x)
    elif verifPiece(y,x) == 5:
        cavalier(y,x)
    elif verifPiece(y,x) == 6:
        tour(y,x)
    print("Il n'y a pas de pièce à cet emplacement")    

def partie():
    continuer =0
    affichePlateau()
    while continuer ==0:
        print("Saissisez les coordonnées :")
        coordY=input('Coordonnée x: ')
        coordX=input('Coordonnée y: ')
        verifCoord(coordY,coordX)
        
partie()      
    