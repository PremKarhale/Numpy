import pandas as pd 
data = {
    "Name": ['Alice Johnson', 'Michael Chen', 'Sarah Williams', 'David Rodriguez', 
             'Emma Thompson', 'James Wilson', 'Olivia Martinez', 'Robert Taylor', 
             'Sophia Anderson', 'William Brown'],
    
    "Age": [28, 34, 25, 41, 29, 37, 31, 45, 26, 38],
    
    "Salary": [52000, 78000, 45000, 95000, 58000, 12000, 60000, 35000, 48000, 89000],
    
    "Performance_Score": [87, 92, 78, 95, 83, 89, 91, 88, 76, 94]
}
df=pd.DataFrame(data)
# print(df)

# print only single  coloumn
name = df['Name']
print("\n",name)

# print multiple coloumns 
print("\n",df[['Name' ,'Age' ,'Salary']])

high_salary = df[df['Salary'] >50000]
print("\n Name of the Employees whose Salaries are greater than 50K :\n \n",high_salary)


# Data filtering on the condition basis 
sal_greater_fiftyK = df[(df["Salary"]>50000) & (df["Age"] >= 30)]

# storedSal = sal_greater_fiftyK[["Name" ,"Age" ,"Salary"]]
only_name = sal_greater_fiftyK["Name"] # It returns me only name 
print(only_name)

