import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# Creating dataframe from a dictionary
data_dict = {"student": ["farhan", "rohan", "karan"],
             "marks": [54, 64, 41]}
data_df = pandas.DataFrame(data_dict)
print(data_df)
# Creating a csv out of it
data_df.to_csv("students_details.csv")