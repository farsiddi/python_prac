file = open("MyFile.txt").read()
print(file)

new_file = open("MyFile.txt")
content = new_file.read()
print(content)
new_file.close()

# use like this as we don't need to close the file now
with open("MyFile.txt") as final_file:
    cont = final_file.read()
    print(cont)

# Writing into files
with open("MyFile.txt", mode="a") as file2:  # by default the mode is read -w for read and a for append
    # file2.write("I live in India")
    file2.write("I live in India")

# If open a file in write mode then it will create that file
with open("New_File.txt",mode="w") as file3:
    file3.write("This is lenovo")