# -*- coding: utf-8 -*-
# from dictionary import *

def make_general_structure(outF, File_title = "Recent Work"):
    #write the tex file
    outF.write("\\documentclass[pdf]{beamer}\n")
    outF.write("\\usepackage{tikz}\n")
    outF.write("\\usepackage[utf8]{inputenc}\n")
    outF.write("\\usepackage{graphicx}\n")
    outF.write("\\usepackage{color}\n")
    outF.write("\\usepackage{lscape}\n")
    outF.write("\\usepackage{subfig}\n")
    outF.write("\\usepackage[skip=0.1cm]{caption}\n")
    # outF.write("\\usepackage[hidelinks]{hyperref}\n")
    outF.write("\\usepackage{standalone}\n")
    outF.write("\\usepackage{tikz}\n")

    # https://tex.stackexchange.com/questions/7953/how-to-expand-texs-main-memory-size-pgfplots-memory-overload

    outF.write("\\usepackage{pgfplots}\n")
    # outF.write("\\usepgfplotslibrary{external} \n")
    outF.write("\\usetikzlibrary{patterns} \n")
    outF.write("\\usetikzlibrary{external} \n")
    outF.write("\\tikzexternalize\n")
    # outF.write("\\tikzset{external/force remake}\n")

    # outF.write("%\\usepackage{underscore}\n")#this package seems not working
    outF.write("\\usepackage{hyperref}\n")
    outF.write("\\captionsetup[subfloat]{captionskip=0.1pt, labelformat=empty, position=top}\n")
    # outF.write("\\captionsetup[figure]{captionskip=1.pt, labelformat=empty}\n")
    outF.write("\\captionsetup{labelformat=empty,labelsep=none}\n")
    outF.write("\\usetikzlibrary{positioning,arrows}\n")
    outF.write("\\mode<presentation>{\n")
    outF.write("    \\usetheme{Warsaw}\n")
    outF.write("    \\usecolortheme{default}\n")
    outF.write("    \\usefonttheme{serif}\n")
    outF.write("    \\setbeamertemplate{navigation symbols}{}\n")
    outF.write("    \\setbeamertemplate{caption}[numbered]\n")
    outF.write("    \\setbeamertemplate{footline}[frame number]{}\n")
    outF.write("}\n")
    outF.write("\\title[Recent Work]{"+File_title+"}\n")
    outF.write("\\author{%\n")
    outF.write("\\textsc{\\scriptsize{\\underline{Meng-Ju Tsai}, Zhi Zheng, Jianming Qian}}\\\\}\n")
    outF.write("\\date{\\today}\n")
    outF.write("\\begin{document}\n")
    outF.write("\\setbeamertemplate{caption}{\\raggedright\\insertcaption\\par}\n")
    outF.write("\\begin{frame}\n")
    outF.write("\\titlepage\n")
    outF.write("\\end{frame}\n")
    # outF.write("\\begin{frame}{Introduction}\n")
    # outF.write("\\tableofcontents\n")
    # outF.write("\\end{frame}\n")


