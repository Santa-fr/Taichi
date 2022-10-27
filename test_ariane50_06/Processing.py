import pandas as pd






raw_data=pd.read_csv("test_ariane50_06\data.TXT")

print(raw_data.shape)
indexes=raw_data.index

print(raw_data.head())




#liste_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"A","B","C","D","E","F"]