import os
import imageio.v3 as iio
import pandas as pd

root_dir = os.getcwd()

input_dir = '/1.18'
output_dir = '/BTW'


def scrape_textures(p):
    d = {}
    for subdir, dirs, files in os.walk(p):
        for file in files:
            if file[-3:] == 'png':
                d[file[:-4]] = os.path.join(subdir[len(root_dir) + 1:], file)
    return d

vanilla_dict = scrape_textures(root_dir + input_dir)
btw_dict = scrape_textures(root_dir + output_dir)

mapping_dict = {'1.18_filename': [], 'BTW_filename': [], '1.18_filepath': [], 'BTW_filepath': []}

for k_van, v_van in vanilla_dict.items():
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
