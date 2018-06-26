#Import data from txt
import csv
import sys

#Cargamos los clusters
#with open('500_clusters_100k_words-wiki-completo.txt', 'rt') as f:

with open('Clusters.txt', 'rt') as f:

    a = []
    clusters = []
    tags_clus = []
    tags1_clus = []
    
    reader = csv.reader(f, delimiter=";")
    
    for row in reader:
        a.append (row) 


    for i in range(len(a)):
        var1 = a[i][0].split(':')
        #print(var1[0].split('-')[0] + str(i))
        tags_clus.append(var1[0].split('-')[0])
        tags1_clus.append(var1[0].split('-')[1])
        var = len(var1[1].split(','))
        clusters.append([None] * var)
        for j in range(var):
            clusters[i][j] = var1[1].split(',')[j]
    f.close()
             
#Cargamos Conll; repetir esta parte para todos los CONLL (testa,testb)      
with open('eng.train.txt', 'rt') as f:
    
    reader = csv.reader(f, quotechar='<', delimiter="\n")
    a=[]
    tags_old=[]

    for row in reader:
        a.append (row)
        #print(a)

    engtesta = [[None] * 4 for i in range(len(a))]

    for i in range(len(a)):
        if a[i] != []:        
            var = len(a[i][0].split(' '))
            tags_old.append(a[i][0].split(' ')[3])
            for j in range(4):
                #if j==0 and engtesta[i][j]=="s":
                    #engtesta[i][j] = '\''+a[i][0].split(' ')[j]
                #else:
                engtesta[i][j] = a[i][0].split(' ')[j]
                print(engtesta[i][j])
        else:
            engtesta[i][0]="\n"

                        
#Ahora haremos la comparacion en bucle buscando elementos

    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            for k in range(len(engtesta)):
                #print(engtesta[k][3], " ", str(k))
                #print("Comparo",engtesta[k][0],"con",clusters[i][j])
                if engtesta[k][3] != "O" and engtesta[k][0] != "\n":
                    #print(engtesta[k][3].split('-')[1] + " " + tags_clus[i])
                    if engtesta[k][3].split('-')[1] == tags_clus[i]: 
                        if engtesta[k][0].lower() == clusters[i][j].lower():
                            #print("Nueva palabra encontrada: ", engtesta[k][0], " Tag: ", tags_clus[i], "-", tags1_clus[i])
                            engtesta[k][3] = "I-"+tags_clus[i]+"-"+tags1_clus[i]
                            break
    f.close()
    

file = open('testfile_pruebas.txt', 'w')

for i in range(len(engtesta)):
    for j in range(4):
        if engtesta[i][0] != "\n":
            file.write(engtesta[i][j])
            if j != 3:
                file.write(" ")
        else:
            break
    file.write("\n")
        

file.close()

