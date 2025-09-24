#Data Modification 
import pandas as pd
data = {
    "Name": ['Alice Johnson', 'Michael Chen', 'Sarah Williams', 'David Rodriguez', 
             'Emma Thompson', 'James Wilson', 'Olivia Martinez', 'Robert Taylor', 
             'Sophia Anderson', 'William Brown'],
    
    "Age": [28, 34, 25, 41, 29, 37, 31, 45, 26, 38],
    
    "Salary": [52000, 78000, 45000, 95000, 58000, 12000, 60000, 35000, 48000, 89000],
    
    "Performance_Score": [87, 92, 78, 95, 83, 89, 91, 88, 76, 94]
}

df = pd.DataFrame(data)
print(df)
# df["coloumn"]='some_data'
# df['Bonos']= df['Salary']*0.1
# print(df)

# to insert the col we used the method insert(loc , 'col name' , 'some_data')
# df.insert(0 ,"Emp_id",[1,2,3,4,5,6,7,8,9,10])
# print(df)

# .loc[] ---> used to update the data in the dataframe .loc['row_index','coloumn name'] = value
# df.loc[2, "Salary"]=68000
# print(df)

# Drop 
#.drop(coloumn=['col_name'],inplace=True)
print("Modified dataframe")
df.drop(columns=['Performance_Score'] , inplace=True)
print(df)