import os
import shutil
import pandas as pd

# source file for texture mappings
texture_map = pd.read_csv('maps.csv', index_col=0)

# folders for pack i/o
input_folder = 'input'
output_folder = 'output'

def app():
    # main loop to rewrite images
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
        print('mapping <' + old_path + '> to <' + new_path + '>')

    # update pack.txt
    with open(output_folder + '/pack.txt', 'w') as pack:
        pack.write('Auto-Generated Textures for BTW!')

if __name__ == '__main__':
    app()
