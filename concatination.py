import pandas as pd 
#region 1 
df_region1 = pd.DataFrame({
    'CustomerId': [1,2],
    'Name': ['gopal','sham']
})

#region 2 
df_region2 =pd.DataFrame({
    'CustomerId' :[3,4],
    'Name' :['raju' ,'gopal']
})

# concatinate vertically (coloumn wise) , axis =0
# df_concate = pd.concat([df_region1,df_region2] ,ignore_index=True)

# rowise axis = 1
df_concate = pd.concat([df_region1,df_region2] , axis = 1 , ignore_index=True)
print(df_concate)