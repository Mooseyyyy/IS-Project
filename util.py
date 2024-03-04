import numpy as np
from scipy.spatial.distance import hamming

group1= np.array([1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
group2 = np.array([0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
group3 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
group4 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
group5 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
group6 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

def generate(size):
    global group1
    global group2
    global group3
    global group4
    global group5
    global group6
    dup = size // 6

    largeGroup1 = np.tile(group1,(dup, 1))
    largeGroup2 = np.tile(group2,(dup, 1))
    largeGroup3 = np.tile(group3,(dup, 1))
    largeGroup4 = np.tile(group5,(dup, 1))
    largeGroup5 = np.tile(group4,(dup, 1))
    largeGroup6 = np.tile(group6,(dup, 1))
    
    master1 = np.concatenate((largeGroup1, largeGroup2, largeGroup3))
    master2 = np.concatenate((largeGroup4, largeGroup5, largeGroup6))
    master = np.concatenate((master1, master2))
    return master
    
def arrayHamming(array1, array2):
    hamming_distance = hamming(array1, array2)
    return hamming_distance

def compare(datapoint):
    global group1
    global group2
    global group3
    global group4
    global group5
    global group6
    flat = datapoint.flatten()
    result = "Bad"
    name = "Bad"

    group1Ham = arrayHamming(flat, group1)
    group2Ham = arrayHamming(flat, group2)
    group3Ham = arrayHamming(flat, group3)
    group4Ham = arrayHamming(flat, group4)
    group5Ham = arrayHamming(flat, group5)
    group6Ham = arrayHamming(flat, group6)

    if group1Ham < 0.1:
        result = "Good"
        name = "Group 1"
    elif group2Ham < 0.1:
        result = "Good"
        name = "Group 2"
    elif group3Ham < 0.1:
        result = "Good"
        name = "Group 3"
    elif group4Ham < 0.1:
        result = "Good"
        name = "Group 4"
    elif group5Ham < 0.1:
        result = "Good"
        name = "Group 5"
    elif group6Ham < 0.1:
        result = "Good"
        name = "Group 6"

    return (result, name)
