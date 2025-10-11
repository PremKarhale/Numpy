# for reading the data in the cloud we use the library name gcfsfs

import pandas as pd
# #read data from a csv file into a data frame 
# df = pd.read_csv(r"c:\Users\Admin\Downloads\sales_data_sample.csv",encoding="latin1")
# print(df)

data={
    "Name":['Ram' , 'Satyam' , 'shivam' , 'sundaram' , 'narayan' , 'murti'],
    "Age":[10,23,45,65,25,14],
    "City":['Nagpur' , 'mah' , 'solapur' , 'kolapur' , 'baner'  , 'kolkata']
}
df=pd.DataFrame(data)
print(df)
# df.to_csv("output_data.csv",index=0)
# df.to_excel("output.xlsx" , index=False)
df.to_json("output.json" , index=False)