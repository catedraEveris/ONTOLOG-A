import csv
import sys

#Cargamos los clusters
#with open('500_clusters_100k_words-wiki-completo.txt', 'rt') as f:

with open('Clusters_pruebas.txt', 'rt') as f:

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
        tags_clus.append(var1[0])
        var = len(var1[1].split(','))
        clusters.append([None] * var)
        for j in range(var):
            clusters[i].append(var1[1].split(',')[j].lower()+",")

file = open("Cluster_noRepeat.txt","w")

for i in range(len(a)):
    clusters[i]=set(clusters[i])
    file.write(tags_clus[i]+":")
    for j in clusters[i]:
        file.write(str(j))
    file.write(";"+"\n")
file.close()
