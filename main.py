import os
import shutil
import pandas as pd

texture_map = pd.read_csv('maps.csv', index_col=0)

input_folder = 'texture_packs/Excalibur_V1.18.1'
output_folder = 'output'

for index, row in texture_map.iterrows():
    old_path = input_folder + row['vanilla_path']
    new_path = output_folder + row['btw_path']
    if os.path.exists(old_path):
        if not os.path.exists(os.path.dirname(new_path)):
            try:
                os.makedirs(os.path.dirname(new_path))
            except FileExistsError as e:
                print(e)
        shutil.copy(old_path, new_path)
    print(old_path, new_path)

with open(output_folder + '/pack.txt', 'w') as pack:
    pack.write('Auto-Generated Textures for BTW!')
