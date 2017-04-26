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
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

def main():
	# setting data frame
	df = quandl.get('WIKI/GOOGL')
	df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
	df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
	df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
	
	df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
	
	forecast_col = 'Adj. Close'
	df.fillna(-9999, inplace=True)
	
	forecast_out = int(math.ceil(0.01*len(df)))
	df['label'] = df[forecast_col].shift(-forecast_out)
	df.dropna(inplace=True)

	# features
	X = numpy.array(df.drop('label', 1))
	# label 
	y = np.array(df['label'])
	
	X = preprocessing.scale(x)

	print(df.tail())
	

if __name__ == '__main__':
	main()
