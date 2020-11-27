from bookingSlides import *
from dictionary import *
import glob

def plot(outF,inputFolder=""):

    dict = glob.glob(inputFolder+"vali*/sta*")
    # dir = "SR_6j_2b"
    # print(dict)
    fileList = []
    for folder in dict:
        # print(folder)
        fileList.append(folder+"/"+"stackplot_pBDT400_multiclass_cat_even_test_odd_allEvent.pdf")
    # print(fileList)
    # slide1 = len(fileList) / 6
    remain = len(fileList) % 6

    for ifile, file in enumerate(fileList):
        

        # if "6p" in plot:
        #     make_6plots(outF, Title,VarList,inputFolder+sel+"/")

                # if ',' in file:
                #     suffix = file.split(',')[1]
                # else:
                #     suffix = ''
                #
                # if len(suffix)>0:
                #     Title = "\large{"+sel+":"+file.split('.')[0]+":"+suffix+":"+campaign+"}"
                #     VarList = [campaign+"_"+file.split('.')[0]+"_"+suffix+"_new_"+item+"_old_"+NewOld_var[item] for item in plot_dict[plot]]
                # else:
                #     Title = "\large{"+sel+":"+file.split('.')[0]+":"+campaign+"}"
                #     VarList = [campaign+"_"+file.split('.')[0]+"__new_"+item+"_old_"+NewOld_var[item] for item in plot_dict[plot]]
                #
                #
                # Title = Title.replace('_','\\_')
                #
                # # print(Title)
                #
                # if "6p" in plot:
                #     make_6plots(outF, Title,VarList,inputFolder+sel+"/")
                # elif "2p" in plot:
                #     make_2plots(outF, Title,VarList,inputFolder+sel+"/")
                # elif "3p" in plot:
                #     make_3plots(outF, Title,VarList,inputFolder+sel+"/")

























#
