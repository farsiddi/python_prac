# def greeting(watch):
#     # print("Hello " + watch + " Good morning")
#     print(f"Hello {watch} Good morning")
# name = input("What is your name?\n").upper()
# greeting(name)

def location(name, loca):
    print(f"Hello {name}.You are from {loca}")


naam = input("What is your name?\n")
place = input("Where are you from?\n")
location(naam, loca=place)
