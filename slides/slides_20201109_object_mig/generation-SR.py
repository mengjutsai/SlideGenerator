from bookingSlides import *
Dict_samples = {"4tops.root":"background",
                "ttZ.root":"background",
                "ttll.root":"background",
                "ttW.root":"background",
                "ttWW.root":"background",
                "vjets.root":"background",
                "vvv.root":"background",
                "single-top.root":"background",
                "single-top.root,410658":"background",
                "single-top.root,410659":"background",
                "single-top.root,410646":"background",
                "single-top.root,410647":"background",
                "single-top.root,410644":"background",
                "single-top.root,410645":"background",
                "single-top.root,410560":"background",
                "single-top.root,410408":"background",
                "ttbar.root":"background",
                "ttbar.root,410470":"background",
                "ttbar.root,407342":"background",
                "ttbar.root,407343":"background",
                "ttbar.root,407344":"background",
                "ttH.root":"background",
                "ttt.root":"background",
                "vh.root":"background",
                "vv.root":"background",
                "BSM4tops.root,400":"signal",
                "BSM4tops.root,500":"signal",
                "BSM4tops.root,600":"signal",
                "BSM4tops.root,700":"signal",
                "BSM4tops.root,800":"signal",
                "BSM4tops.root,900":"signal",
                "BSM4tops.root,1000":"signal",
                "data15.root":"data",
                "data16.root":"data",
                "data17.root":"data",
                "data18.root":"data",
                "data.root":"data"
                }


Dict_new_selection = {"SS3L1b":"(SSee_passECIDS||SSem_passECIDS||SSmm||eee_Zveto||eem_Zveto||emm_Zveto||mmm_Zveto)*",
                      "SR_6j":"((SSee_passECIDS||SSem_passECIDS||SSmm||eee_Zveto||eem_Zveto||emm_Zveto||mmm_Zveto) && nJets>=6)*",
                      "SR_6j_2b":"((SSee_passECIDS||SSem_passECIDS||SSmm||eee_Zveto||eem_Zveto||emm_Zveto||mmm_Zveto) && nJets>=6 && nBTags_DL1r_77>=2)*",
                      "SR":"((SSee_passECIDS||SSem_passECIDS||SSmm||eee_Zveto||eem_Zveto||emm_Zveto||mmm_Zveto) && HT_all>500000. && nBTags_DL1r_77>=2     && nJets>=6 )*",
                     }



NewOld_var = {

"nJets":"nJets",
"HT_all":"HT_all",
"nBTags_DL1r_77":"nBTags_MV2c10_77",
"met_met":"met_met",
"jet_pt[0]":"jet_pt[0]",
"jet_pt[1]":"jet_pt[1]",
"jet_pt[2]":"jet_pt[2]",
"jet_pt[3]":"jet_pt[3]",
"jet_pt[4]":"jet_pt[4]",
"jet_pt[5]":"jet_pt[5]",
"jet_eta[0]":"jet_eta[0]",
"jet_eta[1]":"jet_eta[1]",
"jet_eta[2]":"jet_eta[2]",
"jet_eta[3]":"jet_eta[3]",
"jet_eta[4]":"jet_eta[4]",
"jet_eta[5]":"jet_eta[5]",
"lep_0_pt":"lep_0_pt",
"lep_1_pt":"lep_1_pt",
"lep_2_pt":"lep_2_pt",
"lep_0_eta":"lep_0_eta",
"lep_1_eta":"lep_1_eta",
"lep_2_eta":"lep_2_eta",
"jet_sum_DL1r_Continuous":"jet_sum_mv2c10_Continuous",
"Evt_Channel":"Evt_Channel",
"GenFiltHT":"GenFiltHT",
"Tlepton_0_ID":"lepton_0_tightId",
"Tlepton_0_truthClassificationSM4t_bkgFlag":"lepton_0_truthClassificationSM4t_bkgFlag",
"Tlepton_1_ID":"lepton_1_tightId",
"Tlepton_1_truthClassificationSM4t_bkgFlag":"lepton_1_truthClassificationSM4t_bkgFlag",
"Tlepton_2_ID":"lepton_2_tightId",
"Tlepton_2_truthClassificationSM4t_bkgFlag":"lepton_2_truthClassificationSM4t_bkgFlag",
"event_BkgCategory":"event_BkgCategory",


"jet_pt":"jet_pt",
"jet_eta":"jet_eta",
"el_pt[0]":"el_pt[0]",
"el_pt[1]":"el_pt[1]",
"el_pt[2]":"el_pt[2]",
"el_eta[0]":"el_eta[0]",
"el_eta[1]":"el_eta[1]",
"el_eta[2]":"el_eta[2]",
"mu_pt[0]":"mu_pt[0]",
"mu_pt[1]":"mu_pt[1]",
"mu_pt[2]":"mu_pt[2]",
"mu_eta[0]":"mu_eta[0]",
"mu_eta[1]":"mu_eta[1]",
"mu_eta[2]":"mu_eta[2]",
"leading_bjet_pT":"leading_bjet_pT",

"Tlepton_0_mll_atConV":"lepton_0_mll_atConV",
"Tlepton_1_mll_atConV":"lepton_1_mll_atConV",
"Tlepton_0_mll_atPV":"lepton_0_mll_atPV",
"Tlepton_1_mll_atPV":"lepton_1_mll_atPV",



}



