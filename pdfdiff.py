from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from itertools import tee, islice, chain
import os
import sys
import getopt
import glob

#converts pdf, returns its text content as a string


def previous_and_next(some_iterable):
    prevs, items, nexts = tee(some_iterable, 3)
    prevs = chain([None], prevs)
    nexts = chain(islice(nexts, 1, None), [None])
    return zip(prevs, items, nexts)

def convert(fname, pages=None):
    print("Inside convert")
    print(pages)
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    print("output: ", output)
    manager = PDFResourceManager()
    print("Manager: ", manager)
    converter = TextConverter(manager, output, laparams=LAParams())
    print("Converter: ", converter)
    interpreter = PDFPageInterpreter(manager, converter)
    print("interpreter: " , interpreter)
    infile = open(fname, 'rb')
    print("infile: ", infile)
    print("Pagenums: ",pagenums)
    for page in PDFPage.get_pages(infile, pagenums):
        print("Here")
        interpreter.process_page(page)
    print("Here")
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir


def convertMultiple(pdfDir, txtDir):
    print("Inside convertMultiple")
    if pdfDir == "":
        pdfDir = os.getcwd() + "\\"  # if no pdfDir passed in
    for pdf in os.listdir(pdfDir):
        print("Inside convertMultiple for loop")  # iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        print(fileExtension)
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            print("Filename: ", pdfFilename)
            text = convert(pdfFilename)  # get string of text content of pdf
            textFilename = txtDir + pdf + ".txt"
            # make text file
            textFile = open(textFilename, "w", encoding="utf-8")
            textFile.write(text)  # write text to text file

def main():
    # set paths accordingly:
    pdfDir = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\PDF\\"
    txtDir = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\Text\\"
    #convertMultiple(pdfDir, txtDir)

    os.chdir(r'C:\\Users\\Sohail\\Desktop\\Machine Learning\\Text')
    myFiles = glob.glob('*.txt')
    for index, obj in enumerate(myFiles):
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\Text\\'+obj, 'r', encoding="utf-8")
        for index1, obj1 in enumerate(myFiles):
            if index1 > index:
                file2 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\Text\\'+obj1, 'r', encoding="utf-8")
                FO = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\Difference\\'+obj1+"difference", 'w', encoding="utf-8")
                lines = file1.readlines()
                print("filename:" , obj)
                print(lines)
                for i,line in file2:
                    line = file2.readlines()
                    if lines != line:
                        print("line is different:")
                        #print(lines[i])
                        print(line)
                        if lines == "\n" or line == "\n":
                            print("empty line")
                        else:
                            FO.write(str(lines))
                    else:
                        print("same")
main()
