# ------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Alfredo Arnaiz, 20260222 , Renamed starter script to this version.
#                              Modified script to complete assignment.
# ------------------------------------------------------------------------------------ #

# Import json module
import json

# Define the Data Constants
MENU: str = '''
---------- Course Registration Program ----------
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # dict holding one row of student data
students: list = []  # a table of student data
# Note: Commented out since it is NOT needed with the JSON File
# csv_data: str = '' # Holds combined CSV data.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of dict rows (table)
# Extract the data from the file
# Added structured error handling when the file is read into the list of dictionary rows
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print("File must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except json.decoder.JSONDecodeError as e:
    print("Data file is empty or not a valid JSON file!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    # Check if a file object exists and is still open
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        # Added structured error handling when the user enters an invalid first name.
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must be a string of letters only!")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        # Added structured error handling when the user enters an invalid last name.
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must be a string of letters only!")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}
        students.append(student_data)
        print(
            f"You have registered {student_first_name} {student_last_name} "
            f"for {course_name}."
        )
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(
                f"Student {student['FirstName']} {student['LastName']} "
                f"is enrolled in {student['CourseName']}"
            )
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        # Added structured error handling when the dictionary rows are written to the
        # file.
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            # Check if a file object exists and is still open
            if file is not None and file.closed == False:
                file.close()

        print("The following data was saved to file!")
        for student in students:
            print(
                f"Student {student['FirstName']} {student['LastName']} "
                f"is enrolled in {student['CourseName']}"
            )
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
