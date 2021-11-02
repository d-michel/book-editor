#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:41:23 2020

@author: michel
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import numpy as np

def indexMergerMatrix(N):
    n = (int) (N/2)
    M = np.zeros((n,2))
    
    for i in range(n):
        if i % 2 == 0:
            M[i][0] = N - 1 - i
            M[i][1] = i
        else:
            M[i][0] = i
            M[i][1] = N - 1 - i
    
    k = (int) (n/2)
    
    for i in range(k):
        if i % 2 == 1:
            aux = M[i].copy()
            M[i] = M[n-i].copy()
            M[n-i] = aux.copy()
    
    return(M)

input_file = "main.pdf"             # archivo de entrada
output_file = "print.pdf"           # archivo de salida

pdf = PdfFileReader(input_file)     # se inicializa un objeto PDFFileReader del archivo de entrada
pdf_aux = PdfFileWriter()           # se inicializa un objeto PDFFileWriter auxiliar
pdf_out = PdfFileWriter()           # se inicializa un objeto PDFFileWriter de salida

pdf_aux.appendPagesFromReader(pdf)  # se incluye en el objeto auxiliar las páginas del PDF de entrada

numPagesPreface = 0                # número de páginas de prefacio del PDF

# si el número de páginas de prefacio es impar, se incluye una página en blanco adicional tras éste
if numPagesPreface % 2 == 1:
    pdf_aux.insertBlankPage(index = numPagesPreface)

numPages = pdf_aux.getNumPages()    # número de páginas del PDF auxiliar

# si el número de páginas del PDF es par, se añaden dos páginas en blanco al final
# si es impar, sólo se añade una página más
# el ńumero de páginas resultante será siempre par

lec_file = "lector.pdf"
pdf_lec = PdfFileReader(lec_file)

if numPages % 2 != 0:
    pdf_aux.addBlankPage()
    numPages += 1

if numPages % 4 != 0:
    pdf_aux.addBlankPage()
    pdf_aux.appendPagesFromReader(pdf_lec)
    numPages += 2
else:
    pdf_aux.addBlankPage()
    pdf_aux.addBlankPage()
    pdf_aux.addBlankPage()
    pdf_aux.appendPagesFromReader(pdf_lec)
    numPages += 4

n = (int) (numPages/2)              # mitad de las páginas totales

M = indexMergerMatrix(numPages)         # matriz de índices de página permutados

for i in range(n):
    page0 = pdf_aux.getPage((int) (M[i][0]))
    page1 = pdf_aux.getPage((int) (M[i][1]))
    
    pdf_out.addPage(page0)
    pdf_out.addPage(page1)

out = open(output_file, "wb")   # se abre el archivo de salida
pdf_out.write(out)              # se copia el contenido del PDF en el archivo de salida
out.close()

# for i in range(n):
#     ipage = pdf_aux.getPage(i)                      # página i
#     N_ipage = pdf_aux.getPage(numPages - 1 - i)     # página (N-i)
    
#     # si i es par, se añade en el PDF de salida:
#     if i % 2 == 0:
#         pdf_out.addPage(N_ipage)    # primero la página (N-i)
#         pdf_out.addPage(ipage)      # luego la página i
#     # si i es impar, viceversa
#     else:
#         pdf_out.addPage(ipage)
#         pdf_out.addPage(N_ipage)

# out = open(output_file, "wb")   # se abre el archivo de salida
# pdf_out.write(out)              # se copia el contenido del PDF en el archivo de salida
# out.close()





# printfile = "print.pdf"
# outputfile = "output.pdf"
# # PDF1: A4 Landscape page created in photoshop using PdfCreator, 
# input1 = PdfFileReader(printfile)
# page1 = input1.getPage(1)

# # PDF2: A4 Landscape page, text only, created using Pisa (www.xhtml2pdf.com)
# page2 = input1.getPage(5)

# # Merge
# page1.mergePage(page2)

# # Output
# output = PdfFileWriter()
# output.addPage(page1)
# outputStream = open(outputfile, "wb")
# output.write(outputStream)
# outputStream.close()