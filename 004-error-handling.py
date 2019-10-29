user_input = input('gib mir eine Zahl: ')
try:
    user_input = int(user_input)
except ValueError:
    print("falsche eingabe")
    
print(5 + user_input)   