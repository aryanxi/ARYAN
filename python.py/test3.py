#Coffeeshopbot..//..


print("welcome to coffee shop.. What is your name? ")
user = input("Enter your name : \n") 
print("Hello " + user +" ,thank you for coming to coffeshop\n\n\n")

my_menu= ("coffe")

print("Hey \n"+ user +", what you want today we have this on menu \n")
print(my_menu)

order = input()
 
if order==str.upper(my_menu):

        print("Sounds good "+ user +" your "+ order +" will be ready soon" )
        print("Wait for a moment.......\n\n") 

else:
     print("Please choose the correct menu.....")


