from PIL import Image
import h5py
import os
cwd = os.getcwd()
print(cwd)
save_dir = cwd+'/data/h5/train_img/'
print(save_dir)
h5file_in = h5py.File(cwd+'/data/h5/eu_NL333.h5', 'r')

for i in range(len(h5file_in['/train_imgs/'])):
    compound = h5file_in['/train_imgs/'][i]
    nm = str(compound[0])
    im = Image.fromarray(compound[1])
    im.save(save_dir+str(i)+'.png')

