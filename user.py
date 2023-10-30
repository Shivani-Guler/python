#total=0
#while True:
 #   user_input=input("Enter a number or q to exit\n")
  #  if user_input=='q':
   #     break
    #total+=int(user_input)
#print(total)

#user_input=0
#total=0
#while user_input!='q':
 #   total+=int(user_input)
  #  user_input=input("Enter num or q to exit")
   # if not user_input.isdigit() and user_input!='q':
    #    print("Invalid")
     #   user_input=0
    
#print(total)

user_input=0
total=0
while user_input!='q':
    try:
        total+=int(user_input)
    except ValueError as e:
        print("Invalid")
        break
    user_input=input("Enter num or q to exit")
else:
    print(total)

#user_input=0
#total=0
#while user_input!='q':
 #   try:
  #      total+=int(user_input)
   # except ValueError as e:
    #   print("Invalid")
        
    #user_input=input("Enter num or q to exit")
#print(total)


#user_input=0
#total=0
#while user_input!='q':
 #   try:
  #      total+=int(user_input)
   # except ValueError as e:
    #    print("Invalid") 
     #   break
    #user_input=input("Enter num or q to exit")
#if user_input=='q':
 #   print(total)


