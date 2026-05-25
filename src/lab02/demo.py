from lab02.model import Gym
from lab01.model import SportsmenInGym
def sc1():
    sp = Gym([])
    a = SportsmenInGym('Blex',True)
    a._number_of_visits = 100
    b =  SportsmenInGym('Anna',True)
    c = ['dbwe',True]
    sp.add(a)
    sp.add(b)
    print(sp)
    sp.remove(a)
    print(sp)
    sp.add(c)

def sc2 ():
    sp = Gym([])
    a = SportsmenInGym('Blex',True)
    a._number_of_visits = 100
    b =  SportsmenInGym('Anna',True)
    sp.add(a)
    sp.add(b)
    
    print(len(sp))
    for s in sp:
        print(s)
    sp.add(a)
def sc3():
    sp = Gym([])
    a = SportsmenInGym('Blex',True)
    a._number_of_visits = 100
    b =  SportsmenInGym('Anna',True)
    sp.add(a)
    sp.add(b)
    print(sp[0])
    print(sp.find_by_name('Anna'))
   # b =  SportsmenInGym('Anna',True) #['dbwe',True]
    #sp.add(b)#print(sp)
    #sp.remove(a)
    #print(sp)
    #sp.remove_at(1)
    sp.sort_by_name()
    print(sp)
def sc4():
    sp = Gym([])
    a = SportsmenInGym('Blex',False)
    a._number_of_visits = 100
    b =  SportsmenInGym('Anna',False)
    a.membership_activate()
    a.enter()
    b.membership_activate()
    b.enter()
    sp.add(a)
    sp.add(b)
    print(sp)
    sp.close_gym()
    print(sp)
    


if __name__ == '__main__':
    sc4()
