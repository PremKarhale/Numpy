
import pandas as pd
data = {
    "Name": ['Alice Johnson', 'Michael Chen', 'Sarah Williams', 'David Rodriguez', 
             'Emma Thompson', 'James Wilson', 'Olivia Martinez', 'Robert Taylor', 
             'Sophia Anderson', 'William Brown'],
    
    "Age": [28, 34, 25, 41, 29, 37, 31, 45, 26, 38],
    
    "Salary": [152000, 78000, 45000, 295000, 58000, 82000, 7000, 105000, 148000, 89000],
    
    "Performance_Score": [87, 92, 78, 95, 83, 89, 91, 88, 76, 94]
}
df=pd.DataFrame(data)
df.to_csv("Data of companies Emp",index=0) #save dataframe to the csv
# print("\n",df.describe()) # gives the statistical analysis of the data 

# minimum the standared deviation more is the consistency 

print(df)
print(f"shape:{df.shape}")
print(f"Coloumns values : {df.columns}")
