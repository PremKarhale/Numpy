# 1 preserve data integrity
# 2 predicts the realistic value and update the data instead to keeping it null/none
# 3 smoth trends 
# 4 avoids data loss 
# 5 used only for timer series data 

import pandas as pd 
data = {
    "Name": ['Alice Johnson', 'Michael Chen', 'Sarah Williams', 'David Rodriguez', 
             'Emma Thompson', 'James Wilson', None, 'Robert Taylor', 
             'Sophia Anderson', 'William Brown'],
    
    "Age": [28, None, 25, 41, 29, 37, 31, 45, 26, 38],
    
    "Salary": [52000,None, 45000, 95000, 58000, 12000, 60000, 35000, 48000, 89000],
    
    "Performance_Score": [87, 92, 78, 95, 83, 89, 91, 88, 76, 94]
}
df=pd.DataFrame(data)

# methods --> linear , polynomial , time
# df.interpolate(method='linear',axis=0,inplace=True)
df['Age'].interpolate('linear',axis=0 , inplace=True)
df['Salary'].interpolate('linear',axis=0 , inplace=True)

# Imp !! for update df.loc[]
df.loc[6 ,'Name'] ='JERRY'
print(df)
print("\n Updated name is :\n",df['Name'])
