# [TP1]
# Analyser et manipuler des données avec Python


# ========= 1. VARIABLES ET TYPES =========

## 1.1 Variables
# 1. Déclarer et initialiser deux variables x et y :

# x = 2
# y = 5

# puis calculer et afficher :
# a. La somme
# a = x + y

# b. La multiplication
# b = x * y

# c. La division 
# c = x / y


# 2. Afficher les types des résultats de vos calculs
# a. Les résultats des calculs

# print(a)
# print(b)
# print(c)

# b. Les types des résultats des calculs

# print(type(a))
# print(type(b))
# print(type(c))


# 3. Déclarer une variable de type chaine de caractère, puis afficher la valeur et le type 
# de cette variable.

# x = "Bonjour"
# print(x)
# print(type(x))

# 4. Expliquer et commenter ce code 

#   s = "Bonjour" # Déclaration d'une variable de type chaine de caractère

# Affiche le premier élément de la chaine de caractère
#   print(s[0]) 
# Affiche 2 premiers éléments de la chaine de caractère en partant de 0
#   print(s[0:2]) 
# Affiche 4 premiers éléments de la chaine de caractère en partant de 0
#   print(s[0:4]) 

# Affiche le dernier élément de la chaine de caractère
#   print(s[-1]) 
# Affiche 2 premiers éléments de la chaine de caractère en partant de -4
#   print(s[-4:2]) 
# Affiche les éléments de la chaine de caractère à partir de l'indice 3
#   print(s[3:]) 


## 1.2 Opérations avec des chaînes
# 1. Déclarer deux variables de type chaine de caractères ; 
# firstname et lastname, 

# firstname = "Jean"
# lastname = "Dupont"

# puis concaténer les deux variables avec une séparation par espace, et afficher le résultat.

# name = firstname + " " + lastname
# print(name)

# 2. Expliquer et commenter 

# fullname = 'SLIMANI Khadija' # Déclaration de la variable fullname
# fullname.split('M') # Split the string on the space caracter

# print(fullname.split('M')) # Affiche la liste des éléments de la chaine de caractère

# 'khadija' + 2 # Concatenation impossible 
# car on ne peut pas concaténer une chaine de caractère avec un entier


# price = 3.24 # Déclaration de la variable price
# num_items = 5 # Déclaration de la variable num_items
# year = 2018 # Déclaration de la variable year

# Affiche la chaine de caractère et les variables
# print('the price or the year is ', year, 'is', price) 
# Affiche la chaine de caractère et la variable num_items
# print("the price is %i" %num_items) 
# Affiche la chaine de caractère et la variable price
# print("the price is %f" %price) 
# Affiche la chaine de caractère et les variables year et price
# print("the price for the year %i is %f" %(year, price)) 
# Affiche la chaine de caractère et les variables num_items, price et num_items*price
# print('Jean bought () item(s) at a price of () each or a total of ()'.format(num_items, price, num_items*price))
# print('Jean bought 5 item(s) at a price of 3.24 each or a total of 16,2')


## 1.3 Les fonctions

# 1. Ecrire une fonction add_numbers qui prend deux nombres 
# et les additionne.

# def add_numbers(x, y):
#    return x + y 

# 2. Est-ce qu’une fonction peut être affectée à une variable ?






## 1.4 Expressions conditionnelles


# Tester ce code et commenter 

# x1 = 2 # Déclaration de la variable x1
# x2 = 7 # Déclaration de la variable x2

# Si x1 est supérieur à 5
# if x1 > 5:
    # # Affiche 'x1 is greater than 5'
    # print('x1 is greater than 5') 
# # Sinon
# else: 
    # # Affiche 'x1 is smaller than 5'
    # print('x1 is smaller than 5') 


# Tester ce code et commenter 

# x1 = 2 # Déclaration de la variable x1
# x2 = 7 # Déclaration de la variable x2

# Si x1 est supérieur à 5
# if x1 > 5 and x2 > 5: 
    # Affiche 'x1 and x2 are greater than 5'
    # print('x1 and x2 are greater than 5')
# Sinon si x1 est supérieur à 5
# elif x1 > 5 or x2 > 5:
    # Affiche 'x1 or x2 are greater than 5'
    # print('x1 or x2 is greater than 5')
