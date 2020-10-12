import MySQLdb

# Un petit code pour remplir une base de données sur pythonanywhere.
# 
# Voici comment faire : 
#  0) Copiez-Collez ce code dans un fichier "python_to_db.py"sur votre 
#     compte Pythonanywhere.
#  1) Votre base de données doit s'appeler " mydb "
#  2) DANS LES 2 LIGNES CI-DESSOUS, 
#     a) insérez votre username à vous (entre tictics ) 
#        sur pythonanywhere à la place de 'mon_pseudo'
#     b) insérez lemot de passe de votre base de données 
#        entre (tictics) à la place de 'bbbbaaaa' 
#  3) Une fois que c'est fait, cliquez sur RUN ... Vous devez voir 
#     apparaître dans la console un message disant "c'est fait !" 
#  4) Vous pouvez alors fermer 


myusername='mon_pseudo'
mydbpassword='bbbbaaaa'

# --------------------  Connection à mydb

db=MySQLdb.connect(
    host=myusername+'.mysql.pythonanywhere-services.com',
    user=myusername,
    passwd=mydbpassword,
    db=myusername+'$mydb')
cursor = db.cursor ()

# --------------------  Nettoyage des tables (inutile si tout se passe bien)

def clear_tables() :
    for z in [ 'StudGroups', 'EDT', 'Students','Groups', 'Rooms', 'Slots', 'Teachers'] :
        cursor.execute( "DROP TABLE "+z)

# clear_tables()

# --------------------  Création des tables

cursor.execute ("CREATE TABLE Students(id INT AUTO_INCREMENT, firstname VARCHAR(50), lastname VARCHAR(50), PRIMARY KEY(id))")
cursor.execute ("CREATE TABLE Groups(id INT AUTO_INCREMENT, name VARCHAR(50), PRIMARY KEY(id))")
cursor.execute ("CREATE TABLE StudGroups(student_id INT AUTO_INCREMENT, group_id INT, FOREIGN KEY (student_id) REFERENCES Students(id), FOREIGN KEY (group_id) REFERENCES Groups(id))")
cursor.execute ("CREATE TABLE Teachers(id INT AUTO_INCREMENT, firstname VARCHAR(50), lastname VARCHAR(50), PRIMARY KEY(id))")
cursor.execute ("CREATE TABLE Rooms(id INT AUTO_INCREMENT, name VARCHAR(50), PRIMARY KEY(id))")
cursor.execute ("CREATE TABLE Slots(id INT AUTO_INCREMENT, time_start TIME, time_stop TIME, PRIMARY KEY(id))")
cursor.execute ("CREATE TABLE EDT(group_id INT, room_id INT, teacher_id INT, slot_id INT, FOREIGN KEY (group_id) REFERENCES Groups(id), FOREIGN KEY (teacher_id) REFERENCES Teachers(id), FOREIGN KEY (slot_id) REFERENCES Slots(id), FOREIGN KEY (room_id) REFERENCES Rooms(id) )")
cursor.execute ("CREATE TABLE Articles(student_id INT, text VARCHAR(250), FOREIGN KEY (student_id) REFERENCES Students(id))")
cursor.execute ("CREATE TABLE Friends(f1_id INT, f2_id INT, FOREIGN KEY (f1_id) REFERENCES Students(id), FOREIGN KEY (f2_id) REFERENCES Students(id))")



# --------------------  Remplissage des tables

Studs = [ ['Rim','H'], ['Khaled','L'], ['Mayssa','C'], ['Selim','G'], ['Lilia','K'], ['Youssef','A'], ['Nour','Z'], ['Aziz','B'], ['Sirine','B'], ['Beyram','B'],['Ines','T'],['Robert','L']]
Grps = [ 'NSI', 'Maths', 'SVT', 'Physique']
Teachs = [['Jallila', 'B'], ['Gael', 'C'], ['Maher', 'J']]
Rooms = ['Salle info 1', 'Salle info 2', 'B101', 'Labo Physique', 'Labo SVT']
Slots = [['08:00:00','10:00:00'],['10:00:00','12:00:00'],['12:00:00','14:00:00'],['14:00:00','16:00:00'],['16:00:00','18:00:00']]
StudGrps = [[1,1],[1,2],[2,1],[2,3],[3,1],[3,4],[4,1],[4,4],[5,1],[5,3],[6,1],[6,2],[7,1],[7,3],[8,1],[8,2],[9,1],[9,3],[10,1],[10,4],[11,2],[11,3],[12,3],[12,4]];
EDT=[[1,1,1,1],[2,3,3,2],[3,5,2,2],[2,5,3,3],[3,3,2,3],[4,5,3,4]]
Art=[[1,"qfhdhgxvsjhdfb<kcwbxTOTOwnbvxx,cbv,nxwbv"],[1,"bxTOTOwnbvxx,cbv,nxwbv"],[2,"bxqfbvwnbvxx,cbv,nxwbv"],[3,"eeTOTOwsd;,bvhbqshdbxvk"],[4,"ertTOTOwsd;,bvhbqshdbxvk"],[5,"ertwsd;,bvhbqshdbxvk"]]
Friends=[[1,2],[2,3],[4,5],[6,7],[6,1],[7,8]];

for x in Studs :
    cursor.execute ("INSERT INTO Students (firstname, lastname) VALUES ('{}','{}')".format(x[0],x[1]))
for x in Grps :
    cursor.execute ("INSERT INTO Groups (name) VALUES ('{}')".format(x))
for x in StudGrps :
    cursor.execute ("INSERT INTO StudGroups (student_id, group_id) VALUES ('{}','{}')".format(x[0],x[1]))
for x in Teachs :
    cursor.execute ("INSERT INTO Teachers (firstname, lastname) VALUES ('{}','{}')".format(x[0],x[1]))
for x in Rooms :
    cursor.execute ("INSERT INTO Rooms (name) VALUES ('{}')".format(x))
for x in Slots :
    cursor.execute ("INSERT INTO Slots (time_start,time_stop) VALUES ('{}','{}')".format(x[0],x[1]))
for x in EDT :
    cursor.execute ("INSERT INTO EDT (group_id, room_id, teacher_id, slot_id) VALUES ('{}','{}','{}','{}')".format(x[0],x[1],x[2],x[3]))
for x in Art :
    cursor.execute ("INSERT INTO Articles (student_id, text) VALUES ('{}','{}')".format(x[0],x[1]))
for x in Friends :
    cursor.execute ("INSERT INTO Friends (f1_id, f2_id) VALUES ('{}','{}')".format(x[0],x[1]))


db.commit()

# --------------------  Déconnection de mydb
db.close()

# --------------------  certif
print(" c'est fait ! Allez voir votre base de données ! ")

