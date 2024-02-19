# Imports
from rbm import RBM
import numpy as np

# Numpy print settings to see activated nodes better
np.set_printoptions(linewidth=np.inf, formatter={'all': lambda x: " {:.0f} ".format(x)})

# Initialization of RBM
training_rbm = RBM(num_visible = 15, num_hidden = 8)

# Data used
training_data =np.array([[1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                              [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                              [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0],
                              [1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                              [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                              [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0],
                              [1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                              [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                              [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0],
                              [1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                              [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                              [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0],
			      [1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                              [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                              [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0]])

np.random.shuffle(training_data)

# Training the model
training_rbm.train(training_data, max_epochs = 5000)
print("Done training")

# Generate data
print("Daydream")
print(simple_rbm.daydream(5))
