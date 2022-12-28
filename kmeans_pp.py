import getopt
import sys
import pandas as pd
import numpy as np
import math

def kmeans_pp(k, eps,  input_1,  input_2, iter=300):
    file_1 = open(input_1, 'r')
    file_2 = open(input_2, 'r')
    
    df_1 = pd.read_csv(file_1,header=None)
    df_2 = pd.read_csv(file_2,header=None)
    
    file_1.close()
    file_2.close()
    
    vectors_amt = df_1.shape[0]
    print(vectors_amt)
  
    ##check that the amount of clusters is legal##
    if(k>vectors_amt):
        print("Invalid number of clusters!")
        exit()
    
    ##merge and sort inputs##
    df_1.columns =['key', 'coordinate_0', 'coordinate_1']
    df_2.columns =['key', 'coordinate_2', 'coordinate_3']
    
    df_vectors = pd.merge(df_1, df_2, on='key')
    
    
    df_vectors = df_vectors.sort_values(by='key')
    print(df_vectors)
    ##convert dataframe into numpy array, without keys!##
    vectors = df_vectors.drop('key', axis=1).to_numpy()
    print(vectors)
     
    ##Start algorithm##
    ##step 1##
    centroid_keys = []
   
    
    
    return 0




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