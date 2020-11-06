from PIL import Image
import h5py
import os
import re

files_dir = '/data/h5/all_img/' #relative to this script
output_dir = '/data/h5/sem_seg_all/'

cwd = os.getcwd()
print(cwd)
save_dir = cwd+output_dir
print(save_dir)


for filename in os.listdir(cwd+files_dir):
    h5file_in = h5py.File(cwd+filename, 'r')
    for i in range(len(h5file_in['/train_imgs/'])):
        compound = h5file_in['/train_imgs/'][i]
        nm = str(compound[0])
        nm = nm.replace('b\'', '') #I am the lord of regex
        nm = nm.replace('\'', '')
        im = Image.fromarray(compound[1])
        im.save(save_dir+nm+'.png')

