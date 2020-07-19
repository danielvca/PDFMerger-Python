# github.com/danielvca

# Combining selected pages from different PDFs using PyPDF2 module

# Arguments: ["outputfilename" , "source dir"] ##

import os
import sys
from PyPDF2 import PdfFileMerger, PdfFileReader
a = str(sys.argv)
exportnamme = (sys.argv[1])+'.pdf'
dirr = sys.argv[2]

pdffile =[]

for filename in os.listdir(dirr):
	if filename.endswith('.pdf'):
		pdffile.append(filename)

merger = PdfFileMerger()
for pdf in pdffile:
    input = PdfFileReader(open(dirr+"\\"+pdf,'rb'))
    merger.append((input))

    merger.write(dirr+"\\"+exportnamme)

