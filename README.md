# ONTOLOGIA
Reconocimiento de entidades + Clusterización

Clusterización
------------------

Para crear categorías y poder añadirlas a nuestra base de datos (ConLL) hemos usado clusterización a partir de [1], que se basa en el uso de word embeddingss (Glove.6B), y hemos utilzado de 300d para poder obtener clúster más específicos.

```
python3 word_clustering.py --num_words 100000 --num_clusters 500 --vector_dim 300

```
Hemos realizado pruebas con diferente número de dimensiones y número de clúster finales, pero el mejor resultado ha sido obtenido con 100000 palabras y 500 clústers.


Tagging
--------------------

Hemos creado 3 códigos de etiquetado que etiquetan el coNLL 2003 a partir de los clústers creados. 

1. Limpieza y composición manual de clústers. 
2. Ejecución de clusterToTags.py en testa.txt y testb.txt
```
python clustersToTags.py
```
3. Comprobación de resultado y corrección de errores



+ rmClusterDuplicates.py (Elimina todas las palabras dentro de un mismo clúster dobles)
+  (Rellena el 
+ obtainCategoriesCONLL.py

```
python rmClusterDuplicates.py
```


## Referencias

[1] Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf).
