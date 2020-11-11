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


############ Run with ###############

#  python generateSlides_Fit.py --output ./ --name FitResults

#####################################

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Submit condor jobs')
    parser.add_argument("--output", dest="outputPath", action="store", default=" ", help="output file")
    parser.add_argument("--name", dest="outputName", action="store", default="", help="output file name")
    parser.add_argument("--compile", dest="compile", action="store_true", default=False, help="test mode")
    args = parser.parse_args()



print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

outputPath = args.outputPath
if(len(args.outputName)>0):
    if os.path.isfile(outputPath+args.outputName+".tex"):
        #print("please remove the file")
        os.remove(outputPath+args.outputName+".tex")
        fileName = outputPath+args.outputName+".tex"
    else:
        print("please follow the format")
        fileName = outputPath+args.outputName+".tex"
else:
    if os.path.isfile(outputPath+"Validation.tex"):
        #print("please remove the file")
        os.remove(outputPath+"Validation.tex")
        fileName = outputPath+"Validation.tex"
    else:
        print("please follow the format")
        fileName = outputPath+"Validation.tex"

# print(fileName)
# print(type(fileName))

outF = open(fileName,"w+")

files_list = []
hist_list = []

make_general_structure(outF, "Recent Work")


make_frame(outF, "Fit results")


# SM Plain Asimov Fit
make_FitResults(outF, "\large{SM 4tops Plain Asimov Fit}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/SM4top_Finalfit_Full_Syst_BDT_PlainAsimov_v3/"
        )

# SM Real CR-Only
make_FitResults(outF, "\large{SM/BSM Real CR-Only Fit}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200529/CR-OnlyFit/SM_Finalfit_Full_Syst_BDT_CROnlyFit_v3/"
        )

# SM Realistic Asimov Fit
make_FitResults(outF, "\large{SM Realistic Asimov Fit}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/SM_Finalfit_Full_Syst_BDT_RealisticCR_AsimovSR_Fit_v2/"
        )


# Realistic Asimov HT Fit - Free Float NF\_tttt w/ nominal 1
make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH400 - Free Float NF\_tttt w/ nominal 1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt1/BSM_Finalfit_Full_Syst_mH400_HT_RealisticAsimov_NFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH500 - Free Float NF\_tttt w/ nominal 1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt1/BSM_Finalfit_Full_Syst_mH500_HT_RealisticAsimov_NFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH600 - Free Float NF\_tttt w/ nominal 1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt1/BSM_Finalfit_Full_Syst_mH600_HT_RealisticAsimov_NFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH700 - Free Float NF\_tttt w/ nominal 1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt1/BSM_Finalfit_Full_Syst_mH700_HT_RealisticAsimov_NFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH800 - Free Float NF\_tttt w/ nominal 1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt1/BSM_Finalfit_Full_Syst_mH800_HT_RealisticAsimov_NFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH900 - Free Float NF\_tttt w/ nominal 1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt1/BSM_Finalfit_Full_Syst_mH900_HT_RealisticAsimov_NFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH1000 - Free Float NF\_tttt w/ nominal 1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt1/BSM_Finalfit_Full_Syst_mH1000_HT_RealisticAsimov_NFtttt1_v1/"
        )



# Realistic Asimov HT Fit - Free Float NF\_tttt w/ nominal 2
make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH400 - Free Float NF\_tttt w/ nominal 2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt2/BSM_Finalfit_Full_Syst_mH400_HT_RealisticAsimov_NFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH500 - Free Float NF\_tttt w/ nominal 2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt2/BSM_Finalfit_Full_Syst_mH500_HT_RealisticAsimov_NFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH600 - Free Float NF\_tttt w/ nominal 2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt2/BSM_Finalfit_Full_Syst_mH600_HT_RealisticAsimov_NFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH700 - Free Float NF\_tttt w/ nominal 2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt2/BSM_Finalfit_Full_Syst_mH700_HT_RealisticAsimov_NFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH800 - Free Float NF\_tttt w/ nominal 2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt2/BSM_Finalfit_Full_Syst_mH800_HT_RealisticAsimov_NFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH900 - Free Float NF\_tttt w/ nominal 2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt2/BSM_Finalfit_Full_Syst_mH900_HT_RealisticAsimov_NFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH1000 - Free Float NF\_tttt w/ nominal 2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/FreeFloat/NF_tttt2/BSM_Finalfit_Full_Syst_mH1000_HT_RealisticAsimov_NFtttt2_v1/"
        )





# Realistic Asimov HT Fit - 50\% tttt\_Xsec, NF\_tttt=1
make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH400 - 50\% tttt\_Xsec, NF\_tttt=1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt1/BSM_Finalfit_Full_Syst_mH400_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH500 - 50\% tttt\_Xsec, NF\_tttt=1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt1/BSM_Finalfit_Full_Syst_mH500_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH600 - 50\% tttt\_Xsec, NF\_tttt=1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt1/BSM_Finalfit_Full_Syst_mH600_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH700 - 50\% tttt\_Xsec, NF\_tttt=1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt1/BSM_Finalfit_Full_Syst_mH700_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH800 - 50\% tttt\_Xsec, NF\_tttt=1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt1/BSM_Finalfit_Full_Syst_mH800_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH900 - 50\% tttt\_Xsec, NF\_tttt=1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt1/BSM_Finalfit_Full_Syst_mH900_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt1_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH1000 - 50\% tttt\_Xsec, NF\_tttt=1}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt1/BSM_Finalfit_Full_Syst_mH1000_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt1_v1/"
        )

# Realistic Asimov HT Fit - 50\% tttt\_Xsec, NF\_tttt=2
#
make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH400 - 50\% tttt\_Xsec, NF\_tttt=2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt2/BSM_Finalfit_Full_Syst_mH400_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH500 - 50\% tttt\_Xsec, NF\_tttt=2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt2/BSM_Finalfit_Full_Syst_mH500_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt2_v1/"
        )
#
make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH600 - 50\% tttt\_Xsec, NF\_tttt=2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt2/BSM_Finalfit_Full_Syst_mH600_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH700 - 50\% tttt\_Xsec, NF\_tttt=2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt2/BSM_Finalfit_Full_Syst_mH700_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH800 - 50\% tttt\_Xsec, NF\_tttt=2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt2/BSM_Finalfit_Full_Syst_mH800_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH900 - 50\% tttt\_Xsec, NF\_tttt=2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt2/BSM_Finalfit_Full_Syst_mH900_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt2_v1/"
        )

make_FitResults(outF, "\large{Realistic Asimov HT Fit - mH1000 - 50\% tttt\_Xsec, NF\_tttt=2}"
        ,["NormFactors","CorrMatrix","NuisPar"]
        ,"/Users/ploww/HEP/working/Exotics4top/macro/trex-fitter-config/FinalFit/official/FitResults/Slides20200604/BSMRealisticAsimov/tttt_Xsec_ConstNF_tttt/NF_tttt2/BSM_Finalfit_Full_Syst_mH1000_HT_RealisticAsimov_50tttt_Xsec_ConstNFtttt2_v1/"
        )

closure(outF)




if(args.compile):
    os.system("pdflatex "+fileName)
    os.system("pdflatex "+fileName)
else:
    print("No compile")
