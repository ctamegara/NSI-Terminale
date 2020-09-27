# Pour chaque question de chaque exercice, écrivez votre réponse juste sous la question, sans la mettre en commentaire.




# -----------------------  Exercices de niveau 0

# Exercice 1 :
# Écrire une fonction f qui prend un paramètre x et renvoie le résultat du calcul 3*x+7.

# Exercice 2 :
# Écrire une fonction f qui prend en paramètre un entier n et renvoie n+1. 
# La fonction doit s'assurer que n est bien un entier avant de répondre, 
# et renvoyer une AssertionError sinon. 


# Exercice 3 :
# Écrire une fonction f qui prend en paramètre le ph d'une solution chimique, et renvoie 
#        "Acide", ou "Neutre", ou "Basique suivant que le ph est <7, =7, ou >7.

# Exercice 4 :
# Écrire une fonction f qui prend en paramètre deux nombres réels, et renvoie le plus petit. 

# Exercice 5 :
# Écrire une fonction f qui prend en paramètre trois nombres réels, et renvoie le plus petit. 

# Exercice 6 :
# Écrire une fonction f qui prend en paramètre une liste quelconque de nombres réels, et renvoie le plus petit. 

# Exercice 7 : 
# La fonction x^7+x est strictement croissante. Écrire une fonction f qui prend en paramètre un nombre entier 
# N et renvoie le plus grand entier n pour lequel n^7+n < N.

# Exercice 8 : 
# Écrire une liste en compréhension 
# (c'est à dire du type [f(x) for x in liste])
# contenant les cubes des 10 premiers entiers naturels.



# ----------------------- Exercices de niveau 1 

# Exercice 9 :
# Pour gérer le parc des vélos en libre accès à Paris, la municipalité
# utilise des dictionnaires. 
# 
#  a) Pour chaque vélo, il y a un dictionnaire descriptif contenant les informations suivantes :
#  - "type", qui peut valoir "mécanique" ou "électrique"
#  - "station", qui correspond à la station où se trouve le vélo, ou, s'il est en déplacement, 
#               à la dernière station où il a été stationné.
#  - "statut", qui peut valoir "en déplacement", "disponible" ou "cassé"

#  Créer le dictionnaire descriptif D d'un vélo mécanique qui est en déplacement entre les stations
#               "Bibliothèque Nationale" et "Trocadéro".
#
# b) Pour stocker tous ces dictionnaires, la municipalité a attribué à chaque vélo un numéro. 
#               Ce numéro est unique : deux vélos n'ont pas le même numéro. 
#               Cela permet de stocker les informations de tous vélo sous la forme 
#               d'un dictionnaire Velos dont les clés sont les numéros, et les valeurs sont les dictionnaires descriptifs.
#               Ce dictionnaire est initialisé via la commande
Velos = {}
# 
#     i) Le vélo de la question a) n'est pas encore dans le dictionnaire Velos. Sachant qu'il porte le numéro 17,
#               quelle commande doit taper l'employé municipal pour l'y faire entrer ?
# 
#     ii) L'employé s'est trompé. Quelle commande doit-il taper pour retirer l'item qu'il vient d'ajouter dans Velos ?
#  
# c) La municipalité veut faire des simulations pour le traffic entre les 4 stations suivantes :
#               "Trocadéro", "Bibliothèque municipale", "Odeon" et "République". 
#               Elle demande à l'employé de remplir 
#               le dictionnaire Velos avec 200 items dont les numéros vont de 0 à 199, 
#               et dont les informations sont (toutes) choisies au hasard.
#               Importez la fonction randint depuis la librairie random, puis utilisez-la 
#               pour accomplir cette tâche.

# Exercice 10 : Dans un réseau social, les utilisateurs sont rangés via leurs pseudonymes dans une liste dictionnaire :

RS=["Marc Montagne-de-Sucre" , "Bill Portes" , "Beya On-Sait", "Steeve Travaux" , "Oum Caleçon" , "Michèle Haut-Mais-Bas", "Emmanuel Macaron", "Vladimir Built-In", "Hosni Mou-Obama", "Mickel Jacques-Fils", "Hussein Taxi" , "Steeve Super", "Didier Wonder", "Cameleon Diaz", "Pic-à-chou", "Capitaine Églefin", " Donald Trompette" , "Ronaldo de Assis Moreira", "Johnny Vacances"]



# Deux utilisateurs peuvent être amis sur le réseau, ou pas. Le réseau retient ces informations
# dans une liste contenant les indices des couples d'amis :

Amis=[[1, 5], [8, 9], [4, 8], [0, 8], [10, 16], [1, 17], [3, 17], [12, 14], [17, 19], [3, 11], [11, 14], [5, 16], [4, 15], [15, 17], [5, 18], [10, 13], [3, 16], [15, 19], [4, 16], [6, 8], [3, 9], [5, 19], [12, 14], [10, 12], [11, 14], [8, 15], [13, 14], [11, 13], [8, 17], [4, 9], [4, 9], [3, 11], [0, 11], [2, 18], [7, 17], [14, 19], [3, 6], [10, 15], [2, 16], [5, 7], [0, 7], [5, 13], [5, 14], [12, 13], [9, 18], [1, 11], [6, 18], [13, 17], [4, 13], [16, 17]]

# 
# Par exemple, le premier couple nous dit que "Bill Portes" et "Michèle Haut-Mais-Bas" sont amis.

# 0) Écrire une fonction qui prend en argument un pseudonyme et retourne son indice dans la liste RS.

# 1) Écrire une fonction qui prend en argument deux entiers et retourne 
#                 True si les utilisateurs correspondants sont amis, et False sinon.

# 2) Écrire une fonction qui prend en argument deux pseudonymes et retourne 
#                 True si les utilisateurs correspondants sont amis, et False sinon.

# 3) Deux utilisateurs peuvent devenir amis. Écrire une fonction qui prend en argument 
#                 deux entiers a et b avec a<b, et ajoute le couple (a,b) dans la liste Amis.

# 4) Deux utilisateurs peuvent rompre leur relation. Écrire une fonction qui prend en argument 
#                 deux entiers a et b avec a<b, et retire le couple (a,b) de la liste Amis.

# 5) Écrire une fonction qui prend en argument un entier et retourne la liste des couples de la liste Amis 
#                 qui contiennent cet entier.

# 5) Écrire une fonction qui prend en argument un pseudonyme et retourne la liste des pseudonymes de
#                 ses amis

# 6) Écrire une fonction qui prend en argument deux numéros d'utilisateurs et retourne 
#                 True s'ils ont un ami commun, et False sinon.




