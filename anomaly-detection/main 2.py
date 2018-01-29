import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

wind_machine_data = pd.DataFrame ( np.random.rand ( 3 , 3 ) )
a = pd.DataFrame ( np.random.rand ( 3 , 3 ) )
s = pd.DataFrame ( np.random.rand ( 3 , 3 ) )
Predict = pd.DataFrame ( np.random.rand ( 3 , 3 ) )

test_col = pd.DataFrame ( np.random.rand ( 3 , 3 ) )

h = 10  # assign time gap to 10s


def ma ( dataframe_col , gap ) :
	# f = plt.figure ( dpi = 300 )
	
	# plt.scatter ( [ i for i in range ( len ( dataframe_col ) ) ] , dataframe_col , color = 'r' , s = 1 )
	ma_col = dataframe_col.rolling ( window = gap , center = False ).mean ( )
	#
	# plt.plot ( ma_col , color = 'b' , linewidth = 1 )
	#
	# plt.show ( )
	
	return ma_col

def holt_winters ( dataframe_col,alpha,beta) :
	



def comparer ( original , predict , eps) :
	anomalyIndex = [ ]
	
	for i in range ( len ( original ) ) :
		if predict [ i ] is not None and abs ( original [ i ] - predict [ i ] ) >= eps :
			anomalyIndex.append ( i )
	
	return anomalyIndex


def plot_anomaly ( original , index , predict , scatterLabel , originalLabel , predictLabel , title) :
	anomalyValue = [ ]
	for i in range ( len ( index ) ) :
		anomalyValue.append ( original [ index [ i ] ] )
	
	print ( anomalyValue )
	
	f = plt.figure ( dpi = 300 )
	f.suptitle ( title )
	plt.scatter ( index , anomalyValue , s = 1 , color = 'r' , label = scatterLabel )
	plt.plot ( original , linewidth = 1 , color = 'b' , label = originalLabel )
	plt.plot ( predict , linewidth = 1 , color = "orange" , label = predictLabel )
	plt.legend ( )
	# plt.show ( )
	plt.savefig ( "MA.png" )


def main ( ) :
	print ( "Load data..." )
	
	wind_machine_data = pd.read_csv ( 'windmachine_500.csv' , encoding = "ISO-8859-1" )
	original_data = wind_machine_data [ "U3_HNV10CT104" ]
	original_data = original_data.iloc [ 0 :original_data.shape [ 0 ] ]  # remove redundant data.
	
	# Moving Average Prediction
	predict_data = ma ( original_data , 5 )
	
	AnomalyIndex = comparer ( original_data , predict_data , 0.1 )
	
	plot_anomaly ( original_data , AnomalyIndex , predict_data ,"Anomaly Point", "Original Value", "Predict Value", "Anomaly Detection With MA(windowSize = 5,$\epsilon$ = 0.1)")

	# Holt-Winters
	
	
	
	

if __name__ == '__main__' :
	main ( )
