# Python script to hold replacement model mapping for different analyses
from collections import OrderedDict as od

# Add analyses to globalReplacementMap. See "STXS" as an example
globalReplacementMap = od()

# Example analysis which with cats Untagged_Tag0,VBF_Tag0
globalReplacementMap['example'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['example']['procWV'] = "GG2H"
globalReplacementMap['example']['catWV'] = "Untagged_Tag0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['example']['procRVMap'] = od()
globalReplacementMap["example"]["procRVMap"]["Untagged_Tag0"] = "GG2H"
globalReplacementMap["example"]["procRVMap"]["VBF_Tag0"] = "VBF"
# Replacement category for RV fit
globalReplacementMap["example"]["catRVMap"] = od()
globalReplacementMap["example"]["catRVMap"]["Untagged_Tag0"] = "Untagged_Tag0"
globalReplacementMap["example"]["catRVMap"]["VBF_Tag0"] = "VBF_Tag0"


# STXS analysis
globalReplacementMap['STXS'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['STXS']['procWV'] = "ggh"
globalReplacementMap['STXS']['catWV'] = "RECO_0J_PTH_GT10_Tag1"
# For RIGHT VERTEX SCENARIO:
#  * default mapping is to use diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['STXS']['procRVMap'] = od()
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_200_300_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_300_450_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_450_650_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_PTH_GT650_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_THQ_LEP"] = "thq"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag2"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_200_300_Tag3"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag2"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_HAD_PTH_GT300_Tag3"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag3"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_200_300_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT300_Tag0"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_TTH_LEP_PTH_GT300_Tag1"] = "tth"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "ggh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "vbf"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag0"] = "zh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_VH_MET_Tag1"] = "zh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_HIGH_Tag0"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_HIGH_Tag1"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_HIGH_Tag2"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_LOW_Tag0"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_LOW_Tag1"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_LOW_Tag2"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_0_75_Tag0"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_0_75_Tag1"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_75_150_Tag0"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_75_150_Tag1"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_WH_LEP_PTV_GT150_Tag0"] = "wh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag0"] = "zh"
globalReplacementMap["STXS"]["procRVMap"]["RECO_ZH_LEP_Tag1"] = "zh"
# Replacement category for RV fit
globalReplacementMap["STXS"]["catRVMap"] = od()
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag0"] = "RECO_0J_PTH_0_10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag1"] = "RECO_0J_PTH_0_10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_0_10_Tag2"] = "RECO_0J_PTH_0_10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag0"] = "RECO_0J_PTH_GT10_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag1"] = "RECO_0J_PTH_GT10_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_0J_PTH_GT10_Tag2"] = "RECO_0J_PTH_GT10_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag0"] = "RECO_1J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag1"] = "RECO_1J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_0_60_Tag2"] = "RECO_1J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag0"] = "RECO_1J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag1"] = "RECO_1J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_120_200_Tag2"] = "RECO_1J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag0"] = "RECO_1J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag1"] = "RECO_1J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_1J_PTH_60_120_Tag2"] = "RECO_1J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag0"] = "RECO_GE2J_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag1"] = "RECO_GE2J_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_0_60_Tag2"] = "RECO_GE2J_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag0"] = "RECO_GE2J_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag1"] = "RECO_GE2J_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_120_200_Tag2"] = "RECO_GE2J_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag0"] = "RECO_GE2J_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag1"] = "RECO_GE2J_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_GE2J_PTH_60_120_Tag2"] = "RECO_GE2J_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag0"] = "RECO_PTH_200_300_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_200_300_Tag1"] = "RECO_PTH_200_300_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag0"] = "RECO_PTH_300_450_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_300_450_Tag1"] = "RECO_PTH_300_450_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_450_650_Tag0"] = "RECO_PTH_450_650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_PTH_GT650_Tag0"] = "RECO_PTH_GT650_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_THQ_LEP"] = "RECO_THQ_LEP"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag0"] = "RECO_TTH_HAD_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag1"] = "RECO_TTH_HAD_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag2"] = "RECO_TTH_HAD_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_0_60_Tag3"] = "RECO_TTH_HAD_PTH_0_60_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag0"] = "RECO_TTH_HAD_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag1"] = "RECO_TTH_HAD_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag2"] = "RECO_TTH_HAD_PTH_120_200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_120_200_Tag3"] = "RECO_TTH_HAD_PTH_120_200_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag0"] = "RECO_TTH_HAD_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag1"] = "RECO_TTH_HAD_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag2"] = "RECO_TTH_HAD_PTH_60_120_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_60_120_Tag3"] = "RECO_TTH_HAD_PTH_60_120_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag0"] = "RECO_TTH_HAD_PTH_GT200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag1"] = "RECO_TTH_HAD_PTH_GT200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag2"] = "RECO_TTH_HAD_PTH_GT200_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_HAD_PTH_GT200_Tag3"] = "RECO_TTH_HAD_PTH_GT200_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag0"] = "RECO_TTH_LEP_PTH_0_60_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag1"] = "RECO_TTH_LEP_PTH_0_60_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag2"] = "RECO_TTH_LEP_PTH_0_60_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_0_60_Tag3"] = "RECO_TTH_LEP_PTH_0_60_Tag3"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag0"] = "RECO_TTH_LEP_PTH_120_200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_120_200_Tag1"] = "RECO_TTH_LEP_PTH_120_200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag0"] = "RECO_TTH_LEP_PTH_60_120_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_60_120_Tag1"] = "RECO_TTH_LEP_PTH_60_120_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag0"] = "RECO_TTH_LEP_PTH_GT200_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_TTH_LEP_PTH_GT200_Tag1"] = "RECO_TTH_LEP_PTH_GT200_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag0"] = "RECO_VBFLIKEGGH_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFLIKEGGH_Tag1"] = "RECO_VBFLIKEGGH_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag0"] = "RECO_VBFTOPO_BSM_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_BSM_Tag1"] = "RECO_VBFTOPO_BSM_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3VETO_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"] = "RECO_VBFTOPO_JET3_HIGHMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag0"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_JET3_LOWMJJ_Tag1"] = "RECO_VBFTOPO_JET3_LOWMJJ_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag0"] = "RECO_VBFTOPO_VHHAD_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VBFTOPO_VHHAD_Tag1"] = "RECO_VBFTOPO_VHHAD_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag0"] = "RECO_VH_MET_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_VH_MET_Tag1"] = "RECO_VH_MET_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_HIGH_Tag0"] = "RECO_WH_LEP_HIGH_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_HIGH_Tag1"] = "RECO_WH_LEP_HIGH_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_HIGH_Tag2"] = "RECO_WH_LEP_HIGH_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_LOW_Tag0"] = "RECO_WH_LEP_LOW_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_LOW_Tag1"] = "RECO_WH_LEP_LOW_Tag1"
globalReplacementMap["STXS"]["catRVMap"]["RECO_WH_LEP_LOW_Tag2"] = "RECO_WH_LEP_LOW_Tag2"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag0"] = "RECO_ZH_LEP_Tag0"
globalReplacementMap["STXS"]["catRVMap"]["RECO_ZH_LEP_Tag1"] = "RECO_ZH_LEP_Tag1"

