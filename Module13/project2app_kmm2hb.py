#Kaden Marshall
#query HR_database - Project 2
#Name of Application HRCheck
import mysql.connector

#1
def EmployeesPerRegion(mycursor):
    #create query
    sql_query = "SELECT * FROM EmployeesPerRegion WHERE region_name = 'Americas';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Number of Employees in Americas:\n")
        print(f"Region: {record[0]} \nNumber of Employees: {record[1]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")
    
    return
#2
def managers(mycursor):
    #create query
    sql_query = "SELECT department_name, COUNT(first_name) AS 'Managers in Department' FROM managers GROUP BY department_name ORDER BY COUNT(first_name) DESC;"


    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Number of Managers Listed by Department:\n")
        print(f"Department Name: {record[0]} \nNumber of Managers: {record[1]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")

    
    return
#3
def DependentsByDepartment(mycursor):
    #create query
    sql_query = "SELECT * FROM DependentsByDepartment WHERE NumberOfDependents = (SELECT MAX(NumberOfDependents) FROM DependentsByDepartment) GROUP BY department_name ORDER BY NumberOfDependents DESC;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Number of Dependents Listed by Department:\n")
        print(f"Department Name: {record[0]} \nNumber of Dependents: {record[1]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")
    
    return
#4
def HiresByYear(mycursor):
    #create query
    sql_query = "SELECT * FROM HiresByYear WHERE Year ='1997';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Number of Hires Listed by Year (1997):\n")
        print(f"Year: {record[0]} \nEmployees Hired: {record[1]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")
   
    return    
#5
def SalaryByDepartment(mycursor):
    #create query
    sql_query = "SELECT * FROM SalaryByDepartment WHERE department_name = 'Finance';"


    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Total Salary of Each Department:\n")
        print(f"Department Name: {record[0]} \nTotal Salary: {record[1]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")
    
    return    
#6
def SalaryByJobTitle(mycursor):
    #create query
    sql_query = "SELECT * FROM SalaryByJobTitle WHERE job_title = 'Accountant';"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Number Job Title With Highest Salary:\n")
        print(f"Job Title: {record[0]} \nTotal Salary: {record[1]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")
    
    return  
#7
def EmployeeDependents(mycursor):
    #create query
    sql_query = "SELECT * FROM EmployeeDependents WHERE NumberOfDependents = 0;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Employees With No Dependents:\n")
        print(f"First Name: {record[0]} \nLast Name:{record[1]} \n Email: {record[2]} \n Phone Number: {record[3]} \n Number of Dependents: {record[4]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")
    
    return  
#8
def CountryLocation(mycursor):
    #create query
    sql_query = "SELECT * FROM CountryLocation WHERE NumberofLocations = 0;"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results
    for record in query_result:
        print("\nNow Showing Countries Where we Don't Have a Location:\n")
        print(f"Job Title: {record[0]} \nTotal Salary: {record[1]} \n")
        print("Query Completed! You Will Now be Returned to the Main Menu\n")


        return

def print_menu():
    print("\nWelcome to HRCheck!\nPlease Select the Number That Corresponds to Your Request\n")
    print("1. Display Number of Employees in Americas")
    print("2. Display Number of Managers By Department")
    print("3. Display Department(s) With the Most Dependents")
    print("4. Display Number of Hires in 1997")
    print("5. Display Total Salary of Finance Department")
    print("6. Display Job Title With the Highest Salary")
    print("7. Display Employees With No Dependents")
    print("8. Display Countries Where We Have NO Locations")
    print("9. Exit Application")
    return

def get_user_choice():
    print_menu()
    choice = int(input("\nEnter Choice: "))
    return choice


def main():
#create a connector object
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            passwd="root",
            database="project2"
        )
        print("Successfully connected to Project 2 database! Loading HR Resources...")
    except Exception as err:
        print(f"Error Occured: {err}\nExiting program...")
        quit()

    #create database cursor
    mycursor = mydb.cursor()

    while(True):
        try:
            user_choice = get_user_choice()
            if(user_choice == 1):
            #call the function to query employees per region
                EmployeesPerRegion(mycursor)
            elif(user_choice == 2):
            #call the function to query the managers
                managers(mycursor)
            elif(user_choice == 3):
            #call the function to query the DependentsByDepartment
                DependentsByDepartment(mycursor)
            elif(user_choice == 4):
            #call the function to query the HiresByYear
                HiresByYear(mycursor)
            elif(user_choice == 5):
            #call the function to query the SalaryByDepartment
                SalaryByDepartment(mycursor)
            elif(user_choice == 6):
            #call the function to query the SalaryByJobTitle
                SalaryByJobTitle(mycursor)
            elif(user_choice == 7):
            #call the function to query the EmployeeDependents
                EmployeeDependents(mycursor)
            elif(user_choice == 8):
            #call the function to query CountryLocation
                CountryLocation(mycursor)
            elif(user_choice == 9):
                print("\nNow Exiting the Application! Thank You for Using HRCheck!\n")
                break
        except ValueError:
                print("\nYou must choose a number between 1 and 9! WHOLE NUMBERS ONLY!\n")

main()
    

