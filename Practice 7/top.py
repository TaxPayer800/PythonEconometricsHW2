import random

destinations = ['Milan','New York','London','Paris','Singapore','Buenos Aires','Madrid','Moscow','Tokio','San Antonio','Seattle','Amsterdam','Boston','Athens','Berlin','Dublin','Florence','Rome','Prague','Dubai','Cape Town','Bruges','Sao Paulo','Toronto','Beijing']

def top_cities(cities_list,num=5):
    top={}
    for i in range(1,num+1):
     rnd_num = random.randint(0,len(cities_list)-1)
     top[i] = cities_list[rnd_num]
    return top
    
def top_cities2(cities_list,num=5):
    top={}
    i=1
    while len(top) < num:
     rnd_num = random.randint(0, len(cities_list)-1)
     if cities_list[rnd_num] not in top.values():   
          top[i] = cities_list[rnd_num]
          i=i+1
    return top
