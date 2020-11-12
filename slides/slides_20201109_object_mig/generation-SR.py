from bookingSlides import *


def plot(outF,inputFolder=""):

    # print(Dict_new_selection.keys(),Dict_samples.keys())
    sel = "SR"
    # for sel in Dict_new_selection.keys():
    for file in Dict_samples.keys():
        for campaign in ["mc16a", "mc16d", "mc16e", "mc16", "data"]:
            for plot in plot_dict.keys():


                if "data" in file:
                    if "mc" in campaign:
                        continue
                    if "mconly" in plot:
                        continue
                else:
                    if "data" in campaign:
                        continue


                if ',' in file:
                    suffix = file.split(',')[1]
                else:
                    suffix = ''


                if len(suffix)>0:
                    Title = "\large{"+sel+":"+file.split('.')[0]+":"+suffix+":"+campaign+"}"
                    VarList = [campaign+"_"+file.split('.')[0]+"_"+suffix+"_new_"+item+"_old_"+NewOld_var[item] for item in plot_dict[plot]]
                else:
                    Title = "\large{"+sel+":"+file.split('.')[0]+":"+campaign+"}"
                    VarList = [campaign+"_"+file.split('.')[0]+"__new_"+item+"_old_"+NewOld_var[item] for item in plot_dict[plot]]


                Title = Title.replace('_','\\_')

                # print(Title)


                if "6p" in plot:
                    make_6plots(outF, Title,VarList,inputFolder+sel+"/")
                elif "2p" in plot:
                    make_2plots(outF, Title,VarList,inputFolder+sel+"/")
                elif "3p" in plot:
                    make_3plots(outF, Title,VarList,inputFolder+sel+"/")

























#