globalReplacementMap['STXSmerged'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['STXSmerged']['procWV'] = "ggh"
globalReplacementMap['STXSmerged']['catWV'] = "Untagged_Tag0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['STXSmerged']['procRVMap'] = od()
globalReplacementMap["STXSmerged"]["procRVMap"]["Untagged_Tag0"] = "ggh"
globalReplacementMap["STXSmerged"]["procRVMap"]["Untagged_Tag1"] = "ggh"
globalReplacementMap["STXSmerged"]["procRVMap"]["Untagged_Tag2"] = "ggh"
globalReplacementMap["STXSmerged"]["procRVMap"]["VBF_Tag0"] = "vbf"
globalReplacementMap["STXSmerged"]["procRVMap"]["VBF_Tag1"] = "vbf"
# Replacement category for RV fit
globalReplacementMap["STXSmerged"]["catRVMap"] = od()
globalReplacementMap["STXSmerged"]["catRVMap"]["Untagged_Tag0"] = "Untagged_Tag0"
globalReplacementMap["STXSmerged"]["catRVMap"]["Untagged_Tag1"] = "Untagged_Tag0"
globalReplacementMap["STXSmerged"]["catRVMap"]["Untagged_Tag2"] = "Untagged_Tag0"
globalReplacementMap["STXSmerged"]["catRVMap"]["VBF_Tag0"] = "VBF_Tag0"
globalReplacementMap["STXSmerged"]["catRVMap"]["VBF_Tag1"] = "VBF_Tag0"

globalReplacementMap['Untagged4'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['Untagged4']['procWV'] = "ggh"
globalReplacementMap['Untagged4']['catWV'] = "UntaggedTag_0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['Untagged4']['procRVMap'] = od()
globalReplacementMap["Untagged4"]["procRVMap"]["UntaggedTag_0"] = "ggh"
globalReplacementMap["Untagged4"]["procRVMap"]["UntaggedTag_1"] = "ggh"
globalReplacementMap["Untagged4"]["procRVMap"]["UntaggedTag_2"] = "ggh"
globalReplacementMap["Untagged4"]["procRVMap"]["UntaggedTag_3"] = "ggh"
# Replacement category for RV fit
globalReplacementMap["Untagged4"]["catRVMap"] = od()
globalReplacementMap["Untagged4"]["catRVMap"]["UntaggedTag_0"] = "UntaggedTag_0"
globalReplacementMap["Untagged4"]["catRVMap"]["UntaggedTag_1"] = "UntaggedTag_0"
globalReplacementMap["Untagged4"]["catRVMap"]["UntaggedTag_2"] = "UntaggedTag_0"
globalReplacementMap["Untagged4"]["catRVMap"]["UntaggedTag_3"] = "UntaggedTag_0"


#Untag + VBF
globalReplacementMap['UntagVBF'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['UntagVBF']['procWV'] = "ggh"
globalReplacementMap['UntagVBF']['catWV'] = "UntaggedTag_0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['UntagVBF']['procRVMap'] = od()
globalReplacementMap["UntagVBF"]["procRVMap"]["UntaggedTag_0"] = "ggh"
globalReplacementMap["UntagVBF"]["procRVMap"]["UntaggedTag_1"] = "ggh"
globalReplacementMap["UntagVBF"]["procRVMap"]["UntaggedTag_2"] = "ggh"
globalReplacementMap["UntagVBF"]["procRVMap"]["UntaggedTag_3"] = "ggh"
globalReplacementMap["UntagVBF"]["procRVMap"]["VBFTag_0"] = "vbf" #"ggh"
globalReplacementMap["UntagVBF"]["procRVMap"]["VBFTag_1"] = "vbf" #"ggh"
globalReplacementMap["UntagVBF"]["procRVMap"]["VBFTag_2"] = "vbf" #"ggh"
# Replacement category for RV fit
globalReplacementMap["UntagVBF"]["catRVMap"] = od()
globalReplacementMap["UntagVBF"]["catRVMap"]["UntaggedTag_0"] = "UntaggedTag_0"
globalReplacementMap["UntagVBF"]["catRVMap"]["UntaggedTag_1"] = "UntaggedTag_0"
globalReplacementMap["UntagVBF"]["catRVMap"]["UntaggedTag_2"] = "UntaggedTag_0"
globalReplacementMap["UntagVBF"]["catRVMap"]["UntaggedTag_3"] = "UntaggedTag_0"
globalReplacementMap["UntagVBF"]["catRVMap"]["VBFTag_0"] = "UntaggedTag_0"
globalReplacementMap["UntagVBF"]["catRVMap"]["VBFTag_1"] = "UntaggedTag_0"
globalReplacementMap["UntagVBF"]["catRVMap"]["VBFTag_2"] = "UntaggedTag_0"

#Untag + VBF: (EB+EB) and !(EB+EB)
globalReplacementMap['UntagVBF_TaoCats'] = od()
# For WRONG VERTEX SCENARIO:
#  * single proc x cat for wrong vertex since for dZ > 1cm shape independent of proc x cat
#  * use proc x cat with highest number of WV events
globalReplacementMap['UntagVBF_TaoCats']['procWV'] = "ggh"
globalReplacementMap['UntagVBF_TaoCats']['catWV'] = "BothEBUntaggedTag_0"
# For RIGHT VERTEX SCENARIO:
#  * default you should add is diagonal process from given category 
#  * if few events in diagonal process then may need to change the category aswell (see catRVMap)
#  * map must contain entry for all cats being processed (for replacement proc and cat)
globalReplacementMap['UntagVBF_TaoCats']['procRVMap'] = od()
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["BothEBUntaggedTag_0"] = "ggh"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["BothEBUntaggedTag_1"] = "ggh"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["BothEBUntaggedTag_2"] = "ggh"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["BothEBUntaggedTag_3"] = "ggh"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["NotEBEBUntaggedTag_0"] = "ggh"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["NotEBEBUntaggedTag_1"] = "ggh"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["NotEBEBUntaggedTag_2"] = "ggh"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["BothEBVBFTag_0"] = "vbf"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["BothEBVBFTag_1"] = "vbf"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["BothEBVBFTag_2"] = "vbf"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["NotEBEBVBFTag_0"] = "vbf"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["NotEBEBVBFTag_1"] = "vbf"
globalReplacementMap["UntagVBF_TaoCats"]["procRVMap"]["NotEBEBVBFTag_2"] = "vbf"
# Replacement category for RV fit
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"] = od()
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["BothEBUntaggedTag_0"] = "BothEBUntaggedTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["BothEBUntaggedTag_1"] = "BothEBUntaggedTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["BothEBUntaggedTag_2"] = "BothEBUntaggedTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["BothEBUntaggedTag_3"] = "BothEBUntaggedTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["NotEBEBUntaggedTag_0"] = "NotEBEBUntaggedTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["NotEBEBUntaggedTag_1"] = "NotEBEBUntaggedTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["NotEBEBUntaggedTag_2"] = "NotEBEBUntaggedTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["BothEBVBFTag_0"] = "BothEBVBFTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["BothEBVBFTag_1"] = "BothEBVBFTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["BothEBVBFTag_2"] = "BothEBVBFTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["NotEBEBVBFTag_0"] = "NotEBEBVBFTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["NotEBEBVBFTag_1"] = "NotEBEBVBFTag_0"
globalReplacementMap["UntagVBF_TaoCats"]["catRVMap"]["NotEBEBVBFTag_2"] = "NotEBEBVBFTag_0"
