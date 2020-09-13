######### Fichier à renvoyer rempli avant lundi 14 Septembre à 16h

# Exercice 1 :

# On définit la classe suivante :

class mystery(object) :
    def __init__(self,tic, tac) :
        self.tac = tic
        self.tic = tac

# Quels sont les attributs de cette classe ?
# Réponse :

# On définit a=mystery( 'plip' , 'plop' ) . Quelle est la valeur de a.tic ?
# Réponse :

# On pose X=[ mystery(i,i+1) for i in range(1000)]. Quelle est la valeur de X[100].tic ?
# Réponse :


# Exercice 2 :

# On définit la classe suivante :

class student(object) :
    def __init__(self, name, mail) :
        self.name = name
        self.notes=[]

    def insert_note(self, new_note) :
        self.notes.append(new_note)

    def mean(self) :
        s=0
        for x in self.notes :
            s+=x
        return s/len(notes)

# Le code suivant donne une erreur ... pourquoi ?
# A=student('Nour')
# A.mean()
#
# Réponse :

# Que fournit le code suivant ?
#  B=student('Olfa')
#  B.insert_note(7)
#  B.insert_note(10)
#  B.mean()
# Réponse :


# Exercice 3 :
# ajouter dans la définition précédente (celle de la classe student) une méthode get_last_note() 
# telle que pour un étudiant E, la valeur de E.get_last_note()
# soit la dernière note entrée.

# Exercice 4 :
# On définit les classe suivantes :

class message(object) :
    def __init__ (self,exp,dest,content):
        self.exp=exp
        self.dest=dest
        self.message=message

class mail_server(object) :
    def __init__(self):
        self.data=dict()

    def store(self,m) :
        if m.dest.name in self.data.keys() :
            self.data[m.dest.name].append(m)
        else :
            self.data[m.dest.name]=[m]

    def serve(self,user):
        if  user.name in self.data.keys() :
            return self.data[user.name]

    

MS=mail_server()

class user(object) :
    def __init__ (self,name):
        self.name=name
        self.recieved = []
        self.sent = []

    def send(self,dest,content):
        m=message(self,dest,content)
        self.sent.append(m)
        MS.store(m)

    def upload(self) :
        self.recieved=MS.serve(self)


user1=user('Nour')
user2=user('Inès')
user3=user('Habib')

user3.send(user1,"salut beauté")
user3.send(user2,"salut beauté")
user1.upload()
user1.send(user3,"salut relou")
user2.send(user1,"Hey, t'as des nouvelle d'Habib")
user1.upload()
user1.send(user2,"Non")
user2.upload()
user2.send(user3,"on se voit ce soir ?")
user2.send(user1,"moi non plus")
user3.upload()

# À ce moment de la conversation, que vaut user3.recieved ?
# 
# Réponse : 

