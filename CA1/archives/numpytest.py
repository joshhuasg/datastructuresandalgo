import numpy as np
p=[['','.','.','.']]
z=[['.',',','-','.']]
c=[['.','.','.','.']]
p=np.transpose(p)
z=np.transpose(z)
pz=np.concatenate((p,z),axis=1)
print(type(pz))
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in pz]))
for j in range(len(pz)):
    for i in range(len(pz[j])):
        print(pz[j][i])

print(pz)
'''
Conclusion of experiment:
    transpose then concabtenate
'''