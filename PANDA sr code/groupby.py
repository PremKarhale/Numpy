# 1) sum()
# 2) mean ()
# 3) std()
# 4) count --> gives the count of NAN values in the group 
# 5) min --> gives the min value in the grp 

import pandas as pd 
data ={
    "Name": ['Alice Johnson', 'Michael Chen', 'Sarah Williams', 'David Rodriguez', 
             'Emma Thompson', 'James Wilson','Jarry', 'Robert Taylor', 
             'Sophia Anderson', 'William Brown'],
    
    "Age": [28, 34, 25, 41, 29, 37, 31, 45, 26, 38],
    
    "Salary": [52000,78000, 45000, 95000, 58000, 12000, 60000, 35000, 48000, 89000],
    
    "Performance_Score": [87, 92, 78, 95, 83, 89, 91, 88, 76, 94]
}

df = pd.DataFrame(data)
print(df)
# df= df.groupby('Age')['Salary'].mean()
# groupby= df.groupby('Age')['Salary'].sum()

# groupby on the multiple coloumn 
groupby = df.groupby(['Age','Name'])['Salary'].sum()
print(groupby)