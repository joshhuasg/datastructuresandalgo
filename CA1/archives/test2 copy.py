import numpy as np

z = [['.', '.', '.']]
p = [['.', ',', '-', '.']]
c = [['.', '.', '.', '.']]
zer = [['_', '_', '_', '_', '_']]


p = np.transpose(p)
z = np.transpose(z)
if len(p) != len(z):
    if len(p) < len(z):
        blank = np.empty((1, 1), dtype='str')
        blank[:] = ' '
        while len(p) != len(z):
            print(1)
            p = np.append(blank, p, axis=0)
    elif len(z) < len(p):
        blank = np.empty((1, 1), dtype='str')
        blank[:] = ' '
        while len(z)!=len(p):
            print(2)
            z=np.append(blank,z, axis=0)
print(p)
pz = np.concatenate((p, z), axis=1)
# try to see if you can add to front of

zer = np.transpose(zer)
print(len(pz), len(zer))
print(np.shape(pz), np.shape(zer))
print(len(pz[1]))
blank = np.empty((1, len(pz[1])), dtype='str')
blank[:] = ' '
print(pz)
print(len(pz),len(zer))
if len(pz) != len(zer):
    if len(pz) < len(zer):
        blank = np.empty((1, len(pz[1])), dtype='str')
        blank[:] = ' '
        while len(pz) < len(zer):

            print(1)
            pz = np.append(blank, pz, axis=0)
            print(pz)
    elif len(zer)<len(pz):
        blank = np.empty((1, 1), dtype='str')
        blank[:] = ' '
        while len(zer)<len(zer):
            print(2)
            zer=np.append(blank,pz, axis=0)
            
pz0=np.concatenate((pz,zer),axis=1)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in pz0]))


'''
Conclusion of experiment:
    transpose then concabtenate
'''
'''
New experiment:
try to make it so that all morse are same length

Problem:
need to determine number of columns to add 
so that the number of blanks added is correct
'''
