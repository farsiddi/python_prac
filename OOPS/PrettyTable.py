import prettytable

# from prettytable import PrettyTable

table1 = prettytable.PrettyTable()
print(table1)

table1.field_names = ["Name", "Location", "EmpID", "Department"]
table1.add_row(["Farhan Siddiqui", "Bangalore", 46320088, "Cloud"])
table1.add_row(["Sanchay Singh", "Pune", 46320099, "ML"])
table1.add_row(["Shivam Pal", "Noida", 46320011, "Testing"])
# table1.add_column("Name", ["Sam Adams", "Alok"])
# table1.add_column("Location", ["Gurgaon", "Delhi"])
# table1.add_column("EmpID", [2342344, 42423424])
# table1.add_column("Department", ["Security", "DevOps"])

# table1.align = "l"

print(table1)
