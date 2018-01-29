import matplotlib.pyplot as plt
import pandas as pd


def ma ( dataframe_col , gap ) :
	# f = plt.figure ( dpi = 300 )
	
	# plt.scatter ( [ i for i in range ( len ( dataframe_col ) ) ] , dataframe_col , color = 'r' , s = 1 )
	ma_col = dataframe_col.rolling ( window = gap , center = False ).mean ( )
	#
	# plt.plot ( ma_col , color = 'b' , linewidth = 1 )
	#
	# plt.show ( )
	
	return ma_col


# alpha 为历史数据依赖指数，alpha越小越依赖于历史数据。
def expon_two_method ( dataframe_col , alpha = 0.5 ) :
	if dataframe_col is None :
		return None
	
	dataframe_col = dataframe_col [ 0 ].tolist ( )
	S_one = [ dataframe_col [ 0 ] ]
	S_two = [ dataframe_col [ 0 ] ]
	S = [ ]
	
	print ( len ( dataframe_col ) )
	for i in range ( 1 , len ( dataframe_col ) ) :
		S_one.append ( alpha * dataframe_col [ i ] + (1 - alpha) * S_one [ i - 1 ] )
		S_two.append ( alpha * S_one [ i ] + (1 - alpha) * S_two [ i - 1 ] )
		S.append ( 2 * S_one [ i ] - S_two [ i ] )
	
	print ( S )
	
	X_predict = [ ]
	for i in range ( 0 , len ( S_one ) ) :
		print ( 1 + alpha / float ( 1 - alpha ) )
		X_predict.append ( S_one [ i ] + (alpha / float ( 1 - alpha )) * (S_one [ i ] - S_two [ i ]) )
	
	rsi_fix = trend_predict ( dataframe_col , 0.01 , 3 )
	
	for i in range ( len ( X_predict ) ) :
		X_predict [ i ] *= (rsi_fix [ i ] + 1)
	
	return X_predict


def trend_predict ( data , rsi_param , rsi_window ) :
	rsi_trend = [ ]
	for i in range ( rsi_window ) :
		rsi_trend.append ( 0 )
	for i in range ( rsi_window , len ( data ) ) :
		rsi_rise = 0
		rsi_down = 0
		for j in range ( 1 , rsi_window ) :
			if data [ i - rsi_window + j ] - data [ i - rsi_window + j - 1 ] > 0 :
				rsi_rise = rsi_rise + data [ i - rsi_window + j ] - data [ i - rsi_window + j - 1 ]
			else :
				rsi_down = rsi_down + abs ( data [ i - rsi_window + j ] - data [ i - rsi_window + j - 1 ] )
		if rsi_rise != 0 and rsi_down != 0 :
			rsi_trend.append ( rsi_rise / float ( rsi_rise + rsi_down ) )
		else :
			rsi_trend.append ( 0 )
	
	rsi_trend_fix = [ ]
	for i in range ( rsi_window ) :
		rsi_trend_fix.append ( 0 )
	
	for i in range ( rsi_window , len ( rsi_trend ) ) :
		if rsi_trend [ i ] >= 0.8 :
			# overbought: make minus fix
			rsi_trend_fix.append ( rsi_param * (rsi_trend [ i ] - 0.8) )
		elif rsi_trend [ i ] <= 0.2 :
			#
			rsi_trend_fix.append ( rsi_param * (rsi_trend [ i ] - 0.2) )
		else :
			rsi_trend_fix.append ( 0 )
	
	return rsi_trend_fix


def bollinger_band ( original_data , window , K ) :
	rolling_mean = original_data.rolling ( window = window , center = False ).mean ( )
	rolling_std = original_data.rolling ( window = window , center = False ).std ( )
	
	upper_band = rolling_mean + (K * rolling_std)
	lower_band = rolling_mean - (K * rolling_std)
	
	return upper_band , rolling_mean , lower_band


def bollinger_detection ( upper_band , lower_band , original_data ) :
	# Bollinger band: detect accidentally rise and down
	original_data = original_data [ 0 ].tolist ( )
	upper_band = upper_band [ 0 ].tolist ( )
	lower_band = lower_band [ 0 ].tolist ( )
	anomaly_index_from_bollinger = [ ]
	for i in range ( len ( original_data ) ) :
		if upper_band [ i ] is not None and lower_band [ i ] is not None :
			if original_data [ i ] >= upper_band [ i ] or original_data [ i ] <= lower_band [ i ] :
				anomaly_index_from_bollinger.append ( i )
	
	return anomaly_index_from_bollinger


