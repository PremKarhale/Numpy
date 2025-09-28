#.fillna() to fill the null values 
#.fillna('value',inplace=True)
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
# print(df)

# df.fillna(9 , inplace = True)
# print(df)
df['Age'].fillna(df['Age'].mean() , inplace = True)
print(df)
df['Salary'].fillna(df['Salary'].mean() ,inplace=True) #fillna('takes the what value to be filled with ')
print(df)

#to drop certain columns from the table 
df.drop(columns=['Performance_Score'] , inplace = True)
print(df)