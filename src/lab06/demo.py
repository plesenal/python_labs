from lab06.container import TypedCollection,A,P
from lab04.models import Trainer,EduSportsmen,SportsmenInGym
from lab04.interfaces import Video, Human
from lab05.strategies import    make_type_filter, make_price_filter,make_name_sorter, make_price_sorter, make_state_type_sorter,Activate,Close,profitable
b = EduSportsmen('Cin',True,1)
a = Trainer('Anna',True,20,2,2000,5)
c = EduSportsmen('Bin',True,1)
d= Trainer('Dir',True,20,2,1500,5)
e= Trainer('Pir',False,20,2,1600,5)
f = EduSportsmen('Fin',False,1)
g = SportsmenInGym('Alex', False)
sp = [a,b,c,d,e,f,g]
li = TypedCollection[SportsmenInGym]()
for i in sp:
    li.add(i)
def sc1():
    print(li)
    #print(li.filter_by(make_state_type_sorter()))
    for i in li:
        print(i)
def sc2():
    print(li.find(make_type_filter(Trainer)))
    er = li.find(lambda x: hasattr(x, 'price') and x.price > 10000)
    print(er)
    a = li.filter(make_price_filter(1600))
    print(a)
    print(li.map(lambda x: x.name))
def sc3():
    gym = TypedCollection[P]()
    gym.add(a)
    gym.add(b)
def main():
    sc2()
if __name__ == '__main__':
    main()