from lab04.models import Trainer,EduSportsmen,SportsmenInGym
from lab05.collection import Gym
from lab04.interfaces import Video, Human
from lab05.strategies import    make_type_filter, make_price_filter,make_name_sorter, make_price_sorter, make_state_type_sorter,Activate,Close

b = EduSportsmen('Cin',True,1)
a = Trainer('Anna',True,20,2,2000,5)
c = EduSportsmen('Bin',True,1)
d= Trainer('Dir',True,20,2,1500,5)
e= Trainer('Pir',False,20,2,1600,5)
f = EduSportsmen('Fin',False,1)
g = SportsmenInGym('Alex', False)
sp = Gym([a,b,c,d,e,f,g])
def sc1():
    print(sp)
    print('~'*50)
    #sp.sort_by(make_name_sorter())
    sp.sort_by(make_price_sorter(), reverse=True)
    #sp.sort_by(make_state_type_sorter(), reverse=True)
    print(sp)
    print('~'*50)
    only_sportsmen = sp.filter_by(make_type_filter(EduSportsmen))
    print(only_sportsmen)
    print('~'*50)
    close_gym = Close()
    only_sportsmen.apply(close_gym)
    print(only_sportsmen)
    # only_trainers = sp.filter_by(make_type_filter(Trainer))
    # print(only_trainers)
    # print(sp)
    # sp.sort_by(make_state_type_sorter(), reverse=True)
    # print(sp)
    #print(sp.filter_price())
    
    

def sc2():
    names = list(map(lambda x: x.name, sp))
    print(names)
    budget_ones = sp.filter_by(make_price_filter(1600))
    print(budget_ones)
def sc3():
    print(sp)
    print('-'*50)
    close_gym = Close()
    sp2 = (sp.filter_by(make_type_filter(EduSportsmen)).apply(close_gym))
    print(sp2)

def main():
    sc2()
if __name__ == '__main__':
    main()