def make_6plots(outF, title, variable, file_path):
    # print(variable)
    outF.write("\\begin{frame}{"+title+"}\n")
    outF.write("\\vspace{-1cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    variable_name = []
    for i in range(0,3):
        variable_name = variable[i].replace("_","\\_")
        # outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
        outF.write("\subfloat[]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n\\vspace{-0.8cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    for i in range(3,6):
        variable_name = variable[i].replace("_","\\_")
        # outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
        outF.write("\subfloat[]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\end{frame}\n")

def make_5plots(outF, title, variable, file_path):
    outF.write("\\begin{frame}{"+title+"}\n")
    outF.write("\\vspace{-1cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    variable_name = []
    for i in range(0,3):
        variable_name = variable[i].replace("_","-")
        outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n\\vspace{-0.8cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    for i in range(3,5):
        variable_name = variable[i].replace("_","-")
        outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width=0.35\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\end{frame}\n")


def make_4plots(outF, title, variable, file_path):
    outF.write("\\begin{frame}{"+title+"}\n")
    outF.write("\\vspace{-0.5cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    variable_name = []
    for i in range(0,2):
        variable_name = variable[i].replace("_","-")
        outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width=0.35\\textwidth,height=0.42\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n\\vspace{-0.8cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    for i in range(2,4):
        variable_name = variable[i].replace("_","-")
        outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width=0.35\\textwidth,height=0.42\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\end{frame}\n")

def make_3plots(outF, title, variable, file_path):
    outF.write("\\begin{frame}{"+title+"}\n")
    outF.write("\\vspace{-1cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    variable_name = []
    for i in range(0,3):
        variable_name = variable[i].replace("_","\\_")
        outF.write("\subfloat[]{\\includegraphics[width=0.35\\textwidth,height=0.42\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\end{frame}\n")

def make_2plots(outF, title, variable, file_path):
    outF.write("\\begin{frame}{"+title+"}\n")
    outF.write("\\vspace{-1cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    variable_name = []
    for i in range(0,2):
        variable_name = variable[i].replace("_","\\_")
        # outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width=0.45\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
        outF.write("\subfloat[]{\\includegraphics[width=0.45\\textwidth,height=0.4\\textheight]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\end{frame}\n")

def make_FitResults(outF, title, variable, file_path):
    title = title.replace('_','\_')
    title = title.replace('>','$>$')
    title = title.replace('<','$<$')
    outF.write("\\begin{frame}{"+title+"}\n")
    outF.write("\\vspace{-0.8cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    variable_name = []
    for i in range(0,2):
        # variable_name = variable[i].replace("_","-")
        variable_name=""
        if(variable[i]=="NormFactors"):
            width="0.38"
            height="0.45"
            trim = ",trim=0 0 6cm 0"
        elif(variable[i]=="CorrMatrix"):
            width="0.6"
            height="0.7"
            trim = ""
        outF.write("\subfloat[\\scriptsize{"+variable_name+"}]{\\includegraphics[width="+width+"\\textwidth,height="+height+"\\textheight"+trim+"]{"+file_path+variable[i]+".pdf"+"}}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\vspace{-0.5cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    outF.write("\\includegraphics[width=0.2\\textwidth,angle=90]{"+file_path+variable[2]+".pdf"+"}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\end{frame}\n")

def make_MVAResults(outF, title, file_path):
    # print(title)
    if("_" in title):
        title = title.replace('_','\\_')
    outF.write("\\begin{frame}{"+title+"}\n")
    outF.write("\\vspace{-1cm}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    # variable_name = []
    # for i in range(0,3):
    #     variable_name = variable[i].replace("_","-")
    outF.write("\subfloat[]{\\includegraphics[width=0.35\\textwidth,height=0.42\\textheight]{"+file_path+"CorrelationMatrixS"+"}}\n")
    outF.write("\\hspace{0.5cm}\n")
    outF.write("\subfloat[]{\\includegraphics[width=0.35\\textwidth,height=0.42\\textheight]{"+file_path+"CorrelationMatrixB"+"}}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\begin{figure}\n\\centering\n")
    outF.write("\\includegraphics[width=0.45\\textwidth,height=0.42\\textheight]{"+file_path+"overtrain_BDTG"+"}\n")
    outF.write("\\end{figure}\n")
    outF.write("\\end{frame}\n")



def make_frame(outF,inputText="Backup"):
    outF.write("\\begin{frame}{}\n")
    outF.write("\\centering\n")
    outF.write("\\textbf{"+inputText+"}\n")
    outF.write("\\end{frame}\n")


def closure(outF):
    outF.write("\\begin{frame}\n")
    outF.write("\\centering\n")
    outF.write("\\textbf{Backup}\n")
    outF.write("\\end{frame}\n")
    outF.write("\n\end{document}\n")
    outF.close()




def bookPaper(outF, File_title = "Recent Work"):
    outF.write("\\documentclass[]{report}\n")
    outF.write("\\usepackage{graphicx}\n")
    outF.write("\\usepackage{subfig}\n")
    outF.write("\\usepackage[skip=0.1cm]{caption}\n")
    outF.write("\\captionsetup[subfloat]{captionskip=0.1pt, labelformat=empty, position=top}\n")
    outF.write("\\usepackage[skip=0.1cm]{caption}\n")
    outF.write("\\title{"+File_title+"}\n")
    outF.write("\\begin{document}\n")
    outF.write("\\maketitle\n")

def MakePlot(outF,file,caption):
    outF.write("\\begin{figure}\n\\centering\n")
    outF.write("\\includegraphics[width=0.7\\textwidth]{"+file+"}\n")
    outF.write("\\caption{"+caption+"}\n")
    outF.write("\\end{figure}\n")

def endPaper(outF):
    outF.write("\n\end{document}\n")
    outF.close()
