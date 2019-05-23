
def users():
    
    
    #newuser =[]
    while True:
        users = []
        username = str(input("Enter your user name: "))
        if username in users:
            username=str(input("username already exist. Please give another username"))
            users.append(username)
        else:
            users.append(username)
        if len(users) >= 5:
            break
        print(users)
            
    print(users)   


users() 
"""number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      break    # break here

   print('Number is ' + str(number))

print('Out of loop')"""