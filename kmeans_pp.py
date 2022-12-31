import getopt
import sys
import pandas as pd
import numpy as np
import math
import kmeans_capi

def kmeans_pp(k, eps,  input_1,  input_2, iter=300):
    file_1 = open(input_1, 'r')
    file_2 = open(input_2, 'r')
    
    df_1 = pd.read_csv(file_1,header=None)
    df_2 = pd.read_csv(file_2,header=None)
    
    file_1.close()
    file_2.close()
    
    vectors_amt = df_1.shape[0]
  
    ##check that the amount of clusters is legal##
    if(k>vectors_amt):
        print("Invalid number of clusters!")
        exit()
    
    
    ##merge and sort inputs##
    df_vectors = pd.merge(df_1, df_2, on=0)
    df_vectors = df_vectors.sort_values(by=0)
    
    ##convert dataframe into numpy array, without keys!##
    keys = df_vectors[0].to_numpy()
    vectors = df_vectors.drop(0, axis=1).to_numpy()
    vector_len = np.size(vectors[0])
    
    ##Start algorithm##
    
    ##step 1##
    centroid_keys = []
    centroids = [] ## python array of numpy arrays
    np.random.seed(0)
    curr_index = np.random.choice(np.size(keys))
    centroid_keys.append(keys[curr_index])
    centroids.append(vectors[curr_index].tolist())

    
    for i in range(1,k):
        ##step 2##
        distances = np.array([min_distance(vector, centroids) for vector in vectors])
        
        ##step 3
        probabilities = np.divide(distances, distances.sum())
        
        ##step 2 but with prob function##
        curr_index = np.random.choice(np.size(keys), p=probabilities) ##check to see this is legal
        centroid_keys.append(keys[curr_index])
        centroids.append(vectors[curr_index].tolist())
        
    
    for i in range(len(centroid_keys)-1):
        print(f"{round(centroid_keys[i], 0)}," , end="")
    print(f"{round(centroid_keys[-1],0)}") 
   
    #convert vectors to 2Darray
    vectors = vectors.tolist()
    
    ###send to c####
    new_centroids = kmeans_capi.cKmeans(k, iter, vector_len, vectors_amt, eps, vectors, centroids)

    if(new_centroids == None):
        print("An Error Has Occurred")
        exit()
   
    #print the centroids
    for i in range(len(new_centroids)-1):
        if(i%(vector_len)==vector_len-1):
            print(f"{round(new_centroids[i], 4)}")
        else:    
            print(f"{round(new_centroids[i], 4)}," , end="")
     
   

def euclidian_distance(vec1, vec2):
    sum = 0
    for i in range(np.size(vec1)):
        sum += (vec1[i]-vec2[i])**2
    return sum**(1/2)

def min_distance(vector, centroids):
    min_dis = float('inf')
    for centroid in centroids:
        curr_distance=euclidian_distance(vector,centroid)
        if(curr_distance<min_dis):
           min_dis=curr_distance
    return  min_dis    
           
           
           
            
argv = sys.argv[1:]
if len(argv)==4:
    try:
        k = int(argv[0])
    except:
        print("Invalid number of clusters!")
        exit()
    
    try:
        eps = float(argv[1])
    except:
        print("An Error Has Occurred")
        exit()

    if k>1:
        kmeans_pp(k, eps, argv[2], argv[3])
    else:
        print("Invalid number of clusters!")
        exit()
elif len(argv)==5:
    try:
        k = int(argv[0])
    except:
        print("Invalid number of clusters!")
        exit()
    
    try:
        iter = int(argv[1])
    except:
        print("Invalid maximum iteration!")
        exit()

    try:
        eps = float(argv[2])
    except:
        print("An Error Has Occurred")
        exit()

    if k<=1:
        print("Invalid number of clusters!")
        exit()
    if  1<iter<1000:
        kmeans_pp(k, eps, argv[3], argv[4], iter)
    else:
        print("Invalid maximum iteration!")
        exit()
else:
    print("An Error Has Occurred")
    exit()