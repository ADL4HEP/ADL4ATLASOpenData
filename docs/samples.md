# Samples and merge groups

Summary of `config/samples/*.yaml`.
MC normalisation per sample: histograms x 1/(sumw x eff); XSection and Lumi
(10064 pb^-1) are applied per event in the ADL. Data: no scaling.

## HZZAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_HZZ.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| Higgs | VBFH125_ZZ4lep | 344235 | `4lep/MC/mc_344235.VBFH125_ZZ4lep.4lep.root` | 0.0004633012 | 3680490.83243 | 1.0 |
| Higgs | WH125_ZZ4lep | 341964 | `4lep/MC/mc_341964.WH125_ZZ4lep.4lep.root` | 0.0003769 | 149400.0 | 1.0 |
| Higgs | ZH125_ZZ4lep | 341947 | `4lep/MC/mc_341947.ZH125_ZZ4lep.4lep.root` | 2.1424784e-06 | 150000.0 | 1.0 |
| Higgs | ggH125_ZZ4lep | 345060 | `4lep/MC/mc_345060.ggH125_ZZ4lep.4lep.root` | 0.0060239 | 27881776.6536 | 1.0 |
| V | WlvZqq | 363489 | `4lep/MC/mc_363489.WlvZqq.4lep.root` | 11.42 | 1111991.15979 | 1.0 |
| V | Wminusenu | 361103 | `4lep/MC/mc_361103.Wminusenu.4lep.root` | 8579.63498 | 247538642447.0 | 1.0 |
| V | Wminusmunu | 361104 | `4lep/MC/mc_361104.Wminusmunu.4lep.root` | 8579.63498 | 264338188182.0 | 1.0 |
| V | Wminustaunu | 361105 | `4lep/MC/mc_361105.Wminustaunu.4lep.root` | 8579.63498 | 165195850954.0 | 1.0 |
| V | Wplusenu | 361100 | `4lep/MC/mc_361100.Wplusenu.4lep.root` | 11500.4632 | 473389396815.0 | 1.0 |
| V | Wplusmunu | 361101 | `4lep/MC/mc_361101.Wplusmunu.4lep.root` | 11500.4632 | 446507925520.0 | 1.0 |
| V | Wplustaunu | 361102 | `4lep/MC/mc_361102.Wplustaunu.4lep.root` | 11500.4632 | 670928468875.0 | 1.0 |
| V | WplvWmqq | 363360 | `4lep/MC/mc_363360.WplvWmqq.4lep.root` | 24.724 | 1069526.41899 | 1.0 |
| V | WpqqWmlv | 363359 | `4lep/MC/mc_363359.WpqqWmlv.4lep.root` | 24.708 | 998250.783475 | 1.0 |
| V | WqqZll | 363358 | `4lep/MC/mc_363358.WqqZll.4lep.root` | 3.4328 | 241438.72705 | 1.0 |
| V | Zee | 361106 | `4lep/MC/mc_361106.Zee.4lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| V | Zmumu | 361107 | `4lep/MC/mc_361107.Zmumu.4lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| V | Ztautau | 361108 | `4lep/MC/mc_361108.Ztautau.4lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| V | lllv | 363491 | `4lep/MC/mc_363491.lllv.4lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| V | lvvv | 363493 | `4lep/MC/mc_363493.lvvv.4lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| V | single_antitop_schan | 410026 | `4lep/MC/mc_410026.single_antitop_schan.4lep.root` | 1.288662 | 995400.0 | 1.0 |
| V | single_antitop_tchan | 410012 | `4lep/MC/mc_410012.single_antitop_tchan.4lep.root` | 26.276 | 4989800.0 | 1.0 |
| V | single_antitop_wtchan | 410014 | `4lep/MC/mc_410014.single_antitop_wtchan.4lep.root` | 35.824406 | 4945600.0 | 1.0 |
| V | single_top_schan | 410025 | `4lep/MC/mc_410025.single_top_schan.4lep.root` | 2.06121 | 997800.0 | 1.0 |
| V | single_top_tchan | 410011 | `4lep/MC/mc_410011.single_top_tchan.4lep.root` | 44.152 | 4986200.0 | 1.0 |
| V | single_top_wtchan | 410013 | `4lep/MC/mc_410013.single_top_wtchan.4lep.root` | 35.845486 | 4865800.0 | 1.0 |
| V | ttbar_lep | 410000 | `4lep/MC/mc_410000.ttbar_lep.4lep.root` | 452.693559 | 49386600.0 | 1.0 |
| ZZ | ZqqZll | 363356 | `4lep/MC/mc_363356.ZqqZll.4lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| ZZ | llll | 363490 | `4lep/MC/mc_363490.llll.4lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| ZZ | llvv | 363492 | `4lep/MC/mc_363492.llvv.4lep.root` | 12.466 | 5039259.9696 | 1.0 |
| data | data_A |  | `4lep/Data/data_A.4lep.root` |  |  |  |
| data | data_B |  | `4lep/Data/data_B.4lep.root` |  |  |  |
| data | data_C |  | `4lep/Data/data_C.4lep.root` |  |  |  |
| data | data_D |  | `4lep/Data/data_D.4lep.root` |  |  |  |

## SUSYAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_SUSY.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| Wjets | Wenu_PTV0_70_BFilter | 364172 | `2lep/MC/mc_364172.Wenu_PTV0_70_BFilter.2lep.root` | 832.203758 | 10407897.8772 | 1.0 |
| Wjets | Wenu_PTV0_70_CFilterBVeto | 364171 | `2lep/MC/mc_364171.Wenu_PTV0_70_CFilterBVeto.2lep.root` | 2430.656322 | 5647044.71225 | 1.0 |
| Wjets | Wenu_PTV0_70_CVetoBVeto | 364170 | `2lep/MC/mc_364170.Wenu_PTV0_70_CVetoBVeto.2lep.root` | 15324.216356 | 16615214.8608 | 1.0 |
| Wjets | Wenu_PTV1000 | 364183 | `2lep/MC/mc_364183.Wenu_PTV1000_E_CMS.2lep.root` | 1.197518 | 4075236.23897 | 1.0 |
| Wjets | Wenu_PTV140_280_BFilter | 364178 | `2lep/MC/mc_364178.Wenu_PTV140_280_BFilter.2lep.root` | 35.917295 | 7327201.08884 | 1.0 |
| Wjets | Wenu_PTV140_280_CFilterBVeto | 364177 | `2lep/MC/mc_364177.Wenu_PTV140_280_CFilterBVeto.2lep.root` | 96.277568 | 5263243.42582 | 1.0 |
| Wjets | Wenu_PTV140_280_CVetoBVeto | 364176 | `2lep/MC/mc_364176.Wenu_PTV140_280_CVetoBVeto.2lep.root` | 197.343129 | 6121546.03361 | 1.0 |
| Wjets | Wenu_PTV280_500_BFilter | 364181 | `2lep/MC/mc_364181.Wenu_PTV280_500_BFilter.2lep.root` | 9.586345 | 2835314.68179 | 1.0 |
| Wjets | Wenu_PTV280_500_CFilterBVeto | 364180 | `2lep/MC/mc_364180.Wenu_PTV280_500_CFilterBVeto.2lep.root` | 22.36999 | 2778654.28759 | 1.0 |
| Wjets | Wenu_PTV280_500_CVetoBVeto | 364179 | `2lep/MC/mc_364179.Wenu_PTV280_500_CVetoBVeto.2lep.root` | 38.340533 | 4312357.01458 | 1.0 |
| Wjets | Wenu_PTV500_1000 | 364182 | `2lep/MC/mc_364182.Wenu_PTV500_1000.2lep.root` | 14.598599 | 6003269.52809 | 1.0 |
| Wjets | Wenu_PTV70_140_BFilter | 364175 | `2lep/MC/mc_364175.Wenu_PTV70_140_BFilter.2lep.root` | 94.875534 | 3980401.78673 | 1.0 |
| Wjets | Wenu_PTV70_140_CFilterBVeto | 364174 | `2lep/MC/mc_364174.Wenu_PTV70_140_CFilterBVeto.2lep.root` | 223.63946 | 3661915.17878 | 1.0 |
| Wjets | Wenu_PTV70_140_CVetoBVeto | 364173 | `2lep/MC/mc_364173.Wenu_PTV70_140_CVetoBVeto.2lep.root` | 618.6882 | 5098540.19503 | 1.0 |
| Wjets | Wmunu_PTV0_70_BFilter | 364158 | `2lep/MC/mc_364158.Wmunu_PTV0_70_BFilter.2lep.root` | 828.465384 | 10403012.6599 | 1.0 |
| Wjets | Wmunu_PTV0_70_CFilterBVeto | 364157 | `2lep/MC/mc_364157.Wmunu_PTV0_70_CFilterBVeto.2lep.root` | 2431.204019 | 5643599.11526 | 1.0 |
| Wjets | Wmunu_PTV0_70_CVetoBVeto | 364156 | `2lep/MC/mc_364156.Wmunu_PTV0_70_CVetoBVeto.2lep.root` | 15317.171239 | 16619290.3298 | 1.0 |
| Wjets | Wmunu_PTV1000 | 364169 | `2lep/MC/mc_364169.Wmunu_PTV1000_E_CMS.2lep.root` | 1.198003 | 4068015.22447 | 1.0 |
| Wjets | Wmunu_PTV140_280_BFilter | 364164 | `2lep/MC/mc_364164.Wmunu_PTV140_280_BFilter.2lep.root` | 36.348467 | 7271557.26566 | 1.0 |
| Wjets | Wmunu_PTV140_280_CFilterBVeto | 364163 | `2lep/MC/mc_364163.Wmunu_PTV140_280_CFilterBVeto.2lep.root` | 96.233222 | 5260811.17463 | 1.0 |
| Wjets | Wmunu_PTV140_280_CVetoBVeto | 364162 | `2lep/MC/mc_364162.Wmunu_PTV140_280_CVetoBVeto.2lep.root` | 198.635592 | 6155495.28527 | 1.0 |
| Wjets | Wmunu_PTV280_500_BFilter | 364167 | `2lep/MC/mc_364167.Wmunu_PTV280_500_BFilter.2lep.root` | 8.768196 | 2835707.22044 | 1.0 |
| Wjets | Wmunu_PTV280_500_CFilterBVeto | 364166 | `2lep/MC/mc_364166.Wmunu_PTV280_500_CFilterBVeto.2lep.root` | 22.395647 | 2783968.68238 | 1.0 |
| Wjets | Wmunu_PTV280_500_CVetoBVeto | 364165 | `2lep/MC/mc_364165.Wmunu_PTV280_500_CVetoBVeto.2lep.root` | 38.299835 | 4325283.67358 | 1.0 |
| Wjets | Wmunu_PTV500_1000 | 364168 | `2lep/MC/mc_364168.Wmunu_PTV500_1000.2lep.root` | 14.558821 | 5941704.99235 | 1.0 |
| Wjets | Wmunu_PTV70_140_BFilter | 364161 | `2lep/MC/mc_364161.Wmunu_PTV70_140_BFilter.2lep.root` | 76.213179 | 7990084.35926 | 1.0 |
| Wjets | Wmunu_PTV70_140_CFilterBVeto | 364160 | `2lep/MC/mc_364160.Wmunu_PTV70_140_CFilterBVeto.2lep.root` | 225.006704 | 3693885.78953 | 1.0 |
| Wjets | Wmunu_PTV70_140_CVetoBVeto | 364159 | `2lep/MC/mc_364159.Wmunu_PTV70_140_CVetoBVeto.2lep.root` | 617.439593 | 5418398.88082 | 1.0 |
| Wjets | Wtaunu_PTV0_70_BFilter | 364186 | `2lep/MC/mc_364186.Wtaunu_PTV0_70_BFilter.2lep.root` | 837.531038 | 10498770.1084 | 1.0 |
| Wjets | Wtaunu_PTV0_70_CFilterBVeto | 364185 | `2lep/MC/mc_364185.Wtaunu_PTV0_70_CFilterBVeto.2lep.root` | 2443.425881 | 5671521.55269 | 1.0 |
| Wjets | Wtaunu_PTV0_70_CVetoBVeto | 364184 | `2lep/MC/mc_364184.Wtaunu_PTV0_70_CVetoBVeto.2lep.root` | 15324.887336 | 11929044.1188 | 1.0 |
| Wjets | Wtaunu_PTV1000 | 364197 | `2lep/MC/mc_364197.Wtaunu_PTV1000_E_CMS.2lep.root` | 1.197324 | 4057477.95297 | 1.0 |
| Wjets | Wtaunu_PTV140_280_BFilter | 364192 | `2lep/MC/mc_364192.Wtaunu_PTV140_280_BFilter.2lep.root` | 34.639523 | 7291603.73991 | 1.0 |
| Wjets | Wtaunu_PTV140_280_CFilterBVeto | 364191 | `2lep/MC/mc_364191.Wtaunu_PTV140_280_CFilterBVeto.2lep.root` | 93.808553 | 5085280.31607 | 1.0 |
| Wjets | Wtaunu_PTV140_280_CVetoBVeto | 364190 | `2lep/MC/mc_364190.Wtaunu_PTV140_280_CVetoBVeto.2lep.root` | 197.370776 | 6166514.76606 | 1.0 |
| Wjets | Wtaunu_PTV280_500_BFilter | 364195 | `2lep/MC/mc_364195.Wtaunu_PTV280_500_BFilter.2lep.root` | 9.490847 | 2830341.62344 | 1.0 |
| Wjets | Wtaunu_PTV280_500_CFilterBVeto | 364194 | `2lep/MC/mc_364194.Wtaunu_PTV280_500_CFilterBVeto.2lep.root` | 22.268425 | 2772305.06916 | 1.0 |
| Wjets | Wtaunu_PTV280_500_CVetoBVeto | 364193 | `2lep/MC/mc_364193.Wtaunu_PTV280_500_CVetoBVeto.2lep.root` | 38.34009 | 4322848.66983 | 1.0 |
| Wjets | Wtaunu_PTV500_1000 | 364196 | `2lep/MC/mc_364196.Wtaunu_PTV500_1000.2lep.root` | 14.60345 | 5932750.60186 | 1.0 |
| Wjets | Wtaunu_PTV70_140_BFilter | 364189 | `2lep/MC/mc_364189.Wtaunu_PTV70_140_BFilter.2lep.root` | 95.365521 | 3969118.20687 | 1.0 |
| Wjets | Wtaunu_PTV70_140_CFilterBVeto | 364188 | `2lep/MC/mc_364188.Wtaunu_PTV70_140_CFilterBVeto.2lep.root` | 222.595303 | 3719117.16117 | 1.0 |
| Wjets | Wtaunu_PTV70_140_CVetoBVeto | 364187 | `2lep/MC/mc_364187.Wtaunu_PTV70_140_CVetoBVeto.2lep.root` | 620.166885 | 5427023.47527 | 1.0 |
| Zjets | Zee_PTV0_70_BFilter | 364116 | `2lep/MC/mc_364116.Zee_PTV0_70_BFilter.2lep.root` | 127.0857614 | 4053053.52848 | 1.0 |
| Zjets | Zee_PTV0_70_CFilterBVeto | 364115 | `2lep/MC/mc_364115.Zee_PTV0_70_CFilterBVeto.2lep.root` | 219.9958116 | 2839137.81561 | 1.0 |
| Zjets | Zee_PTV0_70_CVetoBVeto | 364114 | `2lep/MC/mc_364114.Zee_PTV0_70_CVetoBVeto.2lep.root` | 1587.021595 | 5307644.52827 | 1.0 |
| Zjets | Zee_PTV1000 | 364127 | `2lep/MC/mc_364127.Zee_PTV1000_E_CMS.2lep.root` | 0.145046125 | 994142.027341 | 1.0 |
| Zjets | Zee_PTV140_280_BFilter | 364122 | `2lep/MC/mc_364122.Zee_PTV140_280_BFilter.2lep.root` | 6.081254464 | 3396476.98264 | 1.0 |
| Zjets | Zee_PTV140_280_CFilterBVeto | 364121 | `2lep/MC/mc_364121.Zee_PTV140_280_CFilterBVeto.2lep.root` | 9.237605979 | 1976624.57582 | 1.0 |
| Zjets | Zee_PTV140_280_CVetoBVeto | 364120 | `2lep/MC/mc_364120.Zee_PTV140_280_CVetoBVeto.2lep.root` | 24.44184978 | 2966342.61469 | 1.0 |
| Zjets | Zee_PTV280_500_BFilter | 364125 | `2lep/MC/mc_364125.Zee_PTV280_500_BFilter.2lep.root` | 1.49219843 | 1854184.55614 | 1.0 |
| Zjets | Zee_PTV280_500_CFilterBVeto | 364124 | `2lep/MC/mc_364124.Zee_PTV280_500_CFilterBVeto.2lep.root` | 2.249186051 | 908261.497964 | 1.0 |
| Zjets | Zee_PTV280_500_CVetoBVeto | 364123 | `2lep/MC/mc_364123.Zee_PTV280_500_CVetoBVeto.2lep.root` | 4.796836771 | 1622207.75969 | 1.0 |
| Zjets | Zee_PTV500_1000 | 364126 | `2lep/MC/mc_364126.Zee_PTV500_1000.2lep.root` | 1.76415092 | 2942740.91362 | 1.0 |
| Zjets | Zee_PTV70_140_BFilter | 364119 | `2lep/MC/mc_364119.Zee_PTV70_140_BFilter.2lep.root` | 12.73880801 | 2043192.28295 | 1.0 |
| Zjets | Zee_PTV70_140_CFilterBVeto | 364118 | `2lep/MC/mc_364118.Zee_PTV70_140_CFilterBVeto.2lep.root` | 20.3159891 | 715162.089738 | 1.0 |
| Zjets | Zee_PTV70_140_CVetoBVeto | 364117 | `2lep/MC/mc_364117.Zee_PTV70_140_CVetoBVeto.2lep.root` | 74.90381742 | 2164248.98844 | 1.0 |
| Zjets | Zmumu_PTV0_70_BFilter | 364102 | `2lep/MC/mc_364102.Zmumu_PTV0_70_BFilter.2lep.root` | 127.1303743 | 4078710.85229 | 1.0 |
| Zjets | Zmumu_PTV0_70_CFilterBVeto | 364101 | `2lep/MC/mc_364101.Zmumu_PTV0_70_CFilterBVeto.2lep.root` | 219.4826028 | 2834664.0856 | 1.0 |
| Zjets | Zmumu_PTV0_70_CVetoBVeto | 364100 | `2lep/MC/mc_364100.Zmumu_PTV0_70_CVetoBVeto.2lep.root` | 1588.474174 | 5319367.44387 | 1.0 |
| Zjets | Zmumu_PTV1000 | 364113 | `2lep/MC/mc_364113.Zmumu_PTV1000_E_CMS.2lep.root` | 0.14392476 | 1007977.7298 | 1.0 |
| Zjets | Zmumu_PTV140_280_BFilter | 364108 | `2lep/MC/mc_364108.Zmumu_PTV140_280_BFilter.2lep.root` | 6.076989874 | 3441102.46707 | 1.0 |
| Zjets | Zmumu_PTV140_280_CFilterBVeto | 364107 | `2lep/MC/mc_364107.Zmumu_PTV140_280_CFilterBVeto.2lep.root` | 9.145130781 | 1961708.95573 | 1.0 |
| Zjets | Zmumu_PTV140_280_CVetoBVeto | 364106 | `2lep/MC/mc_364106.Zmumu_PTV140_280_CVetoBVeto.2lep.root` | 23.43735064 | 2940060.231 | 1.0 |
| Zjets | Zmumu_PTV280_500_BFilter | 364111 | `2lep/MC/mc_364111.Zmumu_PTV280_500_BFilter.2lep.root` | 1.468357812 | 1854208.83636 | 1.0 |
| Zjets | Zmumu_PTV280_500_CFilterBVeto | 364110 | `2lep/MC/mc_364110.Zmumu_PTV280_500_CFilterBVeto.2lep.root` | 2.214827532 | 906361.047826 | 1.0 |
| Zjets | Zmumu_PTV280_500_CVetoBVeto | 364109 | `2lep/MC/mc_364109.Zmumu_PTV280_500_CVetoBVeto.2lep.root` | 4.657367095 | 1705022.00352 | 1.0 |
| Zjets | Zmumu_PTV500_1000 | 364112 | `2lep/MC/mc_364112.Zmumu_PTV500_1000.2lep.root` | 1.74260121 | 2944710.97814 | 1.0 |
| Zjets | Zmumu_PTV70_140_BFilter | 364105 | `2lep/MC/mc_364105.Zmumu_PTV70_140_BFilter.2lep.root` | 12.50542972 | 2053470.59226 | 1.0 |
| Zjets | Zmumu_PTV70_140_CFilterBVeto | 364104 | `2lep/MC/mc_364104.Zmumu_PTV70_140_CFilterBVeto.2lep.root` | 20.90606833 | 722736.703003 | 1.0 |
| Zjets | Zmumu_PTV70_140_CVetoBVeto | 364103 | `2lep/MC/mc_364103.Zmumu_PTV70_140_CVetoBVeto.2lep.root` | 73.36940289 | 2143575.01278 | 1.0 |
| Zjets | Ztautau_PTV0_70_BFilter | 364130 | `2lep/MC/mc_364130.Ztautau_PTV0_70_BFilter.2lep.root` | 127.0915597 | 4060541.5209 | 1.0 |
| Zjets | Ztautau_PTV0_70_CFilterBVeto | 364129 | `2lep/MC/mc_364129.Ztautau_PTV0_70_CFilterBVeto.2lep.root` | 211.7088872 | 2848153.01809 | 1.0 |
| Zjets | Ztautau_PTV0_70_CVetoBVeto | 364128 | `2lep/MC/mc_364128.Ztautau_PTV0_70_CVetoBVeto.2lep.root` | 1612.531483 | 5261983.52635 | 1.0 |
| Zjets | Ztautau_PTV1000 | 364141 | `2lep/MC/mc_364141.Ztautau_PTV1000_E_CMS.2lep.root` | 0.144568326 | 997974.838867 | 1.0 |
| Zjets | Ztautau_PTV140_280_BFilter | 364136 | `2lep/MC/mc_364136.Ztautau_PTV140_280_BFilter.2lep.root` | 6.192971739 | 3430451.22731 | 1.0 |
| Zjets | Ztautau_PTV140_280_CFilterBVeto | 364135 | `2lep/MC/mc_364135.Ztautau_PTV140_280_CFilterBVeto.2lep.root` | 9.301821784 | 1983172.64602 | 1.0 |
| Zjets | Ztautau_PTV140_280_CVetoBVeto | 364134 | `2lep/MC/mc_364134.Ztautau_PTV140_280_CVetoBVeto.2lep.root` | 24.57266372 | 2969289.71879 | 1.0 |
| Zjets | Ztautau_PTV280_500_BFilter | 364139 | `2lep/MC/mc_364139.Ztautau_PTV280_500_BFilter.2lep.root` | 1.491840072 | 1853029.9701 | 1.0 |
| Zjets | Ztautau_PTV280_500_CFilterBVeto | 364138 | `2lep/MC/mc_364138.Ztautau_PTV280_500_CFilterBVeto.2lep.root` | 2.236223236 | 905387.206237 | 1.0 |
| Zjets | Ztautau_PTV280_500_CVetoBVeto | 364137 | `2lep/MC/mc_364137.Ztautau_PTV280_500_CVetoBVeto.2lep.root` | 4.759698353 | 1656090.74518 | 1.0 |
| Zjets | Ztautau_PTV500_1000 | 364140 | `2lep/MC/mc_364140.Ztautau_PTV500_1000.2lep.root` | 1.76249325 | 2923750.21933 | 1.0 |
| Zjets | Ztautau_PTV70_140_BFilter | 364133 | `2lep/MC/mc_364133.Ztautau_PTV70_140_BFilter.2lep.root` | 11.96510571 | 2071490.99782 | 1.0 |
| Zjets | Ztautau_PTV70_140_CFilterBVeto | 364132 | `2lep/MC/mc_364132.Ztautau_PTV70_140_CFilterBVeto.2lep.root` | 20.50813626 | 717613.996532 | 1.0 |
| Zjets | Ztautau_PTV70_140_CVetoBVeto | 364131 | `2lep/MC/mc_364131.Ztautau_PTV70_140_CVetoBVeto.2lep.root` | 74.70740605 | 2168444.60741 | 1.0 |
| data | data_A |  | `2lep/Data/data_A.2lep.root` |  |  |  |
| data | data_B |  | `2lep/Data/data_B.2lep.root` |  |  |  |
| data | data_C |  | `2lep/Data/data_C.2lep.root` |  |  |  |
| data | data_D |  | `2lep/Data/data_D.2lep.root` |  |  |  |
| diboson | WlvZqq | 363489 | `2lep/MC/mc_363489.WlvZqq.2lep.root` | 11.413 | 1111991.15979 | 1.0 |
| diboson | WplvWmqq | 363360 | `2lep/MC/mc_363360.WplvWmqq.2lep.root` | 112.74 | 1069526.41899 | 1.0 |
| diboson | WpqqWmlv | 363359 | `2lep/MC/mc_363359.WpqqWmlv.2lep.root` | 24.717 | 998250.783475 | 1.0 |
| diboson | WqqZll | 363358 | `2lep/MC/mc_363358.WqqZll.2lep.root` | 3.437 | 241438.72705 | 1.0 |
| diboson | ZqqZll | 363356 | `2lep/MC/mc_363356.ZqqZll.2lep.root` | 15.563 | 3439266.11559 | 1.0 |
| diboson | llll | 363490 | `2lep/MC/mc_363490.llll.2lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| diboson | lllv | 363491 | `2lep/MC/mc_363491.lllv.2lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| diboson | llvv | 363492 | `2lep/MC/mc_363492.llvv.2lep.root` | 12.466 | 5039259.9696 | 1.0 |
| diboson | lvvv | 363493 | `2lep/MC/mc_363493.lvvv.2lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| signal | slep600DM300 | 392985 | `2lep/MC/mc_392985.SlepSlep_direct_600p0_300p0_2L8.2lep.root` | 0.000464769511 | 10457.5703245 | 1.0 |
| stop | single_antitop_schan | 410026 | `2lep/MC/mc_410026.single_antitop_schan.2lep.root` | 1.288662 | 995400.0 | 1.0 |
| stop | single_antitop_tchan | 410012 | `2lep/MC/mc_410012.single_antitop_tchan.2lep.root` | 26.276 | 4989800.0 | 1.0 |
| stop | single_antitop_wtchan | 410014 | `2lep/MC/mc_410014.single_antitop_wtchan.2lep.root` | 35.824406 | 4945600.0 | 1.0 |
| stop | single_top_schan | 410025 | `2lep/MC/mc_410025.single_top_schan.2lep.root` | 2.06121 | 997800.0 | 1.0 |
| stop | single_top_tchan | 410011 | `2lep/MC/mc_410011.single_top_tchan.2lep.root` | 44.152 | 4986200.0 | 1.0 |
| stop | single_top_wtchan | 410013 | `2lep/MC/mc_410013.single_top_wtchan.2lep.root` | 35.845486 | 4865800.0 | 1.0 |
| ttbar | ttbar_lep | 410000 | `2lep/MC/mc_410000.ttbar_lep.2lep.root` | 452.693559 | 49296600.0 | 1.0 |

## SingleTopAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_WBoson.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| Wjets | Wenu_PTV0_70_BFilter | 364172 | `1lep/MC/mc_364172.Wenu_PTV0_70_BFilter.1lep.root` | 832.203758 | 10407897.8772 | 1.0 |
| Wjets | Wenu_PTV0_70_CFilterBVeto | 364171 | `1lep/MC/mc_364171.Wenu_PTV0_70_CFilterBVeto.1lep.root` | 2430.656322 | 5647044.71225 | 1.0 |
| Wjets | Wenu_PTV0_70_CVetoBVeto | 364170 | `1lep/MC/mc_364170.Wenu_PTV0_70_CVetoBVeto.1lep.root` | 15324.216356 | 16615214.8608 | 1.0 |
| Wjets | Wenu_PTV1000 | 364183 | `1lep/MC/mc_364183.Wenu_PTV1000_E_CMS.1lep.root` | 1.197518 | 4075236.23897 | 1.0 |
| Wjets | Wenu_PTV140_280_BFilter | 364178 | `1lep/MC/mc_364178.Wenu_PTV140_280_BFilter.1lep.root` | 35.917295 | 7327201.08884 | 1.0 |
| Wjets | Wenu_PTV140_280_CFilterBVeto | 364177 | `1lep/MC/mc_364177.Wenu_PTV140_280_CFilterBVeto.1lep.root` | 96.277568 | 5263243.42582 | 1.0 |
| Wjets | Wenu_PTV140_280_CVetoBVeto | 364176 | `1lep/MC/mc_364176.Wenu_PTV140_280_CVetoBVeto.1lep.root` | 197.343129 | 6121546.03361 | 1.0 |
| Wjets | Wenu_PTV280_500_BFilter | 364181 | `1lep/MC/mc_364181.Wenu_PTV280_500_BFilter.1lep.root` | 9.586345 | 2835314.68179 | 1.0 |
| Wjets | Wenu_PTV280_500_CFilterBVeto | 364180 | `1lep/MC/mc_364180.Wenu_PTV280_500_CFilterBVeto.1lep.root` | 22.36999 | 2778654.28759 | 1.0 |
| Wjets | Wenu_PTV280_500_CVetoBVeto | 364179 | `1lep/MC/mc_364179.Wenu_PTV280_500_CVetoBVeto.1lep.root` | 38.340533 | 4312357.01458 | 1.0 |
| Wjets | Wenu_PTV500_1000 | 364182 | `1lep/MC/mc_364182.Wenu_PTV500_1000.1lep.root` | 14.598599 | 6003269.52809 | 1.0 |
| Wjets | Wenu_PTV70_140_BFilter | 364175 | `1lep/MC/mc_364175.Wenu_PTV70_140_BFilter.1lep.root` | 94.875534 | 3980401.78673 | 1.0 |
| Wjets | Wenu_PTV70_140_CFilterBVeto | 364174 | `1lep/MC/mc_364174.Wenu_PTV70_140_CFilterBVeto.1lep.root` | 223.63946 | 3661915.17878 | 1.0 |
| Wjets | Wenu_PTV70_140_CVetoBVeto | 364173 | `1lep/MC/mc_364173.Wenu_PTV70_140_CVetoBVeto.1lep.root` | 618.6882 | 5098540.19503 | 1.0 |
| Wjets | Wmunu_PTV0_70_BFilter | 364158 | `1lep/MC/mc_364158.Wmunu_PTV0_70_BFilter.1lep.root` | 828.465384 | 10403012.6599 | 1.0 |
| Wjets | Wmunu_PTV0_70_CFilterBVeto | 364157 | `1lep/MC/mc_364157.Wmunu_PTV0_70_CFilterBVeto.1lep.root` | 2431.204019 | 5643599.11526 | 1.0 |
| Wjets | Wmunu_PTV0_70_CVetoBVeto | 364156 | `1lep/MC/mc_364156.Wmunu_PTV0_70_CVetoBVeto.1lep.root` | 15317.171239 | 16619290.3298 | 1.0 |
| Wjets | Wmunu_PTV1000 | 364169 | `1lep/MC/mc_364169.Wmunu_PTV1000_E_CMS.1lep.root` | 1.198003 | 4068015.22447 | 1.0 |
| Wjets | Wmunu_PTV140_280_BFilter | 364164 | `1lep/MC/mc_364164.Wmunu_PTV140_280_BFilter.1lep.root` | 36.348467 | 7271557.26566 | 1.0 |
| Wjets | Wmunu_PTV140_280_CFilterBVeto | 364163 | `1lep/MC/mc_364163.Wmunu_PTV140_280_CFilterBVeto.1lep.root` | 96.233222 | 5260811.17463 | 1.0 |
| Wjets | Wmunu_PTV140_280_CVetoBVeto | 364162 | `1lep/MC/mc_364162.Wmunu_PTV140_280_CVetoBVeto.1lep.root` | 198.635592 | 6155495.28527 | 1.0 |
| Wjets | Wmunu_PTV280_500_BFilter | 364167 | `1lep/MC/mc_364167.Wmunu_PTV280_500_BFilter.1lep.root` | 8.768196 | 2835707.22044 | 1.0 |
| Wjets | Wmunu_PTV280_500_CFilterBVeto | 364166 | `1lep/MC/mc_364166.Wmunu_PTV280_500_CFilterBVeto.1lep.root` | 22.395647 | 2783968.68238 | 1.0 |
| Wjets | Wmunu_PTV280_500_CVetoBVeto | 364165 | `1lep/MC/mc_364165.Wmunu_PTV280_500_CVetoBVeto.1lep.root` | 38.299835 | 4325283.67358 | 1.0 |
| Wjets | Wmunu_PTV500_1000 | 364168 | `1lep/MC/mc_364168.Wmunu_PTV500_1000.1lep.root` | 14.558821 | 5941704.99235 | 1.0 |
| Wjets | Wmunu_PTV70_140_BFilter | 364161 | `1lep/MC/mc_364161.Wmunu_PTV70_140_BFilter.1lep.root` | 76.213179 | 7990084.35926 | 1.0 |
| Wjets | Wmunu_PTV70_140_CFilterBVeto | 364160 | `1lep/MC/mc_364160.Wmunu_PTV70_140_CFilterBVeto.1lep.root` | 225.006704 | 3693885.78953 | 1.0 |
| Wjets | Wmunu_PTV70_140_CVetoBVeto | 364159 | `1lep/MC/mc_364159.Wmunu_PTV70_140_CVetoBVeto.1lep.root` | 617.439593 | 5418398.88082 | 1.0 |
| Wjets | Wtaunu_PTV0_70_BFilter | 364186 | `1lep/MC/mc_364186.Wtaunu_PTV0_70_BFilter.1lep.root` | 837.531038 | 10498770.1084 | 1.0 |
| Wjets | Wtaunu_PTV0_70_CFilterBVeto | 364185 | `1lep/MC/mc_364185.Wtaunu_PTV0_70_CFilterBVeto.1lep.root` | 2443.425881 | 5671521.55269 | 1.0 |
| Wjets | Wtaunu_PTV0_70_CVetoBVeto | 364184 | `1lep/MC/mc_364184.Wtaunu_PTV0_70_CVetoBVeto.1lep.root` | 15324.887336 | 11929044.1188 | 1.0 |
| Wjets | Wtaunu_PTV1000 | 364197 | `1lep/MC/mc_364197.Wtaunu_PTV1000_E_CMS.1lep.root` | 1.197324 | 4057477.95297 | 1.0 |
| Wjets | Wtaunu_PTV140_280_BFilter | 364192 | `1lep/MC/mc_364192.Wtaunu_PTV140_280_BFilter.1lep.root` | 34.639523 | 7291603.73991 | 1.0 |
| Wjets | Wtaunu_PTV140_280_CFilterBVeto | 364191 | `1lep/MC/mc_364191.Wtaunu_PTV140_280_CFilterBVeto.1lep.root` | 93.808553 | 5085280.31607 | 1.0 |
| Wjets | Wtaunu_PTV140_280_CVetoBVeto | 364190 | `1lep/MC/mc_364190.Wtaunu_PTV140_280_CVetoBVeto.1lep.root` | 197.370776 | 6166514.76606 | 1.0 |
| Wjets | Wtaunu_PTV280_500_BFilter | 364195 | `1lep/MC/mc_364195.Wtaunu_PTV280_500_BFilter.1lep.root` | 9.490847 | 2830341.62344 | 1.0 |
| Wjets | Wtaunu_PTV280_500_CFilterBVeto | 364194 | `1lep/MC/mc_364194.Wtaunu_PTV280_500_CFilterBVeto.1lep.root` | 22.268425 | 2772305.06916 | 1.0 |
| Wjets | Wtaunu_PTV280_500_CVetoBVeto | 364193 | `1lep/MC/mc_364193.Wtaunu_PTV280_500_CVetoBVeto.1lep.root` | 38.34009 | 4322848.66983 | 1.0 |
| Wjets | Wtaunu_PTV500_1000 | 364196 | `1lep/MC/mc_364196.Wtaunu_PTV500_1000.1lep.root` | 14.60345 | 5932750.60186 | 1.0 |
| Wjets | Wtaunu_PTV70_140_BFilter | 364189 | `1lep/MC/mc_364189.Wtaunu_PTV70_140_BFilter.1lep.root` | 95.365521 | 3969118.20687 | 1.0 |
| Wjets | Wtaunu_PTV70_140_CFilterBVeto | 364188 | `1lep/MC/mc_364188.Wtaunu_PTV70_140_CFilterBVeto.1lep.root` | 222.595303 | 3719117.16117 | 1.0 |
| Wjets | Wtaunu_PTV70_140_CVetoBVeto | 364187 | `1lep/MC/mc_364187.Wtaunu_PTV70_140_CVetoBVeto.1lep.root` | 620.166885 | 5427023.47527 | 1.0 |
| ZVV | WlvZqq | 363489 | `1lep/MC/mc_363489.WlvZqq.1lep.root` | 11.42 | 1111991.15979 | 1.0 |
| ZVV | WplvWmqq | 363360 | `1lep/MC/mc_363360.WplvWmqq.1lep.root` | 24.724 | 1069526.41899 | 1.0 |
| ZVV | WpqqWmlv | 363359 | `1lep/MC/mc_363359.WpqqWmlv.1lep.root` | 24.708 | 998250.783475 | 1.0 |
| ZVV | WqqZll | 363358 | `1lep/MC/mc_363358.WqqZll.1lep.root` | 3.4328 | 241438.72705 | 1.0 |
| ZVV | Zee | 361106 | `1lep/MC/mc_361106.Zee.1lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| ZVV | Zmumu | 361107 | `1lep/MC/mc_361107.Zmumu.1lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| ZVV | ZqqZll | 363356 | `1lep/MC/mc_363356.ZqqZll.1lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| ZVV | Ztautau | 361108 | `1lep/MC/mc_361108.Ztautau.1lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| ZVV | llll | 363490 | `1lep/MC/mc_363490.llll.1lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| ZVV | lllv | 363491 | `1lep/MC/mc_363491.lllv.1lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| ZVV | llvv | 363492 | `1lep/MC/mc_363492.llvv.1lep.root` | 12.466 | 5039259.9696 | 1.0 |
| ZVV | lvvv | 363493 | `1lep/MC/mc_363493.lvvv.1lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| data | data_A |  | `1lep/Data/data_A.1lep.root` |  |  |  |
| data | data_B |  | `1lep/Data/data_B.1lep.root` |  |  |  |
| data | data_C |  | `1lep/Data/data_C.1lep.root` |  |  |  |
| data | data_D |  | `1lep/Data/data_D.1lep.root` |  |  |  |
| stop_tWtb | single_antitop_schan | 410026 | `1lep/MC/mc_410026.single_antitop_schan.1lep.root` | 1.288662 | 995400.0 | 1.0 |
| stop_tWtb | single_antitop_wtchan | 410014 | `1lep/MC/mc_410014.single_antitop_wtchan.1lep.root` | 35.824406 | 4945600.0 | 1.0 |
| stop_tWtb | single_top_schan | 410025 | `1lep/MC/mc_410025.single_top_schan.1lep.root` | 2.06121 | 997800.0 | 1.0 |
| stop_tWtb | single_top_wtchan | 410013 | `1lep/MC/mc_410013.single_top_wtchan.1lep.root` | 35.845486 | 4865800.0 | 1.0 |
| stop_tWtb | ttbar_lep | 410000 | `1lep/MC/mc_410000.ttbar_lep.1lep.root` | 452.693559 | 49296600.0 | 1.0 |
| stop_tchan | single_antitop_tchan | 410012 | `1lep/MC/mc_410012.single_antitop_tchan.1lep.root` | 26.276 | 4989800.0 | 1.0 |
| stop_tchan | single_top_tchan | 410011 | `1lep/MC/mc_410011.single_top_tchan.1lep.root` | 44.152 | 4986200.0 | 1.0 |

## TTbarAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_base.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| V | Wminusenu | 361103 | `1lep/MC/mc_361103.Wminusenu.1lep.root` | 8579.63498 | 247538642447.0 | 1.0 |
| V | Wminusmunu | 361104 | `1lep/MC/mc_361104.Wminusmunu.1lep.root` | 8579.63498 | 264338188182.0 | 1.0 |
| V | Wminustaunu | 361105 | `1lep/MC/mc_361105.Wminustaunu.1lep.root` | 8579.63498 | 165195850954.0 | 1.0 |
| V | Wplusenu | 361100 | `1lep/MC/mc_361100.Wplusenu.1lep.root` | 11500.4632 | 473389396815.0 | 1.0 |
| V | Wplusmunu | 361101 | `1lep/MC/mc_361101.Wplusmunu.1lep.root` | 11500.4632 | 446507925520.0 | 1.0 |
| V | Wplustaunu | 361102 | `1lep/MC/mc_361102.Wplustaunu.1lep.root` | 11500.4632 | 670928468875.0 | 1.0 |
| V | Zee | 361106 | `1lep/MC/mc_361106.Zee.1lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| V | Zmumu | 361107 | `1lep/MC/mc_361107.Zmumu.1lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| V | Ztautau | 361108 | `1lep/MC/mc_361108.Ztautau.1lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| data | data_A |  | `1lep/Data/data_A.1lep.root` |  |  |  |
| data | data_B |  | `1lep/Data/data_B.1lep.root` |  |  |  |
| data | data_C |  | `1lep/Data/data_C.1lep.root` |  |  |  |
| data | data_D |  | `1lep/Data/data_D.1lep.root` |  |  |  |
| diboson | WlvZqq | 363489 | `1lep/MC/mc_363489.WlvZqq.1lep.root` | 11.42 | 1111991.15979 | 1.0 |
| diboson | WplvWmqq | 363360 | `1lep/MC/mc_363360.WplvWmqq.1lep.root` | 24.724 | 1069526.41899 | 1.0 |
| diboson | WpqqWmlv | 363359 | `1lep/MC/mc_363359.WpqqWmlv.1lep.root` | 24.708 | 998250.783475 | 1.0 |
| diboson | WqqZll | 363358 | `1lep/MC/mc_363358.WqqZll.1lep.root` | 3.4328 | 241438.72705 | 1.0 |
| diboson | ZqqZll | 363356 | `1lep/MC/mc_363356.ZqqZll.1lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| diboson | llll | 363490 | `1lep/MC/mc_363490.llll.1lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| diboson | lllv | 363491 | `1lep/MC/mc_363491.lllv.1lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| diboson | llvv | 363492 | `1lep/MC/mc_363492.llvv.1lep.root` | 12.466 | 5039259.9696 | 1.0 |
| diboson | lvvv | 363493 | `1lep/MC/mc_363493.lvvv.1lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| stop | single_antitop_schan | 410026 | `1lep/MC/mc_410026.single_antitop_schan.1lep.root` | 1.288662 | 995400.0 | 1.0 |
| stop | single_antitop_tchan | 410012 | `1lep/MC/mc_410012.single_antitop_tchan.1lep.root` | 26.276 | 4989800.0 | 1.0 |
| stop | single_antitop_wtchan | 410014 | `1lep/MC/mc_410014.single_antitop_wtchan.1lep.root` | 35.824406 | 4945600.0 | 1.0 |
| stop | single_top_schan | 410025 | `1lep/MC/mc_410025.single_top_schan.1lep.root` | 2.06121 | 997800.0 | 1.0 |
| stop | single_top_tchan | 410011 | `1lep/MC/mc_410011.single_top_tchan.1lep.root` | 44.152 | 4986200.0 | 1.0 |
| stop | single_top_wtchan | 410013 | `1lep/MC/mc_410013.single_top_wtchan.1lep.root` | 35.845486 | 4865800.0 | 1.0 |
| ttbar | ttbar_lep | 410000 | `1lep/MC/mc_410000.ttbar_lep.1lep.root` | 452.693559 | 49386600.0 | 1.0 |

## WBosonAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_WBoson.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| Wjets | Wenu_PTV0_70_BFilter | 364172 | `1lep/MC/mc_364172.Wenu_PTV0_70_BFilter.1lep.root` | 832.203758 | 10407897.8772 | 1.0 |
| Wjets | Wenu_PTV0_70_CFilterBVeto | 364171 | `1lep/MC/mc_364171.Wenu_PTV0_70_CFilterBVeto.1lep.root` | 2430.656322 | 5647044.71225 | 1.0 |
| Wjets | Wenu_PTV0_70_CVetoBVeto | 364170 | `1lep/MC/mc_364170.Wenu_PTV0_70_CVetoBVeto.1lep.root` | 15324.216356 | 16615214.8608 | 1.0 |
| Wjets | Wenu_PTV1000 | 364183 | `1lep/MC/mc_364183.Wenu_PTV1000_E_CMS.1lep.root` | 1.197518 | 4075236.23897 | 1.0 |
| Wjets | Wenu_PTV140_280_BFilter | 364178 | `1lep/MC/mc_364178.Wenu_PTV140_280_BFilter.1lep.root` | 35.917295 | 7327201.08884 | 1.0 |
| Wjets | Wenu_PTV140_280_CFilterBVeto | 364177 | `1lep/MC/mc_364177.Wenu_PTV140_280_CFilterBVeto.1lep.root` | 96.277568 | 5263243.42582 | 1.0 |
| Wjets | Wenu_PTV140_280_CVetoBVeto | 364176 | `1lep/MC/mc_364176.Wenu_PTV140_280_CVetoBVeto.1lep.root` | 197.343129 | 6121546.03361 | 1.0 |
| Wjets | Wenu_PTV280_500_BFilter | 364181 | `1lep/MC/mc_364181.Wenu_PTV280_500_BFilter.1lep.root` | 9.586345 | 2835314.68179 | 1.0 |
| Wjets | Wenu_PTV280_500_CFilterBVeto | 364180 | `1lep/MC/mc_364180.Wenu_PTV280_500_CFilterBVeto.1lep.root` | 22.36999 | 2778654.28759 | 1.0 |
| Wjets | Wenu_PTV280_500_CVetoBVeto | 364179 | `1lep/MC/mc_364179.Wenu_PTV280_500_CVetoBVeto.1lep.root` | 38.340533 | 4312357.01458 | 1.0 |
| Wjets | Wenu_PTV500_1000 | 364182 | `1lep/MC/mc_364182.Wenu_PTV500_1000.1lep.root` | 14.598599 | 6003269.52809 | 1.0 |
| Wjets | Wenu_PTV70_140_BFilter | 364175 | `1lep/MC/mc_364175.Wenu_PTV70_140_BFilter.1lep.root` | 94.875534 | 3980401.78673 | 1.0 |
| Wjets | Wenu_PTV70_140_CFilterBVeto | 364174 | `1lep/MC/mc_364174.Wenu_PTV70_140_CFilterBVeto.1lep.root` | 223.63946 | 3661915.17878 | 1.0 |
| Wjets | Wenu_PTV70_140_CVetoBVeto | 364173 | `1lep/MC/mc_364173.Wenu_PTV70_140_CVetoBVeto.1lep.root` | 618.6882 | 5098540.19503 | 1.0 |
| Wjets | Wmunu_PTV0_70_BFilter | 364158 | `1lep/MC/mc_364158.Wmunu_PTV0_70_BFilter.1lep.root` | 828.465384 | 10403012.6599 | 1.0 |
| Wjets | Wmunu_PTV0_70_CFilterBVeto | 364157 | `1lep/MC/mc_364157.Wmunu_PTV0_70_CFilterBVeto.1lep.root` | 2431.204019 | 5643599.11526 | 1.0 |
| Wjets | Wmunu_PTV0_70_CVetoBVeto | 364156 | `1lep/MC/mc_364156.Wmunu_PTV0_70_CVetoBVeto.1lep.root` | 15317.171239 | 16619290.3298 | 1.0 |
| Wjets | Wmunu_PTV1000 | 364169 | `1lep/MC/mc_364169.Wmunu_PTV1000_E_CMS.1lep.root` | 1.198003 | 4068015.22447 | 1.0 |
| Wjets | Wmunu_PTV140_280_BFilter | 364164 | `1lep/MC/mc_364164.Wmunu_PTV140_280_BFilter.1lep.root` | 36.348467 | 7271557.26566 | 1.0 |
| Wjets | Wmunu_PTV140_280_CFilterBVeto | 364163 | `1lep/MC/mc_364163.Wmunu_PTV140_280_CFilterBVeto.1lep.root` | 96.233222 | 5260811.17463 | 1.0 |
| Wjets | Wmunu_PTV140_280_CVetoBVeto | 364162 | `1lep/MC/mc_364162.Wmunu_PTV140_280_CVetoBVeto.1lep.root` | 198.635592 | 6155495.28527 | 1.0 |
| Wjets | Wmunu_PTV280_500_BFilter | 364167 | `1lep/MC/mc_364167.Wmunu_PTV280_500_BFilter.1lep.root` | 8.768196 | 2835707.22044 | 1.0 |
| Wjets | Wmunu_PTV280_500_CFilterBVeto | 364166 | `1lep/MC/mc_364166.Wmunu_PTV280_500_CFilterBVeto.1lep.root` | 22.395647 | 2783968.68238 | 1.0 |
| Wjets | Wmunu_PTV280_500_CVetoBVeto | 364165 | `1lep/MC/mc_364165.Wmunu_PTV280_500_CVetoBVeto.1lep.root` | 38.299835 | 4325283.67358 | 1.0 |
| Wjets | Wmunu_PTV500_1000 | 364168 | `1lep/MC/mc_364168.Wmunu_PTV500_1000.1lep.root` | 14.558821 | 5941704.99235 | 1.0 |
| Wjets | Wmunu_PTV70_140_BFilter | 364161 | `1lep/MC/mc_364161.Wmunu_PTV70_140_BFilter.1lep.root` | 76.213179 | 7990084.35926 | 1.0 |
| Wjets | Wmunu_PTV70_140_CFilterBVeto | 364160 | `1lep/MC/mc_364160.Wmunu_PTV70_140_CFilterBVeto.1lep.root` | 225.006704 | 3693885.78953 | 1.0 |
| Wjets | Wmunu_PTV70_140_CVetoBVeto | 364159 | `1lep/MC/mc_364159.Wmunu_PTV70_140_CVetoBVeto.1lep.root` | 617.439593 | 5418398.88082 | 1.0 |
| Wjets | Wtaunu_PTV0_70_BFilter | 364186 | `1lep/MC/mc_364186.Wtaunu_PTV0_70_BFilter.1lep.root` | 837.531038 | 10498770.1084 | 1.0 |
| Wjets | Wtaunu_PTV0_70_CFilterBVeto | 364185 | `1lep/MC/mc_364185.Wtaunu_PTV0_70_CFilterBVeto.1lep.root` | 2443.425881 | 5671521.55269 | 1.0 |
| Wjets | Wtaunu_PTV0_70_CVetoBVeto | 364184 | `1lep/MC/mc_364184.Wtaunu_PTV0_70_CVetoBVeto.1lep.root` | 15324.887336 | 11929044.1188 | 1.0 |
| Wjets | Wtaunu_PTV1000 | 364197 | `1lep/MC/mc_364197.Wtaunu_PTV1000_E_CMS.1lep.root` | 1.197324 | 4057477.95297 | 1.0 |
| Wjets | Wtaunu_PTV140_280_BFilter | 364192 | `1lep/MC/mc_364192.Wtaunu_PTV140_280_BFilter.1lep.root` | 34.639523 | 7291603.73991 | 1.0 |
| Wjets | Wtaunu_PTV140_280_CFilterBVeto | 364191 | `1lep/MC/mc_364191.Wtaunu_PTV140_280_CFilterBVeto.1lep.root` | 93.808553 | 5085280.31607 | 1.0 |
| Wjets | Wtaunu_PTV140_280_CVetoBVeto | 364190 | `1lep/MC/mc_364190.Wtaunu_PTV140_280_CVetoBVeto.1lep.root` | 197.370776 | 6166514.76606 | 1.0 |
| Wjets | Wtaunu_PTV280_500_BFilter | 364195 | `1lep/MC/mc_364195.Wtaunu_PTV280_500_BFilter.1lep.root` | 9.490847 | 2830341.62344 | 1.0 |
| Wjets | Wtaunu_PTV280_500_CFilterBVeto | 364194 | `1lep/MC/mc_364194.Wtaunu_PTV280_500_CFilterBVeto.1lep.root` | 22.268425 | 2772305.06916 | 1.0 |
| Wjets | Wtaunu_PTV280_500_CVetoBVeto | 364193 | `1lep/MC/mc_364193.Wtaunu_PTV280_500_CVetoBVeto.1lep.root` | 38.34009 | 4322848.66983 | 1.0 |
| Wjets | Wtaunu_PTV500_1000 | 364196 | `1lep/MC/mc_364196.Wtaunu_PTV500_1000.1lep.root` | 14.60345 | 5932750.60186 | 1.0 |
| Wjets | Wtaunu_PTV70_140_BFilter | 364189 | `1lep/MC/mc_364189.Wtaunu_PTV70_140_BFilter.1lep.root` | 95.365521 | 3969118.20687 | 1.0 |
| Wjets | Wtaunu_PTV70_140_CFilterBVeto | 364188 | `1lep/MC/mc_364188.Wtaunu_PTV70_140_CFilterBVeto.1lep.root` | 222.595303 | 3719117.16117 | 1.0 |
| Wjets | Wtaunu_PTV70_140_CVetoBVeto | 364187 | `1lep/MC/mc_364187.Wtaunu_PTV70_140_CVetoBVeto.1lep.root` | 620.166885 | 5427023.47527 | 1.0 |
| Zjets | Zee | 361106 | `1lep/MC/mc_361106.Zee.1lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| Zjets | Zmumu | 361107 | `1lep/MC/mc_361107.Zmumu.1lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| Zjets | Ztautau | 361108 | `1lep/MC/mc_361108.Ztautau.1lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| data | data_A |  | `1lep/Data/data_A.1lep.root` |  |  |  |
| data | data_B |  | `1lep/Data/data_B.1lep.root` |  |  |  |
| data | data_C |  | `1lep/Data/data_C.1lep.root` |  |  |  |
| data | data_D |  | `1lep/Data/data_D.1lep.root` |  |  |  |
| diboson | WlvZqq | 363489 | `1lep/MC/mc_363489.WlvZqq.1lep.root` | 11.42 | 1111991.15979 | 1.0 |
| diboson | WplvWmqq | 363360 | `1lep/MC/mc_363360.WplvWmqq.1lep.root` | 24.724 | 1069526.41899 | 1.0 |
| diboson | WpqqWmlv | 363359 | `1lep/MC/mc_363359.WpqqWmlv.1lep.root` | 24.708 | 998250.783475 | 1.0 |
| diboson | WqqZll | 363358 | `1lep/MC/mc_363358.WqqZll.1lep.root` | 3.4328 | 241438.72705 | 1.0 |
| diboson | ZqqZll | 363356 | `1lep/MC/mc_363356.ZqqZll.1lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| diboson | llll | 363490 | `1lep/MC/mc_363490.llll.1lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| diboson | lllv | 363491 | `1lep/MC/mc_363491.lllv.1lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| diboson | llvv | 363492 | `1lep/MC/mc_363492.llvv.1lep.root` | 12.466 | 5039259.9696 | 1.0 |
| diboson | lvvv | 363493 | `1lep/MC/mc_363493.lvvv.1lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| stop | single_antitop_schan | 410026 | `1lep/MC/mc_410026.single_antitop_schan.1lep.root` | 1.288662 | 995400.0 | 1.0 |
| stop | single_antitop_tchan | 410012 | `1lep/MC/mc_410012.single_antitop_tchan.1lep.root` | 26.276 | 4989800.0 | 1.0 |
| stop | single_antitop_wtchan | 410014 | `1lep/MC/mc_410014.single_antitop_wtchan.1lep.root` | 35.824406 | 4945600.0 | 1.0 |
| stop | single_top_schan | 410025 | `1lep/MC/mc_410025.single_top_schan.1lep.root` | 2.06121 | 997800.0 | 1.0 |
| stop | single_top_tchan | 410011 | `1lep/MC/mc_410011.single_top_tchan.1lep.root` | 44.152 | 4986200.0 | 1.0 |
| stop | single_top_wtchan | 410013 | `1lep/MC/mc_410013.single_top_wtchan.1lep.root` | 35.845486 | 4865800.0 | 1.0 |
| ttbar | ttbar_lep | 410000 | `1lep/MC/mc_410000.ttbar_lep.1lep.root` | 452.693559 | 49296600.0 | 1.0 |

## WZDiBosonAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_base.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| V | Wminusenu | 361103 | `3lep/MC/mc_361103.Wminusenu.3lep.root` | 8579.63498 | 247538642447.0 | 1.0 |
| V | Wminusmunu | 361104 | `3lep/MC/mc_361104.Wminusmunu.3lep.root` | 8579.63498 | 264338188182.0 | 1.0 |
| V | Wminustaunu | 361105 | `3lep/MC/mc_361105.Wminustaunu.3lep.root` | 8579.63498 | 165195850954.0 | 1.0 |
| V | Wplusenu | 361100 | `3lep/MC/mc_361100.Wplusenu.3lep.root` | 11500.4632 | 473389396815.0 | 1.0 |
| V | Wplusmunu | 361101 | `3lep/MC/mc_361101.Wplusmunu.3lep.root` | 11500.4632 | 446507925520.0 | 1.0 |
| V | Wplustaunu | 361102 | `3lep/MC/mc_361102.Wplustaunu.3lep.root` | 11500.4632 | 670928468875.0 | 1.0 |
| V | Zee | 361106 | `3lep/MC/mc_361106.Zee.3lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| V | Zmumu | 361107 | `3lep/MC/mc_361107.Zmumu.3lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| V | Ztautau | 361108 | `3lep/MC/mc_361108.Ztautau.3lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| VV | WplvWmqq | 363360 | `3lep/MC/mc_363360.WplvWmqq.3lep.root` | 24.724 | 1069526.41899 | 1.0 |
| VV | WpqqWmlv | 363359 | `3lep/MC/mc_363359.WpqqWmlv.3lep.root` | 24.708 | 998250.783475 | 1.0 |
| VV | ZqqZll | 363356 | `3lep/MC/mc_363356.ZqqZll.3lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| VV | llll | 363490 | `3lep/MC/mc_363490.llll.3lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| VV | llvv | 363492 | `3lep/MC/mc_363492.llvv.3lep.root` | 12.466 | 5039259.9696 | 1.0 |
| WZ | WlvZqq | 363489 | `3lep/MC/mc_363489.WlvZqq.3lep.root` | 11.42 | 1111991.15979 | 1.0 |
| WZ | WqqZll | 363358 | `3lep/MC/mc_363358.WqqZll.3lep.root` | 3.4328 | 241438.72705 | 1.0 |
| WZ | lllv | 363491 | `3lep/MC/mc_363491.lllv.3lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| WZ | lvvv | 363493 | `3lep/MC/mc_363493.lvvv.3lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| data | data_A |  | `3lep/Data/data_A.3lep.root` |  |  |  |
| data | data_B |  | `3lep/Data/data_B.3lep.root` |  |  |  |
| data | data_C |  | `3lep/Data/data_C.3lep.root` |  |  |  |
| data | data_D |  | `3lep/Data/data_D.3lep.root` |  |  |  |
| top | single_antitop_schan | 410026 | `3lep/MC/mc_410026.single_antitop_schan.3lep.root` | 1.288662 | 995400.0 | 1.0 |
| top | single_antitop_tchan | 410012 | `3lep/MC/mc_410012.single_antitop_tchan.3lep.root` | 26.276 | 4989800.0 | 1.0 |
| top | single_antitop_wtchan | 410014 | `3lep/MC/mc_410014.single_antitop_wtchan.3lep.root` | 35.824406 | 4945600.0 | 1.0 |
| top | single_top_schan | 410025 | `3lep/MC/mc_410025.single_top_schan.3lep.root` | 2.06121 | 997800.0 | 1.0 |
| top | single_top_tchan | 410011 | `3lep/MC/mc_410011.single_top_tchan.3lep.root` | 44.152 | 4986200.0 | 1.0 |
| top | single_top_wtchan | 410013 | `3lep/MC/mc_410013.single_top_wtchan.3lep.root` | 35.845486 | 4865800.0 | 1.0 |
| top | ttbar_lep | 410000 | `3lep/MC/mc_410000.ttbar_lep.3lep.root` | 452.693559 | 49386600.0 | 1.0 |

## ZBosonAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_base.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| Wjets | Wminusenu | 361103 | `2lep/MC/mc_361103.Wminusenu.2lep.root` | 8579.63498 | 247538642447.0 | 1.0 |
| Wjets | Wminusmunu | 361104 | `2lep/MC/mc_361104.Wminusmunu.2lep.root` | 8579.63498 | 264338188182.0 | 1.0 |
| Wjets | Wminustaunu | 361105 | `2lep/MC/mc_361105.Wminustaunu.2lep.root` | 8579.63498 | 165195850954.0 | 1.0 |
| Wjets | Wplusenu | 361100 | `2lep/MC/mc_361100.Wplusenu.2lep.root` | 11500.4632 | 473389396815.0 | 1.0 |
| Wjets | Wplusmunu | 361101 | `2lep/MC/mc_361101.Wplusmunu.2lep.root` | 11500.4632 | 446507925520.0 | 1.0 |
| Wjets | Wplustaunu | 361102 | `2lep/MC/mc_361102.Wplustaunu.2lep.root` | 11500.4632 | 670928468875.0 | 1.0 |
| Zjets | Zee | 361106 | `2lep/MC/mc_361106.Zee.2lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| Zjets | Zmumu | 361107 | `2lep/MC/mc_361107.Zmumu.2lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| Zjets | Ztautau | 361108 | `2lep/MC/mc_361108.Ztautau.2lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| data | data_A |  | `2lep/Data/data_A.2lep.root` |  |  |  |
| data | data_B |  | `2lep/Data/data_B.2lep.root` |  |  |  |
| data | data_C |  | `2lep/Data/data_C.2lep.root` |  |  |  |
| data | data_D |  | `2lep/Data/data_D.2lep.root` |  |  |  |
| diboson | WlvZqq | 363489 | `2lep/MC/mc_363489.WlvZqq.2lep.root` | 11.42 | 1111991.15979 | 1.0 |
| diboson | WplvWmqq | 363360 | `2lep/MC/mc_363360.WplvWmqq.2lep.root` | 24.724 | 1069526.41899 | 1.0 |
| diboson | WpqqWmlv | 363359 | `2lep/MC/mc_363359.WpqqWmlv.2lep.root` | 24.708 | 998250.783475 | 1.0 |
| diboson | WqqZll | 363358 | `2lep/MC/mc_363358.WqqZll.2lep.root` | 3.4328 | 241438.72705 | 1.0 |
| diboson | ZqqZll | 363356 | `2lep/MC/mc_363356.ZqqZll.2lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| diboson | llll | 363490 | `2lep/MC/mc_363490.llll.2lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| diboson | lllv | 363491 | `2lep/MC/mc_363491.lllv.2lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| diboson | llvv | 363492 | `2lep/MC/mc_363492.llvv.2lep.root` | 12.466 | 5039259.9696 | 1.0 |
| diboson | lvvv | 363493 | `2lep/MC/mc_363493.lvvv.2lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| stop | single_antitop_schan | 410026 | `2lep/MC/mc_410026.single_antitop_schan.2lep.root` | 1.288662 | 995400.0 | 1.0 |
| stop | single_antitop_tchan | 410012 | `2lep/MC/mc_410012.single_antitop_tchan.2lep.root` | 26.276 | 4989800.0 | 1.0 |
| stop | single_antitop_wtchan | 410014 | `2lep/MC/mc_410014.single_antitop_wtchan.2lep.root` | 35.824406 | 4945600.0 | 1.0 |
| stop | single_top_schan | 410025 | `2lep/MC/mc_410025.single_top_schan.2lep.root` | 2.06121 | 997800.0 | 1.0 |
| stop | single_top_tchan | 410011 | `2lep/MC/mc_410011.single_top_tchan.2lep.root` | 44.152 | 4986200.0 | 1.0 |
| stop | single_top_wtchan | 410013 | `2lep/MC/mc_410013.single_top_wtchan.2lep.root` | 35.845486 | 4865800.0 | 1.0 |
| ttbar | ttbar_lep | 410000 | `2lep/MC/mc_410000.ttbar_lep.2lep.root` | 452.693559 | 49386600.0 | 1.0 |

## ZPrimeBoostedAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_ZPrime.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| V | Wenu_PTV0_70_BFilter | 364172 | `1largeRjet1lep/MC/mc_364172.Wenu_PTV0_70_BFilter.1largeRjet1lep.root` | 832.203758 | 10407897.8772 | 1.0 |
| V | Wenu_PTV0_70_CFilterBVeto | 364171 | `1largeRjet1lep/MC/mc_364171.Wenu_PTV0_70_CFilterBVeto.1largeRjet1lep.root` | 2430.656322 | 5647044.71225 | 1.0 |
| V | Wenu_PTV0_70_CVetoBVeto | 364170 | `1largeRjet1lep/MC/mc_364170.Wenu_PTV0_70_CVetoBVeto.1largeRjet1lep.root` | 15324.216356 | 16615214.8608 | 1.0 |
| V | Wenu_PTV1000 | 364183 | `1largeRjet1lep/MC/mc_364183.Wenu_PTV1000_E_CMS.1largeRjet1lep.root` | 1.197518 | 4075236.23897 | 1.0 |
| V | Wenu_PTV140_280_BFilter | 364178 | `1largeRjet1lep/MC/mc_364178.Wenu_PTV140_280_BFilter.1largeRjet1lep.root` | 35.917295 | 7327201.08884 | 1.0 |
| V | Wenu_PTV140_280_CFilterBVeto | 364177 | `1largeRjet1lep/MC/mc_364177.Wenu_PTV140_280_CFilterBVeto.1largeRjet1lep.root` | 96.277568 | 5263243.42582 | 1.0 |
| V | Wenu_PTV140_280_CVetoBVeto | 364176 | `1largeRjet1lep/MC/mc_364176.Wenu_PTV140_280_CVetoBVeto.1largeRjet1lep.root` | 197.343129 | 6121546.03361 | 1.0 |
| V | Wenu_PTV280_500_BFilter | 364181 | `1largeRjet1lep/MC/mc_364181.Wenu_PTV280_500_BFilter.1largeRjet1lep.root` | 9.586345 | 2835314.68179 | 1.0 |
| V | Wenu_PTV280_500_CFilterBVeto | 364180 | `1largeRjet1lep/MC/mc_364180.Wenu_PTV280_500_CFilterBVeto.1largeRjet1lep.root` | 22.36999 | 2778654.28759 | 1.0 |
| V | Wenu_PTV280_500_CVetoBVeto | 364179 | `1largeRjet1lep/MC/mc_364179.Wenu_PTV280_500_CVetoBVeto.1largeRjet1lep.root` | 38.340533 | 4312357.01458 | 1.0 |
| V | Wenu_PTV500_1000 | 364182 | `1largeRjet1lep/MC/mc_364182.Wenu_PTV500_1000.1largeRjet1lep.root` | 14.598599 | 6003269.52809 | 1.0 |
| V | Wenu_PTV70_140_BFilter | 364175 | `1largeRjet1lep/MC/mc_364175.Wenu_PTV70_140_BFilter.1largeRjet1lep.root` | 94.875534 | 3980401.78673 | 1.0 |
| V | Wenu_PTV70_140_CFilterBVeto | 364174 | `1largeRjet1lep/MC/mc_364174.Wenu_PTV70_140_CFilterBVeto.1largeRjet1lep.root` | 223.63946 | 3661915.17878 | 1.0 |
| V | Wenu_PTV70_140_CVetoBVeto | 364173 | `1largeRjet1lep/MC/mc_364173.Wenu_PTV70_140_CVetoBVeto.1largeRjet1lep.root` | 618.6882 | 5098540.19503 | 1.0 |
| V | Wmunu_PTV0_70_BFilter | 364158 | `1largeRjet1lep/MC/mc_364158.Wmunu_PTV0_70_BFilter.1largeRjet1lep.root` | 828.465384 | 10403012.6599 | 1.0 |
| V | Wmunu_PTV0_70_CFilterBVeto | 364157 | `1largeRjet1lep/MC/mc_364157.Wmunu_PTV0_70_CFilterBVeto.1largeRjet1lep.root` | 2431.204019 | 5643599.11526 | 1.0 |
| V | Wmunu_PTV0_70_CVetoBVeto | 364156 | `1largeRjet1lep/MC/mc_364156.Wmunu_PTV0_70_CVetoBVeto.1largeRjet1lep.root` | 15317.171239 | 16619290.3298 | 1.0 |
| V | Wmunu_PTV1000 | 364169 | `1largeRjet1lep/MC/mc_364169.Wmunu_PTV1000_E_CMS.1largeRjet1lep.root` | 1.198003 | 4068015.22447 | 1.0 |
| V | Wmunu_PTV140_280_BFilter | 364164 | `1largeRjet1lep/MC/mc_364164.Wmunu_PTV140_280_BFilter.1largeRjet1lep.root` | 36.348467 | 7271557.26566 | 1.0 |
| V | Wmunu_PTV140_280_CFilterBVeto | 364163 | `1largeRjet1lep/MC/mc_364163.Wmunu_PTV140_280_CFilterBVeto.1largeRjet1lep.root` | 96.233222 | 5260811.17463 | 1.0 |
| V | Wmunu_PTV140_280_CVetoBVeto | 364162 | `1largeRjet1lep/MC/mc_364162.Wmunu_PTV140_280_CVetoBVeto.1largeRjet1lep.root` | 198.635592 | 6155495.28527 | 1.0 |
| V | Wmunu_PTV280_500_BFilter | 364167 | `1largeRjet1lep/MC/mc_364167.Wmunu_PTV280_500_BFilter.1largeRjet1lep.root` | 8.768196 | 2835707.22044 | 1.0 |
| V | Wmunu_PTV280_500_CFilterBVeto | 364166 | `1largeRjet1lep/MC/mc_364166.Wmunu_PTV280_500_CFilterBVeto.1largeRjet1lep.root` | 22.395647 | 2783968.68238 | 1.0 |
| V | Wmunu_PTV280_500_CVetoBVeto | 364165 | `1largeRjet1lep/MC/mc_364165.Wmunu_PTV280_500_CVetoBVeto.1largeRjet1lep.root` | 38.299835 | 4325283.67358 | 1.0 |
| V | Wmunu_PTV500_1000 | 364168 | `1largeRjet1lep/MC/mc_364168.Wmunu_PTV500_1000.1largeRjet1lep.root` | 14.558821 | 5941704.99235 | 1.0 |
| V | Wmunu_PTV70_140_BFilter | 364161 | `1largeRjet1lep/MC/mc_364161.Wmunu_PTV70_140_BFilter.1largeRjet1lep.root` | 76.213179 | 7990084.35926 | 1.0 |
| V | Wmunu_PTV70_140_CFilterBVeto | 364160 | `1largeRjet1lep/MC/mc_364160.Wmunu_PTV70_140_CFilterBVeto.1largeRjet1lep.root` | 225.006704 | 3693885.78953 | 1.0 |
| V | Wmunu_PTV70_140_CVetoBVeto | 364159 | `1largeRjet1lep/MC/mc_364159.Wmunu_PTV70_140_CVetoBVeto.1largeRjet1lep.root` | 617.439593 | 5418398.88082 | 1.0 |
| V | Wtaunu_PTV0_70_BFilter | 364186 | `1largeRjet1lep/MC/mc_364186.Wtaunu_PTV0_70_BFilter.1largeRjet1lep.root` | 837.531038 | 10498770.1084 | 1.0 |
| V | Wtaunu_PTV0_70_CFilterBVeto | 364185 | `1largeRjet1lep/MC/mc_364185.Wtaunu_PTV0_70_CFilterBVeto.1largeRjet1lep.root` | 2443.425881 | 5671521.55269 | 1.0 |
| V | Wtaunu_PTV0_70_CVetoBVeto | 364184 | `1largeRjet1lep/MC/mc_364184.Wtaunu_PTV0_70_CVetoBVeto.1largeRjet1lep.root` | 15324.887336 | 11929044.1188 | 1.0 |
| V | Wtaunu_PTV1000 | 364197 | `1largeRjet1lep/MC/mc_364197.Wtaunu_PTV1000_E_CMS.1largeRjet1lep.root` | 1.197324 | 4057477.95297 | 1.0 |
| V | Wtaunu_PTV140_280_BFilter | 364192 | `1largeRjet1lep/MC/mc_364192.Wtaunu_PTV140_280_BFilter.1largeRjet1lep.root` | 34.639523 | 7291603.73991 | 1.0 |
| V | Wtaunu_PTV140_280_CFilterBVeto | 364191 | `1largeRjet1lep/MC/mc_364191.Wtaunu_PTV140_280_CFilterBVeto.1largeRjet1lep.root` | 93.808553 | 5085280.31607 | 1.0 |
| V | Wtaunu_PTV140_280_CVetoBVeto | 364190 | `1largeRjet1lep/MC/mc_364190.Wtaunu_PTV140_280_CVetoBVeto.1largeRjet1lep.root` | 197.370776 | 6166514.76606 | 1.0 |
| V | Wtaunu_PTV280_500_BFilter | 364195 | `1largeRjet1lep/MC/mc_364195.Wtaunu_PTV280_500_BFilter.1largeRjet1lep.root` | 9.490847 | 2830341.62344 | 1.0 |
| V | Wtaunu_PTV280_500_CFilterBVeto | 364194 | `1largeRjet1lep/MC/mc_364194.Wtaunu_PTV280_500_CFilterBVeto.1largeRjet1lep.root` | 22.268425 | 2772305.06916 | 1.0 |
| V | Wtaunu_PTV280_500_CVetoBVeto | 364193 | `1largeRjet1lep/MC/mc_364193.Wtaunu_PTV280_500_CVetoBVeto.1largeRjet1lep.root` | 38.34009 | 4322848.66983 | 1.0 |
| V | Wtaunu_PTV500_1000 | 364196 | `1largeRjet1lep/MC/mc_364196.Wtaunu_PTV500_1000.1largeRjet1lep.root` | 14.60345 | 5932750.60186 | 1.0 |
| V | Wtaunu_PTV70_140_BFilter | 364189 | `1largeRjet1lep/MC/mc_364189.Wtaunu_PTV70_140_BFilter.1largeRjet1lep.root` | 95.365521 | 3969118.20687 | 1.0 |
| V | Wtaunu_PTV70_140_CFilterBVeto | 364188 | `1largeRjet1lep/MC/mc_364188.Wtaunu_PTV70_140_CFilterBVeto.1largeRjet1lep.root` | 222.595303 | 3719117.16117 | 1.0 |
| V | Wtaunu_PTV70_140_CVetoBVeto | 364187 | `1largeRjet1lep/MC/mc_364187.Wtaunu_PTV70_140_CVetoBVeto.1largeRjet1lep.root` | 620.166885 | 5427023.47527 | 1.0 |
| V | Zee | 361106 | `1largeRjet1lep/MC/mc_361106.Zee.1largeRjet1lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| V | Zmumu | 361107 | `1largeRjet1lep/MC/mc_361107.Zmumu.1largeRjet1lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| V | Ztautau | 361108 | `1largeRjet1lep/MC/mc_361108.Ztautau.1largeRjet1lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| data | data_A |  | `1largeRjet1lep/Data/data_A.1largeRjet1lep.root` |  |  |  |
| data | data_B |  | `1largeRjet1lep/Data/data_B.1largeRjet1lep.root` |  |  |  |
| data | data_C |  | `1largeRjet1lep/Data/data_C.1largeRjet1lep.root` |  |  |  |
| data | data_D |  | `1largeRjet1lep/Data/data_D.1largeRjet1lep.root` |  |  |  |
| diboson | WlvZqq | 363489 | `1largeRjet1lep/MC/mc_363489.WlvZqq.1largeRjet1lep.root` | 11.42 | 1111991.15979 | 1.0 |
| diboson | WplvWmqq | 363360 | `1largeRjet1lep/MC/mc_363360.WplvWmqq.1largeRjet1lep.root` | 24.724 | 1069526.41899 | 1.0 |
| diboson | WqqZll | 363358 | `1largeRjet1lep/MC/mc_363358.WqqZll.1largeRjet1lep.root` | 3.4328 | 241438.72705 | 1.0 |
| diboson | ZqqZll | 363356 | `1largeRjet1lep/MC/mc_363356.ZqqZll.1largeRjet1lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| diboson | lllv | 363491 | `1largeRjet1lep/MC/mc_363491.lllv.1largeRjet1lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| diboson | llvv | 363492 | `1largeRjet1lep/MC/mc_363492.llvv.1largeRjet1lep.root` | 12.466 | 5039259.9696 | 1.0 |
| diboson | lvvv | 363493 | `1largeRjet1lep/MC/mc_363493.lvvv.1largeRjet1lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| signal | ZPrime1000_tt | 301325 | `1largeRjet1lep/MC/mc_301325.ZPrime1000_tt.1largeRjet1lep.root` | 1.1261 | 199800.0 | 1.0 |
| stop | single_antitop_schan | 410026 | `1largeRjet1lep/MC/mc_410026.single_antitop_schan.1largeRjet1lep.root` | 1.288662 | 995400.0 | 1.0 |
| stop | single_antitop_tchan | 410012 | `1largeRjet1lep/MC/mc_410012.single_antitop_tchan.1largeRjet1lep.root` | 26.276 | 4989800.0 | 1.0 |
| stop | single_antitop_wtchan | 410014 | `1largeRjet1lep/MC/mc_410014.single_antitop_wtchan.1largeRjet1lep.root` | 35.824406 | 4945600.0 | 1.0 |
| stop | single_top_schan | 410025 | `1largeRjet1lep/MC/mc_410025.single_top_schan.1largeRjet1lep.root` | 2.06121 | 997800.0 | 1.0 |
| stop | single_top_tchan | 410011 | `1largeRjet1lep/MC/mc_410011.single_top_tchan.1largeRjet1lep.root` | 44.152 | 4986200.0 | 1.0 |
| stop | single_top_wtchan | 410013 | `1largeRjet1lep/MC/mc_410013.single_top_wtchan.1largeRjet1lep.root` | 35.845486 | 4865800.0 | 1.0 |
| ttbar | ttbar_lep | 410000 | `1largeRjet1lep/MC/mc_410000.ttbar_lep.1largeRjet1lep.root` | 452.693559 | 49296600.0 | 1.0 |

## ZZDiBosonAnalysis

Normalisation table: ATLAS Open Data 13 TeV C++ framework v1.1, Plotting/inputfiles/Files_base.txt

| group | sample | DSID | file | xsec [pb] | sumw | eff |
|---|---|---|---|---|---|---|
| WWZ | WlvZqq | 363489 | `2lep/MC/mc_363489.WlvZqq.2lep.root` | 11.42 | 1111991.15979 | 1.0 |
| WWZ | WplvWmqq | 363360 | `2lep/MC/mc_363360.WplvWmqq.2lep.root` | 24.724 | 1069526.41899 | 1.0 |
| WWZ | WpqqWmlv | 363359 | `2lep/MC/mc_363359.WpqqWmlv.2lep.root` | 24.708 | 998250.783475 | 1.0 |
| WWZ | WqqZll | 363358 | `2lep/MC/mc_363358.WqqZll.2lep.root` | 3.4328 | 241438.72705 | 1.0 |
| WWZ | lllv | 363491 | `4lep/MC/mc_363491.lllv.4lep.root` | 4.6049 | 5441475.00407 | 1.0 |
| WWZ | lvvv | 363493 | `2lep/MC/mc_363493.lvvv.2lep.root` | 3.2286 | 1727991.07441 | 1.0 |
| ZZ | ZqqZll | 363356 | `4lep/MC/mc_363356.ZqqZll.4lep.root` | 2.20355112 | 3439266.11559 | 1.0 |
| ZZ | llll | 363490 | `4lep/MC/mc_363490.llll.4lep.root` | 1.2578 | 7538705.8077 | 1.0 |
| ZZ | llvv | 363492 | `4lep/MC/mc_363492.llvv.4lep.root` | 12.466 | 5039259.9696 | 1.0 |
| data | data_A |  | `4lep/Data/data_A.4lep.root` |  |  |  |
| data | data_B |  | `4lep/Data/data_B.4lep.root` |  |  |  |
| data | data_C |  | `4lep/Data/data_C.4lep.root` |  |  |  |
| data | data_D |  | `4lep/Data/data_D.4lep.root` |  |  |  |
| topV | Wminusenu | 361103 | `2lep/MC/mc_361103.Wminusenu.2lep.root` | 8579.63498 | 247538642447.0 | 1.0 |
| topV | Wminusmunu | 361104 | `2lep/MC/mc_361104.Wminusmunu.2lep.root` | 8579.63498 | 264338188182.0 | 1.0 |
| topV | Wminustaunu | 361105 | `2lep/MC/mc_361105.Wminustaunu.2lep.root` | 8579.63498 | 165195850954.0 | 1.0 |
| topV | Wplusenu | 361100 | `2lep/MC/mc_361100.Wplusenu.2lep.root` | 11500.4632 | 473389396815.0 | 1.0 |
| topV | Wplusmunu | 361101 | `2lep/MC/mc_361101.Wplusmunu.2lep.root` | 11500.4632 | 446507925520.0 | 1.0 |
| topV | Wplustaunu | 361102 | `2lep/MC/mc_361102.Wplustaunu.2lep.root` | 11500.4632 | 670928468875.0 | 1.0 |
| topV | Zee | 361106 | `4lep/MC/mc_361106.Zee.4lep.root` | 1950.5295 | 150277594200.0 | 1.0 |
| topV | Zmumu | 361107 | `4lep/MC/mc_361107.Zmumu.4lep.root` | 1950.6321 | 147334691090.0 | 1.0 |
| topV | Ztautau | 361108 | `4lep/MC/mc_361108.Ztautau.4lep.root` | 1950.6321 | 56171652547.3 | 1.0 |
| topV | single_antitop_schan | 410026 | `4lep/MC/mc_410026.single_antitop_schan.4lep.root` | 1.288662 | 995400.0 | 1.0 |
| topV | single_antitop_tchan | 410012 | `4lep/MC/mc_410012.single_antitop_tchan.4lep.root` | 26.276 | 4989800.0 | 1.0 |
| topV | single_antitop_wtchan | 410014 | `4lep/MC/mc_410014.single_antitop_wtchan.4lep.root` | 35.824406 | 4945600.0 | 1.0 |
| topV | single_top_schan | 410025 | `4lep/MC/mc_410025.single_top_schan.4lep.root` | 2.06121 | 997800.0 | 1.0 |
| topV | single_top_tchan | 410011 | `4lep/MC/mc_410011.single_top_tchan.4lep.root` | 44.152 | 4986200.0 | 1.0 |
| topV | single_top_wtchan | 410013 | `4lep/MC/mc_410013.single_top_wtchan.4lep.root` | 35.845486 | 4865800.0 | 1.0 |
| topV | ttbar_lep | 410000 | `4lep/MC/mc_410000.ttbar_lep.4lep.root` | 452.693559 | 49386600.0 | 1.0 |
