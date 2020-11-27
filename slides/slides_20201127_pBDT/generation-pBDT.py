from bookingSlides import *
from dictionary import *
import glob

def plot(outF,inputFolder="",subfolder):
    outF.write('\\begin{center}{'+subfolder.split("\\")[-2]+'}\\end{center}\n')
    # outF.write('\\Section{'+subfolder.split("\\")[-2]+'}\n')
    outF.write('\\begin{center}{'+subfolder.split("\\")[-1]+'}\\end{center}\n')
    dict = glob.glob(inputFolder+subfolder)

    fileList = []
    for folder in dict:
        fileList.append(folder)

    fileList = sorted(fileList)

    lastRow = len(fileList)/3
    remain = len(fileList) % 3

    for ifile, file in enumerate(fileList):
        filename = file.split("\\")[-1]
        caption = filename
        caption = caption.replace('_','\\_')

        if ifile%3==0:
            PlotBegin(outF)

        MakePlot(outF,file,caption)

        if ifile%3 == 2:
            PlotEnd(outF)
            outF.write('\n')

        if remain!=0 and ifile > 3*lastRow-1:
            PlotEnd(outF)
            outF.write('\n')


def main(outF,inputFolder):
    subfolder = "validation_pBDT_binary_official_NTree1000_allBKG_nominal/separation/"
    plot(outF,inputFolder,subfolder):





















#
