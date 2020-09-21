
# -------------------------------------------------------------------------
# ---------   ***        STACKS (= PILES)       ***   ---------------------
# -------------------------------------------------------------------------


# D'abord, nous commençons par implémenter les piles (= stacks). 
# On rappelle qu'il s'agit du modèle LIFO (Last In First Out), 
# adapté par exemple à la gestion de la navigation dans un navigateur Web
# (voir l'exemple 1)

# ------------ ** définition **

class stack(object) :
    """ Une classe dont les instances sont des piles """
    def __init__(self, top, substack) :
        assert type(substack)==stack or substack==None , "substack must be either empty or a stack"
        self.top = top
        self.substack = substack

    def push_on_top(self,elt) :
        if elt==None:
            pass
        self.substack=stack(self.top,self.substack)
        self.top=elt

    def pop_last(self) :
        ans=self.top
        self.top=self.substack.top
        self.substack=self.substack.substack
        return ans
    
    def __str__(self) :
        ans="    top : \n        "+str(self.top)+"\n    substack :\n"
        st=self.substack
        while st != None :
            ans+= "        "+str(st.top) + ' \n'
            st=st.substack
        return "stack : \n"+ ans     


# ------------ ** exemple 1 **

def ex1():
    V=stack(None,None)
    S1=stack("google.com",V)
    S2=stack("yahoo.fr",S1)
    S3=stack("Wikipedia.fr",S2)

    S3.push_on_top("youtube.com")
    print(S3)
    S3.pop_last()
    print(S3)

#ex1()

# ------------ ** questions **

# 1) Dans la fonction d'initialisation, à quoi sert la ligne 
#    assert type(substack)==stack or ...


# 2) Quelle est la différence entre les deux écritures suivantes :
#
#     S3.push_on_top("youtube.com") 
#     S4=stack("youtube.com",S3)

# 3) Écrire une méthode height() qui renvoie la hauteur de la pile

# 4) Écrire une méthode pop() qui vide la pile 
#
#     S3.push_on_top("youtube.com") 
#     S4=stack("youtube.com",S3)

# 5) Écrire une méthode insert_at bottom(elt) qui 
#     insère un élément en bas de la file. 
#

# 6) écrire une méthode get_reverse() qui renvoie la pile renversée 
#    (le résulat est donc une pile dont le top est le premier élément 
#    inséré dans self)




# -------------------------------------------------------------------------
# ---------   ***        QUEUES (= FILES)       ***   ---------------------
# -------------------------------------------------------------------------


# Ensuite, nous implémentons les files (= queues). 
# On rappelle qu'il s'agit du modèle FIFO (First In First Out), 
# adapté par exemple à la gestion de la navigation dans un navigateur Web
# (voir l'exemple 1)

# ------------ ** définition **

class queue(object) :
    def __init__(self,first,subqueue):
        self.first=first
        assert type(subqueue)==queue or subqueue==None , "subqueue must be either empty or a queue"
        self.subqueue=subqueue

    def enqueue(self,elt) :
        if elt==None :
            pass
        if self.first == None :
            self.first=elt
        elif self.subqueue == None :
            self.subqueue=queue(elt,None)
        else :
            self.subqueue.enqueue(elt)
    
    def dequeue(self) :
        if self.subqueue==None :
            ans=self.first
            self.first=None
            return ans
        else :
            ans=self.first
            self.first = self.subqueue.first
            self.subqueue = self.subqueue.subqueue
            return ans
        
    def __str__(self) :
        ans="    first : \n        "+str(self.first)+"\n    subqueue :\n"
        st=self.subqueue
        while st != None :
            ans+= "        "+str(st.first) + ' \n'
            st=st.subqueue
        return "queue : \n"+ ans     


def ex2():
    V=queue(None,None)
    V.enqueue('1')
    V.enqueue('2')
    V.enqueue('3')
    print(V)  
    V.dequeue()
    print(V)

# ------------ ** exemple 2 **


def ex2():
    V=queue(None,None)
    V.enqueue('1')
    V.enqueue('2')
    V.enqueue('3')
    print(V)  
    V.dequeue()
    print(V)

# ex2()

# ------------ ** questions **

# 1) Écrire une méthode length() qui donne la longueur de la file.

# 2) Écrire une méthode get_elt(i) qui renvoie le ième élément de la file

# 3) Écrire une méthode get_reverse() qui renvoie le la file inversée


# -------------------------------------------------------------------------
# ---------   ***  LINKED LISTS (= LISTES CHAÎNÉES)  ***   ----------------
# -------------------------------------------------------------------------



# Ensuite, nous implémentons les listes chaînées (= linked lists). 
# L'avantage de ces listes est une grande flexibilité vis-à-vis de l'insertion
# et de la délétion d'éléments 


# ------------ ** définition **

class linked_list_cell(object):
    def __init__(self,next_cell,content) :
        self.content=content
        assert type(next_cell)==linked_list_cell or next_cell==None, "next cell must be either empty or a cell"
        self.next_cell=next_cell 

class linked_list(object) :
    def __init__(self,first):
        assert type(first)==linked_list_cell or first==None, "next cell must be either empty or a cell"
        self.first=first

    def last(self) :
        ans= self.first
        while ans.next_cell != None :
            ans=ans.next_cell
        return ans

    def get_cell(self,index) :
        ans=self.first
        for i in range(index) :
            assert ans.next_cell != None , "this chain has no element at this position "+str(index) 
            ans=ans.next_cell
        return ans

    def append(self,content) :
        if content==None :
            pass
        self.last().next_cell=linked_list_cell(None,content)
    
    def __str__(self) :
        ans="   first : "+str(self.first.content)+"\n"
        n=self.first.next_cell
        while n != None :
            ans+= "    next : "+str(n.content) + ' \n'
            n=n.next_cell
        return "linked list : \n"+ ans     



# ------------ ** exemple 3 **


def ex3():
    LLC=linked_list_cell(None,'zbog')
    LL=linked_list(LLC)
    LL.append('woof')
    LL.append('miaw')
    print(LL)
    print(LL.get_cell(1).content)

#ex3()

# ------------ ** questions **

# 1) Écrire une méthode insert_cell(pos , content) qui rajoute une 
#    cellule en position pos dont le contenuest content

# 2) Écrire une méthode remove_cell(pos) qui retire la
#    cellule en position pos 

# 3) En surchargeant l'opérateur __add__ , écrire une méthode qui permet 
#    de mettre bout-à-bout deux listes chaînées. 