import os
import shutil
import pandas as pd

texture_map = pd.read_csv('map_final.csv', index_col=0)

input_file = 'texture_packs/Excalibur_V1.18.1'
output_file = 'output'

for index, row in texture_map.iterrows():
    oldpath = input_file + row['1.18_filepath'][4:]
    newpath = output_file + row['BTW_filepath'][3:]
    if os.path.exists(oldpath):
        if not os.path.exists(os.path.dirname(newpath)):
            os.makedirs(os.path.dirname(newpath))
        shutil.copy(oldpath, newpath)
    print(oldpath, newpath)

with open(output_file + '/pack.txt', 'w') as pack:
    pack.write('Auto-Generated Textures for BTW!')
