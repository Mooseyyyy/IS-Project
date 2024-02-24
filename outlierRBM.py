# Imports
from rbm import RBM
import numpy as np

# Numpy print settings to see activated nodes better
np.set_printoptions(linewidth=np.inf, formatter={'all': lambda x: " {:.0f} ".format(x)})

# Initialization of RBM
training_rbm = RBM(num_visible = 15, num_hidden = 8)

# Data used
spread_training_data =np.array([[1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
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

# Data used
error_training_data =np.array([[1,0,1,0,0,1,0,1,0,0,1,1,0,0,0],
                                [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                                [0,1,0,1,0,1,0,0,1,0,1,0,0,1,0],
                                [1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                                [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                                [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0],
                                [1,0,1,0,0,0,1,1,0,0,1,1,0,0,0],
                                [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                                [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0],
                                [1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                                [0,0,0,0,1,0,1,0,0,1,0,0,1,0,1],
                                [0,1,0,1,0,1,0,1,1,0,0,0,0,1,0],
			        [1,0,1,0,0,0,0,1,0,0,1,1,0,0,0],
                                [0,0,0,0,1,0,1,1,0,1,0,0,1,0,1],
                                [0,1,0,1,0,1,0,0,1,0,0,0,0,1,0]])


np.random.shuffle(error_training_data)

# Training the model
training_rbm.train(error_training_data, max_epochs = 5000)
print("Done training")

# Generate data
print("Daydream")
print(training_rbm.daydream(5))
print("---")
print(training_rbm.daydream(5))
print("---")
print(training_rbm.daydream(5))
print("---")
print(training_rbm.daydream(5))
print("---")
print(training_rbm.daydream(5))
#evaluate(training_rbm.daydream(5))

# Function to evaluate generated outputs
def evalate(input): 
  gen = input[-1,:]
  dp1 = np.array([1,0,1,0,0,0,0,1,0,0,1,1,0,0,0])
  dp2 = np.array([0,0,0,0,1,0,1,0,0,1,0,0,1,0,1])
  dp2 = np.array([0,1,0,1,0,1,0,0,1,0,0,0,0,1,0])

def hammingDistance(input1, input2):
  i = 0
  count = 0

  while(i < len(input1)):
    if(input1[i] != input2[i]):
      count += 1
    i += 1
  return count
