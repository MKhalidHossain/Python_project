import random
from datetime import date
from colored import fg, bg, attr

class shop:
    # Declare list to store the selected course
    cart_items = []
    # Initialize the cart amount
    cart_amount = 0
    # Initialize the student balance
    cust_balance = 0
    # Initialize the variable that will take user's input
    answer = ''

    # Define function to display the main menu 
    def display_menu(self):
        print("\n%s%s%s" %(fg(150), '" CompilerFiller " is the biggest edtech company, it has many cutting edge courses to learn.', attr(1)))
        print("\n%s%s%s" %(fg(150), 'Welcome to Our Online Courses', attr(0)))
        print("\n%s%s" %(fg(140), '1. Our Courses...'))
        print("2. Select Courses...")
        print("3. Exit")
        self.answer = input("\nType 1 or 2 or 3:")
    
    # Define function to read and display the course from the text file
    def display_products(self):
       
        print("\nThe list of products are given below:\n")
        with open('Courses.txt') as f:
            line = f.readline()
            # Print the header of the file
            print("Id Course Name\t\tPrice\tClasses\tDuration")
            while line:
                # Initialize counter to set the space between the fields
                counter = 0
                # Read each line from the file
                line = f.readline()
                # Split each line based on the comma (,) and store in a list
                fieldList = list(line.split(","))
                print('\t')
                # Read each value from the list and print
                for val in fieldList:
                    if counter == 0:
                        space=''
                    else:
                        space='\t' 
                    counter = counter + 1
                    if counter == 3:
                        val = '$' + val
                    print(val, end=space)

    # Define function to check the selected course exists in the file or not
    def check_products(self, search):

        # Open the file for reading 
        with open('Courses.txt') as f:
            # Read each line of the file
            for line in f:
                # Split the line value based on comma(,)
                fieldList = list(line.split(","))
                for val in fieldList:
                    # Check the selected course match with the value or not
                    if search == val.strip():
                        # Add the price of the course with the cart amount if the serch value found
                        self.cart_amount = self.cart_amount + int(fieldList[2].strip())
                        return True
        # Print message if the selected course does not exist in the file
        print("The Course does not exist.")
        return False

'''
'order' class is defined to Add Course into the cart, Remove Course
from the cart, and display the cart item
'''
class order(shop):

    # Define function to Add Course into the cart
    def add_to_cart(self, item):
        # Add Course into the cart 
        self.cart_items.append(item)
        print("%s is added in the cart." %(item))

    # Define function to Remove Course from the cart 
    def remove_from_cart(self, obj):
        item = input("Enter the Course Name:")
        if item in obj.cart_items: 
            # Remove Course from the cart
            obj.cart_items.remove(item)
            print("The Course is removed from the cart")
            # Open the file to search the price of the course
            with open('Courses.txt') as f:
                for line in f:
                    fieldList = list(line.split(","))
                    for val in fieldList:
                        if item == val.strip():
                            # Remove the price of the removed course from the cart amount
                            obj.cart_amount = obj.cart_amount - int(fieldList[2].strip())  
        else:
            print("Course does not exist in the cart.")
        
    # Define function to display the cart items
    def display_cart(self, obj):
        # Check the cart amount to find out the cart is empty or not
        if obj.cart_amount > 0:
            # Display the added cart items
            print("\nYou have added the following item(s) in your cart:\n")
            for val in self.cart_items:
                print(val)
            
            # Print the total cart amount
            print("\n%s%s%d%s"  %(fg(25), 'Total amount:$', obj.cart_amount, attr(0)))
            print()
            print()
            print()
            print()

            # Display the second menu
            print("\n1. Add Course")
            print("2. Remove Course")
            print("3. Confirm Payment")
            print("4. Cancel")
            ans = input("\nType 1 or 2 or 3 or 4:")
            return ans

        else:
            # Print message if the cart is empty
            print("You cart is empty.")
            return 0

