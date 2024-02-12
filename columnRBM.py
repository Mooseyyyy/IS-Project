from rbm import RBM
import numpy as np
import random

# Initialization of RBM
simple_rbm = RBM(num_visible = 6, num_hidden = 2)

# Data used
simple_group_train =np.array([[1,1,0,0,0,0],
                              [0,0,1,1,0,0],
                              [0,0,0,0,1,1],
                              [1,1,0,0,0,0],
                              [0,0,1,1,0,0],
                              [0,0,0,0,1,1]])

random.shuffle(simple_group_train)

print(simple_group_train)

# Training the model
simple_rbm.train(simple_group_train, max_epochs = 5000)
print("Done training")

# Generate data
print("Daydream")
print(simple_rbm.daydream(10))