def comparer ( original , predict , eps ) :
	anomalyIndex = [ ]
	original = original [ 0 ].tolist ( )
	for i in range ( len ( original ) ) :
		if predict [ i ] is not None and abs ( original [ i ] - predict [ i ] ) >= eps :
			anomalyIndex.append ( i )
	return anomalyIndex


def plot_anomaly ( original , index , scatterLabel , originalLabel , predictLabel , title , save_path ,
                   predict = None ) :
	anomalyValue = [ ]
	original = original [ 0 ].tolist ( )
	for i in range ( len ( index ) ) :
		anomalyValue.append ( original [ index [ i ] ] )
	
	print ( anomalyValue )
	
	f = plt.figure ( dpi = 300 )
	f.suptitle ( title )
	
	plt.plot ( original , linewidth = 1 , color = 'blue' , label = originalLabel )
	
	if predict is not None :
		plt.plot ( predict , linewidth = 1 , color = "r" , label = predictLabel )
	
	plt.scatter ( index , anomalyValue , s = 10 , color = 'red' , label = scatterLabel )
	plt.legend ( )


# plt.show ( )
# plt.savefig ( save_path )


def main ( ) :
	print ( "Load data..." )
	# wind_machine_data = pd.read_csv ( 'windmachine_500.csv' , encoding = "ISO-8859-1" )
	# original_data = wind_machine_data [ "U3_HNV10CT104" ]
	original_data = pd.DataFrame (
		[ 1 , 1 , 1 , 1 , 1 , 1 , 4 , 2 , 3 , 1 , 1 , 1 , 1 ,
		  1 , 1 , 1 , 1 ] )
	# original_data = original_data.iloc [ 0 : len(original_data)]  # remove redundant data.
	
	# Moving Average Prediction
	# predict_data = ma ( original_data , 5 )
	
	# AnomalyIndex = comparer ( original_data , predict_data , 0.1 )
	
	# plot_anomaly ( original_data , AnomalyIndex , predict_data , "Anomaly Point" , "Original Value" ,
	# "Predict Value" , "Anomaly Detection With MA(windowSize = 5,$\epsilon$ = 0.1)" )
	
	# Holt-Winters
	
	f = plt.figure ( dpi = 300 )
	f.suptitle ( "Anomaly Detection With 2-EA($\gamma$ = 0.4)" )
	
	predict_data = expon_two_method ( original_data , 0.4 )
	
	upper , aver , lower = bollinger_band ( original_data , 6 , 2 )
	
	anomaly_index = comparer ( original_data , predict_data , 1 )
	
	# 处理预测器和布林通道预测值的冲突
	
	plot_anomaly ( original_data , anomaly_index , "Anomaly Point" , "Original Value" , "Predict Value" ,
	               "Anomaly Detection With EA($\gamma$ = 0.4, fix_param = 0.01)" , "EA.png" , predict_data )
	
	# plt.plot ( predict_data , color = 'r' , linewidth = 1 , label = 'Predicted Value' )
	
	# plt.plot ( original_data , color = 'b' , linewidth = 1 , label = "Original Value" )
	
	plt.plot ( upper , color = 'orange' , linewidth = 1 , label = "Upper band" )
	plt.plot ( lower , color = 'orange' , linewidth = 1 , label = "Lower band" )
	plt.plot ( aver , color = 'orange' , linewidth = 1, label = "Moving Average")
	plt.legend ( )
	
	plt.show ( )


# trend_predict(original_data,0.1,6)
#

#

#
# plot_anomaly(original_data,bollinger_index, "Anomaly Point" , "Original Value" , "Predict Value",
# "Anomaly Detection With BB(window = 15, band_std = 2)" , "Bollinger.png")
# # plt.plot(original_data,color = 'r')
# plt.plot(upper, color = 'orange', linewidth = 1, label = "Upper band")
# # plt.plot(aver,color = 'orange')
# plt.plot(lower, color = 'orange', linewidth = 1, label = "Lower band")
#
# plt.legend()
# plt.savefig("Bollinger.png")
# plt.show()


if __name__ == '__main__' :
	main ( )
