

import os

path = "C:\\Sample files\\"

print(os.listdir(path))

for file in os.listdir(path):
    if file == 'Raw_data.xlsx':
        os.rename(path + file, path + input('How do you want to rename the file Raw_data.xlsx? '))
        print(os.listdir(path))
