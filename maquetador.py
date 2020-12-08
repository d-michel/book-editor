#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 21:41:23 2020

@author: michel
"""

from PyPDF2 import PdfFileReader, PdfFileWriter

input_file = "main.pdf"
output_file = "print.pdf"

pdf = PdfFileReader(input_file)
pdf_aux = PdfFileWriter()
pdf_out = PdfFileWriter()

pdf_aux.appendPagesFromReader(pdf)

numPagesPreface = 21
if numPagesPreface % 2 == 0:
    pdf_aux.insertBlankPage(index = numPagesPreface)
    pdf_aux.insertBlankPage(index = numPagesPreface)
else:
    pdf_aux.insertBlankPage(index = numPagesPreface)

numPages = pdf_aux.getNumPages()

if numPages % 2 == 0:
    pdf_aux.addBlankPage()
    pdf_aux.addBlankPage()
    N = numPages + 2
else:
    pdf_aux.addBlankPage()
    pdf_aux.addBlankPage()
    pdf_aux.addBlankPage()
    N = numPages + 3

n = (int) (N/2)

for i in range(n):
    ipage = pdf_aux.getPage(i)
    N_ipage = pdf_aux.getPage(N - 1 - i)
    
    if i % 2 == 0:
        pdf_out.addPage(ipage)
        pdf_out.addPage(N_ipage)
    else:
        pdf_out.addPage(N_ipage)
        pdf_out.addPage(ipage)

out = open(output_file, "wb")
pdf_out.write(out)
out.close()