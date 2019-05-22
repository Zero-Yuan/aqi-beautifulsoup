# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:52:44 2019

@author: yuan
"""
import pandas as pd

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes,unicode_minus'] = False


def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    
    top10 = aqi_data.sort_values(by=['AQI']).head(10)
    print(top10)
    
    top10 = aqi_data.sort_values(by=['AQI']).tail(10)
    print(top10)
    
    top10.to_csv('top10.csv',index=False)
            
    
if __name__ == '__main__':
    main()