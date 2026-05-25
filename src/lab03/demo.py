from lab03.models import Trainer,EduSportsmen
from lab03.base import SportsmenInGym
from lab02.model import Gym
def sc1():
    a = Trainer('Anna',True,20,2,2000,5)
    print(a)
    a.add_seats(5)
    print(a)
    a.registration()
    print(a)
    b = EduSportsmen('Cin',True,1)
    b.registration(3)
    print(b)
    b.complited_workout()
    print(b)
def sc2():
    #Trainer('neafan',True,22,'deni',200,4)
    #Trainer('neafan',True,'wtf',5,200,4)
    #Trainer('neafan',True,11,1,200,4)
    #Trainer('neafan',True,22,10,200,4)
    b = EduSportsmen('Cin',True,1)
    a = Trainer('Anna',True,20,2,2000,5)
    li  = Gym([a,b])
    print (li)
    #li[1].registration(-5)
def sc3():
    t1 = Trainer('Anna',True,20,2,2000,5)
    t2 = Trainer('Alex',True,20,2,2000,5)
    t3 = Trainer('Jon',True,20,2,2000,5)
    s1 = EduSportsmen('Vladimir',True,1)
    s2 = EduSportsmen('Mik',True,1)
    s3 = EduSportsmen('Jane',True,1)
    sp = Gym([t1,t2,t3,s1,s2,s3])
    #print(sp)
    sp1 = sp.get_only_sportsmen()
    sp2 = sp.get_only_trainer()
    #print(sp1)
    print(sp2)
def main():
    sc3()
if __name__ == '__main__':
    main()