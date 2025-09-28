import pandas as pd 
data = {
    "Name": ['Alice Johnson', 'Michael Chen', 'Sarah Williams', 'David Rodriguez', 
             'Emma Thompson', 'James Wilson','Jarry', 'Robert Taylor', 
             'Sophia Anderson', 'William Brown'],
    
    "Age": [28, 34, 25, 41, 29, 37, 31, 45, 26, 38],
    
    "Salary": [52000,78000, 45000, 95000, 58000, 12000, 60000, 35000, 48000, 89000],
    
    "Performance_Score": [87, 92, 78, 95, 83, 89, 91, 88, 76, 94]
}
df = pd.DataFrame(data)
print(df)
print('\n')
df.sort_values(by=['Age' , 'Salary'],ascending=[True,True], inplace=True)
print(df)