import pandas as pd
import numpy as np

df = pd.read_csv('diabetic_data.csv',delimiter = ',')

def pre_processing(df):
	columns = [2,3,4,5,7,8,9,11,12,13,14,15,16,17,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
	df_new = df.iloc[:,columns]
	df.str.replace('?','NO DATA')
	print(df.iloc[:,2])
	
pre_processing(df)