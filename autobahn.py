DELTA_T=1/3600
DIST_MAX=100

class Car(object) :
    def __init__(self,position,speed) :
        self.position=position
        self.speed=speed

    def update(self,next_car) :
        #print(self.acceleration(next_car))
        self.position += DELTA_T * self.speed
        self.speed+=self.acceleration(next_car)* DELTA_T

class Constant_speed_car(Car) :
    def acceleration(self,next_car):
        return 0
class Excited_car(Car) :
    def acceleration(self,next_car):
        if next_car and next_car.position-self.position<3.2 :
            return (next_car.speed-self.speed*1.01)/DELTA_T
        else:
            return (160-self.speed)/(DELTA_T*100)

class Distracted_car(Car) :
    def acceleration(self,next_car):
        if self.position>=20 and self.position<=30:
            return (60-self.speed)/(20*DELTA_T)
        if next_car and next_car.position-self.position<3.2 :
            return (next_car.speed-self.speed*1.01)/DELTA_T
        else:
            return (130-self.speed)/(DELTA_T*100)

class Shift_car(Car) :
    def acceleration(self,next_car):
        if next_car :
            if next_car.position-self.position<.5 :
                return (next_car.speed-self.speed*1.01)/DELTA_T
            else:
                return (next_car.speed-self.speed)/(DELTA_T*360)
        else :
            return (130-self.speed)/(DELTA_T*360)

class Situation(object) :
    def __init__(self):
        self.list_cars=[]

    def update(self) :
        for i in range(len(self.list_cars)-1) :
            self.list_cars[i].update(self.list_cars[i+1])
        if len(self.list_cars)>0 :
            self.list_cars[-1].update(None)

    def pop_last_car(self) :
        self.list_cars.pop()

    def clean(self) :
        while len(self.list_cars)>0 and self.list_cars[-1].position > DIST_MAX :
            self.pop_last_car()

    def insert_new_car(self, car) :
        car.position=0
        self.list_cars.insert(0,car)

    def is_ok(self) :
        for i in range(len(self.liste_cars)-1) :
            if self.list_cars[i].position > self.list_cars[i+1].position :
                return False

def run(X,car,t,list_of_previous) :
    X.insert_new_car(car)
    N=int(t/DELTA_T)
    for i in range(N) :
        X.update()
        X.clean()
        list_of_previous.append([car.position for car in X.list_cars])

def simul(list_events):
    X=Situation()
    list_of_previous=[]
    for event in list_events :
        run(X,event[0],event[1], list_of_previous)
    print(len(list_of_previous))
    return list_of_previous

def visualize_state(list_of_positions,filename) :
    import matplotlib.pyplot as plt
    plt.figure(figsize=(15,2))
    plt.plot([0,102], [1,1], 'bo-')
    plt.plot([x for x in list_of_positions], [1 for _ in list_of_positions], 'ro')
    plt.axis('off')
    plt.savefig(filename)
    plt.close()

def visualize(list_of_lists_of_positions,number_of_pics):
    import os
    import imageio
    assert len(list_of_lists_of_positions)>=number_of_pics,'problem in making gif'
    s=len(list_of_lists_of_positions)//number_of_pics
    filenames = []
    for i in range(number_of_pics):
        filename = "c{}.png".format(str(i))
        filenames.append(filename)
        visualize_state(list_of_lists_of_positions[s*i],filename)
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    for filename in set(filenames):
        os.remove(filename)

def example1() :
    List=[ [ Constant_speed_car(0,120) , 0.1 ]  for _ in range(10) ]
    LOLOPOS=simul(List)
    visualize( LOLOPOS ,120)

def example2() :
    List=[  [Excited_car(0,120) , 0.02] for _ in range(1)]
    List+=[ [Distracted_car(0,120) , 0.02] ]
    List+=[ [Shift_car(0,120) , 0.02] for _ in range(50)]
    LOLOPOS=simul(List)
    visualize( LOLOPOS ,200)
