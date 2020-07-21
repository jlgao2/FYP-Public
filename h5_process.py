from PIL import Image
import h5py
import os
import re

file_dir = '/data/h5/eu_AT130.h5' #relative to this script
output_dir = '/data/h5/sem_seg/'

cwd = os.getcwd()
print(cwd)
save_dir = cwd+output_dir
print(save_dir)
h5file_in = h5py.File(cwd+file_dir, 'r')

for i in range(len(h5file_in['/train_imgs/'])):
    compound = h5file_in['/train_imgs/'][i]
    nm = str(compound[0])
    nm = nm.replace('b\'', '') #I am the lord of regex
    nm = nm.replace('\'', '')
    im = Image.fromarray(compound[1])
    im.save(save_dir+nm+'.png')

