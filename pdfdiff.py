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
    # pdfDir = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\California\\"
    # txtDir = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextCalifornia\\"
    # convertMultiple(pdfDir, txtDir)
    # pdfDir1 = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\Kaiser\\"
    # txtDir1 = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKaiser\\"
    # convertMultiple(pdfDir1, txtDir1)
    # pdfDir2 = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\KAISER PERMANENTE INSURANCE COMPANY\\"
    # txtDir2 = "C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKAISER PERMANENTE INSURANCE COMPANY\\"
    # convertMultiple(pdfDir2, txtDir2)
    
    os.chdir(r'C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextCalifornia')
    myFiles = glob.glob('*.txt')
    for index, obj in enumerate(myFiles):
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextCalifornia\\'+obj, 'r', encoding="utf-8")
        lines = file1.readlines()
        file1.close()
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextCalifornia\\'+obj, 'w', encoding="utf-8")
        for line in lines:
            if line.rsplit():
                file1.write(line)
        file1.close()

    os.chdir(r'C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKaiser')
    myFiles1 = glob.glob('*.txt')
    for index, obj in enumerate(myFiles1):
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKaiser\\'+obj, 'r', encoding="utf-8")
        lines = file1.readlines()
        file1.close()
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKaiser\\'+obj, 'w', encoding="utf-8")
        for line in lines:
            if line.rsplit():
                file1.write(line)
        file1.close()
    
    os.chdir(r'C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKAISER PERMANENTE INSURANCE COMPANY')
    myFiles2 = glob.glob('*.txt')
    for index, obj in enumerate(myFiles2):
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKAISER PERMANENTE INSURANCE COMPANY\\'+obj, 'r', encoding="utf-8")
        lines = file1.readlines()
        file1.close()
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKAISER PERMANENTE INSURANCE COMPANY\\'+obj, 'w', encoding="utf-8")
        for line in lines:
            if line.rsplit():
                file1.write(line)
        file1.close()


    for index, obj in enumerate(myFiles):
        file1 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextCalifornia\\'+obj, 'r', encoding="utf-8")
        for index1, obj1 in enumerate(myFiles1):
                file2 = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\TextKaiser\\'+obj1, 'r', encoding="utf-8")
                FO = open('C:\\Users\\Sohail\\Desktop\\Machine Learning\\Difference\\'+obj+"+"+obj1+"difference", 'w', encoding="utf-8")
                lines = file1.readlines()
                lines2 = file2.readlines()
                i = 0
                #print(lines)
                # for line in lines:
                while(True and len(lines) > 0 and len(lines2)):
                    if lines[i] != lines2[i]:
                        if lines[i] == "\n" or lines2[i] == "\n" or not lines[i].split() or not lines2[i].split():
                            #print("empty line")
                            pass
                        else:
                            FO.write(str(lines2[i]) + "lines number:  " + str(i))
                            # print("line is different:")
                            # print(lines[i])
                            # print(lines2[i])
                            break
                    else:
                        pass
                    i = i + 1
                    if(i > len(lines) or i > len(lines2)):
                        break
                        #print("same")

    os.chdir(r'C:\Users\Sohail\Desktop\Machine Learning\Difference')
    myFiles3 = glob.glob('*.txt')
    for x in myFiles3:
        print(x)
    for index, obj in enumerate(myFiles3):
        file_stats = os.stat(obj)
        print(obj + " size: " + file_stats.st_size)
        if file_stats.st_size == 0:
            os.remove(obj)

main()
