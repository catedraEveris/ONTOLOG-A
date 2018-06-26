#Import data from txt
import csv
import sys

#csvfile = "<path to output csv or txt>"

with open('testfilea-mod.txt', 'rt') as f:
    
    reader = csv.reader(f, delimiter="\n")
    a=[ ]


    loc_asi = [ "LOC-ASI:" ] 
    loc_eeuu= [ "LOC-EEUU:" ]
    loc_ger = [ "LOC-GER:" ]
    loc_ita = [ "LOC-ITA:" ]
    loc_spa = [ "LOC-SPA:" ]
    loc_uk = [ "LOC-UK:" ]
    loc_isl = [ "LOC-ISL:" ]
    loc_chi = [ "LOC-CHI:" ]
    loc_ame = [ "LOC-AME:" ]
    loc_afr = [ "LOC-AFR:" ]
    loc_eur = [ "LOC-EUR:" ]
    loc_misc = [ "LOC-MISC:" ]

    org_spo = [ "ORG-SPO:" ]
    org_pol = [ "ORG-POL:" ]
    org_mot = [ "ORG-MOT:" ]
    org_com = [ "ORG-COM:" ]
    org_misc = [ "ORG-MISC:" ]

    per_fra = [ "PER-FRA:" ]
    per_uk = [ "PER-UK:" ]
    per_ger = [ "PER-GER:" ]
    per_por = [ "PER-POR:" ]
    per_ita = [ "PER-ITA:" ]
    per_spa = [ "PER-SPA:" ]
    per_eur = [ "PER-EUR:" ]
    per_asi = [ "PER-ASI:" ]
    per_ara = [ "PER-ARA:" ]
    per_misc = [ "PER-MISC:" ]

    for row in reader:
    	a.append (row)
    #for row in f:
    	#if not row.strip():
    		#a.append(row)
    #engtesta = [[None] * 4 for i in range(len(a)-1)]
    for i in range(len(a)-1):
    	print(a[i])
    	if (a[i] != []):
            var = a[i][0].split(" ")
            if (var[3] != "O" and var[3].split("-")[1]== "LOC"):
                if (var[3]=="I-LOC-ASI"):
                        loc_asi += [ var[0]+"," ]
                else:
                    if (var[3]=="I-LOC-EEUU"):
                        loc_eeuu += [ var[0]+"," ]
                    else:
                        if (var[3]=="I-LOC-GER"):
                            loc_ger += [ var[0]+"," ]
                        else:
                            if (var[3]=="I-LOC-ITA"):
                                loc_ita += [ var[0]+"," ]
                            else:
                                if (var[3]=="I-LOC-SPA"):
                                    loc_spa += [ var[0]+"," ]
                                else:
                                    if (var[3]=="I-LOC-UK"):
                                        loc_uk += [ var[0]+"," ]
                                    else: 
                                        if (var[3]=="I-LOC-ISL"):
                                            loc_isl += [ var[0]+"," ]
                                        else:
                                            if (var[3]=="I-LOC-CHI"):
                                                loc_chi += [ var[0]+"," ]
                                            else:
                                                if (var[3]=="I-LOC-AME"):
                                                    loc_ame += [ var[0]+"," ]
                                                else:
                                                    if (var[3]=="I-LOC-AFR"):
                                                        loc_afr += [ var[0]+"," ]
                                                    else:
                                                        if (var[3]=="I-LOC-EUR"):
                                                            loc_eur += [ var[0]+"," ]
                                                        else:
                                                            if (var[3]=="I-LOC-ASI"):
                                                                loc_asi += [ var[0]+"," ]
                                                            else:
                                                                loc_misc += [ var[0]+"," ]
            else:
                if(var[3] != "O" and var[3].split("-")[1]=="ORG"):  
                    if (var[3]=="I-ORG-POL"):
                                org_pol += [ var[0]+"," ]
                    else:
                        if (var[3]=="I-ORG-SPO"):
                            org_spo += [ var[0]+"," ]
                        else:
                            if (var[3]=="I-ORG-MOT"):
                                org_mot += [ var[0]+"," ]
                            else:
                                if (var[3]=="I-ORG-COM"):
                                    org_com += [ var[0]+"," ]
                                else:
                                    org_misc += [ var[0]+"," ]
                else:
                    if(var[3] != "O" and var[3].split("-")[1]=="PER"):
                        if (var[3]=="I-PER-FRA"):
                            per_fra += [ var[0]+"," ]
                        else:
                            if (var[3]=="I-PER-UK"):
                                per_uk += [ var[0]+"," ]
                            else:
                                if (var[3]=="I-PER-GER"):
                                    per_ger += [ var[0]+"," ]
                                else:
                                    if (var[3]=="I-PER-POR"):
                                        per_por += [ var[0]+"," ]
                                    else:
                                        if (var[3]=="I-PER-ITA"):
                                            per_ita += [ var[0]+"," ]
                                        else:
                                            if (var[3]=="I-PER-SPA"):
                                                per_spa += [ var[0]+"," ]
                                            else:
                                                if (var[3]=="I-PER-EUR"):
                                                    per_eur += [ var[0]+"," ]
                                                else:
                                                    if (var[3]=="I-PER-ASI"):
                                                        per_asi += [ var[0]+"," ]
                                                    else:
                                                        if (var[3]=="I-PER-ARA"):
                                                            per_ara += [ var[0]+"," ]
                                                        else:
                                                            per_misc += [ var[0]+"," ]

    with open('testfileb-mod.txt', 'rt') as f:
    
        reader = csv.reader(f, delimiter="\n")
        a=[ ]

        for row in reader:
            a.append (row)
        #for row in f:
            #if not row.strip():
                #a.append(row)
        #engtesta = [[None] * 4 for i in range(len(a)-1)]
        for i in range(len(a)-1):
            print(a[i])
            if (a[i] != []):
                var = a[i][0].split(" ")
                if (var[3] != "O" and var[3].split("-")[1]== "LOC"):
                    if (var[3]=="I-LOC-ASI"):
                            loc_asi += [ var[0]+"," ]
                    else:
                        if (var[3]=="I-LOC-EEUU"):
                            loc_eeuu += [ var[0]+"," ]
                        else:
                            if (var[3]=="I-LOC-GER"):
                                loc_ger += [ var[0]+"," ]
                            else:
                                if (var[3]=="I-LOC-ITA"):
                                    loc_ita += [ var[0]+"," ]
                                else:
                                    if (var[3]=="I-LOC-SPA"):
                                        loc_spa += [ var[0]+"," ]
                                    else:
                                        if (var[3]=="I-LOC-UK"):
                                            loc_uk += [ var[0]+"," ]
                                        else: 
                                            if (var[3]=="I-LOC-ISL"):
                                                loc_isl += [ var[0]+"," ]
                                            else:
                                                if (var[3]=="I-LOC-CHI"):
                                                    loc_chi += [ var[0]+"," ]
                                                else:
                                                    if (var[3]=="I-LOC-AME"):
                                                        loc_ame += [ var[0]+"," ]
                                                    else:
                                                        if (var[3]=="I-LOC-AFR"):
                                                            loc_afr += [ var[0]+"," ]
                                                        else:
                                                            if (var[3]=="I-LOC-EUR"):
                                                                loc_eur += [ var[0]+"," ]
                                                            else:
                                                                if (var[3]=="I-LOC-ASI"):
                                                                    loc_asi += [ var[0]+"," ]
                                                                else:
                                                                    loc_misc += [ var[0]+"," ]
                else:
                    if(var[3] != "O" and var[3].split("-")[1]=="ORG"):  
                        if (var[3]=="I-ORG-POL"):
                                    org_pol += [ var[0]+"," ]
                        else:
                            if (var[3]=="I-ORG-SPO"):
                                org_spo += [ var[0]+"," ]
                            else:
                                if (var[3]=="I-ORG-MOT"):
                                    org_mot += [ var[0]+"," ]
                                else:
                                    if (var[3]=="I-ORG-COM"):
                                        org_com += [ var[0]+"," ]
                                    else:
                                        org_misc += [ var[0]+"," ]
                    else:
                        if(var[3] != "O" and var[3].split("-")[1]=="PER"):
                            if (var[3]=="I-PER-FRA"):
                                per_fra += [ var[0]+"," ]
                            else:
                                if (var[3]=="I-PER-UK"):
                                    per_uk += [ var[0]+"," ]
                                else:
                                    if (var[3]=="I-PER-GER"):
                                        per_ger += [ var[0]+"," ]
                                    else:
                                        if (var[3]=="I-PER-POR"):
                                            per_por += [ var[0]+"," ]
                                        else:
                                            if (var[3]=="I-PER-ITA"):
                                                per_ita += [ var[0]+"," ]
                                            else:
                                                if (var[3]=="I-PER-SPA"):
                                                    per_spa += [ var[0]+"," ]
                                                else:
                                                    if (var[3]=="I-PER-EUR"):
                                                        per_eur += [ var[0]+"," ]
                                                    else:
                                                        if (var[3]=="I-PER-ASI"):
                                                            per_asi += [ var[0]+"," ]
                                                        else:
                                                            if (var[3]=="I-PER-ARA"):
                                                                per_ara += [ var[0]+"," ]
                                                            else:
                                                                per_misc += [ var[0]+"," ]

    loc_asi = set(loc_asi)
    loc_eeuu = set(loc_eeuu)
    loc_ger = set(loc_ger)
    loc_ita = set(loc_ita)
    loc_spa = set(loc_spa)
    loc_uk = set(loc_uk)
    loc_isl = set(loc_isl)
    loc_chi = set(loc_chi)
    loc_ame = set(loc_ame)
    loc_afr = set(loc_afr)
    loc_eur = set(loc_eur)
    loc_misc = set(loc_misc)

    file_loc = open("loc-words-tot.txt","a+")
    file_loc.writelines(loc_asi)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_eeuu)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_ger)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_ita)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_spa)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_uk)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_isl)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_chi)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_ame)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_afr)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_eur)
    file_loc.writelines(";"+'\n')
    file_loc.writelines(loc_misc)
    file_loc.writelines(";")
    file_loc.close()

    org_spo = set(org_spo)
    org_pol = set(org_pol)
    org_mot = set(org_mot)
    org_com = set(org_com)
    org_misc = set(org_misc)


    file_org = open("org-words-tot.txt","a+")
    file_org.writelines(org_spo)
    file_org.writelines(";"+'\n')
    file_org.writelines(org_pol)
    file_org.writelines(";"+'\n')
    file_org.writelines(org_mot)
    file_org.writelines(";"+'\n')
    file_org.writelines(org_com)
    file_org.writelines(";"+'\n')
    file_org.writelines(org_misc)
    file_org.writelines(";"+'\n')
    file_org.close()

    per_fra = set(per_fra)
    per_uk = set(per_uk)
    per_ger = set(per_ger)
    per_por = set(per_por)
    per_ita = set(per_ita)
    per_spa = set(per_spa)
    per_eur = set(per_eur)
    per_asi = set(per_asi)
    per_ara = set(per_ara)
    per_misc = set(per_misc)

    file_per = open("per-words-tot.txt","a+")
    file_per.writelines(per_fra)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_uk)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_ger)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_por)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_ita)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_spa)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_eur)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_asi)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_ara)
    file_per.writelines(";"+'\n')
    file_per.writelines(per_misc)
    file_per.writelines(";"+'\n')
    file_per.close()
