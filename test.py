from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

from fastapi import FastAPI


class ScriptData:

    def __init__(self) -> None:
        # Initialize class with empty map and API key
        self.map = dict()
        self.myKey = "Z8NVJC5M4WYK1JLH"

    def __getitem__(self, stk):
        # Return stock data from map
        return self.map[stk]

    def __setitem__(self, key, value):
        # Add or update stock data in map
        self.map[key] = value

    def __contains__(self, key):
        # Check if stock data is in map
        # print(type(self.map.keys()))
        return key in self.map.keys()

    def fetchNconvert(self, stk):
        self.fetch_intraday_data(stk)
        self.convert_intraday_data(stk)
        return self[stk]

    def convert_intraday_data(self, stk):
        data = pd.DataFrame(self[stk])
        data.columns = data.iloc[0]
        data = data.drop(data.index[0])
        data = data[::-1]
        data.index = data.index[::-1]
        data[['open', 'high', 'low', 'close']] = data[[
            'open', 'high', 'low', 'close']].astype(float)

        data['volume'] = data['volume'].astype(int)

        self[stk] = data
        return data

    def fetch_intraday_data(self, stk):
        # Fetch intraday stock data and store in map
        ts = TimeSeries(key=self.myKey, output_format='csv')
        data, meta_data = ts.get_intraday(stk, interval='5min', )
        self.map[stk] = data


def indicator1(df, timestampperiod=5):

    # set NaN
    lst = [np.nan]*(timestampperiod-1)
    # Mean and create DataFrame
    lst.extend([df['close'][i-timestampperiod:i].mean()
               for i in range(timestampperiod, df['close'].size+1)])
    indiframe = pd.DataFrame()
    indiframe['timestamp'], indiframe['indicator'] = df['timestamp'], lst

    return indiframe


class Strategy:

    def __init__(self, stk) -> None:
        # fetchNconvert

        stock = ScriptData()
        df = stock.fetchNconvert(stk)
        self.close_data = df['close']
        self.indicator_data = indicator1(df, timestampperiod=5)

    def get_script_data(self):
        return self.close_data, self.indicator_data

    def get_signal(self):

        self.signal = pd.DataFrame()
        indi_data = self.indicator_data
        cls_data = self.close_data

        temp = 0

        for i in range(0, cls_data.size):

            if math.isnan(indi_data.iloc[i]['indicator']):
                continue

            action = 0 if cls_data.iloc[i] > indi_data.iloc[i]['indicator'] else 1

            if action != temp:
                temp = action
                _amt = cls_data.iloc[i]
                _timestamp = indi_data.iloc[i]['timestamp']
                new_data = pd.DataFrame(
                    {'amt': _amt, 'timestamp': _timestamp, 'Action': ["buy" if action else "sell"]})

                self.signal = pd.concat(
                    [self.signal, new_data], ignore_index=True)

        return self.signal

        # PLOTTING

    def plot(self):

        plt.figure(figsize=(80, 10))
        plt.xticks(rotation=90)
        plt.grid()

        self.close_data.index -= 1
        print("_"*150, " \nGreen : Purchase \n Red : Sell")

        plt.plot(self.close_data)
        plt.plot(self.indicator_data.timestamp, self.indicator_data.indicator)

        color = ['red' if i == 'sell' else 'green' for i in self.signal['Action']]
        plt.scatter(self.signal.timestamp, self.signal.amt,
                    c=color, marker='h', s=50)


Strateg = Strategy('NVDA')  # CHANGE STOCK-NAME TO TRY ON DIFFERENT DATA-SET

# Currently i am using "get_intraday_extended(stk, '60min', 'year1month1')" for past 1 month of data.
data = pd.DataFrame()

data = Strateg.get_signal()

Strateg.plot()


# app = FastAPI()


# tempframe = pd.DataFrame()

# tempframe['frame']  = [ str(data.iloc[i]['amt'])+" " +str(data.iloc[i]['timestamp'])+" "+str(data.iloc[i]['Action'])+" " for i in range(0 , int(data.size/3)) ]

# @app.get('/')
# def showdata():
#     # print(data.to_json())
    
    
    
#     return data.T ,{
#         "id_number": 10,
#         "number-of-comment": 20
#     }

# Strateg.plot()
