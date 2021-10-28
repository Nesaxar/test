action=(input("enter action"))
numeric_one=int(input("print numeric"))

numeric_too=int(input("print numeric"))
if action == "+""*""-""//""%":
    print(numeric_one+numeric_too, )
elif action=="//":
    print(numeric_one//numeric_too)
elif action=="*":
    print(numeric_one*numeric_too)
elif action=="%":
    print(numeric_one%numeric_too)
elif action=="-":
    print(numeric_one-numeric_one)
else:
    print(numeric_one-numeric_too)








