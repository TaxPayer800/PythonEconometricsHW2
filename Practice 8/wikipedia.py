

destinations2 = ['Milan','New_York','London','Paris','Singapore','Buenos_Aires','Madrid','Moscow','Tokio','San_Antonio','Seattle','Amsterdam','Boston','Athens','Berlin','Dublin','Florence','Rome','Prague','Dubai','Cape_Town','Bruges','Lima','Toronto','Beijing']



def wiki(city):
    '''city = the keyword of the search you want to perform
    on Wikipedia (to be inserted in quotation marks).
    If the term is composed, use "_" instead of space'''
    import webbrowser
    webbrowser.open('https://en.wikipedia.org/wiki/' + city)




def wiki2(cities_list):
    import random, webbrowser
    city = cities_list[random.randint(0, len(cities_list)-1)]
    webbrowser.open('https://en.wikipedia.org/wiki/' + city)
    return "The chosen city is " + city



def wiki3(cities_list):
    import random, webbrowser
    number = int(input("How many cities do you want to visit? "))
    to_be_visited = []
    for i in range(number):
        city = cities_list[random.randint(0, len(cities_list)-1)]
        webbrowser.open('https://en.wikipedia.org/wiki/' + city)
        to_be_visited.append(city)
    return to_be_visited
