import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9])

""" #----------reshape 
reshape = arr.reshape((3,3))
print("reshaped of array:\n",reshape) """


""" #-----------arrange ------------ 
arrg = np.arange(1, 30, 3)
print("arranged value:",arrg) """

""" #----------linspace
ls = np.linspace(0, 20 ,5)
print(ls) """

""" #----------random--------------
# create random values
rndm = np.random.randn(5)
print(rndm)

# create random integers value 
rdm = np.random.randint(1,10,5)
print(rdm)

# create random arrays in n dimensions
rdmm = np.random.randint(1, 20, (3,3))
print(rdmm) """