# Sinon
# else:
    # Affiche 'x1 and x2 are smaller than 5'
    # print('x1 and x2 are smaller than 5')




# ========= 2. TYPES AVANCES =========
## 2.1 Listes

# 1. Déclarer et initialiser une liste
# liste = [1,2,3]

# 2. Afficher le contenu de la liste et son type
# print(liste)
# print(type(liste))

# 3. Les listes sont indexées de la même manière que les chaînes, 
# tester et commenter chaque ligne de ce code :

# x = [1,2,3,4,5,6,7,8,9,10] # Déclaration de la variable x

# Affiche le premier élément de la liste
# print(x[0])
# Affiche 2 premiers éléments de la liste en partant de 0
# print(x[1:3])
# Affiche 4 premiers éléments de la liste en partant de 0
# print(x[:2])
# Affiche le dernier élément de la liste
# print(x[-2:])
# Affiche 2 premiers éléments de la liste en partant de -4
# print(x[-1])
# Affiche les éléments de la liste à partir de l'indice 3
# print(x[::-1])


# 4. Les listes sont une structure de données mutable 
# ==> modifiée après la création, 
# expliquer ce code : 



# Ajoute 3.3 à la fin de la liste
# x.append(3.3) # Use append to append an object to a list
# Affiche la liste x
# print(x) 

# Change la valeur de l'indice 0 de la liste x de 1 à -1
# x[0] = -1 # Change the value of the first element from 1 to -1
# Affiche la liste x
# print(x) 


# 5. Ecrire le code qui permet de parcourir 
# et afficher chaque élément de la liste.

# nums = [1,2,3,4,5,6,7,8,9,10] # Déclaration de la variable nums

# Pour chaque élément de la liste nums
# for num in nums:
    # Affiche l'élément
    # print(num)



# 6. Expliquer et ajouter un commentaire pour ce code.

# Use + to concatenate lists
# print([1,2] + [3,4]) # Affiche [1,2,3,4]

# Use * to repeat lists
# print([1] * 3) # Affiche [1,1,1]

# Use the in operator to check if something is inside a list 
# print (1 in [1, 2, 3]) # Affiche True

# Use the in operator to check if something is inside the list 
# print ('Mimo' in ['Kimo', 'Mimo', 'dodo']) # Affiche True



## 2.2 Tuples

# 1. Déclarer un tuple, 
# puis afficher son contenu et son type.

# mon_tuple = ("Hello", "world")
# print(mon_tuple)
# print(type(mon_tuple))


# 2. Les tuples sont indexés de la même manière que les chaînes et les listes, 
# ils sont une structure dedonnées immuable 
# ==> ne peuvent pas être modifiés. 
# Commenter les lignes de code suivantes :




# Affiche le premier élément du tuple (Hello)
# print(t[0]) 
# Affiche le 2e et 4e élément du tuple (world, Welcome)
# print(t[1:3])
# Affiche tous les élements du tuple à partir de l'indice -2
# print(t[-2:])

# Déclaration de la variable t
# t = ("Hello", "world", "Welcome", "!", "test") 

# Change the value of the first element from 1 to -1 
# Does not work because tuples are immutable
# t[0] = -1 





## 2.3 Dictionnaires

# Les dictionnaires associent les clés aux valeurs.

# Déclaration du dictionnaire d
# d = {'khadija SLIMANI': 'slimani.khadija@qassil.com', 'Khadija SLIMANI': 'pr.kslimani@gmail.com' } 
# Affiche du dictionnaire d
# print(d) 
# Affiche du dictionnaire d et du type de d
# print(d, type(d))




# Les dictionnaires ne sont pas indexés de la même manière que 
# les chaînes, les listes ou les tuples, nous utilisons les clés à la place.

# Retrieve a value by using the indexing operator
# d['Khadija SLIMANI'] 



# Déclaration du dictionnaire d
# d = {'khadija SLIMANI': 'slimani.khadija@qassil.com', 'Khadija SLIMANI': 'pr.kslimani@gmail.com' } 

# 1. Récupérer les clés du dictionnaire
# d.keys()
# afficher les clés du dictionnaire
# print(d.keys())

# 2. Récupérer les valeurs du dictionnaire
# d.values()
# Afficher les valeurs du dictionnaire
# print(d.values())

