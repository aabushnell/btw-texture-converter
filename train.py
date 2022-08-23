import os
import imageio.v3 as iio
import pandas as pd

rootdir = os.getcwd()

van_dict = {}
btw_dict = {}

for subdir, dirs, files in os.walk(rootdir + '/1.18'):
    for file in files:
        if file[-3:] == 'png':
            van_dict[file[:-4]] = os.path.join(subdir[len(rootdir)+1:], file)

for subdir, dirs, files in os.walk(rootdir + '/BTW'):
    for file in files:
        if file[-3:] == 'png':
            btw_dict[file[:-4]] = os.path.join(subdir[len(rootdir)+1:], file)

mapping_dict = {'1.18_filename': [], 'BTW_filename': [], '1.18_filepath': [], 'BTW_filepath': []}

for k_van, v_van in van_dict.items():
    im_van = iio.imread(v_van)
    for k_btw, v_btw in btw_dict.items():
        im_btw = iio.imread(v_btw)
        if im_van.shape == im_btw.shape and (im_van == im_btw).all():
            print('match!')
            print(f'mapping {v_van} to {v_btw}')
            mapping_dict['1.18_filepath'].append(v_van)
            mapping_dict['BTW_filepath'].append(v_btw)
            mapping_dict['1.18_filename'].append(k_van)
            mapping_dict['BTW_filename'].append(k_btw)

mapping_df = pd.DataFrame.from_dict(mapping_dict)
mapping_df.to_csv('mappings.csv')
