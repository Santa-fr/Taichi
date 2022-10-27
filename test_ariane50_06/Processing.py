import pandas as pd






raw_data=pd.read_csv("test_ariane50_06\data.TXT")

print(raw_data.shape)
indexes=raw_data.index
raw_data['Name'][1] = 'Type'
raw_data.set_index([indexes,'Name'], inplace=True)

'''
Here I create a Dataframe for stocking the information for each and every columns of the dataframe containing the values 
I do this in order to have a cleaner dataframe with only the location and rotation data of our avatar
Information stocked : 
the body part ID as 'BP_ID',
the type of data (Rotation or Position) as 'Type',
the axis it refers to as 'Axis'
'''
#Dictionnary
dict_point = {}
for col in raw_data.columns:

    dict = {'BP_ID': raw_data[col].iloc[0],'Type':raw_data[col].iloc[1] ,'Axis':raw_data[col].iloc[2]}
    dict_point[col] = dict    #all the data is stocked with the key equal to the column name

#Dataframe of the columns infos
col_info = pd.DataFrame(dict_point)
print(col_info)

#Dataframe of the values cleaned
values = raw_data.iloc[3:]
values = values.rename_axis(['Frame', 'Time'])
print(values)

values.to_csv('values.csv')
col_info.to_csv('col_info.csv')




#liste_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"A","B","C","D","E","F"]

