#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  regressionIntro.py
#  
#  Copyright 2017 Edd Osorio <dobleub@debian>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

def main():
	# setting data frame
	quandl.ApiConfig.api_key = 'AQ_X5HmEN_Wn1LNWCWfz'
	df = quandl.get_table('WIKI/PRICES')
	print(df.head())
	df = df[['adj_open','adj_high','adj_low','adj_close','adj_volume']]
	df['HL_PCT'] = (df['adj_high'] - df['adj_close']) / df['adj_close'] * 100.0
	df['PCT_change'] = (df['adj_close'] - df['adj_open']) / df['adj_open'] * 100.0
	exit()
	
	df = df[['adj_close', 'HL_PCT', 'PCT_change', 'adj_volume']]
	
	forecast_col = 'adj_close'
	df.fillna(-9999, inplace=True)
	
	forecast_out = int(math.ceil(0.01*len(df)))
	df['label'] = df[forecast_col].shift(-forecast_out)
	df.dropna(inplace=True)

	# features
	X = numpy.array(df.drop('label', 1))
	# label 
	y = np.array(df['label'])

	X = preprocessing.scale(X)
	X = X[:-forecast_out+1]
	df.dropna(inplace=True)
	y = np.array(df['label'])

	print(df.tail())
	

if __name__ == '__main__':
	main()
