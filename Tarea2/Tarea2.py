# encoding: UTF-8 

import sys
import csv
import codecs

infile = codecs.open(sys.argv[1], "r", "utf8")

libro = infile.read()
caracteres=[]
repeticiones=[]

letras=[]
lista=[]

nombre="frecuencias_"+ sys.argv[1]

tablafinal=codecs.open(nombre, "w", "utf8")

omitir= [' '.decode('utf-8'), '.'.decode('utf-8'),','.decode('utf-8'),':'.decode('utf-8'),';'.decode('utf-8'),'"'.decode('utf-8'),'('.decode('utf-8'),')'.decode('utf-8'),'¿'.decode('utf-8'),'?'.decode('utf-8'),'¡'.decode('utf-8'),'!'.decode('utf-8'),'-'.decode('utf-8'),'_'.decode('utf-8'), '\n'.decode('utf-8'), '\r'.decode('utf-8')]

#Metodo que toma el libro y lo convierte en una lista de caracteres

for i in range (len(libro)):

	caracter=libro[i]

	if (caracter not in omitir):

		caracteres.append(caracter)
		letras.append(caracter)

infile.close()

#Para el calculo de la frecuencia, cito informalmente la ayuda de Christian Poveda, estudiante del curso
letras = list(set(caracteres))

for i in range (len(letras)):
	n=caracteres.count(letras[i])
	n/=len(caracteres)
	repeticiones.append(n)

for i in range (len(letras)):

	lista.append((repeticiones[i], letras[i]))

lista.sort()
lista.reverse()

#Archivo de salida

Output=[]

for i in range (len(lista)):

	Output.append((lista[i][1], lista[i][0]))

tablafinal.write('\n'.join("%s %s" % x for x in Output))
tablafinal.close()

	