# 3. Itérer sur tous les éléments (afficher « clés : valeur » de tous les éléments)
# for key, value in d.items():
    # print(key, value)






# ========= 3. DATE ET HEURE =========

# Détailler et expliquer chaque ligne de ce code :

# Importation du module datetime sous le nom dt
# import datetime as dt 
# Importation du module time sous le nom tm
# import time as tm 

# Affiche le temps en secondes depuis le 1er janvier 1970
# print(tm.time()) 

# Affiche la date et l'heure actuelle
# print(dt.datetime.now()) 

# Déclaration de la variable dtnow qui contient la date et l'heure actuelle
# dtnow = dt.datetime.fromtimestamp(tm.time()) 
# dtnow 

# get year, month, day, etc. from a datetime
# Récupérer l'année, le mois, le jour, l'heure, la minute 
# et la seconde de la date et l'heure actuelle
# dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second 

# Affiche le mois actuel
# print(dtnow.month) 

# Strftime met le mois actuel en abrégé
# dtnow.strftime('%b') 
# Affiche le mois actuel en abrégé
# print(dtnow.strftime('%b') )

# Création d'un objet timedelta qui contient 100 jours
# delta = dt.timedelta(days = 100) # create a timedelta of 100 days
# Affiche le type de la variable delta
# print(type(delta)) 
# Affiche le contenu de la variable delta
# print(delta)

# Créer une variable today qui contient la date actuelle
# today = dt.date.today() 
# Affiche la today (date actuelle)
# print(today) 
# Affiche le type de la variable today
# print(type(today)) 

# Today prends la valeur de today - delta
# today - delta # the date 100 days ago
# Affiche la valeur today
# print(today - delta)


# Comparaison entre today et today - delta 
# et voir si today est supérieur à today - delta
# today > today-delta # compare dates
# Affiche la valeur today
# print(today > today-delta) # Returns True










# ========= 4.COMPREHENSION LAMBDA ET LIST =========

# Commenter et expliquer le résultat de ce code :

# Déclaration de la fonction my_function qui prends 3 paramètres a, b et c
# et qui retourne la somme de a et b,
# le lambda sert à créer une fonction en une seule ligne
# my_function = lambda a, b, c : a + b   

# Appel de la fonction my_function avec les paramètres 1, 2 et 3, 
# my_function(1,2,3) 

# Affiche le résultat = 3
# print(my_function(1,2,3)) 



# Création d'une liste vide
# my_list = [] 
# Pour chaque nombre de 0 à 20
# for number in range(0, 20): 
    # si le nombre est divisible par 3
#    if number % 3 == 0:
        # ajouter le nombre à la liste my_list   
#        my_list.append(number) 
# affiche la liste my_list avec un message
# print('my_list contains the following items:', my_list) 

# Même fonctionnalité que le code précédent, mais plus optimisé
# my_list = [number for number in range(0,20) if number % 3 == 0] 
# my_list

# Affichage de my_list
# Correspond au même print que le précedent
# print(my_list)






# ========= 5.PYTHON NUMERIQUE (NumPy) =========

# Import de la librairie numpy, avec le nommage np
import numpy as np


# 1. Créer une liste 
# liste = [1,2,3]
# Afficher la liste
# print(liste)
# et la convertir en un tableau numpy.
# np.array(liste)
# affichage du tableau numpy
# print(np.array(liste))


# 2. Passer une ligne directement avec numpy
# np.array([1,2,3])
# Affichage du tableau numpy
# print(np.array([1,2,3]))


# 3. Passer une liste de listes pour créer un tableau multidimensionnel.
# Déclaration 2 lignes, 1 colonne, 3 éléments
shape = (2, 1, 3)
# Création du tableau multidimensionnel
data = np.ndarray(shape) 
# Affichage du tableau multidimensionnel
print(data) 




# 4. Trouver les dimensions du tableau. (rows, columns).



# 5. Expliquer le rôle et le résultat obtenu après l’utilisation de ces fonctions la classe numpy.
# a. arrange()


# b. reshape()


# c. linspace()


# d. ones()

# e. zeros()

# f. eye()


# 6. Créer un tableau à l'aide d'une liste répétitive.


# 7. Répète les éléments d'un tableau en utilisant la fonction .repeat().

















