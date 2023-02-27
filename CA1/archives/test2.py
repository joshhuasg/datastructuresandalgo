import numpy as np

p=[['.','.','.']]
z=[['.',',','-','.']]
c=[['.','.','.','.']]
p=np.transpose(p)
z=np.transpose(z)
blank=[[' ']]
if len(p)!=len(z):
    if len(p)<len(z):
        print(1)
        p=np.transpose(p)
        p=[np.append(blank,p)]
        p=np.transpose(p)
    elif len(z)<len(p):
        print(2)
        z=z.insert(0,[' '])
print(p)
pz=np.concatenate((p,z),axis=1)

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in pz]))
'''
Conclusion of experiment:
    transpose then concabtenate
'''