# Imports
from rbm import RBM
import numpy as np
from util import generate, compare

# How many times to sample a dp
sample = 2000

# Numpy print settings to see activated nodes better
np.set_printoptions(linewidth=np.inf, formatter={'all': lambda x: " {:.0f} ".format(x)})

# Initialization of RBM
training_rbm = RBM(num_visible = 100, num_hidden = 1000)

training_data = generate(600)

np.random.shuffle(training_data)

# Training the model
training_rbm.train(training_data, max_epochs = 5000)
print("Done training")

# Generate data
print("Daydream Phase")
countBad = 0
countGroup1 = 0
countGroup2 = 0
countGroup3 = 0
countGroup4 = 0
countGroup5 = 0
countGroup6 = 0
for i in range(50):
    array = training_rbm.daydream(sample)
    newArray = array[sample-1:sample]
    result, name = compare(newArray)
    if name == "Bad":
        countBad+=1
    if name == "Group 1":
        countGroup1+=1
    if name == "Group 2":
        countGroup2+=1
    if name == "Group 3":
        countGroup3+=1
    if name == "Group 4":
        countGroup4+=1
    if name == "Group 5":
        countGroup5+=1
    if name == "Group 6":
        countGroup6+=1
    print(name)

print(countBad)
print(countGroup1)
print(countGroup2)
print(countGroup3)
print(countGroup4)
print(countGroup5)
print(countGroup6)
