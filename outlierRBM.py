# Imports
from rbm import RBM
import numpy as np
from util import generate

# Numpy print settings to see activated nodes better
np.set_printoptions(linewidth=np.inf, formatter={'all': lambda x: " {:.0f} ".format(x)})

# Initialization of RBM
training_rbm = RBM(num_visible = 100, num_hidden = 30)

training_data = generate(60)

np.random.shuffle(training_data)

# Training the model
training_rbm.train(training_data, max_epochs = 5000)
print("Done training")

# Generate data
print("Daydream")
array = training_rbm.daydream(30)
print(array[29:30])

