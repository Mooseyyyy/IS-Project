from rbm import RBM
import numpy as np
#temp

# Initialization of RBM
rbm1 = RBM(num_visible = 5, num_hidden = 3)

# Data used
training_data = np.array([[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]])
visible_data = np.array([[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1]])


rbm1.train(training_data, max_epochs = 5000)
print("Done training")

print("HU activated from training data")
print(rbm1.run_visible(training_data))

print("HU activated from test data")
print(rbm1.run_visible(visible_data))
