import sys
sys.path.append("C:\ServerHome\Anaconda3\Lib\site-packages")
import datetime as dt
import time
from datetime import date
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans


#perason相關系數, 測試:將相關係數相乘,期結果為>0.8則視為非常類似的盤口
df = pd.DataFrame({'A':[56,60,58,56,63],
    'B':[60,59,58,60,61]})
df2 = pd.DataFrame({'A':[-3.5,-3,-3,-3,-3],
     'B':[-3.5,-3.5,-3,-3.5,-3]})  
print(df.corr().iat[0,1])
print(df2.corr().iat[0,1])
