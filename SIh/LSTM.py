
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

df = pd.read_csv('SIh/monthly_milk_production.csv',
				index_col='Date',
				parse_dates=True)
df.index.freq = 'MS'

df.head()
# Plotting graph b/w production and date
df.plot(figsize=(12, 6))

from statsmodels.tsa.seasonal import seasonal_decompose
results = seasonal_decompose(df['Production'])
results.plot()


from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator

n_input = 3
n_features = 1
generator = TimeseriesGenerator(scaled_train,
								scaled_train,
								length=n_input,
								batch_size=1)
X, y = generator[0]
print(f'Given the Array: \n{X.flatten()}')
print(f'Predict this y: \n {y}')
# We do the same thing, but now instead for 12 months
n_input = 12
generator = TimeseriesGenerator(
                            scaled_train,
                            scaled_train,
                            length=n_input,
                            batch_size=1
)