plot_dict = {
"6p_both_basic":["Evt_Channel","nJets","nBTags_DL1r_77","HT_all","met_met","jet_sum_DL1r_Continuous"],
"6p_both_jet_pt":["jet_pt[0]","jet_pt[1]","jet_pt[2]","jet_pt[3]","jet_pt[4]","jet_pt[5]"],
"6p_both_jet_eta":["jet_eta[0]","jet_eta[1]","jet_eta[2]","jet_eta[3]","jet_eta[4]","jet_eta[5]"],
"6p_both_lep_pt_eta":["lep_0_pt","lep_1_pt","lep_2_pt","lep_0_eta","lep_1_eta","lep_2_eta"],
"6p_mconly_truth":["Tlepton_0_ID","Tlepton_0_truthClassificationSM4t_bkgFlag","Tlepton_1_ID","Tlepton_1_truthClassificationSM4t_bkgFlag","Tlepton_2_ID","Tlepton_2_truthClassificationSM4t_bkgFlag"],
"2p_mconly_truth":["GenFiltHT","event_BkgCategory"],

"6p_both_el_pt_eta":["el_pt[0]","el_pt[1]","el_pt[2]","el_eta[0]","el_eta[1]","el_eta[2]"],
"6p_both_mu_pt_eta":["mu_pt[0]","mu_pt[1]","mu_pt[2]","mu_eta[0]","mu_eta[1]","mu_eta[2]"],
"3p_both_jet_pt_eta":["jet_pt","jet_eta","leading_bjet_pT"],


}



Dict_NewVar = {"nJets": "both",
                "HT_all": "both",
                "nBTags_DL1r_77": "both",
                "met_met": "both",
                "jet_pt[0]": "both",
                "jet_pt[1]": "both",
                "jet_pt[2]": "both",
                "jet_pt[3]": "both",
                "jet_pt[4]": "both",
                "jet_pt[5]": "both",
                "jet_eta[0]": "both",
                "jet_eta[1]": "both",
                "jet_eta[2]": "both",
                "jet_eta[3]": "both",
                "jet_eta[4]": "both",
                "jet_eta[5]": "both",
                "lep_0_pt": "both",
                "lep_1_pt": "both",
                "lep_2_pt": "both",
                "lep_0_eta": "both",
                "lep_1_eta": "both",
                "lep_2_eta": "both",
                "jet_sum_DL1r_Continuous": "both",
                "Evt_Channel": "both",
                "GenFiltHT": "mc",
                "Tlepton_0_ID": "mc",
                "Tlepton_0_truthClassificationSM4t_bkgFlag": "mc",
                "Tlepton_1_ID": "mc",
                "Tlepton_1_truthClassificationSM4t_bkgFlag": "mc",
                "Tlepton_2_ID": "mc",
                "Tlepton_2_truthClassificationSM4t_bkgFlag": "mc",
                "event_BkgCategory": "mc",

                "jet_pt": "both",
                "jet_eta": "both",
                "el_pt[0]": "both",
                "el_pt[1]": "both",
                "el_pt[2]": "both",
                "el_eta[0]": "both",
                "el_eta[1]": "both",
                "el_eta[2]": "both",
                "mu_pt[0]": "both",
                "mu_pt[1]": "both",
                "mu_pt[2]": "both",
                "mu_eta[0]": "both",
                "mu_eta[1]": "both",
                "mu_eta[2]": "both",
                "leading_bjet_pT": "both",

                "Tlepton_0_mll_atConV": "mc",
                "Tlepton_1_mll_atConV": "mc",
                "Tlepton_0_mll_atPV": "mc",
                "Tlepton_1_mll_atPV": "mc",


            }


def plot(outF):

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
                    make_6plots(outF, Title
                            ,VarList
                            ,"/Users/ploww/dropbox_meng/HEP/Results/BSM4tops/Slides20201106_new_offline_production/results/"+sel+"/"
                            )
                elif "2p" in plot:
                    make_2plots(outF, Title
                            ,VarList
                            ,"/Users/ploww/dropbox_meng/HEP/Results/BSM4tops/Slides20201106_new_offline_production/results/"+sel+"/"
                            )
                elif "3p" in plot:
                    make_3plots(outF, Title
                            ,VarList
                            ,"/Users/ploww/dropbox_meng/HEP/Results/BSM4tops/Slides20201106_new_offline_production/results/"+sel+"/"
                            )

























#
