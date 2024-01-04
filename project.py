from rbm import RBM
import numpy as np

rbm1 = RBM(num_visible = 20, num_hidden = 2)

training_data1 = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
rbm1.train(training_data1, max_epochs = 5000)

print ("Done") 