'''
'student' class id defined to display the purchase information
after confirming the payment
'''
class student(order):

    # Define constructor to initialize the student information
    def __init__(self,  Name, address, phone, cash):
        Name =  Name
        address = address
        contact_no = phone
        add_cash = cash

    # Define function to display the purchase information with student details
    def purchase_info(self,obj):
        # Gnerate a random order number
        order_no = random.random()*100000000
        order_no = round(order_no)
        # Initilize the order date
        today = date.today()
        order_date = today.strftime("%B %d, %Y")

        # Print purchase information
        print("\nYour purchase information is given below:\n")
        print("Course ID          :%s" %order_no)
        print("Payment Date       :%s" %order_date)
        print("Student's Name    :%s" %Name)
        print("Student's Address  :%s" %address)
        print("Student's Phone No :%s" %contact_no)

        # Print purchased course information
        print("\nPurchased Course List:\n")
        for val in self.cart_items:
           print(val)
        print("\n%s%s%d%s"  %(fg(25), 'Total amount:$', obj.cart_amount, attr(0)))
        print("Thank you.")
        print("Be with Us! Expand your knowledge.")



# Declare object of the 'shop' class
objShop = shop()
# Declare the infinite loop to display the menu repeatedly 
# until the user presses '3' 
while True:
    # Display the main menu
    objShop.display_menu()
    # Set initial value for the remove_item
    remove_item = False
    
    # Display the main menu if the user presses '1'
    if objShop.answer == '1':
        objShop.display_products()
    # Display the purchase option if the user presses '2'
    elif objShop.answer == '2':
        # Declare object of the 'order' class
        objOrder = order()
        
        # Declare the infinite loop to display the second menu repeatedly 
        # until the user presses '3' or '4'
        while True:
            # Take the  Course Name to add into the cart if the value of remove_item is False
            if remove_item == False:
                item = input("\nType the Course Name:")
            if item == 'none' :
                # Display the cart after adding or removing the course
                return_val = objOrder.display_cart(objShop)
                # Terminate from the loop if the cart is empty
                if return_val == 0:
                    break
                elif return_val == '1':
                    item = input("Type the  Course Name:")
                    # Check the course exists in the  file or not
                    pro_exist = objShop.check_products(item)
                    # Add the course into the cart if the course exists
                    if pro_exist == True:
                        objOrder.add_to_cart(item)
                    remove_item = False
                    
                elif return_val == '2':
                    # Remove the selected course from the cart
                    return_val = objOrder.remove_from_cart(objShop)
                    remove_item = True
                    
                elif return_val == '3':
                    # Take student's information
                    Name = input("Enter your Name:")
                    address = input("Enter your Address:")
                    contact_no = input("Enter your Contact Number:")
                    print(f'Your Ballance: ${objShop.cust_balance} ')
                    cash = int(input("Add Cash: $"))
                    # Add the cash value with the student's current balance
                    objShop.cust_balance = objShop.cust_balance + cash

                    # Check the balance of the student is less than the cart amount ot not 
                    if objShop.cust_balance < objShop.cart_amount:
                        print()
                        print("You have not enough balance.")
                        print("\n%s%s%d%s"  %(fg(25), 'Avaiable Ballance:$', objShop.cust_balance, attr(0)))
                        print("\n%s%s%d%s"  %(fg(25), 'You Must need $', (objShop.cart_amount-objShop.cust_balance), attr(0)))
                        print('or more Ballace to Buy selected course')
                        print()
                        print()
                        print()
                        print()
                        print()
                        print()
                                        
                    else:
                        # Create object of the 'student' class
                        objstudent = student(Name, address, contact_no, cash)
                        # Print the purchase information
                        objstudent.purchase_info(objShop)
                        # Deduct the purchase amount from the students's balance
                        objShop.cust_balance = cash - objShop.cart_amount   
                        print(f'Available Ballance: ${objShop.cust_balance} ')
                        print()
                        print()
                        print()
                        print()
                        print()
                        print()
                    break
                else:
                    # Print message if the student cancels the purchase
                    print("You have cancelled your purchase.")
                    break
            else:
                # Add the course into the cart if the course exists
                pro_exist = objShop.check_products(item)
                if pro_exist == True:
                     objOrder.add_to_cart(item)
                print("Type 'none' to stop adding Course")
        # Clear the cart list after purchased or cancelled
        objShop.cart_items.clear()
        # Clear the cart amount after purchased or cancelled
        objShop.cart_amount = 0    
    # Terminate from the application if the users presses '3'
    elif objShop.answer == '3':
        print("\nTerminated from the application.")
        exit()