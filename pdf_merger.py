import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()
        
for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("new_file_combined.pdf")
