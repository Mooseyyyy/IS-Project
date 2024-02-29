# Imports
from rbm import RBM
import numpy as np
from util import generate, compare

# How many times to sample a dp
sample = 30

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
print("Daydream Phase")
for i in range(10):
    array = training_rbm.daydream(sample)
    result, name = compare(array[sample-1:sample])
    if result == 'Good':
        print(name)
