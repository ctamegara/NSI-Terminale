# Dans ce fichier, nous allons 
#   - créer des classes, 
#   - définir des attributs et des méthodes, 
#   - instancier quelques objets,
#   - surcharger des opérateurs,
#   - définir des classes héritant d'autres classes.


##################### Premier exemple (attributs) #############################

class singer(object) :
    """ ceci est une classe dont les instances sont des chanteurs."""

    def  __init__(self, first_name, last_name) :
        self.first_name = first_name
        self.last_name = last_name



# C'est une classe qui n'a que deux attributs : le prenom et le nom


# Une instance de la classe singer est définie comme suit :

A=singer("Oum","Kaltoum")

# Pour retrouver le prénom de A : tapez "A.fist_name". 
# Devinez comment retrouver le nom de famille de A.

# Créez un objet B de la classe singer correspondant à la chanteuse Emel Mathlouti.


# Note : lorsque l'on définit une classe, on insère souvent une "documentation". 
# C'est le rôle de la chaîne de caractères qui se trouve juste après la déclaration.
# Pour y accéder, on saisit par exemple "print(A.__doc__)"
#  

##################### Deuxième exemple #############################

# Créez une classe "mobile" dont les objets ont pour attributs :
# - une couleur
# - une abscisse
# - une ordonnée




##################### Troisième exemple (méthodes) #############################

# Pour définir une méthode, on s'y prend comme suit :

# On aura besoin d'une fonction auxiliaire calculant 
# le pgcd de deux nombres entiers positifs non tous deux nuls :

def gcd(a,b) :
    if a==0 and b!=0 : 
        return b
    elif a>b : 
        return gcd(b,a)
    else :
        return gcd (b%a,a)


class rational(object) :
    """ ceci est une classe dont les instances sont des nombres rationnels."""

    def  __init__(self, num, den) :
        self.denominator = den
        self.numerator = num

    def reduce(self) :
        d=gcd(abs(self.numerator),abs(self.denominator))
        self.denominator = self.denominator // d
        self.numerator = self.numerator // d

    def equal(self,x) :
        return self.denominator * x.numerator == self.numerator * x.denominator

    def display(self) :
            print( str(self.numerator) +" / "+ str(self.denominator)) 

# On appelle ensuite ces méthodes de la façon suivante :

# y = rational(22,121)
# y.display()

# y.reduce()
# y.display()

# x = rational (36,198)
# print( x.equal(y) )



        

##################### Deuxième exemple (suite) #############################

# Reprenez votre classe "mobile" et ajoutez-lui 
# - une méthode "display" qui affiche ses attributs, 
# - une méthode "translate" qui prend 2 paramètres "dx" et "dy" et transforme ajoute dx à 
# l'abscisse du mobile, et dy à son ordonnée. 




##################### Quatrième exemple (surcharge) #############################

# Lorsque 2 objets A et B de la même classe sont créés, 
# on voudrait dire qu'ils sont égaux s'ils ont les mêmes attributs.
# Python ne fait pas ça ... testez :

#A = singer("Jacques","Brel")
#B = singer("Jacques","Brel")
#A==A
#A==B

# Cela s'explique. Rien ne nous dit qu'il n'existe pas, par exemple, 
# deux chateurs qui ont le même nom et le même prénom.

# De plus, comme on l'a vu avec l'exemple des nombres rationnels, il arrive
# aussi que l'on veuille considérer que deux objets sont égaux même si leurs 
# attributs sont a priori différents.

# On a la possibilité de "surcharger" l'opérateur "==" de la façon suivante

class time(object) :
    """ une classe dont les instances sont des temps."""

    def  __init__(self, h, m, s) :
        self.h = h
        self.m = m
        self.s = s

    def convert (self) :
        return 3600*self.h+60*self.m+self.s

    def __eq__(self, t) :
        return self.convert() == t.convert()

    def __str__(self) :
        return str(self.h) + " h " + str(self.m) + " m " + str(self.s) + " s"

#t1=time(5,90,2)
#t2=time(6,30,2)

#print(t1==t2)

#Comme vous le voyez, on a aussi surchargé une méthode "str" ... tapez ceci pour voir 
# à quoi ça sert :




##################### Troisième exemple (suite) #############################

# Reprenez la définition de la classe "rational", et surchargez 
# -   l'opérateur "==" (via " def __eq__ " comme ci-dessus)
# -   l'opérateur " + " (via " def __add__ ")
# -   l'opérateur " * " (via " def __mul__ ")
# -   la méthode str (via def __str__") pour remplacer la méthode "display".




##################### Cinquième exemple (héritage) #############################

from math import sqrt

class point(object) :
    """ une classe dont les instances sont des points du plan."""

    def  __init__(self, x, y) :
        self.x = x
        self.y = y

def dist (p1,p2) :
    return sqrt( (p2.x-p1.x)**2 + (p2.y-p1.y)**2 )

class polygon(object) :
    """ une classe dont les instances sont des polygones."""
    def __init__(self, vertices) :
        self.vertices=vertices

    def n_vert(self) :
        return len(self.vertices)

    def perimeter(self) :
        ans=0
        for i in range( self.nvert-2 ) :
            ans+=dist(self.vertices[i],self.vertices[i+1])
        ans+=dist(self.vertices[self.nvert-1],self.vertices[0])

# Rien de nouveau pour l'instant. Mais lorsqu'on étudie les polygones, 
# on a des méthodes et des définitions supplémentaires dans le cas des triangles, 
# ou bien dans le cas des quadrilatères etc. On ne veut pas créer une nouvelle 
# classe pour chacun de ces cas particuliers, et devoir réécrire les méthodes déjà disponibles.
 
class triangle(polygon) :
    """ une classe dont les instances sont des triangles."""

    def is_right(self) :
        a = dist(self.vertices[0], self.vertices[1])
        b = dist(self.vertices[1], self.vertices[2])
        c = dist(self.vertices[2], self.vertices[0])
        lengths=[a,b,c]
        lengths.sort()
        return lengths[2]**2 - lengths[1]**2 - lengths[0]**2 == 0

    def is_equilateral(self) :
        a = dist(self.vertices[0], self.vertices[1])
        b = dist(self.vertices[1], self.vertices[2])
        c = dist(self.vertices[2], self.vertices[0])
        return a == b and b == c



class quadrilateral(polygon) :
    """ une classe dont les instances sont des quadrilatères."""

    def is_parallelogram(self) :
        A=self.vertices[0]
        B=self.vertices[1]
        C=self.vertices[2]
        D=self.vertices[3]
        vec1 = (A.x-B.x,A.y-B.y)
        vec2 = (D.x-C.x,D.y-C.y)
        return vec1 == vec2


#t= triangle( [point(0,0) , point(0,3), point(4,3)] )
#print( t.is_right() )
#print( t.is_equilateral() )

#q = quadrilateral( [ point(0,0),point(2,1),point(3,2),point(1,1) ] )

#print( q.is_parallelogram() )
