# ONTOLOGIA
Reconocimiento de entidades + Clusterización

Clustering
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
2. Ejecución de _clusterToTags.py_ en _testa.txt y testb.txt_
```
python clustersToTags.py
```
3. Comprobación de resultado y corrección de errores
4. Ejecución de _obtainCategoriesCONLL.py_ para obtener las palabras que se han corregido o las palabras que no estaban etiquetadas para añadirlas a los clústeres existentes. 
```
python obtainCategoriesCONLL.py
```
5. Ejecución de _rmClusterDuplicates.py_ para eliminar los elementos duplicados de los clústers.
```
python rmClusterDuplicates.py
```
6. Realización del paso 2, pero con _filetrain.txt_

NER
--------------------

Para la realización se han utilizado 2 redes BI-LSTM (recurrentes) una escrita con la librería Keras y otra con TF. 

Mirar el README.md de cada uno en las carpetas correspondientes. 

En Keras el código está optimizado para utilizarlo con _word embeddings_ de dimensión 300.

Resultados
--------------------

### TensorFlow ###

(15 epochs)
acc 94.90 - f1 63.65
train loss: 0.4756
```
Michael   loves visiting Morocco   
I-PER-EUR O     O        I-LOC-AFR 

Li    Yung  loves playing in Japan     
I-PER I-PER O     O       O  I-LOC-ASI 
```

Aquí podemos observar que al no estar muy balanceado el dataset y debido al gran número de etiquetas que existen no siempre se consigue el resultado óptimo.

### Keras ###

avg f1 fold scores so far:  0.6769426773003454

f1 fold scores:  [0.6815258040388931, 0.6723595505617977]

final avg f1 fold scores:  0.6769426773003454


![Accuracy](https://github.com/catedraEveris/ONTOLOG-A/blob/master/tensorboard/acc.png)![Loss](https://github.com/catedraEveris/ONTOLOG-A/blob/master/tensorboard/loss.png)

![fold0](https://github.com/catedraEveris/ONTOLOG-A/blob/master/Results/Fold0.png)![fold1](https://github.com/catedraEveris/ONTOLOG-A/blob/master/Results/Fold1.png)

Collaboratory
--------------------
Aquí se detallan los pasos para la ejecución en el entorno de Google Drive. 

1. Subir archivos a Drive
2. Crear un nuevo archivo con doble click. (Connect more apps)
3. Añadir Colab a Drive. 
4. Cambiar configuración del entorno a Python 3 y GPU.
5. Para linkear el colaborative con tu unidad de Google drive:
```
!apt-get install -y -qq software-properties-common python-software-properties module-init-tools
!add-apt-repository -y ppa:alessandro-strada/ppa 2>&1 > /dev/null
!apt-get update -qq 2>&1 > /dev/null
!apt-get -y install -qq google-drive-ocamlfuse fuse
from google.colab import auth
auth.authenticate_user()
from oauth2client.client import GoogleCredentials
creds = GoogleCredentials.get_application_default()
import getpass
!google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret} < /dev/null 2>&1 | grep URL
vcode = getpass.getpass()
!echo {vcode} | google-drive-ocamlfuse -headless -id={creds.client_id} -secret={creds.client_secret}


!mkdir -p drive
!google-drive-ocamlfuse drive
```


Líneas futuras
--------------------

- Realizar el proceso de tagging con mas detalle, ya que debido a la gran carga de trabajo que conlleva, el resultado del trabajo que hemos realizado es aceptable para un primer acercamiento, pero se debe comprobar más detalladamente el correcto etiquetado. 
- Reducir el número de etiquetas y crear clústers correspondientes a las mismas. 
- Avanzar en el estudio de ontologías, realizando el siguiente paso que sería NEL (Name ENTITY LINKING)
- Opcional, crear una interfaz gráfica para una mejor visión de los resultados

## Referencias

[1] Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. [GloVe: Global Vectors for Word Representation](https://nlp.stanford.edu/pubs/glove.pdf).

[2] Thomas Jungblut [Keras Conv+BiLSTM for Named Entity Recognition] (https://github.com/thomasjungblut/ner-sequencelearning)

[3] Guillaume Genthial [Named Entity Recognition with Tensorflow] (https://github.com/guillaumegenthial/sequence_tagging)
