import os
import pandas as pd

rootdir = os.getcwd()

map_1 = pd.read_csv('map_final.csv', index_col=0)

file_list = []

for subdir, dirs, files in os.walk(rootdir + '/BTW'):
    for file in files:
        if file[-3:] == 'png':
            file_list.append(os.path.join(subdir[len(rootdir)+1:], file))

missing_list = []

for texture in file_list:
    if texture not in [*map_1['BTW_filepath']]:
        missing_list.append(texture)

map_2 = pd.DataFrame(missing_list)
map_2.to_csv('missing.csv')
