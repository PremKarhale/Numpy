# pd.merge(df1 , df2 ,on="col name " , how = "type of join ")
import pandas as pd

#customers datafrome
Customers = pd.DataFrame({
    'CustomerID' : [1,2,3],
    'Name':["Ramesh" , "suresh " , "Mangesh"] 
})

# orders dataframe
Orders = pd.DataFrame({
    'CustomerID':[1,2,4,5],
    'Purchase' : [250 ,450 , 399 , 567]
})

# df_merge = pd.merge(Customers , Orders , on='CustomerID' ,how='inner')
df_merge =pd.merge(Customers , Orders , on='CustomerID' , how='outer')
print('outerJoin')
print(df_merge)

'''
inner join gives only those valus col = 'customerID'
outer join gives all values and do NAN for col != 'customerID'

'''
