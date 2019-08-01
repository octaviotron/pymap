#!/usr/bin/python

# -*- coding: utf-8 -*-
import random

def matriz(tama):
	matriz = [[0]*tama for x in xrange(tama)]
	return matriz

# not used yet (non-square empty matrix)
def emptymatrix(x,y):
    matriz = [[None]*y for x in xrange(x)]
    return matriz


def muestramatriztxt(matriz):
	for i, e in reversed(list(enumerate(matriz))):
		print str('%02d' % i)+" ",
		for j in (range(0, len(e))):
			if matriz[i][j]<10:
				print "",
			if matriz[i][j]<100:
				print "",
			print matriz[i][j],
		print
	print "  ",
	print

def rndmatriz(matriz):
	for i in range(0, len(matriz)):
		for j in (range(0, len(matriz[i]))):
			r = random.random()
			rr = r * 255
			rrr = int(round(rr,0))
			matriz[i][j]=rrr
	return matriz 

def rrange(v1, v2):
	if v1 == v2:
		return v1
	if v1 - v2 > 0:
		rrrr = random.randrange(v2,v1,1)
	else:
		rrrr = random.randrange(v1,v2,1)
	return rrrr

def arm_horizontal(matriz):
	salida = []
	temp =[]
	for i in range(0, len(matriz)):
		for j in (range(0, len(matriz[i])-1)):
			temp.append(matriz[i][j])
			actual = int(matriz[i][j])
			siguiente = int(matriz[i][j+1])
			intermedio = rrange(actual,siguiente)
			temp.append(int(intermedio))
		temp.append(matriz[i][-1])
		salida.append(temp)
		temp=[]
	return salida

def arm_vertical(matriz):
	salida = []
	temp =[]
	for i in range(0, len(matriz)-1):
		salida.append(matriz[i])
		for j in (range(0, len(matriz[i]))):
			actual = int(matriz[i][j])
			siguiente = int(matriz[i+1][j])
			intermedio = rrange(actual,siguiente)
			temp.append(int(intermedio))
		salida.append(temp)
		temp=[]
	salida.append(matriz[-1])
	return salida

def creamatriz(semilla, pasos):
	matriz_vacia = matriz(semilla)
	r=rndmatriz(matriz_vacia)
	muestramatriztxt(r)
	for i in range(0, pasos):
		r = arm_horizontal(r)
		r = arm_vertical(r)
		muestramatriztxt(r)
	return r

def matrizterreno(entrop, ciclos):
	salida = []
	tmp = []
	terr = creamatriz(entrop,ciclos)
	for i in range(0, len(terr)):
		for j in range(0, len(terr[0])):
			val = terr[i][j]
			tmp.append([val,False,False,False])
		salida.append(tmp)
		tmp = []
	return salida

def guardamap(matriz):
	with open('data.py', 'w') as datafile:
		datafile.write("matriz="+str(matriz))
		datafile.close()


t = creamatriz(10,2)
muestramatriztxt(t)
