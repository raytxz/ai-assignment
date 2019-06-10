## Following steps helps in calculating bias and variance for linear and Decision tree model. 

import pandas as pd
import numpy as np
import random
from sklearn import linear_model
from sklearn.tree import DecisionTreeRegressor

## Defining Real population
def real_population(x1, x2, x3, x4, x5, size=5000, random_state=1234):
	#set.seed(99)
	b0= 1.1
	b1=2.2
	b2 = 3.3
	b3= 4.4
	b4=5.5
	b5= 6.6
	y = b0 + b1*x1 + b2*(x2**2) + b3*(x3*x4) + b4*x4 + b5*x5 
	r = np.random.RandomState(random_state)
	irr_noise = r.normal(-5,10,size)
	y = y + irr_noise
	df = pd.DataFrame({'target':y, 'X1':x1, 'X2':x2, 'X3':x3, 'X4':x4, 'X5':x5})
	return df

## Function to simulate the data as per the real population
def simulation_data(size = 5000, random_seed= 99):
	np.random.seed(random_seed)
	x1 = np.random.rand(size)
	x2 = np.random.rand(size)
	x3 = np.random.rand(size)
	x4 = np.random.rand(size)
	x5 = np.random.rand(size)
	df = real_population(x1,x2,x3,x4,x5,size)
	return df

## function to compute mean square error
def get_mse(mydf, model='Lin'):
	truth = real_population(X_test[0], X_test[1],X_test[2],X_test[3],X_test[4], size=1)['target'][0]
	truth = [truth] * simulations
	if(model== 'Lin'):
		estimate = mydf[1]
	else:
		estimate = mydf[2]
	m = np.mean((estimate-truth)**2)
	return m

## function to compute bias
def get_bias(mydf, model='Lin'):
	truth = real_population(X_test[0], X_test[1],X_test[2],X_test[3],X_test[4], size=1)['target'][0]
	#truth = [truth] * simulations
	if(model== 'Lin'):
		estimate = mydf[1]
	else:
		estimate = mydf[2]
	bias = np.mean(estimate) - truth
	return bias
	
## fucntion to compute variance
def get_var(mydf, model='Lin'):
	if(model== 'Lin'):
		estimate = mydf[1]
	else:
		estimate = mydf[2]
	var = np.mean((estimate - np.mean(estimate))**2)
	return var

## fucntion to run the simulation 
def run_simulation(lin_model, tree_model, sims = 100):
	simulations = sims
	predicted = []
	for i in range(0,simulations):
			D = simulation_data(5000, i)
			X = D[['X1', 'X2', 'X3', 'X4', 'X5']]
			Y = D['target']
      lin_model.fit(X,Y)
      tree_model.fit(X,Y)
			tup = (i, reg.predict(pd.DataFrame(X_test).T), tree.predict(pd.DataFrame(X_test).T))
			predicted.append(tup)
	predicted_df = pd.DataFrame(predicted)
	return predicted_df

## function to evaluate the different metrics of simulation
def evaluate_simulation(prediction_df):
	print("Bias for Lin model is: ", get_bias(prediction_df, 'Lin')**2)
	print("Bias for Tree model is: ", get_bias(prediction_df, 'tree')**2)
	
	print("Var for Lin model is:", get_var(prediction_df, 'Lin'))
	print("var for Tree model is:", get_var(prediction_df, 'tree'))
	
	print("MSE for Lin model is:", get_mse(prediction_df, 'Lin'))
	print("MSE for Tree model is:", get_mse(prediction_df, 'tree'))

	return()

## Invoking the functions defined above
reg = reg = linear_model.LinearRegression()
simulations = 100
np.random.seed(22)
X_test = np.random.rand(5)
for depth in [3,4,6,8,9,10]:
	tree = DecisionTreeRegressor(max_depth=depth)
	results = run_simulation(reg, tree)
	evaluate_simulation(results)
	print("\n end of iter for depth", depth)
	print('\n')