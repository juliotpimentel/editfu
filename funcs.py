#! /usr/bin/env python

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
import re

import pytesseract
from PIL import Image

def editpdftopng(srcFile):

    pdf = PdfFileReader(srcFile)
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(1))

    dirname = os.path.dirname(os.path.abspath(srcFile))
#    pdb.gimp_message(dirname)
    fname = os.path.splitext(os.path.basename(srcFile))[0]
#    pdb.gimp_message(fname)
#    fname = srcFile+"_pg2"
    
    fname1 = fname+'_pg2.pdf'
#    pdb.gimp_message(fname1)
    
 
    with open(dirname+'/'+fname1, 'wb') as out:
        pdf_writer.write(out)
        
    os.system('pdftoppm -r 300 '+dirname+'/'+fname1+' '+dirname+'/pg2')
    os.system('pnmtopng '+dirname+'/'+ 'pg2-1.ppm > '+dirname+'/'+'pg2-1.png')
    filename1 = dirname+'/'+'pg2-1.png'
    
    pdf = PdfFileReader(srcFile)
    pdf_writer = PdfFileWriter()
    pdf_writer.addPage(pdf.getPage(3))
    
    fname2 = fname+'_pg4.pdf'
#    pdb.gimp_message(fname2)
 
    with open(dirname+'/'+fname2, 'wb') as out:
        pdf_writer.write(out)
    
    os.system('pdftoppm -r 300 '+dirname+'/'+fname2+' '+dirname+'/pg4')
    os.system('pnmtopng '+dirname+'/'+ 'pg4-1.ppm > '+dirname+'/'+'pg4-1.png')
    filename2 = dirname+'/'+'pg4-1.png'
    
    return(dirname, filename1, filename2)

def findRE(srcFile):
    
    text = pytesseract.image_to_string(Image.open(srcFile))
       
    index = text.find('\n')
    
    item = text[0:index]
    item = item.replace(' ', '')
    item = item.replace('/', '')
    item = item.replace('-', '')
    item = item.replace('+', '')    
    print (item)
    
    reQuanti = re.compile('Quantidade:\s(\d+)')
    quanti = reQuanti.search(text).group(1)
    print(quanti)
    
    reDesti = re.compile('Comprador:\s([a-z]+)', re.IGNORECASE)
    desti = reDesti.search(text).group(1)
    print(desti)
    
    return(item, quanti, desti)

srcFile = '/home/juliop/Downloads/Vendas/CapaHDD-x230-t430/pg2-1.ppm'

findRE(srcFile)

