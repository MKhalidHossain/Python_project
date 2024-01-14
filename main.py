#from courses
#object = 

from datetime import datetime


def admin_login():
    print("\n** Admin Login Menu **")
    admin_name = str(input("> UserName: "))
    admin_pass = str(input("> Password: "))
    admin_file = open("admin_info.txt", "r")
    for line in admin_file:
        login_admin = line.strip().split(",")
        if (admin_name == login_admin[1] and admin_pass == login_admin[2]):
            print("\n\n     WELCOME, ", login_admin[1], "as a Admin")
            admin_menu()
            return True
    print("!!! You enter wrong ID or Password !!!")
    print("\n--- Return to Admin Login ---\n\n")
    admin_login()
    return False


# Admin menu after login function
def admin_menu():
    print("\n ADMIN MENU:")
    print("1. Insert NEW course \n2. View All Course\n3. Search Course Details\n4. Log Out")
    opt_admin_menu = int(input("> Please select your option (1/2/3/4): "))
    while(opt_admin_menu != '5'):
        if (opt_admin_menu == 1):
            admin_new_course()
        elif(opt_admin_menu == 2):
            view_all_course_data()
            #view_all_course_data().display_products()
        elif(opt_admin_menu == 3):
            admin_search_course_data()
        elif(opt_admin_menu == 4):
            print("=== GOOD BYE, SEE YOU AGAIN! ===\n\n")
            main_menu()
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!\n")
        opt_admin_menu = int(input("Please select your option (1/2/3/4): "))


# Admin new course profile
def admin_new_course():
    print("\nYou choose '1' to INSERT A  NEW COURSE'")
    print("----------------------------------")
    course_file = open("courses.txt", "a")
    new_course_id = str(input("> Enter new course ID: "))
    new_course_name = str(input("> Enter new course Name: "))
    new_course_price = str(input("> Enter new course Price: "))
    new_course_classes = str(input("> Enter new course Classes Number: "))
    new_course_duration = str(input("> Enter new course Duration: "))

   


    course_file.write(new_course_id+", " + new_course_name+","+new_course_price+","+new_course_classes+" classes, "
                        + new_course_duration+" month\n")
    course_file.close()

    dateTimeOfTransaction = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("*** NEW COURSES IS CREATED! ***")
    print("\n--- BACK TO THE ADMIN MENU ---\n")
    admin_menu()

#view all course data
def view_all_course_data():
    print("\nYou choose '2. View All course Data'")
    print("----------------------------------")
    def display_products():
       
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
    display_products()


# Admin search course data
def admin_search_course_data():
    print("\nYou choose '3. Search course Details'")
    print("----------------------------------")

    course_id = str(input("> Enter course ID: "))
    course_file = open("courses.txt", "r")
    for line in course_file:
        search_course = line.strip().split(",")
        if (course_id == search_course[0]):
           
            print("===== COURSE FOUND =====")
            print("Course ID\t:"+search_course[0]+"\nCourse Name\t:"+search_course[1] +
                  "\nPrice\t:"+search_course[2]+"\nClasses\t:"+search_course[3]+"\nDuration\t:"+search_course[4])
            print("\n--- RETURN TO ADMIN MENU ---\n")
            admin_menu()
            return True
    print("!!! COURSE  NOT FOUND ! !!!")
    print("\n--- RETURN TO ADMIN MENU ---\n")
    admin_menu()
    return False




# Main menu
def main_menu():
    print("**** WELCOME TO OUR ONLINE COURSES****\n")
    print(">> MAIN MENU")
    print("1. Admin login \n2. User Interface\n3. Exit")
    opt_main_menu = int(input("> Please select your login as (1/2/3): "))
    while(opt_main_menu != '4'):
        if (opt_main_menu == 1):
            admin_login()
        elif(opt_main_menu == 2):
            import courses
            courses()
        elif(opt_main_menu == 3):
            print("*** Good bye! Thanks for using our system***\n\n")
            quit()
        else:
            print("!!! Invalid Option! Please read the option carefully! !!!\n")
        opt_main_menu = int(input("> Please select your login as (1/2/3): "))


main_menu()




