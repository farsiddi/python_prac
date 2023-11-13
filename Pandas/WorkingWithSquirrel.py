import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# print(full_data)
# new_data = full_data.to_dict()
# print(new_data)
# new_data1 = new_data.
# Getting grey squirrels
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
# print(grey_squirrels)
red_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]
# print(red_squirrel)
print(len(grey_squirrels))
print(len(red_squirrel))
print(len(black_squirrel))

data_dict = {"Fur Color": ["Grey", "Red", "black"],
             "Count": [len(grey_squirrels), len(red_squirrel), len(black_squirrel)]
             }
print(data_dict)
squirrel_df = pandas.DataFrame(data_dict)
squirrel_df.to_csv("AnalysedSquirrel.csv")
