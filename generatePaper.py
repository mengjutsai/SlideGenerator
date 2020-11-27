# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime
import argparse

from os import listdir
from os.path import isfile, join, getsize
from os import walk
from bookingSlides import *
from dictionary import *

import glob
# import package from filename: https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
import imp
# from slides.slides_20201109_object_mig.dictionary import *

# import


############ Run with ###############

#  python generateSlides.py --output outputfolder

#####################################

def getArgs():
    # username = os.environ["USER"]
    parser = argparse.ArgumentParser(description='Submit condor jobs')
    # parser.add_argument("--job", dest="job", action="store", default="default", help="Input for the job name")
    parser.add_argument("--output", dest="outputPath", action="store", default="", help="output file")
    parser.add_argument("--outputfile", dest="outputfile", action="store", default="", help="output file")
    parser.add_argument("--input", dest="input", action="store", default="", help="input file")
    parser.add_argument("--inputFolder", dest="inputFolder", action="store", default="", help="input folder")

    # parser.add_argument("--var", dest="variables", action="store", default="HT_all", help="Variables for trainning")
    # parser.add_argument("--mass", dest="mass", action="store", default="", help="Mass point")
    # parser.add_argument("--train_parity", dest="train_parity", action="store", default="", help="trainning sample's parity: even or odd")
    parser.add_argument("--compile", dest="compile", action="store_true", default=False, help="test mode")
    # args = parser.parse_args()
    return  parser.parse_args()

def main():

    args=getArgs()
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    outputPath = args.outputPath
    outputfile = args.outputfile
    out = outputPath+outputfile
    print(out)


    if len(outputfile)>0:
        if os.path.isfile(out):
            os.remove(out)
    else:
        out = outputPath+"Validation.tex"
        if os.path.isfile(out):
            #print("please remove the file")
            os.remove(out)
        else:
            print("please follow the format")

    outF = open(out,"w+")

    # abs_file_path = os.path.abspath(file_path) # get abs path for file path go for latex compile

    files_list = []
    hist_list = []

    bookPaper(outF, "stackplot")

    # make_frame(outF, "Results")

    input = args.input
    inputFolder = args.inputFolder
    dict = glob.glob(inputFolder+"vali*/sta*")

    fileList = []
    for folder in dict:
        fileList.append(folder+"/"+"stackplot_pBDT400_multiclass_cat_even_test_odd_allEvent.pdf")

    for ifile, file in enumerate(fileList):
        filename = "stackplot_pBDT400_multiclass_cat_even_test_odd_allEvent"
        weight = file.split("ClassWeight_")[1].split('/')[0]
        caption = filename + " and weight is " + weight
        caption = caption.replace('_','\\_')

        if ifile==0:
            PlotBegin(outF)

        MakePlot(outF,file,caption)

        if ifile%3 == 2:
            PlotEnd(outF)
            outF.write('\n')

        # if ifile%9 == 8:
        #     PlotEnd(outF)
        #     outF.write('\\newpage')
        # else:
        #     PlotBegin(outF)
        #     if ifile%3 == 2:
        #         PlotBegin

    endPaper(outF)


    if(args.compile):
        # os.system("pdflatex --interaction=batchmode "+outputPath+"Validation.tex")
        # os.system("pdflatex --interaction=batchmode "+outputPath+"Validation.tex")
        # os.system("lualatex "+outputPath+"Validation.tex")
        # os.system("pdflatex  "+outputPath+"Validation.tex")
        os.chdir(outputPath)
        os.system("lualatex -halt-on-error "+outputfile)
        # os.system("pdflatex -halt-on-error "+outputfile)

    else:
        print("No compile")


if __name__ == "__main__":
    args=getArgs()
    main()
