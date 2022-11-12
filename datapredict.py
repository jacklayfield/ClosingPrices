import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def generate(startDate, endDate, stock):
  #Grab stock quote
  print(stock + " " + startDate + " " + endDate)
  # sq = web.DataReader(stock, data_source='yahoo', start=startDate, end=endDate)
  sq = web.DataReader('MSFT', data_source='yahoo', start='2017-01-01', end='2022-01-17')
  print(sq)

  plt.figure(figsize=(16,8))
  plt.title('Closing price data')
  plt.plot(sq['Close'])
  plt.xlabel('Date', fontsize=14)
  plt.ylabel('Close Price (USD $)', fontsize=14)
  # plt.show()

  #Create dataframe for close column
  data = sq.filter(['Close'])
  #Convert dataframe to numpy array
  dataset = data.values
  #Get num rows to train model
  training_data_len = math.ceil(len(dataset) * 0.8)
  print(training_data_len)

  #Scale data
  scaler = MinMaxScaler(feature_range=(0,1))
  scaled_data = scaler.fit_transform(dataset)

  #Create the training data set
  #Create the scaled training data set
  train_data = scaled_data[0:training_data_len , :]
  #Split data into x_train and y_train sets
  x_train = []
  y_train = []

  for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i,0])
    y_train.append(train_data[i, 0])

    if i<=61:
      print(x_train)
      print(y_train)
      print()

  #Convert the x_train and y_train to numpy arrays

  x_train, y_train = np.array(x_train), np.array(y_train)

  #Reshape data
  x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

  #Building Model

  model = Sequential()
  model.add(LSTM(50, return_sequences=True, input_shape = (x_train.shape[1], 1)))
  model.add(LSTM(50, return_sequences=False))
  model.add(Dense(25))
  model.add(Dense(1))

  #Compile the model

  model.compile(optimizer='adam', loss='mean_squared_error')

  #Train model
  model.fit(x_train, y_train, batch_size=1, epochs=1)

  #Create the testing data set
  #Scaled values from 1543-2003
  # print(len(dataset))s
  test_data = scaled_data[training_data_len -60: len(dataset), :]
  print(test_data)
  print(len(test_data))
  #Create the data sets x_test and y_test
  x_test = []
  y_test = dataset[training_data_len:, :]
  for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

    #Convert to numpy/reshape
  x_test = np.array(x_test)
  print(x_test)
  x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

  #Get models predicted price vals
  predictions = model.predict(x_test)
  predictions = scaler.inverse_transform(predictions)

  #Get RSME
  rmse = np.sqrt(np.mean(((predictions- y_test)**2)))

  #Plotting
  train = data[:training_data_len]
  valid = data[training_data_len:]
  valid['Predictions'] = predictions
  #Data visual
  plt.figure(figsize=(16,8))
  plt.title('Our Model')
  plt.xlabel('Date', fontsize=14)
  plt.ylabel('Close Price (USD)', fontsize=14)
  plt.plot(train['Close'])
  plt.plot(valid[['Close', 'Predictions']])
  plt.legend(['Train','Val','Predictions'], loc='lower right')
  plt.show()


  #Show the valid and predicted prices
  print(valid)

  #Quote/DF
  apple_quote = web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end='2019-12-17')
  new_df = apple_quote.filter(['Close'])
  last_60_days = new_df[-60:].values
  #Scale data (0-1)
  last_60_days_scaled = scaler.transform(last_60_days)

  #List of scaled data + reshape
  X_test = []
  X_test.append(last_60_days_scaled)
  X_test = np.array(X_test)
  X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

  #Undo scaling
  pred_price = model.predict(X_test)
  pred_price = scaler.inverse_transform(pred_price)
  print(pred_price)

  #Quote on specific day
  apple_quote_day = web.DataReader('AAPL', data_source='yahoo', start='2019-12-18', end='2019-12-18')
  print(apple_quote_day['Close'])