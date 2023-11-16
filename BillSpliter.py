#1st Stage, user input, stores users names as dictionaries
users = int(input("Enter the number of friends joining (including you):")) # people that want to join

dict = {}

if users == 0 or users < 0:
    print("No one is joining for the party")
else:
    for user in range(users):
        names = str(input("Enter the names"))
        dict.update({names: 0})
    bill = int(input("Enter the total bill value:"))
    bill_split = round((bill/users),2)
    dict = dict.fromkeys(dict, bill_split)
    print(dict)



