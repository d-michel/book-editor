#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 15:48:48 2021

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

def merger_2():
    input0 = "port.pdf"
    input1 = "main1.pdf"
    input2 = "main2.pdf"
    
    output_file = "main.pdf"
    
    pdf0 = PdfFileReader(input0)
    pdf1 = PdfFileReader(input1)
    pdf2 = PdfFileReader(input2)
    
    pdf_out = PdfFileWriter()
    
    pdf_out.appendPagesFromReader(pdf0)
    pdf_out.addBlankPage()
    pdf_out.appendPagesFromReader(pdf1)
    
    numPages = pdf_out.getNumPages()
    
    if numPages % 2 != 0:
        pdf_out.addBlankPage()
    
    pdf_out.appendPagesFromReader(pdf2)
    
    out = open(output_file, "wb")   # se abre el archivo de salida
    pdf_out.write(out)              # se copia el contenido del PDF en el archivo de salida
    out.close()

def merger_3():
    input0 = "port.pdf"
    input1 = "main1.pdf"
    input2 = "main2.pdf"
    input3 = "main3.pdf"
    
    output_file = "main.pdf"
    
    pdf0 = PdfFileReader(input0)
    pdf1 = PdfFileReader(input1)
    pdf2 = PdfFileReader(input2)
    pdf3 = PdfFileReader(input3)
    
    pdf_out = PdfFileWriter()
    
    pdf_out.appendPagesFromReader(pdf0)
    pdf_out.addBlankPage()
    pdf_out.appendPagesFromReader(pdf1)
    
    numPages = pdf_out.getNumPages()
    
    if numPages % 2 != 0:
        pdf_out.addBlankPage()
    
    pdf_out.appendPagesFromReader(pdf2)
    
    numPages = pdf_out.getNumPages()
    
    if numPages % 2 != 0:
        pdf_out.addBlankPage()
    
    pdf_out.appendPagesFromReader(pdf3)
    
    out = open(output_file, "wb")   # se abre el archivo de salida
    pdf_out.write(out)              # se copia el contenido del PDF en el archivo de salida
    out.close()

merger_2()