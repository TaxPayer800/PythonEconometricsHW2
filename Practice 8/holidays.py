
import webbrowser

path = "C:\\Sample files\\"

new_file = open(path + 'holidays.txt', 'a')

new_file.write('City\tWeb address\n')

answer = "Y"

while answer.upper() == "Y":
    my_town = input('Enter the city you want to visit: ')
    new_file.write(my_town + '\thttps://en.wikipedia.org/wiki/'+ my_town + '\n')
    webbrowser.open('https://en.wikipedia.org/wiki/' + my_town)
    answer = input("Do you want to visit another city? (Y/N) ")

new_file.close()

