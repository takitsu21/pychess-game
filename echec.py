#! /usr/bin/env python3
# coding: utf-8
plateau=[['t', 'c', 'f', 'k', 'q', 'f', 'c', 't'],
 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
 ['.', '.', '.', '.', '.', '.', '.','.'] ,
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.', '.','.'],
 ['.', '.', '.', '.', '.', '.', '.', '.'],
 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
 ['T', 'C', 'F', 'K', 'Q', 'F', 'C', 'T']]

def affichePlateau():
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
            print('Coordonées incorrecte, ressaisissez les coordonnées:')
            coordY=input('Coordonnée x: ')
            coordX=input('Coordonnée y: ')
        elif int(coordY) < 0 or int(coordY) > 8 or int(coordX) < 0 or int(coordX) > 8:
            print('Coordonées incorrecte, ressaisissez les coordonnées:')
            coordY=input('Coordonnée x: ')
            coordX=input('Coordonnée y: ')
        else:
            erreur=1

def verifPiece(y,x):
    if plateau[y][x].lower()=='p':
        return 1
    if plateau[y][x].lower()=='f':
        return 2
    if plateau[y][x].lower()=='q':
        return 3
    if plateau[y][x].lower()=='k':
        return 4
    if plateau[y][x].lower()=='c':
        return 5
    if plateau[y][x].lower()=='t':
        return 6
    return 0
    
#y1 = x1
#y2 = x2
def pion(y1,x1,y2,x2):
    if  y1==6 and y1==y2+2 and verifPiece(y2,x2)==0:#Avancer de 2 noir
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    if y1==1 and y1==y2-2 and verifPiece(y2,x2)==0:#Avancer de 2 blanc
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    if x1 == x2-1 and y2 == y1 and verifPiece(y2,x2) == 0:#Avancer de 1
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    if verifPiece(y2,x2)!= 0 and x1+1==x2 and y2==y1+1 or y2==y1-1 and y1-1>0 and y1+1<8 and x1+1<8:#Manger piece
        tmp=plateau[y1][x1]
        plateau[y1][x1]='.'
        plateau[y2][x2]=tmp
        return affichePlateau()
    else :
        print('Impossible')
    
        
        
##def fou():
##
##def reine():
##
##def roi():
##
##def cavalier():
##
##def tour():
##
##
##
##def main():

affichePlateau()